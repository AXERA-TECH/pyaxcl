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

from ctypes import *
import os
import sys
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.lib.axcl_lib import libaxcl_rt
from axcl.axcl_base import *
from axcl.utils.axcl_logger import *


def create_context(device_id: int) -> tuple[int, int]:
    """
    Create context

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtCreateContext(axclrtContext *context, int32_t deviceId);`
        **python**              `context, ret = axcl.rt.create_context(device_id)`
        ======================= =====================================================

    :param int device_id: device id.
    :returns: tuple[int, int]

        - **context** (*int*) - context handle.
        - **ret** (*int*) - 0 indicates success, otherwise failure

    .. note::

        If device has not been actived, `create_context` will active device first.
    """
    ret = -1
    context = c_void_p(0)
    try:
        libaxcl_rt.axclrtCreateContext.restype = axclError
        libaxcl_rt.axclrtCreateContext.argtypes=[POINTER(c_void_p), c_int32]
        deviceId = c_int32(device_id)

        ret = libaxcl_rt.axclrtCreateContext(byref(context), deviceId)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return context.value, ret


def destroy_context(context: int) -> int:
    """
    Destroy context

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtDestroyContext(axclrtContext context);`
        **python**              `ret = axcl.rt.destroy_context(context)`
        ======================= =====================================================

    :param int context: context handle.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtDestroyContext.restype = axclError
        libaxcl_rt.axclrtDestroyContext.argtypes=[c_void_p]
        if context:
            c_context = c_void_p(context)
            ret = libaxcl_rt.axclrtDestroyContext(c_context)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_current_context(context: int) -> int:
    """
    Set current context

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtSetCurrentContext(axclrtContext context)`
        **python**              `ret = axcl.rt.set_current_context(context)`
        ======================= =====================================================

    :param int context: context handle.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtSetCurrentContext.restype = axclError
        libaxcl_rt.axclrtSetCurrentContext.argtypes=[c_void_p]
        if context:
            c_context = c_void_p(context)
            ret = libaxcl_rt.axclrtSetCurrentContext(c_context)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_current_context() -> tuple[int, int]:
    """
    Get current context

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtGetCurrentContext(axclrtContext *context);`
        **python**              `context, ret = axcl.rt.get_current_context()`
        ======================= =====================================================

    :returns: tuple[int, int]

        - **context** (*int*) - context handle.
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    context = c_void_p(0)
    try:
        libaxcl_rt.axclrtGetCurrentContext.restype = axclError
        libaxcl_rt.axclrtGetCurrentContext.argtypes=[POINTER(c_void_p)]
        ret = libaxcl_rt.axclrtGetCurrentContext(byref(context))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return context.value, ret


def get_default_context(device_id: int) -> tuple[int, int]:
    """
    Get default context

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtGetDefaultContext(axclrtContext *context, int32_t deviceId)`
        **python**              `context, ret = axcl.rt.get_default_context(device_id)`
        ======================= =====================================================

    :param int device_id: device id.
    :returns: tuple[int, int]

        - **context** (*int*) - context handle.
        - **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    context = c_void_p(0)
    try:
        libaxcl_rt.axclrtGetDefaultContext.restype = axclError
        libaxcl_rt.axclrtGetDefaultContext.argtypes=[POINTER(c_void_p), c_int32]
        deviceId = c_int32(device_id)
        ret = libaxcl_rt.axclrtGetDefaultContext(byref(context), deviceId)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return context.value, ret
