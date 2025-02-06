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
from ctypes import memset







BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR + '/..')
sys.path.append(BASE_DIR + '/../..')


import axcl
from axclite.axclite_device import AxcliteDevice
from axclite.axclite_system import axclite_system
from axclite.axclite_utils import axclite_memcmp


def main(device_id):
    """
    loop memcpy sample:
            HOST          |               DEVICE
        host_mem[0] -----------> dev_mem[0]
                                     |---------> dev_mem[1]
        host_mem[1] <----------------------------------|
    """
    size = 8 * 1024 * 1024

    host_mem = [None, None]
    dev_mem = [None, None]

    print(f"alloc host and device memory, size: 0x{size:x}")

    is_ok = True

    for i in range(2):
        host_mem[i], ret = axcl.rt.malloc_host(size)
        if axcl.AXCL_SUCC != ret:
            is_ok = False
            break

        dev_mem[i], ret = axcl.rt.malloc(size, axcl.AXCL_MEM_MALLOC_NORMAL_ONLY)
        if axcl.AXCL_SUCC != ret:
            is_ok = False
            break

        print(f"memory [{i}]: host 0x{host_mem[i]:x}, device 0x{dev_mem[i]:x}")

    while is_ok:
        memset(host_mem[0], 0xA8, size)
        memset(host_mem[1], 0x00, size)

        print(f"memcpy from host memory[0] 0x{host_mem[0]:x} to device memory[0] 0x{dev_mem[0]:x}")
        ret = axcl.rt.memcpy(dev_mem[0], host_mem[0], size, axcl.AXCL_MEMCPY_HOST_TO_DEVICE)
        if axcl.AXCL_SUCC != ret:
            print(f"memcpy from host memory[0] 0x{host_mem[0]:x} to device memory[0] 0x{dev_mem[0]:x} fail, ret = 0x{ret&0xFFFFFFFF:x}")
            break

        print(f"memcpy device memory[0] 0x{dev_mem[0]:x} to device memory[1] 0x{dev_mem[1]:x}")
        ret = axcl.rt.memcpy(dev_mem[1], dev_mem[0], size, axcl.AXCL_MEMCPY_DEVICE_TO_DEVICE)
        if axcl.AXCL_SUCC != ret:
            print(f"memcpy from device memory 0x{dev_mem[0]:x} to device memory 0x{dev_mem[1]:x} fail, ret = 0x{ret&0xFFFFFFFF:x}")
            break

        print(f"memcpy device memory[1] 0x{dev_mem[1]:x} to host memory[1] 0x{host_mem[1]:x}")
        ret = axcl.rt.memcpy(host_mem[1], dev_mem[1], size, axcl.AXCL_MEMCPY_DEVICE_TO_HOST)
        if axcl.AXCL_SUCC != ret:
            print(f"memcpy from device memory 0x{dev_mem[1]:x} to host memory 0x{host_mem[1]:x} fail, ret = 0x{ret&0xFFFFFFFF:x}")
            break

        if 0 == axclite_memcmp(host_mem[0], host_mem[1], size):
            print(f"compare host memory[0] 0x{host_mem[0]:x} and host memory[1] 0x{host_mem[1]:x} success")
        else:
            print(f"compare host memory[0] 0x{host_mem[0]:x} and host memory[1] 0x{host_mem[1]:x} failure")

        break

    for i in range(2):
        if host_mem[i]:
            axcl.rt.free_host(host_mem[i])

        if dev_mem[i]:
            axcl.rt.free(dev_mem[i])


if __name__ == '__main__':
    print(f"============== sample memory started ==============")

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', type=int, default=0,
                        help="device id, if 0 means auto select 1 from connected")
    parser.add_argument('--json', type=str, default='/usr/bin/axcl/axcl.json', help="axcl.json path")
    args = parser.parse_args()
    device_id = args.device
    json = args.json
    print(f"cmd args: device id={device_id}, json={json}")

    try:
        with axclite_system(json):
            device = AxcliteDevice(device_id)
            if device.create():
                main(device.device_id)
                device.destroy()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())

    print("============== sample memory exited ==============")
