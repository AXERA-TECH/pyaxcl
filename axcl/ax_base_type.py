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

from ctypes import c_int32, c_uint32, c_char, c_int64, c_uint64, c_uint8, c_int8, c_float, c_uint16, c_int16, c_double, c_ulong, c_long

# types of variables typedef
AX_U64 = c_uint64
AX_U32 = c_uint32
AX_U16  = c_uint16
AX_U8  = c_uint8
AX_S64 = c_int64
AX_S32 = c_int32
AX_S16 = c_int16
AX_S8 = c_int8
AX_CHAR = c_char
AX_LONG  = c_long
AX_ULONG = c_ulong
AX_ADDR = c_ulong
AX_F32 = c_float
AX_F64 = c_double
AX_VOID = None
AX_SIZE_T = c_uint32

AX_BOOL = c_int32
AX_FALSE = 0
AX_TRUE  = 1

AX_NULL = 0
