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

import os
import sys
import argparse
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR + '/..')
sys.path.append(BASE_DIR + '/../..')

import axcl
from axclite.axclite_device import AxcliteDevice
from axclite.axclite_system import axclite_system
from axclite.axclite_file import *
from axclite.axclite_memory import *
from axclite.axclite_utils import *


def _init():
    ret = axcl.sys.init()
    if axcl.AXCL_SUCC != ret:
        print(f"axcl.sys.init() fail, ret = 0x{ret&0xFFFFFFFF:x}")

    ret = axcl.ivps.init()
    if axcl.AXCL_SUCC != ret:
        print(f"axcl.ivps.init() fail, ret = 0x{ret&0xFFFFFFFF:x}")


def _deinit():
    axcl.ivps.deinit()

    ret = axcl.sys.deinit()
    if axcl.AXCL_SUCC != ret:
        print(f"axcl.sys.deinit() fail, ret = 0x{ret&0xFFFFFFFF:x}")


def _type_convert(type):
    if type == 'nv12':
        return axcl.AX_FORMAT_YUV420_SEMIPLANAR
    elif type == 'nv21':
        return axcl.AX_FORMAT_YUV420_SEMIPLANAR_VU
    elif type == 'rgb888':
        return axcl.AX_FORMAT_RGB888
    elif type == 'bgr888':
        return axcl.AX_FORMAT_BGR888
    elif type == 'rgb565':
        return axcl.AX_FORMAT_RGB565
    elif type == 'argb8888':
        return axcl.AX_FORMAT_ARGB8888
    elif type == 'rgba8888':
        return axcl.AX_FORMAT_RGBA8888
    else:
        return None


def _image_type_string(type):
    if type == axcl.AX_FORMAT_YUV420_SEMIPLANAR:
        return 'nv12'
    elif type == axcl.AX_FORMAT_YUV420_SEMIPLANAR_VU:
        return 'nv21'
    elif type == axcl.AX_FORMAT_RGB888:
        return 'rgb888'
    elif type == axcl.AX_FORMAT_BGR888:
        return 'bgr888'
    elif type == axcl.AX_FORMAT_RGB565:
        return 'rgb565'
    elif type == axcl.AX_FORMAT_ARGB8888:
        return 'argb8888'
    elif type == axcl.AX_FORMAT_RGBA8888:
        return 'rgba8888'
    else:
        return 'nv12'


def crop_resize_test(src_file, dst_path, width, height, src_type, dst_type, engine):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()
    src_stride = axclite_get_stride(width, src_type)

    if src_dev_mem == 0:
        return

    dst_width = width//2
    dst_height = height//2
    dst_stride = axclite_get_stride(dst_width, dst_type)
    dst_size = axclite_get_image_size(dst_stride, dst_height, dst_type)
    dst_dev_mem_object = AxcliteDeviceMalloc(dst_size)
    dst_dev_mem = dst_dev_mem_object.address

    if dst_dev_mem == 0:
        return

    src = {
        'width': width,
        'height': height,
        'img_format': src_type,
        'pic_stride': [src_stride, src_stride, 0],
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0],
        'crop_x': width//4,
        'crop_y': height//4,
        'crop_width': width//2,
        'crop_height': height//2,
        'frame_size': src_size
    }

    dst = {
        'width': dst_width,
        'height': dst_height,
        'img_format': dst_type,
        'pic_stride': [dst_stride, dst_stride, 0],
        'phy_addr': [dst_dev_mem, 0, 0],
        'vir_addr': [0],
        'frame_size': dst_size
    }

    aspect_ratio = {
        'aspect_ratio_mode': axcl.AX_IVPS_ASPECT_RATIO_STRETCH,
        'background_color': 0x000000,
        'alignments': [axcl.AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT, axcl.AX_IVPS_ASPECT_RATIO_VERTICAL_TOP],
        'rectangle': {
            'x': 0,
            'y': 0,
            'width': 0,
            'height': 0
        }
    }

    if engine == 'vgp':
        ret = axcl.ivps.crop_resize_vgp(src, dst, aspect_ratio)
    elif engine == 'vpp':
        ret = axcl.ivps.crop_resize_vpp(src, dst, aspect_ratio)
    elif engine == 'tdp':
        ret = axcl.ivps.crop_resize_tdp(src, dst, aspect_ratio)

    if 0 == ret:
        print(f"crop_resize_{engine} operation completed successfully")
        frame_type = _image_type_string(dst_type)
        file_name = f"crop_resize_{engine}_output_image_{dst_width}x{dst_height}.{frame_type}"
        dst_file = AxcliteStoreFileFromDevice(dst_dev_mem, dst_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"crop_resize_{engine} failed with error code {ret}.")


