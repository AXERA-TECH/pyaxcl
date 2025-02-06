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
import ctypes
import traceback
from random import randint, choice

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

import axcl
from axcl.lib.axcl_lib import libaxcl_rt
from axcl.utils.axcl_utils import *
from axcl.utils.axcl_basestructure import BaseStructure


MAX_UINT64 = 2**64 - 1
MAX_UINT32 = 2**32 - 1


class DataArray(Structure):
    _fields_ = [
        ("data", c_void_p),
        ("size", c_uint32)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buf = None  # to hold buffer like create_string_buffer


def create_data_array_from_str(s: str) -> DataArray:
    bytes = s.encode("utf-8")
    buf = ctypes.create_string_buffer(bytes)
    arr = DataArray()
    arr.buf = buf
    arr.data = ctypes.cast(buf, ctypes.c_void_p)
    arr.size = len(bytes)
    return arr


def create_random_struct_instance(ctype, cobj=None):
    if issubclass(ctype, BaseStructure):
        if cobj is None:
            obj = ctype()
            obj.random_struct(obj)
            return obj
        else:
            cobj.random_struct(cobj)
            return cobj
    else:
        return create_random_ctypes_instance(ctype)


def random_initialize_struct(obj):
    obj.random_struct(obj)


def create_random_int(min_value=0, max_value=255):
    return randint(min_value, max_value)


def choose_random_from_list(elements: list):
    return choice(elements)


def create_random_ctypes_instance(ctype):
    size = ctypes.sizeof(ctype)
    mem = (ctypes.c_uint8 * size)()

    for i in range(size):
        mem[i] = randint(0, 255)

    return ctypes.cast(mem, ctypes.POINTER(ctype)).contents


def serialize_ctypes_args(*args):
    data = bytearray()

    for arg in args:
        if isinstance(arg, ctypes._SimpleCData):
            data.extend(ctypes.string_at(ctypes.addressof(arg), ctypes.sizeof(arg)))
        elif isinstance(arg, DataArray):
            if arg.data:
                data.extend(ctypes.string_at(arg.data, arg.size))
        elif isinstance(arg, ctypes.Structure):
            data.extend(bytes(arg))

        else:
            raise TypeError(f"Unsupported type: {type(arg)}")

    return bytes(data)


def check_input_output(inputs_args: bytes, output_args: bytes):
    ret = -1
    try:
        libaxcl_rt.AXCL_STUB_CheckInputAndOutput.restype = ctypes.c_int32
        libaxcl_rt.AXCL_STUB_CheckInputAndOutput.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32]

        inputs_ptr, inputs_len = (bytes_to_ptr(inputs_args), c_uint32(len(inputs_args))) if inputs_args else (c_void_p(0), c_uint32(0))
        output_ptr, output_len = (bytes_to_ptr(output_args), c_uint32(len(output_args))) if output_args else (c_void_p(0), c_uint32(0))

        # print(f"inputs_ptr = {inputs_ptr} inputs_args = {inputs_args}")
        ret = libaxcl_rt.AXCL_STUB_CheckInputAndOutput(inputs_ptr, inputs_len, output_ptr, output_len)
        # if ret != 0:
        #    bytes_data = ctypes.string_at(inputs_ptr, inputs_len.value)
        #    hex_str = ' '.join(f'{b:02x}' for b in bytes_data)
        #    print(f"inputs_args = {inputs_args}, inputs_len = {inputs_len}, inputs_ptr = {inputs_ptr} bytes_data = {bytes_data}")
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret
