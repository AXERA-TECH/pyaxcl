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

import argparse
import time

import axcl
from axcl.rt.axcl_rt_type import *
from axcl.utils import bytes_to_ptr

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR + "/..")
sys.path.append(BASE_DIR + "/../..")
from axclite.axclite_device import AxcliteDevice
from axclite.axclite_system import axclite_system


vnpu_str = ["Disable", "Enable", "BigLittle", "LittleBig"]
dtype_str = [
    "none",
    "uint8",
    "uint16",
    "fp32",
    "int16",
    "int8",
    "int32",
    "uint32",
    "fp64",
]
layout_str = ["none", "nhwc", "nchw"]


def on_release(vnpu, handle, io, ret=1):
    if io is not None:
        input_count = io["input_size"]
        for i in range(input_count):
            phy = io["inputs"][i]["physical_address"]
            if phy != 0:
                axcl.rt.free(c_void_p(phy))
        output_count = io["output_size"]
        for i in range(output_count):
            phy = io["outputs"][i]["physical_address"]
            if phy != 0:
                axcl.rt.free(c_void_p(phy))
    if handle is not None:
        axcl.npu.destroy_handle(handle)
    if vnpu is not None:
        axcl.npu.deinit()
    axcl.sys.deinit()
    if 0 != ret:
        exit(ret)


