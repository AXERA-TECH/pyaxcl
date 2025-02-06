# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ******************************************************************************
#
#  Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
#
#  This source file is the property of Axera Semiconductor Co., Ltd. and
#  may not be copied or distributed in any isomorphic form without the prior
#  written consent of Axera Semiconductor Co., Ltd.
#
# ******************************************************************************
import copy
import axcl
import threading
from axclite.axclite_resource import AxcliteResource
from axclite.axclite_context import AxcliteContext
from axclite.axclite_observer import AxcliteObserver, AxcliteSubject


class AxcliteVenc(AxcliteResource):
    venc_type = axcl.AX_VENC_MULTI_ENCODER
    explicit_sched = 0
    sched_policy = axcl.AX_VENC_SCHED_OTHER
    sched_priority = 0
    total_thread_num = 2
    _inited = False

    @classmethod
    def init(cls):
        if not cls._inited:
            ret = axcl.venc.init({'venc_type': cls.venc_type, 'mod_thd_attr': {'explicit_sched': cls.explicit_sched,
                                                                               'sched_policy': cls.sched_policy,
                                                                               'sched_priority': cls.sched_priority,
                                                                               'total_thread_num': cls.total_thread_num}})

            if ret != axcl.AXCL_SUCC:
                return ret

            cls._inited = True
        return axcl.AXCL_SUCC

    @classmethod
    def deinit(cls):
        if cls._inited:
            ret = axcl.venc.deinit()
            if ret != axcl.AXCL_SUCC:
                return ret

            cls._inited = False

        return axcl.AXCL_SUCC

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.device = -1
        self.chn = -1
        self.chn_attr = {}
        self.started = False
        self.recv_thread = None
        self.subject = AxcliteSubject()

    def get_chn_id(self):
        return self.chn

    def check_attr(self, attr: dict):
        if 'venc_attr' not in attr:
            print(f"device {self.device:02x}: key 'venc_attr' not found in attr")
            return False

        w = attr['venc_attr'].get('pic_width_src', 0)
        h = attr['venc_attr'].get('pic_height_src', 0)
        if w < axcl.MIN_VENC_PIC_WIDTH or w > axcl.MAX_VENC_PIC_WIDTH or h < axcl.MIN_VENC_PIC_HEIGHT or h > axcl.MAX_VENC_PIC_HEIGHT:
            print(f"device {self.device:02x}: invalid pic_width_src: {w} or pic_height_src: {h}")
            return False

        if 'rc_attr' not in attr:
            print(f"device {self.device:02x}: key 'rc_attr' not found in attr")
            return False

        rc_mode = attr['rc_attr'].get('rc_mode', axcl.AX_VENC_RC_MODE_H264CBR)
        rc_mode_keys = {
            axcl.AX_VENC_RC_MODE_H264CBR: 'h264_cbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H264VBR: 'h264_vbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H264AVBR: 'h264_avbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H264QVBR: 'h264_qvbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H264CVBR: 'h264_cvbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H264FIXQP: 'h264_fixqp_rc_attr',
            axcl.AX_VENC_RC_MODE_H264QPMAP: 'h264_qpmap_rc_attr',
            axcl.AX_VENC_RC_MODE_H265CBR: 'h265_cbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H265VBR: 'h265_vbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H265AVBR: 'h265_avbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H265QVBR: 'h265_qvbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H265CVBR: 'h265_cvbr_rc_attr',
            axcl.AX_VENC_RC_MODE_H265FIXQP: 'h265_fixqp_rc_attr',
            axcl.AX_VENC_RC_MODE_H265QPMAP: 'h265_qpmap_rc_attr',
            axcl.AX_VENC_RC_MODE_MJPEGCBR: 'mjpeg_cbr_rc_attr',
            axcl.AX_VENC_RC_MODE_MJPEGVBR: 'mjpeg_vbr_rc_attr',
            axcl.AX_VENC_RC_MODE_MJPEGFIXQP: 'mjpeg_fixqp_rc_attr'
        }
        if rc_mode in rc_mode_keys:
            key = rc_mode_keys[rc_mode]
            if key not in attr['rc_attr']:
                print(f"device {self.device:02x}: key '{key}' not found for rc mode {rc_mode}")
                return False

        if 'gop_attr' not in attr or 'gop_mode' not in attr['gop_attr']:
            print(f"device {self.device:02x}: key 'gop_attr' or key 'gop_mode' not found in attr")
            return False

        return True

    def create(self, attr: dict, device: int):
        self.device = device
        if not self.check_attr(attr):
            return 1

        chn_attr = attr
        chn_attr['venc_attr']['type'] = attr['venc_attr'].get('type', axcl.PT_H264)
        chn_attr['venc_attr']['max_pic_width'] = attr['venc_attr'].get('max_pic_width', chn_attr['venc_attr']['pic_width_src'])
        chn_attr['venc_attr']['max_pic_height'] = attr['venc_attr'].get('max_pic_width', chn_attr['venc_attr']['pic_height_src'])
        chn_attr['venc_attr']['mem_source'] = attr['venc_attr'].get('mem_source', axcl.AX_MEMORY_SOURCE_CMM)
        buf_size = chn_attr['venc_attr'].get('buf_size', 0)
        if buf_size == 0:
            buf_size = chn_attr['venc_attr']['pic_width_src'] * chn_attr['venc_attr']['pic_height_src'] * 3 // 2
            print(f"device {self.device:02x}: set venc buf size to {buf_size}")
            chn_attr['venc_attr']['buf_size'] = buf_size
        chn_attr['venc_attr']['profile'] = attr['venc_attr'].get('profile', axcl.AX_VENC_H264_MAIN_PROFILE)
        chn_attr['venc_attr']['level'] = attr['venc_attr'].get('level', axcl.AX_VENC_H264_LEVEL_5_1)
        chn_attr['venc_attr']['strm_bit_depth'] = attr['venc_attr'].get('strm_bit_depth', axcl.AX_VENC_STREAM_BIT_8)
        chn_attr['venc_attr']['in_fifo_depth'] = attr['venc_attr'].get('in_fifo_depth', 4)
        chn_attr['venc_attr']['out_fifo_depth'] = attr['venc_attr'].get('out_fifo_depth', 4)

        chn_attr['rc_attr']['rc_mode'] = attr['rc_attr'].get('rc_mode', axcl.AX_VENC_RC_MODE_H264CBR)
        chn_attr['gop_attr']['gop_mode'] = attr['gop_attr'].get('gop_mode', axcl.AX_VENC_GOPMODE_NORMALP)
        self.chn, ret = axcl.venc.create_chn_ex(chn_attr)
        if ret != axcl.AXCL_SUCC:
            return ret

        self.chn_attr = copy.deepcopy(chn_attr)
        print(f"device {self.device:02x}: veChn {self.chn} is created")
        return axcl.AXCL_SUCC

    def destroy(self):
        if self.chn < 0:
            print(f"device {self.device:02x}: veChn is not created yet")
            return

        axcl.venc.destroy_chn(self.chn)
        print(f"device {self.device:02x}: veChn {self.chn} is destroyed")
        self.chn = -1

    def register_observer(self, observer: AxcliteObserver):
        self.subject.register(observer)

    def unregister_observer(self, observer: AxcliteObserver):
        self.subject.unregister(observer)

    def start(self):
        if self.started:
            print(f"device {self.device:02x}: veChn {self.chn} is already started")
            return axcl.AXCL_SUCC

        ret = axcl.venc.start_recv_frame(self.chn, {'recv_pic_num': -1})
        if ret != axcl.AXCL_SUCC:
            return ret

        self.recv_thread = threading.Thread(target=self.recv_worker)
        self.recv_thread.start()

        self.started = True

        print(f"device {self.device:02x}: veChn {self.chn} is started")
        return axcl.AXCL_SUCC

    def stop(self):
        if not self.started:
            print(f"device {self.device:02x}: veChn {self.chn} is not started yet")
            return axcl.AXCL_SUCC

        self.started = False

        ret = axcl.venc.stop_recv_frame(self.chn)
        if ret != axcl.AXCL_SUCC:
            return ret

        ret = axcl.venc.reset_chn(self.chn)
        if ret != axcl.AXCL_SUCC:
            return ret

        self.recv_thread.join()

        print(f"device {self.device:02x}: veChn {self.chn} is stopped")
        return axcl.AXCL_SUCC

    def send_frame(self, frame: dict, timeout: int):
        return axcl.venc.send_frame(self.chn, frame, timeout)

    def recv_worker(self):
        # print(f"device {self.device:02x}: veChn {self.chn} on device {self.device} recv worker +++")
        context = AxcliteContext()
        context.create(self.device)

        while self.started:
            stream, ret = axcl.venc.get_stream(self.chn, -1)
            if ret != axcl.AXCL_SUCC:
                if ret == axcl.AX_ERR_VENC_FLOW_END:
                    break
                continue

            self.subject.notify(stream)

            axcl.venc.release_stream(self.chn, stream)

        context.destroy()
        # print(f"device {self.device:02x}: veChn {self.chn} on device {self.device} recv worker ---")
