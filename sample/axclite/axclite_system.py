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
import axcl
from contextlib import contextmanager


@contextmanager
def axclite_system(json):
    initialized = False
    try:
        ret = axcl.init(json)
        if ret == axcl.AXCL_SUCC:
            initialized = True
            yield
        else:
            raise RuntimeError("axcl.init() failed to initialize the system.")
    finally:
        if initialized:
            axcl.finalize()
