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


def _init():
    ret = axcl.sys.init()
    if axcl.AXCL_SUCC != ret:
        print(f"axcl.sys.init() fail, ret = 0x{ret&0xFFFFFFFF:x}")

    ret = axcl.ive.init()
    if axcl.AXCL_SUCC != ret:
        print(f"axcl.ive.init() fail, ret = 0x{ret&0xFFFFFFFF:x}")


def _deinit():
    axcl.ive.exit()

    ret = axcl.sys.deinit()
    if axcl.AXCL_SUCC != ret:
        print(f"axcl.sys.deinit() fail, ret = 0x{ret&0xFFFFFFFF:x}")


def _dma_test(src_file, dst_path, width, height):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()

    if src_dev_mem == 0:
        return

    dst_dev_mem_object = AxcliteDeviceMalloc(src_size)
    dst_dev_mem = dst_dev_mem_object.address

    if dst_dev_mem == 0:
        return

    src = {
        'phy_addr': src_dev_mem,
        'vir_addr': 0,
        'stride': width,
        'width': width,
        'height': height
    }

    dst = {
        'phy_addr': dst_dev_mem,
        'vir_addr': 0,
        'stride': width,
        'width': width,
        'height': height
    }

    ctrl = {
        'mode': axcl.AX_IVE_DMA_MODE_DIRECT_COPY,
        'val': 0,
        'hor_seg_size': 0,
        'elem_size': 0,
        'ver_seg_rows': 0,
        'crp_x': 0,
        'crp_y': 0
    }

    instant = True

    handle, ret = axcl.ive.dma(src, dst, ctrl, instant)

    if ret == 0:
        print("dma operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")

        file_path = Path(src_file)
        file_name = file_path.name

        file_name = "out_dma" + "_" + file_name

        dst_file = AxcliteStoreFileFromDevice(dst_dev_mem, src_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"dma operation failed with error code {ret}.")


def _filter_test(src_file, dst_path, width, height, frame_type):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()

    if src_dev_mem == 0:
        return

    dst_dev_mem_object = AxcliteDeviceMalloc(src_size)
    dst_dev_mem = dst_dev_mem_object.address

    if dst_dev_mem == 0:
        return

    src = {
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0, 0, 0],
        'stride': [width, width, 0],
        'width': width,
        'height': height,
        'type': frame_type
    }

    dst = {
        'phy_addr': [dst_dev_mem, 0, 0],
        'vir_addr': [0, 0, 0],
        'stride': [width, width, 0],
        'width': width,
        'height': height,
        'type': frame_type
    }

    ctrl = {
        'mask': [
            -60926, -48381, -47545, 33147, 49431,
            63723, -64488, 37430, -27681, -48659,
            19031, -16709, 26667, 2023, 51858,
            -34899, 19455, 19648, 55833, -2102,
            47260, -11678, 13204, 20532, -2051
        ]
    }

    instant = True

    handle, ret = axcl.ive.filter(src, dst, ctrl, instant)

    if ret == 0:
        print("dma operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")

        file_path = Path(src_file)
        file_name = file_path.name

        file_name = "out_filter" + "_" + file_name

        dst_file = AxcliteStoreFileFromDevice(dst_dev_mem, src_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"filter operation failed with error code {ret}.")


