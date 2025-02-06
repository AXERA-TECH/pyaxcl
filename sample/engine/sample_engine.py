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
from axcl.rt.axcl_rt_engine import *
from axcl.rt.axcl_rt_type import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR + "/..")
sys.path.append(BASE_DIR + "/../..")
from axclite.axclite_device import AxcliteDevice
from axclite.axclite_system import axclite_system


vnpu_str = ["Disable", "Enable", "BigLittle", "LittleBig"]
dtype_str = [
    "none",
    "int4",
    "uint4",
    "int8",
    "uint8",
    "int16",
    "uint16",
    "int32",
    "uint32",
    "int64",
    "uint64",
    "fp4",
    "fp8",
    "fp16",
    "bf16",
    "fp32",
    "fp64",
]
layout_str = ["none", "nhwc", "nchw"]


def on_release(model_id, info, io, ret=1):
    if info is not None and io is not None:
        input_count = engine_get_num_inputs(info)
        for i in range(input_count):
            buf, size, ret = engine_get_input_buffer_by_index(io, i)
            if 0 == ret and c_void_p(0) != buf:
                axcl.rt.free(buf)
        output_count = engine_get_num_outputs(info)
        for i in range(output_count):
            buf, size, ret = engine_get_output_buffer_by_index(io, i)
            if 0 == ret and c_void_p(0) != buf:
                axcl.rt.free(buf)
    if io is not None:
        engine_destroy_io(io)
    if info is not None:
        engine_destroy_io_info(info)
    if model_id is not None:
        engine_unload(model_id)
    _, ret = engine_get_vnpu_kind()
    if 0 == ret:
        engine_finalize()
    if 0 != ret:
        exit(ret)


def main(model, vnpu, warmup, repeat):
    ret = engine_init(vnpu)
    if 0 != ret:
        print("engine init failed with error code: %d" % ret)
    print(f"          vnpu: {vnpu_str[vnpu]}")

    model_id, ret = engine_load_from_file(model)
    if 0 != ret:
        print("engine load model file failed with error code: %d" % ret)
        on_release(None, None, None)

    model_type, ret = engine_get_model_type_from_model_id(model_id)
    if 0 != ret:
        print("engine get model type failed with error code: %d" % ret)
        on_release(model_id, None, None)
    print(f"          type: {model_type + 1} core")

    info, ret = engine_get_io_info(model_id)
    if 0 != ret:
        print("engine get model io info failed with error code: %d" % ret)
        on_release(model_id, None, None)

    io, ret = engine_create_io(info)
    if 0 != ret:
        print("engine create io failed with error code: %d" % ret)
        on_release(model_id, info, io)

    print(f"         input:")
    for i in range(engine_get_num_inputs(info)):
        name = engine_get_input_name_by_index(info, i)
        layout, _ = engine_get_input_data_layout(info, i)
        dtype, _ = engine_get_input_data_type(info, i)
        dims, _ = engine_get_input_dims(info, 0, i)
        size = engine_get_input_size_by_index(info, 0, i)
        print(
            f"                [{i}]: name='{name.decode()}', layout={layout_str[layout]}, dtype={dtype_str[dtype]}, dims={dims}, size={size}"
        )
        mem, ret = axcl.rt.malloc(size, AXCL_MEM_MALLOC_NORMAL_ONLY)
        if 0 != ret:
            print(f"axclrt malloc for '{name.decode()}' failed with error code: {ret}")
            on_release(model_id, info, io)
        ret = engine_set_input_buffer_by_index(io, i, mem, size)
        if 0 != ret:
            print(
                f"axclrt set io buffer for '{name.decode()}' failed with error code: {ret}"
            )

    print(f"        output:")
    for i in range(engine_get_num_outputs(info)):
        name = engine_get_output_name_by_index(info, i)
        layout, _ = engine_get_output_data_layout(info, i)
        dtype, _ = engine_get_output_data_type(info, i)
        dims, _ = engine_get_output_dims(info, 0, i)
        size = engine_get_output_size_by_index(info, 0, i)
        print(
            f"                [{i}]: name='{name.decode()}', layout={layout_str[layout]}, dtype={dtype_str[dtype]}, dims={dims}, size={size}"
        )
        mem, ret = axcl.rt.malloc(size, AXCL_MEM_MALLOC_NORMAL_ONLY)
        if 0 != ret:
            print(f"axclrt malloc for '{name.decode()}' failed with error code: {ret}")
            on_release(model_id, info, io)
        ret = engine_set_output_buffer_by_index(io, i, mem, size)
        if 0 != ret:
            print(
                f"axclrt set io buffer for '{name.decode()}' failed with error code: {ret}"
            )

    ctx, ret = engine_create_context(model_id)
    if 0 != ret:
        print("engine create context failed with error code: %d" % ret)

    for i in range(warmup):
        ret = engine_execute(model_id, ctx, 0, io)
        if 0 != ret:
            print("engine run model failed with error code: %d" % ret)
            break
    time_costs = []
    for i in range(repeat):
        t = time.time()
        ret = engine_execute(model_id, ctx, 0, io)
        time_costs.append(time.time() - t)
        if 0 != ret:
            print("engine run model failed with error code: %d" % ret)
            break

    on_release(model_id, info, io, ret)
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
    model = args.model
    vnpu = args.vnpu
    warmup = args.warmup
    repeat = args.repeat

    print(f"   Run AxModel:")
    print(f"         model: {model}")
    print(f"        warmup: {warmup}")
    print(f"        repeat: {repeat}")

    with axclite_system(json):
        device = AxcliteDevice(device_index)
        if device.create():
            main(model, vnpu, warmup, repeat)
            device.destroy()
