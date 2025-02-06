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
BASE_DIR += "/../.."
sys.path.append(BASE_DIR)

from axcl.lib.axcl_lib import libaxcl_rt
from axcl.axcl_base import *
from axcl.utils.axcl_logger import *


def get_version() -> tuple[int, int, int, int]:
    """
    Get sdk version

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtGetVersion(int32_t *major, int32_t *minor, int32_t *patch);`
        **python**              `major, minor, patch, ret = axcl.rt.get_version()`
        ======================= =====================================================

    :returns: tuple[int, int, int, int]

        - **major** (*int*) - major verison
        - **minor** (*int*) - minor verison
        - **patch** (*int*) - patch verison
        - **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

        .. code-block:: python

            major, minor, patch, ret = axcl.rt.get_version()
    """
    ret = -1
    major = c_int32(0)
    minor = c_int32(0)
    patch = c_int32(0)
    try:
        libaxcl_rt.axclrtGetVersion.restype = axclError
        libaxcl_rt.axclrtGetVersion.argtypes=[POINTER(c_int32), POINTER(c_int32), POINTER(c_int32)]

        ret = libaxcl_rt.axclrtGetVersion(byref(major),byref(minor),byref(patch))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return major.value, minor.value, patch.value, ret


def get_soc_name() -> str:
    """
    Get soc name

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `const char *axclrtGetSocName();`
        **python**              `name = axcl.rt.get_soc_name()`
        ======================= =====================================================

    :returns: **name** (*str*) - soc name

    **Example**

        .. code-block:: python

            name = axcl.rt.get_soc_name()
    """
    name = None
    try:
        libaxcl_rt.axclrtGetSocName.restype = c_char_p
        _name = libaxcl_rt.axclrtGetSocName()
        if _name:
            name = _name.decode('utf-8')
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return name
