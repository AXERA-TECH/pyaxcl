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
import time
import sys
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.lib.axcl_lib import libaxcl_rt
from axcl.axcl_base import *
from axcl.utils.axcl_logger import *


def create_stream() -> tuple[int, int]:
    """
    Create stream

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtCreateStream(axclrtStream *stream);`
        **python**              `stream, ret = axcl.rt.create_stream()`
        ======================= =====================================================

    :returns: tuple[int, int]

        - **stream** (*int*) - stream handle
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    stream = c_void_p(0)
    try:
        libaxcl_rt.axclrtCreateStream.restype = axclError
        libaxcl_rt.axclrtCreateStream.argtypes=[POINTER(c_void_p)]

        ret = libaxcl_rt.axclrtCreateStream(byref(stream))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return stream.value, ret


def destroy_stream(stream: int) -> int:
    """
    Destroy steam

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtDestroyStream(axclrtStream stream);`
        **python**              `ret = axcl.rt.destroy_stream(stream)`
        ======================= =====================================================

    :param int stream: stream handle.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtDestroyStream.restype = axclError
        libaxcl_rt.axclrtDestroyStream.argtypes=[c_void_p]

        if stream:
            c_stream = c_void_p(stream)
            ret = libaxcl_rt.axclrtDestroyStream(c_stream)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def destroy_stream_force(stream: int) -> int:
    """
    Force to destroy device

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtDestroyStreamForce(axclrtStream stream);`
        **python**              `ret = axcl.rt.destroy_stream_force(stream)`
        ======================= =====================================================

    :param int stream: stream handle.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtDestroyStreamForce.restype = axclError
        libaxcl_rt.axclrtDestroyStreamForce.argtypes=[c_void_p]

        if stream:
            c_stream = c_void_p(stream)
            ret = libaxcl_rt.axclrtDestroyStreamForce(c_stream)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def synchronize_stream(stream: int) -> int:
    """
    Synchronize stream

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtSynchronizeStream(axclrtStream stream);`
        **python**              `ret = axcl.rt.synchronize_stream(stream)`
        ======================= =====================================================

    :param int stream: stream handle.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtSynchronizeStream.restype = axclError
        libaxcl_rt.axclrtSynchronizeStream.argtypes=[c_void_p]
        if stream:
            c_stream = c_void_p(stream)
            ret = libaxcl_rt.axclrtSynchronizeStream(c_stream)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def synchronize_stream_with_timeout(stream: int, timeout: int) -> int:
    """
    Synchronize stream with timeout

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtSynchronizeStreamWithTimeout(axclrtStream stream, int32_t timeout);`
        **python**              `ret = axcl.rt.synchronize_stream_with_timeout(stream, timeout)`
        ======================= =====================================================

    :param int stream: stream handle.
    :param int timeout: timeout ms
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtSynchronizeStreamWithTimeout.restype = axclError
        libaxcl_rt.axclrtSynchronizeStreamWithTimeout.argtypes=[c_void_p]
        c_timeout = c_int32(timeout)

        if stream:
            c_stream = c_void_p(stream)
            ret = libaxcl_rt.axclrtSynchronizeStreamWithTimeout(c_stream, c_timeout)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret
