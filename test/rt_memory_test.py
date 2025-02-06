
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

import axcl
from axcl.axcl_base import *
from axcl.rt.axcl_rt_type import *
from ut_help import *


class TestRtMemory:
    def test_malloc(self):
        size = create_random_int(1, 4*1024*1024*1024)
        policy = choose_random_from_list([AXCL_MEM_MALLOC_HUGE_FIRST, AXCL_MEM_MALLOC_HUGE_ONLY, AXCL_MEM_MALLOC_NORMAL_ONLY])
        ptr, ret = axcl.rt.malloc(size, policy)
        inputs_args = serialize_ctypes_args(c_size_t(size), axclrtMemMallocPolicy(policy))
        output_args = serialize_ctypes_args(axclError(ret), c_void_p(ptr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_malloc_cached(self):
        size = create_random_int(1, 4*1024*1024*1024)
        policy = choose_random_from_list([AXCL_MEM_MALLOC_HUGE_FIRST, AXCL_MEM_MALLOC_HUGE_ONLY, AXCL_MEM_MALLOC_NORMAL_ONLY])
        ptr, ret = axcl.rt.malloc_cached(size, policy)
        inputs_args = serialize_ctypes_args(c_size_t(size), axclrtMemMallocPolicy(policy))
        output_args = serialize_ctypes_args(axclError(ret), c_void_p(ptr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_free(self):
        ptr = create_random_int(1, MAX_UINT64)
        ret = axcl.rt.free(ptr)
        inputs_args = serialize_ctypes_args(c_void_p(ptr))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_flush(self):
        ptr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, 4*1024*1024*1024)
        ret = axcl.rt.mem_flush(ptr, size)
        inputs_args = serialize_ctypes_args(c_void_p(ptr), c_size_t(size))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_invalidate(self):
        ptr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, 4*1024*1024*1024)
        ret = axcl.rt.mem_invalidate(ptr, size)
        inputs_args = serialize_ctypes_args(c_void_p(ptr), c_size_t(size))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_malloc_host(self):
        size = create_random_int(1, 4*1024*1024*1024)
        ptr, ret = axcl.rt.malloc_host(size)
        inputs_args = serialize_ctypes_args(c_size_t(size))
        output_args = serialize_ctypes_args(axclError(ret), c_void_p(ptr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_free_host(self):
        ptr = create_random_int(1, MAX_UINT64)
        ret = axcl.rt.free_host(ptr)
        inputs_args = serialize_ctypes_args(c_void_p(ptr))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_memset(self):
        ptr = create_random_int(1, MAX_UINT64)
        val = create_random_int(0, 255)
        cnt = create_random_int(1, 1*1024*1024*1024)
        ret = axcl.rt.memset(ptr, val, cnt)
        inputs_args = serialize_ctypes_args(c_void_p(ptr), c_uint8(val), c_size_t(cnt))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_memcpy(self):
        kind = choose_random_from_list([AXCL_MEMCPY_HOST_TO_HOST,
                                        AXCL_MEMCPY_HOST_TO_DEVICE,
                                        AXCL_MEMCPY_DEVICE_TO_HOST,
                                        AXCL_MEMCPY_DEVICE_TO_DEVICE,
                                        AXCL_MEMCPY_HOST_PHY_TO_DEVICE,
                                        AXCL_MEMCPY_DEVICE_TO_HOST_PHY])

        src = create_random_int(1, MAX_UINT64)
        dst = create_random_int(1, MAX_UINT64)
        cnt = create_random_int(1, 4*1024*1024*1024)
        ret = axcl.rt.memcpy(dst, src, cnt, kind)
        inputs_args = serialize_ctypes_args(c_void_p(dst), c_void_p(src), c_size_t(cnt), axclrtMemcpyKind(kind))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_memcmp(self):
        pt1 = create_random_int(1, MAX_UINT64)
        pt2 = create_random_int(1, MAX_UINT64)
        cnt = create_random_int(1, 4*1024*1024*1024)
        ret = axcl.rt.memcmp(pt1, pt2, cnt)
        inputs_args = serialize_ctypes_args(c_void_p(pt1), c_void_p(pt2), c_size_t(cnt))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)
