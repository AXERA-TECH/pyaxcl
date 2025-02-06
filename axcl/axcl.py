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
sys.path.append(BASE_DIR + '/..')

from axcl.lib.axcl_lib import libaxcl_rt
from axcl.axcl_base import *


def init(config):
    """
    Init

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclInit(const char *config);`
        **python**              `ret = axcl.rt.init(config)`
        ======================= =====================================================

    :param str config: json config file path.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_config = c_char_p(0)
    try:
        libaxcl_rt.axclInit.restype = axclError
        libaxcl_rt.axclInit.argtypes=[c_char_p]

        if config and len(config) > 0:
            c_config = config.encode('utf-8')

        ret = libaxcl_rt.axclInit(c_config)
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret

def finalize():
    """
    Finalize

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclFinalize();`
        **python**              `ret = axcl.rt.finalize()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclFinalize.restype = axclError
        libaxcl_rt.axclInit.argtypes= None

        ret = libaxcl_rt.axclFinalize()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret

def set_log_level(level):
    """
    c api: axclError axclSetLogLevel(int32_t lv);
    """
    ret = -1
    try:
        libaxcl_rt.axclSetLogLevel.restype = axclError
        libaxcl_rt.axclSetLogLevel.argtypes = [c_int32]
        c_level = c_int32(level)
        ret = libaxcl_rt.axclSetLogLevel(c_level)
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret

def app_log(level, func, file, line, message):
    """
    Output app log to log file or console

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `void axclAppLog(int32_t lv, const char *func, const char *file, uint32_t line, const char *fmt, ...);`
        **python**              `ret = axcl.rt.app_log(level, func, file, line, message)`
        ======================= =====================================================

    :param int level: log level.
    :param str func: function name.
    :param str file: file name.
    :param int line: code line.
    :param str message: log message.
    """
    c_func = c_char_p(0)
    c_file = c_char_p(0)
    c_message = c_char_p(0)
    try:
        libaxcl_rt.axclAppLog.restype = None
        libaxcl_rt.axclAppLog.argtypes = [c_int32, c_char_p, c_char_p, c_uint32, c_char_p]
        c_level = c_int32(level)
        c_line = c_uint32(line)

        if func and len(func) > 0:
            c_func = c_char_p(func.encode('utf-8'))

        if file and len(file) > 0:
            c_file = c_char_p(file.encode('utf-8'))

        if message and len(message) > 0:
            c_message = c_char_p(message.encode('utf-8'))

        libaxcl_rt.axclAppLog(c_level, c_func, c_file, c_line, c_message)
    except:
        print(sys.exc_info())
        print(traceback.format_exc())

