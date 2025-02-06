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

AXCL_USE_LOCAL_PATH = 0
AXCL_USE_TEST_LIB = 0

def get_axcl_lib_path():
    if AXCL_USE_LOCAL_PATH == 1:
        lib_path = os.path.dirname(os.path.abspath(__file__))
        lib_path = lib_path[0:lib_path.rfind('/')]
        lib_path = lib_path[0:lib_path.rfind('/')]
        lib_path = lib_path[0:lib_path.rfind('/')]
        return lib_path + '/out/axcl_linux_x86/lib'
    else:
        return os.getenv('AXCL_LIB_PATH', '/usr/lib/axcl')
