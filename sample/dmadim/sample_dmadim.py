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


def _deinit():
    ret = axcl.sys.deinit()
    if axcl.AXCL_SUCC != ret:
        print(f"axcl.sys.deinit() fail, ret = 0x{ret&0xFFFFFFFF:x}")


def dma_copy():
    dev_mem_object = [None, None]
    dev_mem = [None, None]
    size = 4 * 1024 * 1024

    for i in range(2):
        dev_mem_object[i] = AxcliteDeviceMalloc(size)
        dev_mem[i] = dev_mem_object[i].address
        print(f"memory [{i}]: device 0x{dev_mem[i]:x}")

    ret = axcl.rt.memset(dev_mem[0], 0xAA, size)
    ret = axcl.dmadim.mem_copy(dev_mem[1], dev_mem[0], size)
    ret = axcl.rt.memset(dev_mem[0], 0xAA, size)
    if 0 == axcl.rt.memcmp(dev_mem[0], dev_mem[1], size):
        print(f"dma_copy: compare dev memory[0] 0x{dev_mem[0]:x} and dev memory[1] 0x{dev_mem[1]:x} successfully")
    else:
        print(f"dma_copy: compare dev memory[0] 0x{dev_mem[0]:x} and dev memory[1] 0x{dev_mem[1]:x} failed")


def dma_memset():
    size = 4 * 1024 * 1024

    dev_mem_object = AxcliteDeviceMalloc(size)
    dev_mem = dev_mem_object.address
    print(f"memory : device 0x{dev_mem:x}")

    ret = axcl.dmadim.mem_set(dev_mem, 0xAA, size)

    if 0 == ret:
        print(f"dma_memset: memset 0x{dev_mem:x} operation completed successfully.")
    else:
        print(f"dma_memset: memset failed with error code {ret}.")


def dma_checksum():
    size = 4 * 1024 * 1024

    dev_mem_object = AxcliteDeviceMalloc(size)
    dev_mem = dev_mem_object.address
    print(f"memory : device 0x{dev_mem:x}")

    ret = axcl.dmadim.mem_set(dev_mem, 0xAA, size)

    checksum, ret = axcl.dmadim.checksum(dev_mem, size)

    if 0 == ret:
        print(f"dma_checksum: checksum: 0x{checksum:x} successfully")
    else:
        print(f"dma_checksum: checksum failed with error code {ret}.")


def dma_copy2d(src_file, dst_path, width, height):
    src_file_object = AxcliteLoadFileToDevice(src_file)
    src_dev_mem, size = src_file_object.result()

    if src_dev_mem == 0:
        return

    # Y
    dst_width = width // 2
    dst_height = height // 2
    dst_y_size = dst_width * dst_height
    dst_y_dev_mem_object = AxcliteDeviceMalloc(dst_y_size)
    dst_y_dev_mem = dst_y_dev_mem_object.address
    # UV
    dst_uv_width = dst_width
    dst_uv_height = dst_height // 2
    dst_uv_size = dst_uv_width * dst_uv_height
    dst_uv_dev_mem_object = AxcliteDeviceMalloc(dst_uv_size)
    dst_uv_dev_mem = dst_uv_dev_mem_object.address

    dim_desc = [
        # Y
        {
            'n_tiles': [dst_height],
            'src_info': {
                'phy_addr': src_dev_mem,
                'img_w': dst_width,
                'stride': [width]
            },
            'dst_info': {
                'phy_addr': dst_y_dev_mem,
                'img_w': dst_width,
                'stride': [dst_width]
            }
        },
        # UV
        {
            'n_tiles': [dst_uv_height],
            'src_info': {
                'phy_addr': src_dev_mem + width * height,
                'img_w': dst_uv_width,
                'stride': [width]
            },
            'dst_info': {
                'phy_addr': dst_uv_dev_mem,
                'img_w': dst_uv_width,
                'stride': [dst_uv_width]
            }
        },
    ]

    mode = axcl.AX_DMADIM_2D

    for i in range(2):
        ret = axcl.dmadim.mem_copy_xd(dim_desc[i], mode)

        if ret != 0:
            break

    if 0 == ret:
        print(f"dma_copy2d: mem_copy_xd operation completed successfully")
        file_name = f"dma2d_output_image_{dst_width}x{dst_height}.nv12"
        dst_file = AxcliteStoreFileFromDevice(dst_y_dev_mem, dst_y_size, dst_path, file_name).result()
        dst_file = AxcliteStoreFileFromDevice(dst_uv_dev_mem, dst_uv_size, dst_path, file_name, True).result()
        if dst_file != None:
            print(f"store file '{dst_file}' successfully.")
    else:
        print(f"dma_copy2d: mem_copy_xd failed with error code {ret}.")


def main(device_id, src_file, dst_path, width, height):
    _init()

    dma_copy()
    dma_memset()
    dma_checksum()
    dma_copy2d(src_file, dst_path, width, height)

    _deinit()


if __name__ == '__main__':
    print(f"============== sample dmadim started ==============")

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', type=int, default=0,
                        help="device id, if 0 means auto select 1 from connected")
    parser.add_argument('--json', type=str, default='/usr/bin/axcl/axcl.json', help="axcl.json path")
    parser.add_argument('-i', '--input', type=str, default='./data/1280x720_nv12.yuv', help="input file")
    parser.add_argument('-o', '--output', type=str, default='/tmp/axcl/data/output', help="output path")
    parser.add_argument('--width', type=int, default=1280, help="input file resolution width")
    parser.add_argument('--height', type=int, default=720, help="input file resolution height")
    args = parser.parse_args()
    device_id = args.device
    json = args.json
    src_file = args.input
    dst_path = args.output
    width = args.width
    height = args.height

    print(f"cmd args: device id={device_id}, json={json}")

    try:
        with axclite_system(json):
            device = AxcliteDevice(device_id)
            if device.create():
                main(device.device_id, src_file, dst_path, width, height)
                device.destroy()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())

    print("============== sample dmadim exited ==============")
