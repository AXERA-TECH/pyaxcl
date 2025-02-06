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
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

from axcl.axcl import app_log

__AXCL_TRACE = 0
__AXCL_DEBUG = 1
__AXCL_INFO = 2
__AXCL_WARN = 3
__AXCL_ERROR = 4
__AXCL_CRITICAL = 5
__AXCL_OFF = 6

def log_error(*msg):
    """
    Log error message

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **python**              `log_error(*msg)`
        ======================= =====================================================

    :param list msg: list of string
    """
    log_str = [str(i) for i in msg]
    log_str = ''.join(log_str)

    print('[ERROR] ' + log_str)

    invoker = sys._getframe().f_back
    func_name = invoker.f_code.co_name
    file_name = invoker.f_code.co_filename
    line_no = invoker.f_lineno

    # message = '[' + file_name + ':' + str(line_no) +  ' ' + func_name + '] ' + log_str
    # print(message)

    app_log(__AXCL_ERROR, func_name, file_name, line_no, log_str)

def log_warning(*msg):
    """
    Log warning message

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **python**              `log_warning(*msg)`
        ======================= =====================================================

    :param list msg: list of string
    """
    log_str = [str(i) for i in msg]
    log_str = ''.join(log_str)

    print('[WARNING] ' + log_str)

    invoker = sys._getframe().f_back
    func_name = invoker.f_code.co_name
    file_name = invoker.f_code.co_filename
    line_no = invoker.f_lineno

    # message = '[' + file_name + ':' + str(line_no) +  ' ' + func_name + '] ' + log_str
    # print(message)

    app_log(__AXCL_WARN, func_name, file_name, line_no, log_str)

def log_info(*msg):
    """
    Log info message

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **python**              `log_info(*msg)`
        ======================= =====================================================

    :param list msg: list of string
    """
    log_str = [str(i) for i in msg]
    log_str = ''.join(log_str)

    print('[INFO] ' + log_str)

    invoker = sys._getframe().f_back
    func_name = invoker.f_code.co_name
    file_name = invoker.f_code.co_filename
    line_no = invoker.f_lineno

    # message = '[' + file_name + ':' + str(line_no) +  ' ' + func_name + '] ' + log_str
    # print(message)

    app_log(__AXCL_INFO, func_name, file_name, line_no, log_str)

def log_debug(*msg):
    """
    Log debug message

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **python**              `log_debug(*msg)`
        ======================= =====================================================

    :param list msg: list of string
    """
    log_str = [str(i) for i in msg]
    log_str = ''.join(log_str)

    print('[DEBUG] ' + log_str)

    invoker = sys._getframe().f_back
    func_name = invoker.f_code.co_name
    file_name = invoker.f_code.co_filename
    line_no = invoker.f_lineno

    # message = '[' + file_name + ':' + str(line_no) +  ' ' + func_name + '] ' + log_str
    # print(message)

    app_log(__AXCL_DEBUG, func_name, file_name, line_no, log_str)
