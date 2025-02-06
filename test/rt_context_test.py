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


class TestRtContext:
    def test_create_context(self):
        device_id = create_random_int(1, AXCL_MAX_DEVICE_COUNT)
        context, ret = axcl.rt.create_context(device_id)
        inputs_args = serialize_ctypes_args(c_int32(device_id))
        output_args = serialize_ctypes_args(axclError(ret), axclrtContext(context))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_destroy_context(self):
        context = create_random_int(1, MAX_UINT64)
        ret = axcl.rt.destroy_context(context)
        inputs_args = serialize_ctypes_args(axclrtContext(context))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_set_current_context(self):
        context = create_random_int(1, MAX_UINT64)
        ret = axcl.rt.set_current_context(context)
        inputs_args = serialize_ctypes_args(axclrtContext(context))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_current_context(self):
        context, ret = axcl.rt.get_current_context()
        output_args = serialize_ctypes_args(axclError(ret), axclrtContext(context))
        assert 0 == check_input_output(None, output_args)

    def test_get_default_context(self):
        device_id = create_random_int(1, AXCL_MAX_DEVICE_COUNT)
        context, ret = axcl.rt.get_default_context(device_id)
        inputs_args = serialize_ctypes_args(c_int32(device_id))
        output_args = serialize_ctypes_args(axclError(ret), axclrtContext(context))
        assert 0 == check_input_output(inputs_args, output_args)