def crop_resize_v2_test(src_file, dst_path, width, height, src_type, dst_type, engine):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()
    src_stride = axclite_get_stride(width, src_type)

    if src_dev_mem == 0:
        return

    dst_width = width//2
    dst_height = height//2
    dst_stride = axclite_get_stride(dst_width, dst_type)
    dst_size = axclite_get_image_size(dst_stride, dst_height, dst_type)
    dst1_dev_mem_object = AxcliteDeviceMalloc(dst_size)
    dst1_dev_mem = dst1_dev_mem_object.address

    dst2_dev_mem_object = AxcliteDeviceMalloc(dst_size)
    dst2_dev_mem = dst2_dev_mem_object.address

    if dst1_dev_mem == 0 or dst2_dev_mem == 0:
        return

    src = {
        'width': width,
        'height': height,
        'img_format': src_type,
        'pic_stride': [src_stride, src_stride, 0],
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0],
        'frame_size': src_size
    }

    box_list = [
        {
            'x': width//8,
            'y': height//8,
            'width': dst_width//2,
            'height': dst_height//2
        },
        {
            'x': width//4,
            'y': width//4,
            'width': dst_width,
            'height': dst_height
        }
    ]

    dst_list = [
        {
            'width': dst_width,
            'height': dst_height,
            'img_format': dst_type,
            'pic_stride': [dst_stride, dst_stride, 0],
            'phy_addr': [dst1_dev_mem, 0, 0],
            'vir_addr': [0],
            'frame_size': dst_size
        },
        {
            'width': dst_width,
            'height': dst_height,
            'img_format': dst_type,
            'pic_stride': [dst_stride, dst_stride, 0],
            'phy_addr': [dst2_dev_mem, 0, 0],
            'vir_addr': [0],
            'frame_size': dst_size
        }
    ]

    aspect_ratio = {
        'aspect_ratio_mode': axcl.AX_IVPS_ASPECT_RATIO_STRETCH,
        'background_color': 0x000000,
        'alignments': [axcl.AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT, axcl.AX_IVPS_ASPECT_RATIO_VERTICAL_TOP],
        'rectangle': {
            'x': 0,
            'y': 0,
            'width': 0,
            'height': 0
        }
    }

    if engine == 'vgp':
        ret = axcl.ivps.crop_resize_v2_vgp(src, box_list, dst_list, aspect_ratio)
    elif engine == 'vpp':
        ret = axcl.ivps.crop_resize_v2_vpp(src, box_list, dst_list, aspect_ratio)
    elif engine == 'tdp':
        ret = axcl.ivps.crop_resize_v2_tdp(src, box_list, dst_list, aspect_ratio)

    if 0 == ret:
        print(f"crop_resize_v2_{engine} operation completed successfully")
        frame_type = _image_type_string(type)
        file_name = f"crop_resize_v2_{engine}_output_image_{dst_width}x{dst_height}_1.{frame_type}"
        dst_file = AxcliteStoreFileFromDevice(dst1_dev_mem, dst_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
        file_name = f"crop_resize_v2_{engine}_output_image_{dst_width}x{dst_height}_2.{frame_type}"
        dst_file = AxcliteStoreFileFromDevice(dst2_dev_mem, dst_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"crop_resize_v2_{engine} failed with error code {ret}.")


def crop_resize_v3_test(src_file, dst_path, width, height, src_type, dst_type, engine):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()
    src_stride = axclite_get_stride(width, src_type)

    if src_dev_mem == 0:
        return

    dst1_width = width
    dst1_height = height
    dst1_stride = axclite_get_stride(dst1_width, dst_type)
    dst1_size = axclite_get_image_size(dst1_stride, dst1_height, dst_type)
    dst1_dev_mem_object = AxcliteDeviceMalloc(dst1_size)
    dst1_dev_mem = dst1_dev_mem_object.address

    dst2_width = width//2
    dst2_height = height//2
    dst2_stride = axclite_get_stride(dst2_width, dst_type)
    dst2_size = axclite_get_image_size(dst2_stride, dst2_height, dst_type)
    dst2_dev_mem_object = AxcliteDeviceMalloc(dst2_size)
    dst2_dev_mem = dst2_dev_mem_object.address

    if dst1_dev_mem == 0 or dst2_dev_mem == 0:
        return

    src = {
        'width': width,
        'height': height,
        'img_format': src_type,
        'pic_stride': [src_stride, src_stride, 0],
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0],
        'crop_x': width//4,
        'crop_y': height//4,
        'crop_width': width//2,
        'crop_height': height//2,
        'frame_size': src_size
    }

    dst_list = [
        {
            'width': dst1_width,
            'height': dst1_height,
            'img_format': dst_type,
            'pic_stride': [dst1_stride, dst1_stride, 0],
            'phy_addr': [dst1_dev_mem, 0, 0],
            'vir_addr': [0],
            'frame_size': dst1_size
        },
        {
            'width': dst2_width,
            'height': dst2_height,
            'img_format': dst_type,
            'pic_stride': [dst2_stride, dst2_stride, 0],
            'phy_addr': [dst2_dev_mem, 0, 0],
            'vir_addr': [0],
            'frame_size': dst2_size
        }
    ]

    aspect_ratio = {
        'aspect_ratio_mode': axcl.AX_IVPS_ASPECT_RATIO_STRETCH,
        'background_color': 0x000000,
        'alignments': [axcl.AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT, axcl.AX_IVPS_ASPECT_RATIO_VERTICAL_TOP],
        'rectangle': {
            'x': 0,
            'y': 0,
            'width': 0,
            'height': 0
        }
    }

    if engine == 'vpp':
        ret = axcl.ivps.crop_resize_v3_vpp(src, dst_list, aspect_ratio)

    if 0 == ret:
        print(f"crop_resize_v3_{engine} operation completed successfully")
        frame_type = _image_type_string(dst_type)
        file_name = f"crop_resize_v3_{engine}_output_image_{dst1_width}x{dst1_height}.{frame_type}"
        dst_file = AxcliteStoreFileFromDevice(dst1_dev_mem, dst1_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
        file_name = f"crop_resize_v3_{engine}_output_image_{dst2_width}x{dst2_height}.{frame_type}"
        dst_file = AxcliteStoreFileFromDevice(dst2_dev_mem, dst2_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"crop_resize_v3_{engine} failed with error code {ret}.")


def crop_resize_v4_test(src_file, dst_path, width, height, src_type, dst_type, engine):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()
    src_stride = axclite_get_stride(width, src_type)

    if src_dev_mem == 0:
        return

    dst_width = width//2
    dst_height = height//2
    dst_stride = axclite_get_stride(dst_width, dst_type)
    dst_size = axclite_get_image_size(dst_stride, dst_height, dst_type)
    dst_dev_mem_object = AxcliteDeviceMalloc(dst_size)
    dst_dev_mem = dst_dev_mem_object.address

    if dst_dev_mem == 0:
        return

    src = {
        'width': width,
        'height': height,
        'img_format': src_type,
        'pic_stride': [src_stride, src_stride, 0],
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0],
        'crop_x': width//4,
        'crop_y': height//4,
        'crop_width': width//2,
        'crop_height': height//2,
        'frame_size': src_size
    }

    dst = {
        'width': dst_width,
        'height': dst_height,
        'img_format': dst_type,
        'pic_stride': [dst_stride, dst_stride, 0],
        'phy_addr': [dst_dev_mem, 0, 0],
        'vir_addr': [0],
        'frame_size': dst_size
    }

    aspect_ratio = {
        'aspect_ratio_mode': axcl.AX_IVPS_ASPECT_RATIO_STRETCH,
        'background_color': 0x000000,
        'alignments': [axcl.AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT, axcl.AX_IVPS_ASPECT_RATIO_VERTICAL_TOP],
        'rectangle': {
            'x': 0,
            'y': 0,
            'width': 0,
            'height': 0
        }
    }

    scale_step = {
        'enabled': True,
        'scale_step_width': width//dst_width*1024,
        'scale_step_height': height//dst_height*1024
    }

    if engine == 'vgp':
        ret = axcl.ivps.crop_resize_v4_vgp(src, dst, aspect_ratio, scale_step)

    if 0 == ret:
        print(f"crop_resize_v4_{engine} operation completed successfully")
        frame_type = _image_type_string(dst_type)
        file_name = f"crop_resize_v4_{engine}_output_image_{dst_width}x{dst_height}.{frame_type}"
        dst_file = AxcliteStoreFileFromDevice(dst_dev_mem, dst_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"crop_resize_v4_{engine} failed with error code {ret}.")


