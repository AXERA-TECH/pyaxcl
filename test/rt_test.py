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
from ut_help import *


class TestRt:
    def test_init(self):
        ret = axcl.init('xxxx.json')
        assert 0 == ret

    def test_finalize(self):
        ret = axcl.finalize()
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(None, output_args)

    def test_set_log_level(self):
        lv = create_random_int(0, 10)
        ret = axcl.set_log_level(lv)
        inputs_args = serialize_ctypes_args(c_int32(lv))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_app_log(self):
        lv = create_random_int(0, 10)
        line = create_random_int(1, 100000)

        func = 'test_app_log'
        file = __file__
        argv = 'hello'
        axcl.app_log(lv, func, file, line, argv)

        c_func = create_data_array_from_str(func)
        c_file = create_data_array_from_str(file)
        c_argv = create_data_array_from_str(argv)
        inputs_args = serialize_ctypes_args(c_int32(lv), c_func, c_file, c_uint32(line), c_argv)
        assert 0 == check_input_output(inputs_args, None)

    def test_get_version(self):
        major, minor, patch, ret = axcl.rt.get_version()
        output_args = serialize_ctypes_args(axclError(ret), c_int32(major), c_int32(minor), c_int32(patch))
        assert 0 == check_input_output(None, output_args)

    def test_get_soc_name(self):
        soc_name = axcl.rt.get_soc_name()
        assert 'AX650N' == soc_name
