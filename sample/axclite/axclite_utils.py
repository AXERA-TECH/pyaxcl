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
import ctypes
import sys
import traceback

import axcl


def axclite_align_up(x, align):
    return (x + (align - 1)) & ~(align - 1)


def axclite_align_down(x, align):
    return x & ~(align - 1)


def axclite_memcmp(s1: ctypes.c_void_p, s2: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
    try:
        libc = ctypes.CDLL(None)
        libc.memcmp.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
        libc.memcmp.restype = ctypes.c_int
        ret = libc.memcmp(s1, s2, n)
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def axclite_get_stride(width, type):
    if type == axcl.AX_FORMAT_YUV420_SEMIPLANAR:
        return width
    elif type == axcl.AX_FORMAT_YUV420_SEMIPLANAR_VU:
        return width
    elif type == axcl.AX_FORMAT_RGB888:
        return width * 3
    elif type == axcl.AX_FORMAT_BGR888:
        return width * 3
    elif type == axcl.AX_FORMAT_RGB565:
        return width * 2
    elif type == axcl.AX_FORMAT_ARGB8888:
        return width * 4
    elif type == axcl.AX_FORMAT_RGBA8888:
        return width * 4
    else:
        return width


def axclite_get_image_size(stride, height, type):
    if type == axcl.AX_FORMAT_YUV420_SEMIPLANAR:
        return int(stride * height * 3 / 2)
    elif type == axcl.AX_FORMAT_YUV420_SEMIPLANAR_VU:
        return int(stride * height * 3 / 2)
    elif type == axcl.AX_FORMAT_RGB888:
        return int(stride * height)
    elif type == axcl.AX_FORMAT_BGR888:
        return int(stride * height)
    elif type == axcl.AX_FORMAT_RGB565:
        return int(stride * height)
    elif type == axcl.AX_FORMAT_ARGB8888:
        return int(stride * height)
    elif type == axcl.AX_FORMAT_RGBA8888:
        return int(stride * height)
    else:
        return int(stride * height)