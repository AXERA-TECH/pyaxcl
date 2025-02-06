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


def malloc(size: int, policy: int) -> tuple[int, int]:
    """
    Malloc memory from device

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMalloc(void **devPtr, size_t size, axclrtMemMallocPolicy policy);`
        **python**              `dev_ptr, ret = axcl.rt.malloc(size, policy)`
        ======================= =====================================================

    :param int size: size to malloc.
    :param int policy: :class:`axclrtMemMallocPolicy <axcl.rt.axcl_rt_type.axclrtMemMallocPolicy>`
    :returns: tuple[int, int]

        - **dev_ptr** (*int*) - memory address.
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    devPtr = c_void_p(0)
    try:
        libaxcl_rt.axclrtMalloc.restype = axclError
        libaxcl_rt.axclrtMalloc.argtypes = [POINTER(c_void_p), c_size_t, c_int32]
        c_size = c_size_t(size)
        c_policy = c_int32(policy)

        ret = libaxcl_rt.axclrtMalloc(byref(devPtr), c_size, c_policy)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return devPtr.value, ret


def malloc_cached(size: int, policy: int) -> tuple[int, int]:
    """
    Malloc cached memory from device

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMallocCached(void **devPtr, size_t size, axclrtMemMallocPolicy policy);`
        **python**              `dev_ptr, ret = axcl.rt.malloc_cached(size, policy)`
        ======================= =====================================================

    :param int size: size to malloc.
    :param int policy: :class:`axclrtMemMallocPolicy <axcl.rt.axcl_rt_type.axclrtMemMallocPolicy>`
    :returns: tuple[int, int]

        - **dev_ptr** (*int*) - memory address.
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    devPtr = c_void_p(0)
    try:
        libaxcl_rt.axclrtMallocCached.restype = axclError
        libaxcl_rt.axclrtMallocCached.argtypes = [POINTER(c_void_p), c_size_t, c_int32]
        c_size = c_size_t(size)
        c_policy = c_int32(policy)

        ret = libaxcl_rt.axclrtMallocCached(byref(devPtr), c_size, c_policy)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return devPtr.value, ret


def free(dev_ptr: int) -> int:
    """
    Free memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtFree(void *devPtr);`
        **python**              `ret = axcl.rt.free(dev_ptr)`
        ======================= =====================================================

    :param int dev_ptr: memory address.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtFree.restype = axclError
        libaxcl_rt.axclrtFree.argtypes = [c_void_p]
        if dev_ptr:
            c_dev_ptr = c_void_p(dev_ptr)
            ret = libaxcl_rt.axclrtFree(c_dev_ptr)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_flush(dev_ptr: int, size: int) -> int:
    """
    Flush memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMemFlush(void *devPtr, size_t size);`
        **python**              `ret = axcl.rt.mem_flush(dev_ptr, size)`
        ======================= =====================================================

    :param int dev_ptr: memory address.
    :param int size: memory size.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtMemFlush.restype = axclError
        libaxcl_rt.axclrtMemFlush.argtypes = [c_void_p, c_size_t]
        c_size = c_size_t(size)

        if dev_ptr:
            c_dev_ptr = c_void_p(dev_ptr)
            ret = libaxcl_rt.axclrtMemFlush(c_dev_ptr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_invalidate(dev_ptr: int, size: int) -> int:
    """
    Invalidate memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMemInvalidate(void *devPtr, size_t size);`
        **python**              `ret = axcl.rt.mem_invalidate(dev_ptr, size)`
        ======================= =====================================================

    :param int dev_ptr: memory address.
    :param int size: memory size.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtMemInvalidate.restype = axclError
        libaxcl_rt.axclrtMemInvalidate.argtypes = [c_void_p, c_size_t]
        c_size = c_size_t(size)

        if dev_ptr:
            c_dev_ptr = c_void_p(dev_ptr)
            ret = libaxcl_rt.axclrtMemInvalidate(c_dev_ptr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def malloc_host(size: int) -> tuple[int, int]:
    """
    Malloc memory from host

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMallocHost(void **hostPtr, size_t size);`
        **python**              `host_ptr, ret = axcl.rt.malloc_host(size)`
        ======================= =====================================================

    :param int size: memory size.
    :returns: tuple[int, int]

        - **host_ptr** (*int*) - memory address.
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    hostPtr = c_void_p(0)
    try:
        libaxcl_rt.axclrtMallocHost.restype = axclError
        libaxcl_rt.axclrtMallocHost.argtypes = [POINTER(c_void_p), c_size_t]
        c_size = c_size_t(size)

        ret = libaxcl_rt.axclrtMallocHost(byref(hostPtr), c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return hostPtr.value, ret


def free_host(host_ptr: int) -> int:
    """
    Free memory from host

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtFreeHost(void *hostPtr);`
        **python**              `ret = axcl.rt.free_host(host_ptr)`
        ======================= =====================================================

    :param int host_ptr: memory address.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtFreeHost.restype = axclError
        libaxcl_rt.axclrtFreeHost.argtypes = [c_void_p]

        if host_ptr:
            c_host_ptr = c_void_p(host_ptr)
            ret = libaxcl_rt.axclrtFreeHost(host_ptr)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def memset(dev_ptr: int, value: int, count: int) -> int:
    """
    Set memory content

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMemset(void *devPtr, uint8_t value, size_t count);`
        **python**              `ret = axcl.rt.memset(dev_ptr, value, count)`
        ======================= =====================================================

    :param int dev_ptr: memory address.
    :param int value: value to set.
    :param int count: count.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtMemset.restype = axclError
        libaxcl_rt.axclrtMemset.argtypes = [c_void_p, c_uint8, c_size_t]
        c_value = c_uint8(value)
        c_count = c_size_t(count)
        if dev_ptr:
            c_dev_ptr = c_void_p(dev_ptr)
            ret = libaxcl_rt.axclrtMemset(c_dev_ptr, c_value, c_count)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def memcpy(dst_ptr: int, src_ptr: int, count: int, kind: int) -> int:
    """
    Copy memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMemcpy(void *dstPtr, const void *srcPtr, size_t count, axclrtMemcpyKind kind);`
        **python**              `ret = axcl.rt.memcpy(dst_ptr, src_ptr, count, kind)`
        ======================= =====================================================

    :param int dst_ptr: dest memory address.
    :param int src_ptr: source memoty address.
    :param int count: count.
    :param int kind: :class:`axclrtMemcpyKind <axcl.rt.axcl_rt_type.axclrtMemcpyKind>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtMemcpy.restype = axclError
        libaxcl_rt.axclrtMemcpy.argtypes = [c_void_p, c_void_p, c_size_t, c_int32]
        c_count = c_size_t(count)
        c_kind = c_int32(kind)
        if dst_ptr and src_ptr:
            c_dst_ptr = c_void_p(dst_ptr)
            c_src_ptr = c_void_p(src_ptr)
            ret = libaxcl_rt.axclrtMemcpy(c_dst_ptr, c_src_ptr, c_count, c_kind)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def memcmp(dev_ptr1: int, dev_ptr2: int, count: int) -> int:
    """
    Compare memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtMemcmp(const void *devPtr1, const void *devPtr2, size_t count);`
        **python**              `ret = axcl.rt.memcmp(dev_ptr1, dev_ptr2, count)`
        ======================= =====================================================

    :param int dev_ptr1: memory address.
    :param int dev_ptr2: memoty address.
    :param int count: count.
    :returns: **ret** (*int*) - 0 indicates equal, otherwise not equal.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtMemcmp.restype = axclError
        libaxcl_rt.axclrtMemcmp.argtypes = [c_void_p, c_void_p, c_size_t]
        c_count = c_size_t(count)
        if dev_ptr1 and dev_ptr2:
            c_dev_ptr1 = c_void_p(dev_ptr1)
            c_dev_ptr2 = c_void_p(dev_ptr2)
            ret = libaxcl_rt.axclrtMemcmp(c_dev_ptr1, c_dev_ptr2, c_count)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret
