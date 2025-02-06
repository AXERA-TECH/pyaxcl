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
sys.path.append(BASE_DIR)

from axcl.lib.axcl_lib import libaxcl_rt
from axcl.rt.axcl_rt_type import *
from axcl.utils.axcl_logger import *


def set_device(device_id: int) -> int:
    """
    Active device.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtSetDevice(int32_t deviceId);`
        **python**              `ret = axcl.rt.set_device(device_id)`
        ======================= =====================================================

    :param int device_id: device id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    .. note::

        As for PCIe device, device id is the bus number returned by ``lspci`` or ``axcl-smi``.

        .. code-block:: bash

            $ lspci
            0001:81:00.0 Class 0604: Device 16c3:abcd (rev 01)
            # device id: 0x81
    """
    ret = -1
    try:
        libaxcl_rt.axclrtSetDevice.restype = axclError
        libaxcl_rt.axclrtSetDevice.argtypes=[c_int32]
        deviceId = c_int32(device_id)

        ret = libaxcl_rt.axclrtSetDevice(deviceId)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def reset_device(device_id: int) -> int:
    """
    Reset device

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtResetDevice(int32_t deviceId);`
        **python**              `ret = axcl.rt.reset_device(device_id)`
        ======================= =====================================================

    :param int device_id: device id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    .. note::

        Active device first by :func:`set_device <axcl.rt.axcl_rt_device.set_device>`.
    """
    ret = -1
    try:
        libaxcl_rt.axclrtResetDevice.restype = axclError
        libaxcl_rt.axclrtResetDevice.argtypes=[c_int32]
        deviceId = c_int32(device_id)

        ret = libaxcl_rt.axclrtResetDevice(deviceId)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_device() -> tuple[int, int]:
    """
    Get the latest actived device by :func:`set_device <axcl.rt.axcl_rt_device.set_device>`

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtGetDevice(int32_t *deviceId);`
        **python**              `device_id, ret = axcl.rt.get_device()`
        ======================= =====================================================

    :returns: tuple[int, int]
        - **device_id** (*int*) - device id
        - **ret** (*int*) - 0 indicates success, otherwise failure

    .. note::

        At least one device has been actived by :func:`set_device <axcl.rt.axcl_rt_device.set_device>`.
    """
    ret = -1
    deviceId = c_int32(0)
    try:
        libaxcl_rt.axclrtGetDevice.restype = axclError
        libaxcl_rt.axclrtGetDevice.argtypes=[POINTER(c_int32)]

        ret = libaxcl_rt.axclrtGetDevice(byref(deviceId))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return deviceId.value, ret


def get_device_count() -> tuple[int, int]:
    """
    Get the count of connected devices.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtGetDeviceCount(uint32_t *count);`
        **python**              `device_count, ret = axcl.rt.get_device_count()`
        ======================= =====================================================

    :returns: tuple[int, int]

        - **device_count** (*int*) - device count
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    count = c_int32(0)
    try:
        libaxcl_rt.axclrtGetDeviceCount.restype = axclError
        libaxcl_rt.axclrtGetDeviceCount.argtypes=[POINTER(c_int32)]

        ret = libaxcl_rt.axclrtGetDeviceCount(byref(count))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return count.value, ret


def get_device_list() -> tuple[list, int]:
    """
    Get the id list of connected devices.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtGetDeviceList(axclrtDeviceList *deviceList);`
        **python**              `device_list, ret = axcl.rt.get_device_list()`
        ======================= =====================================================

    :returns: tuple[list, int]
        - **device_list** (*list*) - device id list
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    deviceList = axclrtDeviceList(0)
    dev_list = []
    try:
        libaxcl_rt.axclrtGetDeviceList.restype = axclError
        libaxcl_rt.axclrtGetDeviceList.argtypes=[POINTER(axclrtDeviceList)]

        ret = libaxcl_rt.axclrtGetDeviceList(byref(deviceList))

        if ret == 0 and deviceList.num > 0:
            for i in range(deviceList.num):
                dev_list.append(deviceList.devices[i])
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return dev_list, ret


def synchronize_device() -> int:
    """
    Synchronize device

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtSynchronizeDevice();`
        **python**              `device_count, ret = axcl.rt.synchronize_device()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtSynchronizeDevice.restype = axclError

        ret = libaxcl_rt.axclrtSynchronizeDevice()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_device_utilization_rate(device_id: int) -> tuple[int, int, int, int]:
    """
    Get device utilization rate

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtGetDeviceUtilizationRate(int32_t deviceId, axclrtUtilizationInfo *utilizationInfo);`
        **python**              `cpu_utilization, npu_utilization, mem_utilization, ret = axcl.rt.get_device_utilization_rate(device_id)`
        ======================= =====================================================

    :param int device_id: device id.
    :returns: tuple[int, int, int, int]

        - **cpu_utilization** (*int*) - cpu utilization
        - **npu_utilization** (*int*) - npu utilization
        - **mem_utilization** (*int*) - memory utilization
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    utilizationInfo = axclrtUtilizationInfo(0)
    try:
        libaxcl_rt.axclrtGetDeviceUtilizationRate.restype = axclError
        libaxcl_rt.axclrtGetDeviceUtilizationRate.argtypes=[c_int32, POINTER(axclrtUtilizationInfo)]
        deviceId = c_int32(device_id)

        ret = libaxcl_rt.axclrtGetDeviceUtilizationRate(deviceId, byref(utilizationInfo))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return utilizationInfo.cpuUtilization, utilizationInfo.npuUtilization, utilizationInfo.memUtilization, ret