def _gmm2_test(src_file, dst_path, width, height, model, frame_type):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()

    if src_dev_mem == 0:
        return

    model_file_object = AxcliteLoadFileToDevice(model)
    model_dev_mem, model_size = model_file_object.result()

    if model_dev_mem == 0:
        return

    dst_fg_dev_mem_object = AxcliteDeviceMalloc(src_size)
    dst_fg_dev_mem = dst_fg_dev_mem_object.address

    dst_bg_dev_mem_object = AxcliteDeviceMalloc(src_size)
    dst_bg_dev_mem = dst_bg_dev_mem_object.address

    src = {
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0, 0, 0],
        'stride': [width, width, 0],
        'width': width,
        'height': height,
        'type': frame_type
    }

    dst_fg = {
        'phy_addr': [dst_fg_dev_mem, 0, 0],
        'vir_addr': [0, 0, 0],
        'stride': [width, width, 0],
        'width': width,
        'height': height,
        'type': frame_type
    }

    dst_bg = {
        'phy_addr': [dst_bg_dev_mem, 0, 0],
        'vir_addr': [0, 0, 0],
        'stride': [width, width, 0],
        'width': width,
        'height': height,
        'type': frame_type
    }

    model = {
        'phy_addr': model_dev_mem,
        'vir_addr': 0,
        'size': model_size
    }

    ctrl = {
        'init_var': 202820,
        'min_var': 110515,
        'max_var': 197086,
        'learn_rate': 114,
        'bg_ratio': 124,
        'var_thr': 84,
        'var_thr_check': 243,
        'ct': 31,
        'thr': 199
    }

    instant = True

    handle, ret = axcl.ive.gmm2(src, dst_fg, dst_bg, model, ctrl, instant)

    if ret == 0:
        print("dma operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst_fg: {dst_fg}")
        print(f"dst_bg: {dst_bg}")

        # fg
        file_path = Path(src_file)
        file_name = file_path.name

        file_name = "out_gmm2_fg" + "_" + file_name

        dst_file = AxcliteStoreFileFromDevice(dst_fg_dev_mem, src_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")

        # bg
        file_path = Path(src_file)
        file_name = file_path.name

        file_name = "out_gmm2_bg" + "_" + file_name

        dst_file = AxcliteStoreFileFromDevice(dst_bg_dev_mem, src_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"gmm2 operation failed with error code {ret}.")


def _crop_resize_test(src_file, dst_path, width, height, frame_type, engine):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, src_size = src_file_object.result()

    if src_dev_mem == 0:
        return

    dst_dev_mem_object = AxcliteDeviceMalloc(src_size)
    dst_dev_mem = dst_dev_mem_object.address

    if dst_dev_mem == 0:
        return

    src = {
        'phy_addr': [src_dev_mem, 0, 0],
        'vir_addr': [0, 0, 0],
        'stride': [width, width, 0],
        'width': width,
        'height': height,
        'type' if engine == 0 else 'glb_type': frame_type
    }

    dst = [
        {
            'phy_addr': [dst_dev_mem, 0, 0],
            'vir_addr': [0, 0, 0],
            'stride': [width, width, 0],
            'width': width,
            'height': height,
            'type' if engine == 0 else 'glb_type': frame_type
        }
    ]

    box = [
        {
            'x': 0,
            'y': 0,
            'w': 640,
            'h': 360
        }
    ]

    ctrl = {
        'num': 1,
        'align': [axcl.AX_IVE_ASPECT_RATIO_FORCE_RESIZE, axcl.AX_IVE_ASPECT_RATIO_FORCE_RESIZE],
        'border_color': 255
    }

    instant = True

    handle, ret = axcl.ive.crop_resize(src, dst, box, ctrl, engine, instant)

    if ret == 0:
        print("dma operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")

        file_path = Path(src_file)
        file_name = file_path.name

        file_name = "out_crop_resize" + "_" + file_name

        dst_file = AxcliteStoreFileFromDevice(dst_dev_mem, src_size, dst_path, file_name).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"crop_resize operation failed with error code {ret}.")


def main(device_id, case_no, src_file, dst_path, width, height, model, frame_type, engine):
    _init()

    if case_no == 0:
        _dma_test(src_file, dst_path, width, height)
    elif case_no == 1:
        _filter_test(src_file, dst_path, width, height, frame_type)
    elif case_no == 2:
        _gmm2_test(src_file, dst_path, width, height, model, frame_type)
    elif case_no == 3:
        _crop_resize_test(src_file, dst_path, width, height, frame_type, engine)

    _deinit()


if __name__ == '__main__':
    print(f"============== sample ive started ==============")

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', type=int, default=0,
                        help="device id, if 0 means auto select 1 from connected")
    parser.add_argument('--json', type=str, default='/usr/bin/axcl/axcl.json', help="axcl.json path")
    parser.add_argument('-c', '--case', type=int, default=0, help="case number")
    parser.add_argument('-i', '--input', type=str, default='./data/common/1280x720_u8c1_gray.yuv', help="input file")
    parser.add_argument('-o', '--output', type=str, default='/tmp/axcl/data/output', help="output path")
    parser.add_argument('-t', '--type', type=int, default=0, help="frame type")
    parser.add_argument('-e', '--engine', type=int, default=0, help="engine type")
    parser.add_argument('--width', type=int, default=1280, help="input file resolution width")
    parser.add_argument('--height', type=int, default=720, help="input file resolution height")
    parser.add_argument('--model', type=str, default='./data/gmm/gmm_gray_1280x720_model.bin', help="model file")
    args = parser.parse_args()
    device_id = args.device
    json = args.json
    case_no = args.case
    src_file = args.input
    dst_path = args.output
    width = args.width
    height = args.height
    model = args.model
    frame_type = args.type
    engine = args.engine

    print(f"cmd args: device id={device_id}, json={json}")

    try:
        with axclite_system(json):
            device = AxcliteDevice(device_id)
            if device.create():
                main(device.device_id, case_no, src_file, dst_path, width, height, model, frame_type, engine)
                device.destroy()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())

    print("============== sample ive exited ==============")
