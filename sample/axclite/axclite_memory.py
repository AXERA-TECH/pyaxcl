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


def device_mem_alloc(size):
    dev_mem, ret = axcl.rt.malloc(size, axcl.AXCL_MEM_MALLOC_NORMAL_ONLY)

    if axcl.AXCL_SUCC != ret:
        return 0

    return dev_mem


def device_mem_free(dev_mem):
    if dev_mem != 0:
        axcl.rt.free(dev_mem)


class AxcliteDeviceMalloc(object):
    def __init__(self, size):
        self.dev_mem = device_mem_alloc(size)

    @property
    def address(self):
        return self.dev_mem

    def __del__(self):
        device_mem_free(self.dev_mem)
