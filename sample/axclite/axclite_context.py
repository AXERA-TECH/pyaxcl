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
from axclite.axclite_resource import AxcliteResource


class AxcliteContext(AxcliteResource):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self._context = None
        self._device_id = 0

    @property
    def context(self):
        return self._context

    def create(self, device_id) -> bool:
        if device_id <= 0:
            print(f"invalid device id: {device_id}")
            return False

        if self._context:
            print(f"context has been created on device {device_id}")
            return False

        self._device_id = device_id

        self._context, ret = axcl.rt.create_context(self._device_id)
        if ret != axcl.AXCL_SUCC:
            print(f"create context on device {self._device_id}) fail, ret = 0x{ret&0xFFFFFFFF:x}")
            return False

        return True

    def destroy(self):
        if not self._context:
            return

        ret = axcl.rt.destroy_context(self._context)
        if ret != axcl.AXCL_SUCC:
            print(f"destroy context on device {self._device_id} fail, ret = 0x{ret&0xFFFFFFFF:x}")
