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

def bytes_to_ptr(data):
    """
    bytes to pointer

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **python**              `ptr = axcl.utils.bytes_to_ptr(data)`
        ======================= =====================================================

    :param bytes data: data
    :returns: **ptr** (*int*) - address, None is failure
    """
    if data and isinstance(data, bytes):
        size = len(data)
        if size > 0:
            data_ptr = cast(data, POINTER(c_uint8))
            return addressof(data_ptr.contents)
        else:
            return None  # Return None for empty data
    else:
        return None  # Invalid input case

def ptr_to_bytes(ptr, size):
    """
    Pointer to bytes

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **python**              `data = axcl.utils.ptr_to_bytes(data)`
        ======================= =====================================================

    :param int ptr: address
    :param int size: size
    :returns: **data** (*bytes*) - None is failure
    """
    if ptr and size > 0:
        # Create a byte array and copy the data from the pointer
        _ptr = cast(ptr, POINTER(c_uint8))
        return bytes((c_uint8 * size).from_address(addressof(_ptr.contents)))
    else:
        return None  # Return None for invalid pointer or size

def dict_array_to_array(dict_array, type, max_len, default_value=0):
    """
    Dict array to array

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **python**              `array = dict_array_to_array(dict_array, type, max_len, default_value=0)`
        ======================= =====================================================

    :param dict dict_array: address
    :param type size: data type
    :param int max_len: max length
    :param int default_value: set default value
    :returns: **array** (*array*) - array
    """
    if isinstance(dict_array, str):
        dict_array = [ord(c) for c in dict_array]
    elif isinstance(dict_array, list) and all(isinstance(i, str) for i in dict_array):
        dict_array = [ord(c) for c in dict_array]

    array = dict_array[:max_len]
    array.extend([default_value] * (max_len - len(array)))

    return (type * max_len)(*array)

