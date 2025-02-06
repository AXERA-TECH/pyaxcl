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
from pathlib import Path
import ctypes

import axcl
from axclite.axclite_memory import device_mem_alloc, device_mem_free


class AxcliteLoadFileToDevice(object):
    def __init__(self, file_name):
        self.dev_mem = 0
        self.size = 0
        try:
            self.size = os.path.getsize(file_name)
            with open(file_name, 'rb') as file:
                self.dev_mem = device_mem_alloc(self.size)
                if self.dev_mem != 0:
                    content = file.read()
                    content_ptr = axcl.utils.bytes_to_ptr(content)
                    axcl.rt.memcpy(self.dev_mem, content_ptr, self.size, axcl.AXCL_MEMCPY_HOST_TO_DEVICE)
        except:
            print(sys.exc_info())
            print(traceback.format_exc())

    def result(self):
        return self.dev_mem, self.size

    def __del__(self):
        device_mem_free(self.dev_mem)


class AxcliteStoreFileFromDevice(object):
    def __init__(self, phy_addr, size, dst_path, file_name, is_append=False):
        self.dst_file = None
        try:
            folder = Path(dst_path)
            folder.mkdir(parents=True, exist_ok=True)
            self.dst_file = dst_path + "/" + file_name
            with open(self.dst_file, 'ab' if is_append else 'wb') as f:
                buffer = ctypes.create_string_buffer(size)
                addr = ctypes.addressof(buffer)
                axcl.rt.memcpy(addr, phy_addr, size, axcl.AXCL_MEMCPY_DEVICE_TO_HOST)
                f.write(buffer.raw)
        except:
            print(sys.exc_info())
            print(traceback.format_exc())

    def result(self):
        return self.dst_file