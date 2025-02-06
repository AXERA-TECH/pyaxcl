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

from ctypes import c_int32, c_void_p

NO_TIMEOUT = -1
AXCL_MAX_DEVICE_COUNT = 256

axclError = c_int32
axclrtContext = c_void_p
axclrtStream = c_void_p


AXCL_ERROR_E = c_int32
AXCL_SUCC                   = 0x00
AXCL_FAIL                   = 0x01
AXCL_ERR_UNKNOWN            = AXCL_FAIL
AXCL_ERR_NULL_POINTER       = 0x02
AXCL_ERR_ILLEGAL_PARAM      = 0x03
AXCL_ERR_UNSUPPORT          = 0x04
AXCL_ERR_TIMEOUT            = 0x05
AXCL_ERR_BUSY               = 0x06
AXCL_ERR_NO_MEMORY          = 0x07
AXCL_ERR_ENCODE             = 0x08
AXCL_ERR_DECODE             = 0x09
AXCL_ERR_UNEXPECT_RESPONSE  = 0x0A
AXCL_ERR_OPEN               = 0x0B
AXCL_ERR_EXECUTE_FAIL       = 0x0C
AXCL_ERR_BUTT               = 0x7F


AX_ID_AXCL = 0x30

# module
AXCL_RUNTIME         = 0x00
AXCL_NATIVE          = 0x01
AXCL_LITE            = 0x02

# runtime sub module
AXCL_RUNTIME_DEVICE  = 0x01
AXCL_RUNTIME_CONTEXT = 0x02
AXCL_RUNTIME_STREAM  = 0x03
AXCL_RUNTIME_TASK    = 0x04
AXCL_RUNTIME_MEMORY  = 0x05
AXCL_RUNTIME_CONFIG  = 0x06
AXCL_RUNTIME_ENGINE  = 0x07
AXCL_RUNTIME_SYSLOG  = 0x08
AXCL_RUNTIME_SYSCTRL = 0x09


def AXCL_DEF_ERR(module, sub, errid):
    return axclError(0x80000000 | ((module & 0x7F) << 24) | (AX_ID_AXCL << 16 ) | (sub << 8) | errid)

def AXCL_DEF_RUNTIME_ERR(sub, errid):
     AXCL_DEF_ERR(AXCL_RUNTIME, sub, errid)
def AXCL_DEF_NATIVE_ERR(sub, errid):
     AXCL_DEF_ERR(AXCL_NATIVE, sub, errid)
def AXCL_DEF_LITE_ERR(sub, errid):
     AXCL_DEF_ERR(AXCL_LITE, sub, errid)