def csc_test(src_file, dst_path, width, height, src_type, dst_type, engine):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()
    src_stride = axclite_get_stride(width, src_type)

    if src_dev_mem == 0:
        return

    dst_width = width
    dst_height = height
    dst_stride = axclite_get_stride(dst_width, dst_type)
    dst_size = axclite_get_image_size(dst_stride, dst_height, dst_type)
    dst_dev_mem_object = AxcliteDeviceMalloc(dst_size)
    dst_dev_mem = dst_dev_mem_object.address

    if dst_dev_mem == 0:
        return

    src = {
        'width': width,
        'height': height,
        'img_format': src_type,
        'pic_stride': [src_stride, src_stride, 0],
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0],
        'frame_size': src_size
    }

    dst = {
        'width': dst_width,
        'height': dst_height,
        'img_format': dst_type,
        'pic_stride': [dst_stride, src_stride, 0],
        'phy_addr': [dst_dev_mem, 0, 0],
        'vir_addr': [0],
        'frame_size': dst_size
    }

    if engine == 'vgp':
        ret = axcl.ivps.csc_vgp(src, dst)
    elif engine == 'vpp':
        ret = axcl.ivps.csc_vpp(src, dst)
    elif engine == 'tdp':
        ret = axcl.ivps.csc_tdp(src, dst)

    if 0 == ret:
        print(f"csc_{engine} operation completed successfully")
        frame_type = _image_type_string(dst_type)
        file_name = f"csc_{engine}_output_image_{dst_width}x{dst_height}.{frame_type}"
        dst_file = AxcliteStoreFileFromDevice(dst_dev_mem, dst_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"csc_{engine} failed with error code {ret}.")