def main(vnpu, file, warmup, repeat):
    # init sys
    ret = axcl.sys.init()
    if axcl.AXCL_SUCC != ret:
        print(f"sys init failed, ret = 0x{ret&0xFFFFFFFF:x}")

    # init npu
    attr = {"eHardMode": vnpu}
    ret = axcl.npu.init(attr)
    if 0 != ret:
        print(f"engine init failed, ret = 0x{ret&0xFFFFFFFF:x}")
        on_release(None, None, None)
    print(f"          vnpu: {vnpu_str[vnpu]}")

    # load model
    with open(file, "rb") as model:
        buffer = model.read()
        size = os.path.getsize(file)
        host_ptr = bytes_to_ptr(buffer)
        dev_ptr, ret = axcl.rt.malloc(size, AXCL_MEM_MALLOC_NORMAL_ONLY)
        if 0 != ret:
            print(f"engine malloc device memory for model file failed, ret = 0x{ret&0xFFFFFFFF:x}")
            on_release(vnpu, None, None)

    ret = axcl.rt.memcpy(dev_ptr, host_ptr, size, axcl.AXCL_MEMCPY_HOST_TO_DEVICE)
    if 0 != ret:
        print(f"engine send model file to device failed, ret = 0x{ret&0xFFFFFFFF:x}")
        axcl.rt.free(dev_ptr)
        on_release(vnpu, None, None)

    handle, ret = axcl.npu.create_handle(dev_ptr, size)
    axcl.rt.free(dev_ptr)
    if 0 != ret:
        print(f"engine load model file failed, ret = 0x{ret&0xFFFFFFFF:x}")
        on_release(vnpu, None, None)

    model_type, ret = axcl.npu.get_handle_model_type(handle)
    if 0 != ret:
        print(f"engine get model type failed, ret = 0x{ret&0xFFFFFFFF:x}")
        on_release(vnpu, handle, None)
    print(f"          type: {model_type + 1} core")

    info, ret = axcl.npu.get_io_info(handle)
    if 0 != ret:
        print(f"engine io_info failed, ret = 0x{ret&0xFFFFFFFF:x}")
        on_release(vnpu, handle, None)

    print("         input:")
    for i, meta in enumerate(info["inputs"]):
        name = meta["name"].decode()
        layout = layout_str[meta["layout"]]
        dtype = dtype_str[meta["data_type"]]
        size = meta["size"]
        dims = []
        for j in range(meta["shape_size"]):
            dims.append(meta["shape"][j])
        print(
            f"                [{i}]: name='{name}', layout={layout}, dtype={dtype}, dims={dims}, size={size}"
        )

    print("        output:")
    for i, meta in enumerate(info["outputs"]):
        name = meta["name"].decode()
        layout = layout_str[meta["layout"]]
        dtype = dtype_str[meta["data_type"]]
        size = meta["size"]
        dims = []
        for j in range(meta["shape_size"]):
            dims.append(meta["shape"][j])
        print(
            f"                [{i}]: name='{name}', layout={layout}, dtype={dtype}, dims={dims}, size={size}"
        )

    ctx, ret = axcl.npu.create_context_v2(handle)
    if 0 != ret:
        print(f"engine create context failed, ret = 0x{ret&0xFFFFFFFF:x}")
        on_release(vnpu, handle, info)

    # input buffer
    input_count = len(info["inputs"])
    input_buffers = []
    for i, meta in enumerate(info["inputs"]):
        size = meta["size"]
        phy, ret = axcl.rt.malloc(size, AXCL_MEM_MALLOC_NORMAL_ONLY)
        if 0 != ret:
            print(f"engine malloc device memory for input failed, ret = 0x{ret&0xFFFFFFFF:x}")
            phy = 0
        buf = {
            "physical_address": phy.value,
            "virtual_address": 0,
            "size": size,
            "pStride": None,
            "stride_size": 0,
        }
        input_buffers.append(buf)

    # output buffer
    output_count = len(info["outputs"])
    output_buffers = []
    for i, meta in enumerate(info["outputs"]):
        size = meta["size"]
        phy, ret = axcl.rt.malloc(size, AXCL_MEM_MALLOC_NORMAL_ONLY)
        if 0 != ret:
            print(f"engine malloc device memory for output failed, ret = 0x{ret&0xFFFFFFFF:x}")
            phy = 0
        buf = {
            "physical_address": phy.value,
            "virtual_address": 0,
            "size": size,
            "pStride": None,
            "stride_size": 0,
        }
        output_buffers.append(buf)

    io = {
        "inputs": input_buffers,
        "outputs": output_buffers,
        "input_size": input_count,
        "output_size": output_count,
        "batch_size": 0,
        "parallel_run": 0,
    }

    # warmup
    for i in range(warmup):
        ret = axcl.npu.run_sync_v2(handle, ctx, io)
        if 0 != ret:
            print(f"engine run sync failed, ret = 0x{ret&0xFFFFFFFF:x}")
            on_release(vnpu, handle, io)

    # run
    time_costs = []
    for i in range(repeat):
        t = time.time()
        ret = axcl.npu.run_sync_v2(handle, ctx, io)
        time_costs.append(time.time() - t)
        if 0 != ret:
            print(f"engine run sync failed, ret = 0x{ret&0xFFFFFFFF:x}")
            on_release(vnpu, handle, io)

    on_release(vnpu, handle, io, ret)
    time_costs = [cost * 1000 for cost in time_costs]
    print("  ------------------------------------------------------")
    print(
        f"  min =   {min(time_costs):.3f} ms   max =   {max(time_costs):.3f} ms   avg =   {sum(time_costs) / len(time_costs):.3f} ms"
    )
    print("  ------------------------------------------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--device",
        type=int,
        default=0,
        help="device id, if 0 means auto select 1 from connected",
    )
    parser.add_argument(
        "--json", type=str, default="/usr/bin/axcl/axcl.json", help="axcl.json path"
    )
    parser.add_argument("-m", "--model", type=str, help="axmodel path")
    parser.add_argument("-v", "--vnpu", type=int, default=0, help="vnpu kind")
    parser.add_argument(
        "-w", "--warmup", type=int, default=1, help=" model warmup times"
    )
    parser.add_argument(
        "-r", "--repeat", type=int, default=5, help="model running repeat times"
    )
    args = parser.parse_args()
    device_index = args.device
    json = args.json
    file = args.model
    vnpu = args.vnpu
    warmup = args.warmup
    repeat = args.repeat

    print(f"   Run AxModel:")
    print(f"         model: {file}")
    print(f"        warmup: {warmup}")
    print(f"        repeat: {repeat}")

    with axclite_system(json):
        device = AxcliteDevice(device_index)
        if device.create():
            main(vnpu, file, warmup, repeat)
            device.destroy()
