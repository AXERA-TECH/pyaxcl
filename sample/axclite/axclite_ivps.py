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
import time
import threading
import axcl
from axclite.axclite_context import AxcliteContext
from axclite.axclite_resource import AxcliteResource
from axclite.axclite_utils import axclite_align_up
from axclite.axclite_observer import AxcliteObserver, AxcliteSubject


def axcl_ivps_create_nop_filter():
    return {
        'engaged': 0,
        'engine': 0,
        'frame_rate_control': {'src_frame_rate': 0.0, 'dst_frame_rate': 0.0},
        'crop': 0, 'crop_rect': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
        'dst_pic_width': 0, 'dst_pic_height': 0, 'dst_pic_stride': 0,
        'dst_pic_format': 0,
        'compression_info': {'compress_mode': 0, 'compress_level': 0},
        'in_place': 0,
        'aspect_ratio': {'aspect_ratio_mode': 0,
                         'background_color': 0,
                         'alignments': [0, 0],
                         'rectangle': {'x': 0, 'y': 0, 'width': 0, 'height': 0}
                         },
        'reserved': 0,
        'scale_mode': 0
    }


class AxcliteIvps(AxcliteResource):
    _inited = False

    @classmethod
    def init(cls):
        if not cls._inited:
            ret = axcl.ivps.init()
            if ret != axcl.AXCL_SUCC:
                return ret

            cls._inited = True
        return axcl.AXCL_SUCC

    @classmethod
    def deinit(cls):
        if cls._inited:
            ret = axcl.ivps.deinit()
            if ret != axcl.AXCL_SUCC:
                return ret

            cls._inited = False

        return axcl.AXCL_SUCC

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.device = -1
        self.grp = -1
        self.chn = []
        self.backup_fifo_depth = 0
        self.started = False

    def get_grp_id(self):
        return self.grp

    def check_attr(self, attr):
        if 'grp_attr' not in attr:
            print(f"device {self.device:02x}: key 'grp_attr' not found in attr")
            return False

        if 'filters' not in attr:
            print(f"device {self.device:02x}: key 'filters' not found in attr")
            return False

        num = len(attr['filters'])
        if num == 0 or num > axcl.AX_IVPS_MAX_OUTCHN_NUM:
            print(f"device {self.device:02x}: invalid number of filter {num}")
            return False

        for i in range(num):
            w = attr['filters'][i].get('dst_pic_width', 0)
            h = attr['filters'][i].get('dst_pic_height', 0)
            if w < axcl.AX_IVPS_MIN_IMAGE_WIDTH or w > axcl.AX_IVPS_MAX_IMAGE_WIDTH or h < axcl.AX_IVPS_MIN_IMAGE_HEIGHT or h > axcl.AX_IVPS_MAX_IMAGE_HEIGHT:
                print(f"device {self.device:02x}: invalid dst_pic_width: {w} or dst_pic_height: {h}")
                return False

        return True

    def create(self, attr, device):
        """
        'grp_attr': {
            'in_fifo_depth': int
        },
        'backup_fifo_depth': int,
        'filters': [{
            'engaged': bool,
            'link': bool,
            'out_fifo_depth': int
            'frame_rate_control': {
                'src_frame_rate': float,
                'dst_frame_rate': float
            }
            'engine': AX_IVPS_ENGINE_E,
            'crop': bool,
            'crop_rect': {
                'x': int,
                'y': int,
                'width': int,
                'height': int
            },
            'dst_pic_width': int,
            'dst_pic_height': int,
            'dst_pic_format': AX_IMG_FORMAT_E,
            'compression_info': {
                'compress_mode': AX_COMPRESS_MODE_E,
                'compress_level': int
            },
            'in_place': bool,
            'frame_buf_num': int
        }]
        """
        self.device = device
        if not self.check_attr(attr):
            return 1

        grp_attr = {'in_fifo_depth': attr['grp_attr'].get('in_fifo_depth', 4), 'pipeline': axcl.AX_IVPS_PIPELINE_DEFAULT}
        self.grp, ret = axcl.ivps.create_grp_ex(grp_attr)
        if ret != axcl.AXCL_SUCC:
            return ret

        pipe_attr = {'out_channel_num': len(attr['filters']),
                     'in_debug_fifo_depth': 0,
                     'out_fifo_depth': [0] * axcl.AX_IVPS_MAX_OUTCHN_NUM,
                     'filters': [
                         [axcl_ivps_create_nop_filter() for _ in range(axcl.AX_IVPS_MAX_FILTER_NUM_PER_OUTCHN)]
                         for _ in range(axcl.AX_IVPS_MAX_OUTCHN_NUM + 1)
                     ]}

        self.chn = [{} for _ in range(pipe_attr['out_channel_num'])]

        for i in range(axcl.AX_IVPS_MAX_OUTCHN_NUM):
            if i < pipe_attr['out_channel_num']:
                self.chn[i]['link'] = attr['filters'][i].get('link', False)
                if not self.chn[i]['link']:
                    self.chn[i]['subject'] = AxcliteSubject()
                    pipe_attr['out_fifo_depth'][i] = attr['filters'][i].get('out_fifo_depth', 4)

                filter0 = pipe_attr['filters'][i + 1][0]
                filter0['engaged'] = 1 if attr['filters'][i].get('engaged', False) else 0
                filter0['engine'] = attr['filters'][i].get('engine', axcl.AX_IVPS_ENGINE_VPP)
                filter0['frame_rate_control'] = attr['filters'][i].get('frame_rate_control', {'src_frame_rate': 0.0, 'dst_frame_rate': 0.0})
                filter0['compression_info'] = attr['filters'][i].get('compression_info', {'compress_mode': axcl.AX_COMPRESS_MODE_NONE, 'compress_level': 0})
                filter0['crop'] = 1 if attr['filters'][i].get('crop', False) else 0
                filter0['crop_rect'] = attr['filters'][i].get('crop_rect', {'x': 0, 'y': 0, 'width': 0, 'height': 0})
                filter0['dst_pic_width'] = attr['filters'][i]['dst_pic_width']
                filter0['dst_pic_height'] = attr['filters'][i]['dst_pic_height']
                stride = attr['filters'][i].get('dst_pic_stride', 0)
                if stride == 0:
                    align = 128 if (filter0['compression_info']['compress_mode'] != axcl.AX_COMPRESS_MODE_NONE) else 16
                    stride = axclite_align_up(attr['filters'][i]['dst_pic_width'], align)
                filter0['dst_pic_stride'] = stride
                filter0['dst_pic_format'] = attr['filters'][i].get('dst_pic_format', axcl.AX_FORMAT_YUV420_SEMIPLANAR)
                filter0['in_place'] = 1 if attr['filters'][i].get('in_place', False) else 0

        ret = axcl.ivps.set_pipeline_attr(self.grp, pipe_attr)
        if ret != axcl.AXCL_SUCC:
            axcl.ivps.destroy_grp(self.grp)
            self.grp = -1
            return ret

        for i in range(pipe_attr['out_channel_num']):
            pool_attr = {'pool_source': axcl.POOL_SOURCE_PRIVATE, 'frame_buf_num': attr['filters'][i].get('frame_buf_num', 4)}
            ret = axcl.ivps.set_chn_pool_attr(self.grp, i, pool_attr)
            if ret != axcl.AXCL_SUCC:
                axcl.ivps.destroy_grp(self.grp)
                self.grp = -1
                return ret

            ret = axcl.ivps.enable_chn(self.grp, i)
            if ret != axcl.AXCL_SUCC:
                axcl.ivps.destroy_grp(self.grp)
                self.grp = -1
                return ret

        self.backup_fifo_depth = attr.get('backup_fifo_depth', 0)
        if self.backup_fifo_depth > 0:
            print(f"device {self.device:02x}: ivGrp {self.grp} enable backup fifo, depth: {self.backup_fifo_depth}")
            ret = axcl.ivps.enable_backup_frame(self.grp, self.backup_fifo_depth)
            if ret != axcl.AXCL_SUCC:
                axcl.ivps.destroy_grp(self.grp)
                self.grp = -1
                return ret

        print(f"device {self.device:02x}: ivGrp {self.grp} is created")
        return axcl.AXCL_SUCC

    def destroy(self):
        if self.grp < 0:
            print("device {self.device:02x}: ivGrp is not created yet")
            return

        for i in range(len(self.chn)):
            axcl.ivps.disable_chn(self.grp, i)

        if self.backup_fifo_depth > 0:
            axcl.ivps.disable_backup_frame(self.grp)

        axcl.ivps.destroy_grp(self.grp)
        print(f"device {self.device:02x}: ivGrp {self.grp} is destroyed")
        self.grp = -1

    def register_observer(self, chn, observer: AxcliteObserver):
        if chn < len(self.chn):
            self.chn[chn]['subject'].register(observer)

    def unregister_observer(self, chn, observer: AxcliteObserver):
        if chn < len(self.chn):
            self.chn[chn]['subject'].unregister(observer)

    def start(self):
        if self.started:
            print(f"ivGrp {self.grp} is already started")
            return axcl.AXCL_SUCC

        ret = axcl.ivps.start_grp(self.grp)
        if ret != axcl.AXCL_SUCC:
            return ret

        # start thread to receive decoded image
        for i in range(len(self.chn)):
            if not self.chn[i]['link']:
                self.chn[i]['worker'] = threading.Thread(target=self.recv_worker, args=(i,))
                self.chn[i]['worker'].start()

        self.started = True

        print(f"device {self.device:02x}: ivGrp {self.grp} is started")
        return axcl.AXCL_SUCC

    def stop(self):
        if not self.started:
            print(f"device {self.device:02x}: ivGrp {self.grp} is not started yet")
            return axcl.AXCL_SUCC

        self.started = False

        for i in range(len(self.chn)):
            if not self.chn[i]['link']:
                self.chn[i]['worker'].join()

        ret = axcl.ivps.stop_grp(self.grp)
        if ret != axcl.AXCL_SUCC:
            return ret

        print(f"device {self.device:02x}: ivGrp {self.grp} is stopped")
        return axcl.AXCL_SUCC

    def send_frame(self, frame, timeout):
        return axcl.ivps.send_frame(self.grp, frame, timeout)

    def recv_worker(self, chn):
        # print(f"device {self.device:02x}: ivGrp {self.grp} on device {self.device} recv worker +++")
        context = AxcliteContext()
        context.create(self.device)

        timeout = 100
        while self.started:
            frame, ret = axcl.ivps.get_chn_frame(self.grp, chn, timeout)
            if ret != axcl.AXCL_SUCC:
                time.sleep(0.001)
                continue

            self.chn[chn]['subject'].notify(frame)

            axcl.ivps.release_chn_frame(self.grp, chn, frame)

        context.destroy()
        # print(f"device {self.device:02x}: ivGrp {self.grp} on device {self.device} recv worker ---")



