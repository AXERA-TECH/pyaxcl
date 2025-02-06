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

from ctypes import Structure, c_int32


AXCLRT_ENGINE_MAX_DIM_CNT = 32

axclrtEngineModelKind = c_int32
"""
    Engine model kind

    .. parsed-literal::

        AXCL_MODEL_TYPE_1CORE = 0
        AXCL_MODEL_TYPE_2CORE = 1
        AXCL_MODEL_TYPE_3CORE = 2
"""
AXCL_MODEL_TYPE_1CORE = 0
AXCL_MODEL_TYPE_2CORE = 1
AXCL_MODEL_TYPE_3CORE = 2

axclrtEngineVNpuKind = c_int32
"""
    Engine vnpu kind

    .. parsed-literal::

        AXCL_VNPU_DISABLE = 0
        AXCL_VNPU_ENABLE = 1
        AXCL_VNPU_BIG_LITTLE = 2
        AXCL_VNPU_LITTLE_BIG = 3
"""
AXCL_VNPU_DISABLE = 0
AXCL_VNPU_ENABLE = 1
AXCL_VNPU_BIG_LITTLE = 2
AXCL_VNPU_LITTLE_BIG = 3

axclrtEngineDataType = c_int32
"""
    Engine data type

    .. parsed-literal::

        AXCL_DATA_TYPE_NONE = 0
        AXCL_DATA_TYPE_INT4 = 1
        AXCL_DATA_TYPE_UINT4 = 2
        AXCL_DATA_TYPE_INT8 = 3
        AXCL_DATA_TYPE_UINT8 = 4
        AXCL_DATA_TYPE_INT16 = 5
        AXCL_DATA_TYPE_UINT16 = 6
        AXCL_DATA_TYPE_INT32 = 7
        AXCL_DATA_TYPE_UINT32 = 8
        AXCL_DATA_TYPE_INT64 = 9
        AXCL_DATA_TYPE_UINT64 = 10
        AXCL_DATA_TYPE_FP4 = 11
        AXCL_DATA_TYPE_FP8 = 12
        AXCL_DATA_TYPE_FP16 = 13
        AXCL_DATA_TYPE_BF16 = 14
        AXCL_DATA_TYPE_FP32 = 15
        AXCL_DATA_TYPE_FP64 = 16
"""
AXCL_DATA_TYPE_NONE = 0
AXCL_DATA_TYPE_INT4 = 1
AXCL_DATA_TYPE_UINT4 = 2
AXCL_DATA_TYPE_INT8 = 3
AXCL_DATA_TYPE_UINT8 = 4
AXCL_DATA_TYPE_INT16 = 5
AXCL_DATA_TYPE_UINT16 = 6
AXCL_DATA_TYPE_INT32 = 7
AXCL_DATA_TYPE_UINT32 = 8
AXCL_DATA_TYPE_INT64 = 9
AXCL_DATA_TYPE_UINT64 = 10
AXCL_DATA_TYPE_FP4 = 11
AXCL_DATA_TYPE_FP8 = 12
AXCL_DATA_TYPE_FP16 = 13
AXCL_DATA_TYPE_BF16 = 14
AXCL_DATA_TYPE_FP32 = 15
AXCL_DATA_TYPE_FP64 = 16

axclrtEngineDataLayout = c_int32
"""
    Engine vnpu kind

    .. parsed-literal::

        AXCL_DATA_LAYOUT_NONE = 0
        AXCL_DATA_LAYOUT_NHWC = 0
        AXCL_DATA_LAYOUT_NCHW = 1
"""
AXCL_DATA_LAYOUT_NONE = 0
AXCL_DATA_LAYOUT_NHWC = 0
AXCL_DATA_LAYOUT_NCHW = 1


class axclrtEngineIODims(Structure):
    """
    IO dims

    .. parsed-literal::

        list_dims = [int * AXCLRT_ENGINE_MAX_DIM_CNT]
    """
    _fields_ = [
        ("dimCount", c_int32),
        ("dims", c_int32 * AXCLRT_ENGINE_MAX_DIM_CNT)
    ]
