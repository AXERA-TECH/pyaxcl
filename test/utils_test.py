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

import os
import sys
from ctypes import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

import axcl
from axcl.lib.axcl_lib import libaxcl_sys

def test():
    axcl.utils.log_error('error2 ...', ' param1', ' param2')

if __name__ == '__main__':
    class TEST_DATA_T(Structure):
        _fields_ = [
            ("pData", POINTER(c_char)),
            ("nSize", c_int32)
        ]

    data = 'hello'.encode('utf-8')
    size = len(data)

    a = TEST_DATA_T()
    ptr = axcl.utils.bytes_to_ptr(data)
    a.pData = cast(ptr, POINTER(c_char))
    a.nSize = size

    libaxcl_sys.test_input.restype = c_int
    libaxcl_sys.test_input.argtypes=[POINTER(TEST_DATA_T)]

    libaxcl_sys.test_output.restype = c_int
    libaxcl_sys.test_output.argtypes=[POINTER(TEST_DATA_T)]

    libaxcl_sys.test_input(byref(a))

    b = TEST_DATA_T()
    libaxcl_sys.test_output(byref(b))
    print(b.nSize)
    b_data = axcl.utils.ptr_to_bytes(b.pData, b.nSize)
    print(b_data)

    p = cast(ptr, POINTER(c_int32))
    print(ptr)
    print(addressof(p.contents))
    print(p.contents)
    print(f"0x{p.contents.value:x}")

    axcl.utils.log_error('error ...', ' param1', ' param2')
    axcl.utils.log_warning('warning ...', ' param1', ' param2')
    axcl.utils.log_info('info ...', ' param1', ' param2')
    axcl.utils.log_debug('debug ...', ' param1', ' param2')

    test()
