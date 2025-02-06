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

from ctypes import Structure, c_void_p, c_uint32, c_int32
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.axcl_base import *


class axclrtUtilizationInfo(Structure):
    """
    .. parsed-literal::

        dict_utilization_nfo = {
            "cpu_utilization": int,
            "npu_utilization": int,
            "mem_utilization": int,
            "ext_utilization": int
        }
    """
    _fields_ = [
        ("cpuUtilization", c_int32),
        ("npuUtilization", c_int32),
        ("memUtilization", c_int32),
        ("extUtilization", c_void_p)
    ]

    field_aliases = {
        "cpuUtilization": "cpu_utilization",
        "npuUtilization": "npu_utilization",
        "memUtilization": "mem_utilization",
        "extUtilization": "ext_utilization"
    }


class axclrtDeviceList(Structure):
    """
    .. parsed-literal::

        dict_device_list = {
            "num": int,
            "devices": [int]
        }
    """
    _fields_ = [
        ("num", c_uint32),
        ("devices", c_int32 * AXCL_MAX_DEVICE_COUNT)
    ]

    field_aliases = {
        "num": "num",
        "devices": "devices"
    }


axclrtMemMallocPolicy = c_int32
"""
    Memory malloc policy

    .. parsed-literal::

        AXCL_MEM_MALLOC_HUGE_FIRST = 0
        AXCL_MEM_MALLOC_HUGE_ONLY = 1
        AXCL_MEM_MALLOC_NORMAL_ONLY = 2
"""
AXCL_MEM_MALLOC_HUGE_FIRST = 0
AXCL_MEM_MALLOC_HUGE_ONLY = 1
AXCL_MEM_MALLOC_NORMAL_ONLY = 2


axclrtMemcpyKind = c_int32
"""
    Memory copy kind

    .. parsed-literal::

        AXCL_MEMCPY_HOST_TO_HOST = 0
        AXCL_MEMCPY_HOST_TO_DEVICE = 1
        AXCL_MEMCPY_DEVICE_TO_HOST = 2
        AXCL_MEMCPY_DEVICE_TO_DEVICE = 3
        AXCL_MEMCPY_HOST_PHY_TO_DEVICE = 4
        AXCL_MEMCPY_DEVICE_TO_HOST_PHY = 5
"""
AXCL_MEMCPY_HOST_TO_HOST = 0
AXCL_MEMCPY_HOST_TO_DEVICE = 1
AXCL_MEMCPY_DEVICE_TO_HOST = 2
AXCL_MEMCPY_DEVICE_TO_DEVICE = 3
AXCL_MEMCPY_HOST_PHY_TO_DEVICE = 4
AXCL_MEMCPY_DEVICE_TO_HOST_PHY = 5