def main(device_id, case_no, src_file, dst_path, width, height, frame_src_type, frame_dst_type, engine, api_version):
    src_type = _type_convert(frame_src_type)
    dst_type = _type_convert(frame_dst_type)

    if src_type == None or dst_type == None:
        print(f"unsupport frame_src_type: {frame_src_type} or frame_dst_type: {frame_dst_type}")
        return

    _init()

    if case_no == 'crop_resize':
        if engine == 'vgp':
            if api_version == 1:
                crop_resize_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            elif api_version == 2:
                crop_resize_v2_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            elif api_version == 4:
                crop_resize_v4_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            else:
                print(f"unsupport case: {case_no} engine: {engine} v{api_version}")
        elif engine == 'vpp':
            if api_version == 1:
                crop_resize_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            elif api_version == 2:
                crop_resize_v2_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            elif api_version == 3:
                crop_resize_v3_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            else:
                print(f"unsupport case: {case_no} engine: {engine} v{api_version}")
        elif engine == 'tdp':
            if api_version == 1:
                crop_resize_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            elif api_version == 2:
                crop_resize_v2_test(src_file, dst_path, width, height, src_type, dst_type, engine)
            else:
                print(f"unsupport case: {case_no} engine: {engine} v{api_version}")
        else:
            print(f"unsupport case: {case_no} {engine}")
    elif case_no == 'csc':
        if engine == 'vgp' or engine == 'vpp' or engine == 'tdp':
            csc_test(src_file, dst_path, width, height, src_type, dst_type, engine)
        else:
            print(f"unsupport case: {case_no} engine: {engine}")
    else:
        print(f"unsupport case: {case_no}")

    _deinit()


if __name__ == '__main__':
    print(f"============== sample ivps started ==============")

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', type=int, default=0,
                        help="device id, if 0 means auto select 1 from connected")
    parser.add_argument('--json', type=str, default='/usr/bin/axcl/axcl.json', help="axcl.json path")
    parser.add_argument('-c', '--case', type=str, default='crop_resize', help="case string, option: crop_resize/csc")
    parser.add_argument('-i', '--input', type=str, default='./data/1920x1080.nv12', help="input file")
    parser.add_argument('-o', '--output', type=str, default='/tmp/axcl/data/output', help="output path")
    parser.add_argument('-s', '--src_type', type=str, default='nv12', help="source frame type, option: nv12/nv21/rgb888/bgr888/rgb565/argb8888/rgba8888")
    parser.add_argument('-t', '--dst_type', type=str, default='nv12', help="destination frame type, option: nv12/nv21/rgb888/bgr888/rgb565/argb8888/rgba8888")
    parser.add_argument('-e', '--engine', type=str, default='vgp', help="engine type, option: vgp/vpp/tdp")
    parser.add_argument('-v', '--version', type=int, default=1, help="api version, option: 1/2/3/4")
    parser.add_argument('--width', type=int, default=1920, help="input file resolution width")
    parser.add_argument('--height', type=int, default=1080, help="input file resolution height")
    args = parser.parse_args()
    device_id = args.device
    json = args.json
    case_no = args.case
    src_file = args.input
    dst_path = args.output
    width = args.width
    height = args.height
    frame_src_type = args.src_type
    frame_dst_type = args.dst_type
    engine = args.engine
    api_version = args.version

    print(f"cmd args: device id={device_id}, json={json}")

    try:
        with axclite_system(json):
            device = AxcliteDevice(device_id)
            if device.create():
                main(device.device_id, case_no, src_file, dst_path, width, height, frame_src_type, frame_dst_type, engine, api_version)
                device.destroy()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())

    print("============== sample ivps exited ==============")
