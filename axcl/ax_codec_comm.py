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

from ctypes import c_int32

AX_FRAME_TYPE_E = c_int32
"""
    Channel flag attribute.

    .. parsed-literal::

        AX_FRAME_TYPE_NONE = 0
        AX_FRAME_TYPE_AUTO = 1
        AX_FRAME_TYPE_IDR = 2
        AX_FRAME_TYPE_I = 3
        AX_FRAME_TYPE_P = 4
        AX_FRAME_TYPE_B = 5
        AX_FRAME_TYPE_BUTT = 6
"""
AX_FRAME_TYPE_NONE = 0
AX_FRAME_TYPE_AUTO = 1
AX_FRAME_TYPE_IDR = 2
AX_FRAME_TYPE_I = 3
AX_FRAME_TYPE_P = 4
AX_FRAME_TYPE_B = 5
AX_FRAME_TYPE_BUTT = 6


AX_AAC_TRANS_TYPE_E = c_int32
AX_AAC_TRANS_TYPE_UNKNOWN = -1
AX_AAC_TRANS_TYPE_RAW = 0
AX_AAC_TRANS_TYPE_ADTS = 2
AX_AAC_TRANS_TYPE_BUTT = 3



