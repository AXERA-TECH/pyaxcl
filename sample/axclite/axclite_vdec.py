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
import threading
import time
import axcl
from axcl.utils.axcl_utils import bytes_to_ptr
from axclite.axclite_context import AxcliteContext
from axclite.axclite_resource import AxcliteResource
from axclite.axclite_utils import axclite_align_up
from axclite.axclite_observer import AxcliteObserver, AxcliteSubject

VDEC_STRIDE_ALIGN = 256


class AxcliteVdec(AxcliteResource):
    decode_mode = axcl.AX_ENABLE_BOTH_VDEC_JDEC
    max_grp_num = 32
    _inited = False

    @classmethod
    def init(cls):
        if not cls._inited:
            mod_attr = {'max_group_count': cls.max_grp_num, 'dec_module': cls.decode_mode, 'vdec_mc': 0, 'vdec_virt_chn': 0}
            ret = axcl.vdec.init(mod_attr)
            if ret != axcl.AXCL_SUCC:
                return ret

            cls._inited = True
        return axcl.AXCL_SUCC

    @classmethod
    def deinit(cls):
        if cls._inited:
            ret = axcl.vdec.deinit()
            if ret != axcl.AXCL_SUCC:
                return ret

            cls._inited = False

        return axcl.AXCL_SUCC

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.device = -1
        self.grp = -1
        self.attr = None
        self.started = False
        self.recv_threads = []
        self.subjects = [AxcliteSubject(), AxcliteSubject(), AxcliteSubject()]

    def get_grp_id(self):
        return self.grp

    def check_attr(self, attr):
        if 'grp_attr' not in attr:
            print(f"device {self.device:02x}: key 'grp_attr' not found in attr")
            return False

        w = attr['grp_attr'].get('max_pic_width', 0)
        h = attr['grp_attr'].get('max_pic_height', 0)
        if w < axcl.AX_VDEC_MIN_WIDTH or w > axcl.AX_VDEC_MAX_WIDTH or h < axcl.AX_VDEC_MIN_HEIGHT or h > axcl.AX_VDEC_MAX_HEIGHT:
            print(f"device {self.device:02x}: invalid grp max_pic_width: {w} or max_pic_height: {h}")
            return False

        if 'chn_attr' not in attr or len(attr['chn_attr']) != axcl.AX_DEC_MAX_CHN_NUM:
            print(f"device {self.device:02x}: key 'chn_attr' not found in attr or len of 'chn_attr' is not {axcl.AX_DEC_MAX_CHN_NUM}")
            return False

        num = 0
        for i in range(axcl.AX_DEC_MAX_CHN_NUM):
            if 'enable' not in attr['chn_attr'][i]:
                print(f"device {self.device:02x}: key 'enable' not found in attr['chn_attr'][{i}]")
                return False

            if attr['chn_attr'][i]['enable']:
                w = attr['chn_attr'][i].get('pic_width', 0)
                h = attr['chn_attr'][i].get('pic_height', 0)
                if w < axcl.AX_VDEC_MIN_WIDTH or w > axcl.AX_VDEC_MAX_WIDTH or h < axcl.AX_VDEC_MIN_HEIGHT or h > axcl.AX_VDEC_MAX_HEIGHT:
                    print(f"device {self.device:02x}: invalid chn pic_width: {w} or pic_height: {h}")
                    return False

            num += 1

        if num == 0:
            print(f"device {self.device:02x}: at least 1 chn should be enabled")
            return False

        return True

    def create(self, attr, device):
        """
        'grp_attr': {
            'codec_type': AX_PAYLOAD_TYPE_E,
            'max_pic_width': int,
            'max_pic_height': int,
            'output_order' : AX_VDEC_OUTPUT_ORDER_E,
            'display_mode' : AX_VDEC_DISPLAY_MODE_E,
            }
        'chn_attr': [{
            'enable': bool,
            'link': bool,
            'crop_x': int,
            'crop_y': int,
            'pic_width': int,
            'pic_height': int,
            'compress_info': {
                'compress_mode': AX_COMPRESS_MODE_E,
                'compress_level': int
                },
            'output_fifo_depth': int
            'frame_buf_cnt': int,
            'recv_frame_timeout': int
            }]
        """
        self.device = device

        if not self.check_attr(attr):
            return 1

        w = axclite_align_up(attr['grp_attr']['max_pic_width'], 16)
        h = axclite_align_up(attr['grp_attr']['max_pic_height'], 16)
        grp_attr = {'codec_type': attr['grp_attr'].get('codec_type', axcl.PT_H264), 'input_mode': axcl.AX_VDEC_INPUT_MODE_FRAME,
                    'max_pic_width': w, 'max_pic_height': h, 'stream_buf_size': w * h * 2, 'sdk_auto_frame_pool': 1}
        self.grp, ret = axcl.vdec.create_grp_ex(grp_attr)
        if ret != axcl.AXCL_SUCC:
            return ret

        grp_param = {'output_order': attr['grp_attr'].get('output_order', axcl.AX_VDEC_OUTPUT_ORDER_DEC),
                     'vdec_mode': attr['grp_attr'].get('vdec_mode', axcl.VIDEO_DEC_MODE_IPB)}
        ret = axcl.vdec.set_grp_param(self.grp, grp_param)
        if ret != axcl.AXCL_SUCC:
            axcl.vdec.destroy_grp(self.grp)
            self.grp = -1
            return ret

        ret = axcl.vdec.set_display_mode(self.grp, attr['grp_attr'].get('display_mode', axcl.AX_VDEC_DISPLAY_MODE_PREVIEW))
        if ret != axcl.AXCL_SUCC:
            axcl.vdec.destroy_grp(self.grp)
            self.grp = -1
            return ret

        for i in range(axcl.AX_DEC_MAX_CHN_NUM):
            if not attr['chn_attr'][i]['enable']:
                print(f"device {self.device:02x}: vdGrp {self.grp} vdChn {i} is disabled")
                continue

            stride = axclite_align_up(attr['chn_attr'][i]['pic_width'], VDEC_STRIDE_ALIGN)
            chn_attr = {'pic_width': attr['chn_attr'][i]['pic_width'], 'pic_height': attr['chn_attr'][i]['pic_height'],
                        'frame_stride': stride,
                        'crop_x': attr['chn_attr'][i].get('crop_x', 0),
                        'crop_y': attr['chn_attr'][i].get('crop_y', 0)}

            if chn_attr['crop_x'] > 0 or chn_attr['crop_x'] > 0:
                chn_attr['output_mode'] = axcl.AX_VDEC_OUTPUT_CROP
            else:
                chn_attr['output_mode'] = axcl.AX_VDEC_OUTPUT_ORIGINAL if i == 0 else axcl.AX_VDEC_OUTPUT_SCALE

            chn_attr['img_format'] = axcl.AX_FORMAT_YUV420_SEMIPLANAR
            chn_attr['compress_info'] = attr['chn_attr'][i].get('compress_info', {'compress_mode': axcl.AX_COMPRESS_MODE_NONE, 'compress_level': 0})
            if chn_attr['compress_info']['compress_mode'] == axcl.AX_COMPRESS_MODE_LOSSLESS:
                print(f"invalid vdGrp {self.grp} compress mode, set to AX_COMPRESS_MODE_NONE")
                chn_attr['compress_info']['compress_mode'] = axcl.AX_COMPRESS_MODE_NONE
                chn_attr['compress_info']['compress_level'] = 0

            chn_attr['output_fifo_depth'] = attr['chn_attr'][i].get('output_fifo_depth', 4)
            chn_attr['frame_buf_cnt'] = attr['chn_attr'][i].get('frame_buf_cnt', 8)
            chn_attr['frame_buf_size'] = axcl.vdec.get_buf_size(chn_attr['pic_width'],
                                                                chn_attr['pic_height'],
                                                                chn_attr['img_format'],
                                                                chn_attr['compress_info'],
                                                                grp_attr['codec_type'])
            ret = axcl.vdec.set_chn_attr(self.grp, i, chn_attr)
            if ret != axcl.AXCL_SUCC:
                for j in range(i):
                    axcl.vdec.disable_chn(self.grp, j)
                axcl.vdec.destroy_grp(self.grp)
                self.grp = -1

            ret = axcl.vdec.enable_chn(self.grp, i)
            if ret != axcl.AXCL_SUCC:
                for j in range(i):
                    axcl.vdec.disable_chn(self.grp, j)
                axcl.vdec.destroy_grp(self.grp)
                self.grp = -1

            print(f"device {self.device:02x}: vdGrp {self.grp} vdChn {i} is enabled")

        self.attr = copy.deepcopy(attr)
        print(f"device {self.device:02x}: vdGrp {self.grp} is created")
        return axcl.AXCL_SUCC

    def destroy(self):
        if self.grp < 0:
            print(f"device {self.device:02x}: vdGrp is not created yet")
            return

        for i in range(axcl.AX_DEC_MAX_CHN_NUM):
            axcl.vdec.disable_chn(self.grp, i)

        axcl.vdec.destroy_grp(self.grp)
        print(f"device {self.device:02x}: vdGrp {self.grp} is destroyed")
        self.grp = -1

    def register_observer(self, chn, observer: AxcliteObserver):
        self.subjects[chn].register(observer)

    def unregister_observer(self, chn, observer: AxcliteObserver):
        self.subjects[chn].unregister(observer)

    def start(self):
        if self.started:
            print(f"device {self.device:02x}: vdGrp {self.grp} is already started")
            return axcl.AXCL_SUCC

        recv_param = {'recv_pic_num': -1}
        ret = axcl.vdec.start_recv_stream(self.grp, recv_param)
        if ret != axcl.AXCL_SUCC:
            return ret

        # start thread to receive decoded image
        self.recv_threads.clear()
        for i in range(axcl.AX_DEC_MAX_CHN_NUM):
            if self.attr['chn_attr'][i].get('enable', False) and not self.attr['chn_attr'][i].get('link', False):
                timeout = self.attr['chn_attr'][i].get('recv_frame_timeout', 1000)
                t = threading.Thread(target=self.recv_worker, args=(i, timeout), name="vdec_recv_{}_{}".format(self.grp, i))
                self.recv_threads.append(t)
                t.start()
                break

        self.started = True
        print(f"device {self.device:02x}: vdGrp {self.grp} is started")
        return axcl.AXCL_SUCC

    def query_status(self):
        status, ret = axcl.vdec.query_status(self.grp)
        return status if ret == axcl.AXCL_SUCC else None

    def stop(self):
        if not self.started:
            print(f"device {self.device:02x}: vdGrp {self.grp} is not started yet")
            return axcl.AXCL_SUCC

        ret = axcl.vdec.stop_recv_stream(self.grp)
        if ret != axcl.AXCL_SUCC:
            return ret

        self.started = False

        retry = 0
        while retry < 3:
            retry += 1
            ret = axcl.vdec.reset_grp(self.grp)
            if ret != axcl.AXCL_SUCC:
                if ret == axcl.AX_ERR_VDEC_BUSY:
                    print(f"device {self.device:02x}: vdGrp {self.grp} is busy, try again to reset")
                else:
                    print(f"device {self.device:02x}: reset vdGrp {self.grp} fail, ret = 0x{ret&0xFFFFFFFF:x}, try again to reset")
                time.sleep(0.04)
            else:
                break
        if ret != axcl.AXCL_SUCC:
            print(f"device {self.device:02x}: reset vdGrp {self.grp} fail, ret = 0x{ret&0xFFFFFFFF:x}")
            return ret

        for t in self.recv_threads:
            if t:
                t.join()

        print(f"device {self.device:02x}: vdGrp {self.grp} is stopped")
        return axcl.AXCL_SUCC

    def send_stream(self, data: bytes, pts, user_data=0, timeout=1000):
        if not self.started:
            print(f"device {self.device:02x}: vdGrp {self.grp} is not started")
            return 1

        stream = {'pts': pts, 'user_data': user_data,
                  'end_of_frame': 1, 'end_of_stream': 1 if data is None or len(data) == 0 else 0,
                  'stream_pack_len': 0 if data is None else len(data),
                  'addr': bytes_to_ptr(data)}
        ret = axcl.vdec.send_stream(self.grp, stream, timeout)
        if ret != axcl.AXCL_SUCC:
            return ret

        return axcl.AXCL_SUCC

    def recv_worker(self, chn, timeout):
        # print(f"device {self.device:02x}: vdGrp {self.grp} vdChn {chn} recv worker +++")
        context = AxcliteContext()
        context.create(self.device)

        while self.started:
            frame, ret = axcl.vdec.get_chn_frame(self.grp, chn, timeout)
            if ret != axcl.AXCL_SUCC:
                continue

            if frame['video_frame']['blk_id'][0] == axcl.AX_INVALID_BLOCKID:
                print(f"device {self.device:02x}: invalid frame of vdGrp {self.grp} vdChn {chn}: frame blkId[0] == {axcl.AX_INVALID_BLOCKID}")
            elif frame['video_frame']['width'] == 0 or frame['video_frame']['height'] == 0:
                print(f"device {self.device:02x}: invalid frame width {frame['video_frame']['width']} or height {frame['video_frame']['height']} of vdGrp {self.grp} vdChn {chn}")
            else:
                self.subjects[chn].notify(frame)

            axcl.vdec.release_chn_frame(self.grp, chn, frame)

        context.destroy()
        # print(f"device {self.device:02x}: vdGrp {self.grp} vdChn {chn} recv worker ---")
