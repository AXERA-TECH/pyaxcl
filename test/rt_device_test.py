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
from ut_help import *
from axcl.axcl_base import *
from axcl.rt.axcl_rt_type import *


class TestRtDevice:
    def test_set_device(self):
        device_id = create_random_int(1, AXCL_MAX_DEVICE_COUNT)
        ret = axcl.rt.set_device(device_id)
        inputs_args = serialize_ctypes_args(c_int32(device_id))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_reset_device(self):
        device_id = create_random_int(1, AXCL_MAX_DEVICE_COUNT)
        ret = axcl.rt.reset_device(device_id)
        inputs_args = serialize_ctypes_args(c_int32(device_id))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_device(self):
        device_id, ret = axcl.rt.get_device()
        output_args = serialize_ctypes_args(axclError(ret), c_int32(device_id))
        assert 0 == check_input_output(None, output_args)

    def test_get_device_count(self):
        count, ret = axcl.rt.get_device_count()
        output_args = serialize_ctypes_args(axclError(ret), c_int32(count))
        assert 0 == check_input_output(None, output_args)

    def test_get_device_list(self):
        dev_list, ret = axcl.rt.get_device_list()
        c_dev_list = axclrtDeviceList()
        c_dev_list.num = len(dev_list)
        for i in range(c_dev_list.num):
            c_dev_list.devices[i] = dev_list[i]
        output_args = serialize_ctypes_args(axclError(ret), c_dev_list)
        assert 0 == check_input_output(None, output_args)

    def test_synchronize_device(self):
        ret = axcl.rt.synchronize_device()
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(None, output_args)

    def test_get_device_utilization_rate(self):
        device_id = create_random_int(1, AXCL_MAX_DEVICE_COUNT)
        cpuUtilization, npuUtilization, memUtilization, ret = axcl.rt.get_device_utilization_rate(device_id)
        c_utilization_info = axclrtUtilizationInfo()
        c_utilization_info.cpuUtilization = cpuUtilization
        c_utilization_info.npuUtilization = npuUtilization
        c_utilization_info.memUtilization = memUtilization
        inputs_args = serialize_ctypes_args(c_int32(device_id))
        output_args = serialize_ctypes_args(axclError(ret), c_utilization_info)
        assert 0 == check_input_output(inputs_args, output_args)
