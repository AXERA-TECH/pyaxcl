
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


class TestRtStream:
    def test_create_stream(self):
        stream, ret = axcl.rt.create_stream()
        output_args = serialize_ctypes_args(axclError(ret), axclrtStream(stream))
        assert 0 == check_input_output(None, output_args)

    def test_destroy_stream(self):
        stream = create_random_int(1, MAX_UINT64)
        ret = axcl.rt.destroy_stream(stream)
        inputs_args = serialize_ctypes_args(axclrtStream(stream))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_destroy_stream_force(self):
        stream = create_random_int(1, MAX_UINT64)
        ret = axcl.rt.destroy_stream_force(stream)
        inputs_args = serialize_ctypes_args(axclrtStream(stream))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_synchronize_stream(self):
        stream = create_random_int(1, MAX_UINT64)
        ret = axcl.rt.synchronize_stream(stream)
        inputs_args = serialize_ctypes_args(axclrtStream(stream))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_synchronize_stream_with_timeout(self):
        stream = create_random_int(1, MAX_UINT64)
        timeout = create_random_int(-1, 1000000)
        ret = axcl.rt.synchronize_stream_with_timeout(stream, timeout)
        inputs_args = serialize_ctypes_args(axclrtStream(stream), c_int32(timeout))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)
