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
from axcl.rt.axcl_rt_engine_type import *
from axcl.axcl_base import *
from axcl.utils.axcl_logger import *


def engine_init(npu_kind: int) -> int:
    """
    Init engine

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineInit(axclrtEngineVNpuKind npuKind);`
        **python**              `ret = axcl.rt.engine_init(npu_kind)`
        ======================= =====================================================

    :param int npu_kind: :class:`axclrtEngineVNpuKind <axcl.rt.axcl_rt_engine_type.axclrtEngineVNpuKind>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtEngineInit.restype = axclError
        libaxcl_rt.axclrtEngineInit.argtypes=[c_int32]
        c_npu_kind = c_int32(npu_kind)

        ret = libaxcl_rt.axclrtEngineInit(c_npu_kind)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_get_vnpu_kind()-> tuple[int, int]:
    """
    Get vnpu kind

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetVNpuKind(axclrtEngineVNpuKind *npuKind);`
        **python**              `npu_kind, ret = axcl.rt.engine_get_vnpu_kind()`
        ======================= =====================================================

    :returns: tuple[int, int]

        - **npu_kind** (*int*) - :class:`axclrtEngineVNpuKind <axcl.rt.axcl_rt_engine_type.axclrtEngineVNpuKind>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtEngineGetVNpuKind.restype = axclError
        libaxcl_rt.axclrtEngineGetVNpuKind.argtypes=[POINTER(c_int32)]
        c_npu_kind = c_int32(0)

        ret = libaxcl_rt.axclrtEngineGetVNpuKind(byref(c_npu_kind))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_npu_kind.value, ret


def engine_finalize() -> int:
    """
    Finalize

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineFinalize();`
        **python**              `ret = axcl.rt.engine_finalize()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtEngineFinalize.restype = axclError

        ret = libaxcl_rt.axclrtEngineFinalize()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_load_from_file(model_path: str) -> tuple[int, int]:
    """
    Load model from file

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineLoadFromFile(const char *modelPath, uint64_t *modelId);`
        **python**              `model_id, ret = axcl.rt.engine_load_from_file(model_path)`
        ======================= =====================================================

    :param str model_path: model file path
    :returns: tuple[int, int]

        - **model_id** (*int*) - model id
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_model_id = c_uint64(0)
    try:
        libaxcl_rt.axclrtEngineLoadFromFile.restype = axclError
        libaxcl_rt.axclrtEngineLoadFromFile.argtypes=[c_char_p, POINTER(c_uint64)]
        if model_path and len(model_path) > 0:
            c_mode_path = c_char_p(model_path.encode('utf-8'))
            ret = libaxcl_rt.axclrtEngineLoadFromFile(c_mode_path, byref(c_model_id))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_model_id.value, ret


def engine_load_from_mem(model: int, model_size: int) -> tuple[int, int]:
    """
    Load model from memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineLoadFromMem(const void *model, uint64_t modelSize, uint64_t *modelId);`
        **python**              `model_id, ret = axcl.rt.engine_load_from_mem(model, model_size)`
        ======================= =====================================================

    :param int model: memory address of model
    :param int model_size: model size
    :returns: tuple[int, int]

        - **model_id** (*int*) - model id
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_model_id = c_uint64(0)
    try:
        libaxcl_rt.axclrtEngineLoadFromMem.restype = axclError
        libaxcl_rt.axclrtEngineLoadFromMem.argtypes=[c_void_p, c_uint64, POINTER(c_uint64)]
        c_model_size = c_uint64(model_size)
        if model:
            c_model = c_void_p(model)
            ret = libaxcl_rt.axclrtEngineLoadFromMem(c_model, c_model_size, byref(c_model_id))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_model_id.value, ret


def engine_unload(model_id: int) -> int:
    """
    Unload model

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineUnload(uint64_t modelId);`
        **python**              `ret = axcl.rt.engine_unload(model_id)`
        ======================= =====================================================

    :param int model_id: model id
    :returns:  **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtEngineUnload.restype = axclError
        libaxcl_rt.axclrtEngineUnload.argtypes=[c_uint64]
        c_model_id = c_uint64(model_id)
        ret = libaxcl_rt.axclrtEngineUnload(c_model_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_get_model_compiler_version(model_id: int) -> str:
    """
    Get model compiler version

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `const char *axclrtEngineGetModelCompilerVersion(uint64_t modelId);`
        **python**              `version = axcl.rt.engine_get_model_compiler_version(model_id)`
        ======================= =====================================================

    :param int model_id: model id
    :returns: **version** (*str*) - model compiler version
    """
    version = None
    try:
        libaxcl_rt.axclrtEngineGetModelCompilerVersion.restype = c_char_p
        libaxcl_rt.axclrtEngineGetModelCompilerVersion.argtypes=[c_uint64]
        c_model_id = c_uint64(model_id)
        c_version = libaxcl_rt.axclrtEngineGetModelCompilerVersion(c_model_id)
        if c_version:
            version = c_version.decode('utf-8')
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return version


def engine_set_affinity(model_id: int, mask: int) -> int:
    """
    Set affinity

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineSetAffinity(uint64_t modelId, axclrtEngineSet set);`
        **python**              `ret = axcl.rt.engine_set_affinity(model_id, mask)`
        ======================= =====================================================

    :param int model_id: model id
    :param int mask: affinity
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtEngineSetAffinity.restype = axclError
        libaxcl_rt.axclrtEngineSetAffinity.argtypes=[c_uint64, c_uint32]
        c_model_id = c_uint64(model_id)
        c_set = c_uint32(mask)
        ret = libaxcl_rt.axclrtEngineSetAffinity(c_model_id, c_set)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_get_affinity(model_id: int) -> tuple[int, int]:
    """
    Get affinity

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetAffinity(uint64_t modelId, axclrtEngineSet *set);`
        **python**              `mask, ret = axcl.rt.engine_get_affinity(model_id)`
        ======================= =====================================================

    :param int model_id: model id
    :returns: tuple[int, int]

        - **mask** (*int*) - affinity mask
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_set = c_uint32(0)
    try:
        libaxcl_rt.axclrtEngineGetAffinity.restype = axclError
        libaxcl_rt.axclrtEngineGetAffinity.argtypes=[c_uint64, POINTER(c_uint32)]
        c_model_id = c_uint64(model_id)

        ret = libaxcl_rt.axclrtEngineGetAffinity(c_model_id, byref(c_set))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_set.value, ret


def engine_get_usage(model_path: str) -> tuple[int, int, int]:
    """
    Get usage from model path

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetUsage(const char *modelPath, int64_t *sysSize, int64_t *cmmSize);`
        **python**              `sys_size, cmm_size, ret = axcl.rt.engine_get_usage(model_path)`
        ======================= =====================================================

    :param str model_path: model path
    :returns: tuple[int, int, int]

        - **sys_size** (*int*) - sys used size
        - **cmm_size** (*int*) - cmm used size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_sys_size = c_int64(0)
    c_cmm_size = c_int64(0)
    try:
        libaxcl_rt.axclrtEngineGetUsage.restype = axclError
        libaxcl_rt.axclrtEngineGetUsage.argtypes=[c_char_p, POINTER(c_int64), POINTER(c_int64)]
        if model_path and len(model_path) > 0:
            c_model_path = c_char_p(model_path.encode('utf-8'))
            ret = libaxcl_rt.axclrtEngineGetUsage(c_model_path, byref(c_sys_size), byref(c_cmm_size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_sys_size.value, c_cmm_size.value, ret


def engine_get_usage_from_mem(model: int, model_size: int) -> tuple[int, int, int]:
    """
    Get usage from model memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetUsageFromMem(const void *model, uint64_t modelSize, int64_t *sysSize, int64_t *cmmSize);`
        **python**              `sys_size, cmm_size, ret = axcl.rt.engine_get_usage_from_mem(model, model_size)`
        ======================= =====================================================

    :param int model: model memory address
    :param int model_size: model size
    :returns: tuple[int, int, int]

        - **sys_size** (*int*) - sys used size
        - **cmm_size** (*int*) - cmm used size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_sys_size = c_int64(0)
    c_cmm_size = c_int64(0)
    try:
        libaxcl_rt.axclrtEngineGetUsageFromMem.restype = axclError
        libaxcl_rt.axclrtEngineGetUsageFromMem.argtypes=[c_void_p, c_uint64, POINTER(c_int64), POINTER(c_int64)]
        c_model_size = c_uint64(model_size)
        if model and model_size > 0:
            ret = libaxcl_rt.axclrtEngineGetUsageFromMem(model, c_model_size, byref(c_sys_size), byref(c_cmm_size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_sys_size.value, c_cmm_size.value, ret


def engine_get_usage_from_mode_id(model_id: int) -> tuple[int, int, int]:
    """
    Get usage from model id

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetUsageFromModelId(uint64_t modelId, int64_t *sysSize, int64_t *cmmSize);`
        **python**              `sys_size, cmm_size, ret = axcl.rt.engine_get_usage_from_mode_id(model_id)`
        ======================= =====================================================

    :param int model_id: model id
    :returns: tuple[int, int, int]

        - **sys_size** (*int*) - sys used size
        - **cmm_size** (*int*) - cmm used size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_sys_size = c_int64(0)
    c_cmm_size = c_int64(0)
    try:
        libaxcl_rt.axclrtEngineGetUsageFromModelId.restype = axclError
        libaxcl_rt.axclrtEngineGetUsageFromModelId.argtypes=[c_uint64, POINTER(c_int64), POINTER(c_int64)]
        c_model_id = c_uint64(model_id)
        ret = libaxcl_rt.axclrtEngineGetUsageFromModelId(c_model_id, byref(c_sys_size), byref(c_cmm_size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_sys_size.value, c_cmm_size.value, ret


def engine_get_model_type(model_path: str) -> tuple[int, int]:
    """
    Get model type form model path

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetModelType(const char *modelPath, axclrtEngineModelKind *modelType);`
        **python**              `model_type, ret = axcl.rt.engine_get_model_type(model_path)`
        ======================= =====================================================

    :param str model_path: model path
    :returns: tuple[int, int]

        - **model_type** (*int*) - model type
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_mode_type = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetModelType.restype = axclError
        libaxcl_rt.axclrtEngineGetModelType.argtypes=[c_char_p, POINTER(c_int32)]
        if model_path and len(model_path) > 0:
            c_model_path = c_char_p(model_path.encode('utf-8'))
            ret = libaxcl_rt.axclrtEngineGetModelType(c_model_path, byref(c_mode_type))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_mode_type.value, ret


def engine_get_model_type_from_mem(model: int, model_size: int) -> tuple[int, int]:
    """
    Get model type form model memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetModelTypeFromMem(const void *model, uint64_t modelSize, axclrtEngineModelKind *modelType);`
        **python**              `model_type, ret = axcl.rt.engine_get_model_type_from_mem(model, model_size)`
        ======================= =====================================================

    :param int model: model memory address
    :param int model_size: model size
    :returns: tuple[int, int]

        - **model_type** (*int*) - model type
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_mode_type = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetModelTypeFromMem.restype = axclError
        libaxcl_rt.axclrtEngineGetModelTypeFromMem.argtypes=[c_void_p, c_uint64, POINTER(c_int32)]
        c_model_size = c_uint64(model_size)
        if model and model_size > 0:
            ret = libaxcl_rt.axclrtEngineGetModelTypeFromMem(model, c_model_size, byref(c_mode_type))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_mode_type.value, ret


def engine_get_model_type_from_model_id(model_id: int) -> tuple[int, int]:
    """
    Get model type form model id

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetModelTypeFromModelId(uint64_t modelId, axclrtEngineModelKind *modelType);`
        **python**              `model_type, ret = axcl.rt.engine_get_model_type_from_model_id(model_id)`
        ======================= =====================================================

    :param int model_id: model id
    :returns: tuple[int, int]

        - **model_type** (*int*) - model type
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_mode_type = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetModelTypeFromModelId.restype = axclError
        libaxcl_rt.axclrtEngineGetModelTypeFromModelId.argtypes=[c_uint64, POINTER(c_int32)]
        c_model_id = c_uint64(model_id)
        ret = libaxcl_rt.axclrtEngineGetModelTypeFromModelId(c_model_id, byref(c_mode_type))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_mode_type.value, ret


def engine_get_io_info(model_id: int) -> tuple[int, int]:
    """
    Get io info

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetIOInfo(uint64_t modelId, axclrtEngineIOInfo *ioInfo);`
        **python**              `io_info, ret = axcl.rt.engine_get_io_info(model_id)`
        ======================= =====================================================

    :param int model_id: model id
    :returns: tuple[int, int]

        - **io_info** (*int*) - io info address
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    io_info = c_void_p(0)
    try:
        libaxcl_rt.axclrtEngineGetIOInfo.restype = axclError
        libaxcl_rt.axclrtEngineGetIOInfo.argtypes=[c_uint64, POINTER(c_void_p)]
        c_model_id = c_uint64(model_id)
        ret = libaxcl_rt.axclrtEngineGetIOInfo(c_model_id, byref(io_info))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return io_info.value, ret


def engine_destroy_io_info(io_info: int) -> int:
    """
    Destroy io info

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineDestroyIOInfo(axclrtEngineIOInfo ioInfo);`
        **python**              `ret = axcl.rt.engine_destroy_io_info(io_info)`
        ======================= =====================================================

    :param int io_info: io info address
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtEngineDestroyIOInfo.restype = axclError
        libaxcl_rt.axclrtEngineDestroyIOInfo.argtypes=[c_void_p]
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineDestroyIOInfo(c_io_info)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_get_shape_groups_count(io_info: int) -> tuple[int, int]:
    """
    Get shape groups count of io info

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetShapeGroupsCount(axclrtEngineIOInfo ioInfo, int32_t *count);`
        **python**              `count, ret = axcl.rt.engine_get_shape_groups_count(io_info)`
        ======================= =====================================================

    :param int io_info: io info address
    :returns: tuple[int, int]

        - **count** (*int*) - shape groups count of io info
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_count = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetShapeGroupsCount.restype = axclError
        libaxcl_rt.axclrtEngineGetShapeGroupsCount.argtypes=[c_void_p, POINTER(c_int32)]
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineGetShapeGroupsCount(c_io_info, byref(c_count))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_count.value, ret


def engine_get_num_inputs(io_info: int) -> int:
    """
    Get number of inputs

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `uint32_t axclrtEngineGetNumInputs(axclrtEngineIOInfo ioInfo);`
        **python**              `num_inputs = axcl.rt.engine_get_shape_groups_count(io_info)`
        ======================= =====================================================

    :param int io_info: io info address
    :returns: **num_inputs** (*int*) - number of inputs
    """
    num_inputs = 0
    try:
        libaxcl_rt.axclrtEngineGetNumInputs.restype = c_uint32
        libaxcl_rt.axclrtEngineGetNumInputs.argtypes=[c_void_p]
        if io_info:
            c_io_info = c_void_p(io_info)
            num_inputs = libaxcl_rt.axclrtEngineGetNumInputs(c_io_info)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return num_inputs


def engine_get_num_outputs(io_info: int) -> int:
    """
    Get number of outputs

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `uint32_t axclrtEngineGetNumOutputs(axclrtEngineIOInfo ioInfo);`
        **python**              `num_outputs = axcl.rt.engine_get_num_outputs(io_info)`
        ======================= =====================================================

    :param int io_info: io info address
    :returns: **num_outputs** (*int*) - number of outputs
    """
    num_outputs = 0
    try:
        libaxcl_rt.axclrtEngineGetNumOutputs.restype = c_uint32
        libaxcl_rt.axclrtEngineGetNumOutputs.argtypes=[c_void_p]
        if io_info:
            c_io_info = c_void_p(io_info)
            num_outputs = libaxcl_rt.axclrtEngineGetNumOutputs(c_io_info)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return num_outputs


def engine_get_input_size_by_index(io_info: int, group: int, index: int) -> int:
    """
    Get input size by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `uint64_t axclrtEngineGetInputSizeByIndex(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index);`
        **python**              `size = axcl.rt.engine_get_input_size_by_index(io_info, group, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int group: group
    :param int index: index
    :returns: **size** (*int*) - input size
    """
    size = 0
    try:
        libaxcl_rt.axclrtEngineGetInputSizeByIndex.restype = c_uint64
        libaxcl_rt.axclrtEngineGetInputSizeByIndex.argtypes=[c_void_p, c_uint32, c_uint32]
        if io_info:
            c_io_info = c_void_p(io_info)
            size = libaxcl_rt.axclrtEngineGetInputSizeByIndex(c_io_info, c_uint32(group), c_uint32(index))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return size


def engine_get_output_size_by_index(io_info: int, group: int, index: int) -> int:
    """
    Get output size by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `uint64_t axclrtEngineGetOutputSizeByIndex(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index);`
        **python**              `size = axcl.rt.engine_get_output_size_by_index(io_info, group, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int group: group
    :param int index: index
    :returns: **size** (*int*) - output size
    """
    size = 0
    try:
        libaxcl_rt.axclrtEngineGetOutputSizeByIndex.restype = c_uint64
        libaxcl_rt.axclrtEngineGetOutputSizeByIndex.argtypes=[c_void_p, c_uint32, c_uint32]
        if io_info:
            c_io_info = c_void_p(io_info)
            size = libaxcl_rt.axclrtEngineGetOutputSizeByIndex(c_io_info, c_uint32(group), c_uint32(index))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return size


def engine_get_input_name_by_index(io_info: int, index: int) -> str:
    """
    Get input name by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `const char *axclrtEngineGetInputNameByIndex(axclrtEngineIOInfo ioInfo, uint32_t index);`
        **python**              `name = axcl.rt.engine_get_input_name_by_index(io_info, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int index: index
    :returns: **name** (*str*) - input name
    """
    name = None
    try:
        libaxcl_rt.axclrtEngineGetInputNameByIndex.restype = c_char_p
        libaxcl_rt.axclrtEngineGetInputNameByIndex.argtypes=[c_void_p, c_uint32]
        if io_info:
            c_io_info = c_void_p(io_info)
            c_name = libaxcl_rt.axclrtEngineGetInputNameByIndex(c_io_info, c_uint32(index))
            if c_name:
                name = c_name.decode('utf-8')
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return name


def engine_get_output_name_by_index(io_info: int, index: int) -> str:
    """
    Get output name by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `const char *axclrtEngineGetOutputNameByIndex(axclrtEngineIOInfo ioInfo, uint32_t index);`
        **python**              `name = axcl.rt.engine_get_output_name_by_index(io_info, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int index: index
    :returns: **name** (*str*) - input name
    """
    name = None
    try:
        libaxcl_rt.axclrtEngineGetOutputNameByIndex.restype = c_char_p
        libaxcl_rt.axclrtEngineGetOutputNameByIndex.argtypes=[c_void_p, c_uint32]
        if io_info:
            c_io_info = c_void_p(io_info)
            c_name = libaxcl_rt.axclrtEngineGetOutputNameByIndex(c_io_info, c_uint32(index))
            if c_name:
                name = c_name.decode('utf-8')
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return name


def engine_get_input_index_by_name(io_info: int, name: str) -> int:
    """
    Get input index by name

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `int32_t axclrtEngineGetInputIndexByName(axclrtEngineIOInfo ioInfo, const char *name);`
        **python**              `index = axcl.rt.engine_get_input_index_by_name(io_info, name)`
        ======================= =====================================================

    :param int io_info: io info address
    :param str name: input name
    :returns: **index** (*int*) - input index
    """
    index = -1
    try:
        libaxcl_rt.axclrtEngineGetInputIndexByName.restype = c_int32
        libaxcl_rt.axclrtEngineGetInputIndexByName.argtypes=[c_void_p, c_char_p]
        if io_info and name and len(name) > 0:
            c_io_info = c_void_p(io_info)
            c_name = c_char_p(name.encode('utf-8'))
            index = libaxcl_rt.axclrtEngineGetInputIndexByName(c_io_info, c_name)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return index


def engine_get_output_index_by_name(io_info: int, name: str) -> int:
    """
    Get output index by name

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `int32_t axclrtEngineGetOutputIndexByName(axclrtEngineIOInfo ioInfo, const char *name);`
        **python**              `index = axcl.rt.engine_get_output_index_by_name(io_info, name)`
        ======================= =====================================================

    :param int io_info: io info address
    :param str name: input name
    :returns: **index** (*int*) - output index
    """
    index = -1
    try:
        libaxcl_rt.axclrtEngineGetOutputIndexByName.restype = c_int32
        libaxcl_rt.axclrtEngineGetOutputIndexByName.argtypes=[c_void_p, c_char_p]
        if io_info and name and len(name) > 0:
            c_io_info = c_void_p(io_info)
            c_name = c_char_p(name.encode('utf-8'))
            index = libaxcl_rt.axclrtEngineGetOutputIndexByName(c_io_info, c_name)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return index


def engine_get_input_dims(io_info: int, group: int, index: int) -> tuple[list, int]:
    """
    Get input dims by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetInputDims(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index, axclrtEngineIODims *dims);`
        **python**              `dims, ret = axcl.rt.engine_get_input_dims(io_info, group, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int group: group
    :param int index: index
    :returns: tuple[list, int]

        - **dims** (*list*) - list of dims
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_dims = axclrtEngineIODims(0)
    dims = []

    try:
        libaxcl_rt.axclrtEngineGetInputDims.restype = axclError
        libaxcl_rt.axclrtEngineGetInputDims.argtypes=[c_void_p, c_uint32, c_uint32, POINTER(axclrtEngineIODims)]
        c_group = c_uint32(group)
        c_index = c_uint32(index)
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineGetInputDims(c_io_info, c_group, c_index, byref(c_dims))
            if ret == 0:
                for i in range(c_dims.dimCount):
                    dims.append(c_dims.dims[i])
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return dims, ret


def engine_get_output_dims(io_info: int, group: int, index: int) -> tuple[list, int]:
    """
    Get output dims by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetOutputDims(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index, axclrtEngineIODims *dims);`
        **python**              `dims, ret = axcl.rt.engine_get_output_dims(io_info, group, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int group: group
    :param int index: index
    :returns: tuple[list, int]

        - **dims** (*list*) - list of dims
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_dims = axclrtEngineIODims(0)
    dims = []

    try:
        libaxcl_rt.axclrtEngineGetOutputDims.restype = axclError
        libaxcl_rt.axclrtEngineGetOutputDims.argtypes=[c_void_p, c_uint32, c_uint32, POINTER(axclrtEngineIODims)]
        c_group = c_uint32(group)
        c_index = c_uint32(index)
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineGetOutputDims(c_io_info, c_group, c_index, byref(c_dims))
            if ret == 0:
                for i in range(c_dims.dimCount):
                    dims.append(c_dims.dims[i])
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return dims, ret


def engine_get_input_data_type(io_info: int, index: int) -> tuple[int, int]:
    """
    Get input data type by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `int32_t axclrtEngineGetInputDataType(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataType *type);`
        **python**              `type, ret = axcl.rt.engine_get_input_data_type(io_info, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int index: index
    :returns: tuple[int, int]

        - **type** (*int*) - data type
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_type = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetInputDataType.restype = axclError
        libaxcl_rt.axclrtEngineGetInputDataType.argtypes=[c_void_p, c_uint32, POINTER(c_int32)]
        c_index = c_uint32(index)
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineGetInputDataType(c_io_info, c_index, byref(c_type))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_type.value, ret


def engine_get_output_data_type(io_info: int, index: int) -> tuple[int, int]:
    """
    Get output data type by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `int32_t axclrtEngineGetOutputDataType(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataType *type);`
        **python**              `type, ret = axcl.rt.engine_get_output_data_type(io_info, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int index: index
    :returns: tuple[int, int]

        - **type** (*int*) - data type
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_type = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetOutputDataType.restype = axclError
        libaxcl_rt.axclrtEngineGetOutputDataType.argtypes=[c_void_p, c_uint32, POINTER(c_int32)]
        c_index = c_uint32(index)
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineGetOutputDataType(c_io_info, c_index, byref(c_type))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_type.value, ret


def engine_get_input_data_layout(io_info: int, index: int) -> tuple[int, int]:
    """
    Get input data layout by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `int32_t axclrtEngineGetInputDataLayout(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataLayout *layout);`
        **python**              `layout, ret = axcl.rt.engine_get_input_data_layout(io_info, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int index: index
    :returns: tuple[int, int]

        - **layout** (*int*) - data layout
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_layout = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetInputDataLayout.restype = axclError
        libaxcl_rt.axclrtEngineGetInputDataLayout.argtypes=[c_void_p, c_uint32, POINTER(c_int32)]
        c_index = c_uint32(index)
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineGetInputDataLayout(c_io_info, c_index, byref(c_layout))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_layout.value, ret


def engine_get_output_data_layout(io_info: int, index: int) -> tuple[int, int]:
    """
    Get output data layout by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `int32_t axclrtEngineGetOutputDataLayout(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataLayout *layout);`
        **python**              `layout, ret = axcl.rt.engine_get_output_data_layout(io_info, index)`
        ======================= =====================================================

    :param int io_info: io info address
    :param int index: index
    :returns: tuple[int, int]

        - **layout** (*int*) - data layout
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_layout = c_int32(0)
    try:
        libaxcl_rt.axclrtEngineGetOutputDataLayout.restype = axclError
        libaxcl_rt.axclrtEngineGetOutputDataLayout.argtypes=[c_void_p, c_uint32, POINTER(c_int32)]
        c_index = c_uint32(index)
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineGetOutputDataLayout(c_io_info, c_index, byref(c_layout))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_layout.value, ret


def engine_create_io(io_info: int) -> tuple[int, int]:
    """
    Create io

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineCreateIO(axclrtEngineIOInfo ioInfo, axclrtEngineIO *io);`
        **python**              `io, ret = axcl.rt.engine_create_io(io_info)`
        ======================= =====================================================

    :param int io_info: io info address
    :returns: tuple[int, int]

        - **io** (*int*) - io address
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    io = c_void_p(0)

    try:
        libaxcl_rt.axclrtEngineCreateIO.restype = axclError
        libaxcl_rt.axclrtEngineCreateIO.argtypes=[c_void_p, POINTER(c_void_p)]
        if io_info:
            c_io_info = c_void_p(io_info)
            ret = libaxcl_rt.axclrtEngineCreateIO(c_io_info, byref(io))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return io.value, ret


def engine_destroy_io(io: int) -> int:
    """
    Destroy io

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineDestroyIO(axclrtEngineIO io);`
        **python**              `ret = axcl.rt.engine_destroy_io(io)`
        ======================= =====================================================

    :param int io: io address
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1

    try:
        libaxcl_rt.axclrtEngineDestroyIO.restype = axclError
        libaxcl_rt.axclrtEngineDestroyIO.argtypes=[c_void_p]
        if io:
            c_io = c_void_p(io)
            ret = libaxcl_rt.axclrtEngineDestroyIO(c_io)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_set_input_buffer_by_index(io: int, index: int, data_buffer: int, size: int) -> int:
    """
    Set input buffer by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineSetInputBufferByIndex(axclrtEngineIO io, uint32_t index, const void *dataBuffer, uint64_t size);`
        **python**              `ret = axcl.rt.engine_set_input_buffer_by_index(io, index, data_buffer, size)`
        ======================= =====================================================

    :param int io: io address
    :param int index: index
    :param int data_buffer: data buffer address
    :param int size: data buffer size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1

    try:
        libaxcl_rt.axclrtEngineSetInputBufferByIndex.restype = axclError
        libaxcl_rt.axclrtEngineSetInputBufferByIndex.argtypes=[c_void_p, c_uint32, c_void_p, c_uint64]
        c_index = c_uint32(index)
        c_size = c_uint64(size)
        if io:
            c_io = c_void_p(io)
            ret = libaxcl_rt.axclrtEngineSetInputBufferByIndex(c_io, c_index, data_buffer, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_set_output_buffer_by_index(io: int, index: int, data_buffer: int, size: int) -> int:
    """
    Set output buffer by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineSetOutputBufferByIndex(axclrtEngineIO io, uint32_t index, const void *dataBuffer, uint64_t size);`
        **python**              `ret = axcl.rt.engine_set_output_buffer_by_index(io, index, data_buffer, size)`
        ======================= =====================================================

    :param int io: io address
    :param int index: index
    :param int data_buffer: data buffer address
    :param int size: data buffer size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1

    try:
        libaxcl_rt.axclrtEngineSetOutputBufferByIndex.restype = axclError
        libaxcl_rt.axclrtEngineSetOutputBufferByIndex.argtypes=[c_void_p, c_uint32, c_void_p, c_uint64]
        c_index = c_uint32(index)
        c_size = c_uint64(size)
        if io:
            c_io = c_void_p(io)
            ret = libaxcl_rt.axclrtEngineSetOutputBufferByIndex(c_io, c_index, data_buffer, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_set_input_buffer_by_name(io: int, name: str, data_buffer: int, size: int) -> int:
    """
    Set input buffer by name

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineSetInputBufferByName(axclrtEngineIO io, const char *name, const void *dataBuffer, uint64_t size);`
        **python**              `ret = axcl.rt.engine_set_input_buffer_by_name(io, name, data_buffer, size)`
        ======================= =====================================================

    :param int io: io address
    :param str name: name
    :param int data_buffer: data buffer address
    :param int size: data buffer size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1

    try:
        libaxcl_rt.axclrtEngineSetInputBufferByName.restype = axclError
        libaxcl_rt.axclrtEngineSetInputBufferByName.argtypes=[c_void_p, c_char_p, c_void_p, c_uint64]
        c_size = c_uint64(size)
        if io and name and len(name) > 0:
            c_io = c_void_p(io)
            c_name = c_char_p(name.encode('utf-8'))
            ret = libaxcl_rt.axclrtEngineSetInputBufferByName(c_io, c_name, data_buffer, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_set_output_buffer_by_name(io: int, name: str, data_buffer: int, size: int) -> int:
    """
    Set output buffer by name

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineSetOutputBufferByName(axclrtEngineIO io, const char *name, const void *dataBuffer, uint64_t size);`
        **python**              `ret = axcl.rt.engine_set_output_buffer_by_name(io, name, data_buffer, size)`
        ======================= =====================================================

    :param int io: io address
    :param str name: name
    :param int data_buffer: data buffer address
    :param int size: data buffer size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1

    try:
        libaxcl_rt.axclrtEngineSetOutputBufferByName.restype = axclError
        libaxcl_rt.axclrtEngineSetOutputBufferByName.argtypes=[c_void_p, c_char_p, c_void_p, c_uint64]
        c_size = c_uint64(size)
        if io and name and len(name) > 0:
            c_io = c_void_p(io)
            c_name = c_char_p(name.encode('utf-8'))
            ret = libaxcl_rt.axclrtEngineSetOutputBufferByName(c_io, c_name, data_buffer, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_get_input_buffer_by_index(io: int, index: int) -> tuple[int, int, int]:
    """
    Get input buffer by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetInputBufferByIndex(axclrtEngineIO io, uint32_t index, void **dataBuffer, uint64_t *size);`
        **python**              `buffer, size, ret = axcl.rt.engine_get_input_buffer_by_index(io, index)`
        ======================= =====================================================

    :param int io: io address
    :param int index: index
    :returns: tuple[int, int, int]

        - **buffer** (*int*) - buffer address
        - **size** (*int*) - buffer size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    data_buffer = c_void_p(0)
    size = c_uint64(0)
    try:
        libaxcl_rt.axclrtEngineGetInputBufferByIndex.restype = axclError
        libaxcl_rt.axclrtEngineGetInputBufferByIndex.argtypes=[c_void_p, c_uint32, POINTER(c_void_p), POINTER(c_uint64)]
        c_index= c_uint32(index)
        if io:
            c_io = c_void_p(io)
            ret = libaxcl_rt.axclrtEngineGetInputBufferByIndex(c_io, c_index, byref(data_buffer), byref(size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return data_buffer.value, size.value, ret


def engine_get_output_buffer_by_index(io: int, index: int) -> tuple[int, int, int]:
    """
    Get output buffer by index

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetOutputBufferByIndex(axclrtEngineIO io, uint32_t index, void **dataBuffer, uint64_t *size);`
        **python**              `buffer, size, ret = axcl.rt.engine_get_output_buffer_by_index(io, index)`
        ======================= =====================================================

    :param int io: io address
    :param int index: index
    :returns: tuple[int, int, int]

        - **buffer** (*int*) - buffer address
        - **size** (*int*) - buffer size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    data_buffer = c_void_p(0)
    size = c_uint64(0)
    try:
        libaxcl_rt.axclrtEngineGetOutputBufferByIndex.restype = axclError
        libaxcl_rt.axclrtEngineGetOutputBufferByIndex.argtypes=[c_void_p, c_uint32, POINTER(c_void_p), POINTER(c_uint64)]
        c_index= c_uint32(index)
        if io:
            c_io = c_void_p(io)
            ret = libaxcl_rt.axclrtEngineGetOutputBufferByIndex(c_io, c_index, byref(data_buffer), byref(size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return data_buffer.value, size.value, ret


def engine_get_input_buffer_by_name(io: int, name: str) -> tuple[int, int, int]:
    """
    Get input buffer by name

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetInputBufferByName(axclrtEngineIO io, const char *name, void **dataBuffer, uint64_t *size);`
        **python**              `buffer, size, ret = axcl.rt.engine_get_input_buffer_by_name(io, name)`
        ======================= =====================================================

    :param int io: io address
    :param str name: name
    :returns: tuple[int, int, int]

        - **buffer** (*int*) - buffer address
        - **size** (*int*) - buffer size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    data_buffer = c_void_p(0)
    size = c_uint64(0)
    try:
        libaxcl_rt.axclrtEngineGetInputBufferByName.restype = axclError
        libaxcl_rt.axclrtEngineGetInputBufferByName.argtypes=[c_void_p, c_char_p, POINTER(c_void_p), POINTER(c_uint64)]
        if io and name and len(name) > 0:
            c_io = c_void_p(io)
            c_name = c_char_p(name.encode('utf-8'))
            ret = libaxcl_rt.axclrtEngineGetInputBufferByName(c_io, c_name, byref(data_buffer), byref(size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return data_buffer.value, size.value, ret


def engine_get_output_buffer_by_name(io: int, name: str) -> tuple[int, int, int]:
    """
    Get output buffer by name

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineGetOutputBufferByName(axclrtEngineIO io, const char *name, void **dataBuffer, uint64_t *size);`
        **python**              `buffer, size, ret = axcl.rt.engine_get_output_buffer_by_name(io, name)`
        ======================= =====================================================

    :param int io: io address
    :param str name: name
    :returns: tuple[int, int, int]

        - **buffer** (*int*) - buffer address
        - **size** (*int*) - buffer size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    data_buffer = c_void_p(0)
    size = c_uint64(0)
    try:
        libaxcl_rt.axclrtEngineGetOutputBufferByName.restype = axclError
        libaxcl_rt.axclrtEngineGetOutputBufferByName.argtypes=[c_void_p, c_char_p, POINTER(c_void_p), POINTER(c_uint64)]
        if io and name and len(name) > 0:
            c_io = c_void_p(io)
            c_name = c_char_p(name.encode('utf-8'))
            ret = libaxcl_rt.axclrtEngineGetOutputBufferByName(c_io, c_name, byref(data_buffer), byref(size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return data_buffer.value, size.value, ret


def engine_set_dynamic_batch_size(io: int, batch_size: int) -> int:
    """
    Set dynamic batch size

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineSetDynamicBatchSize(axclrtEngineIO io, uint32_t batchSize);`
        **python**              `ret = axcl.rt.engine_set_dynamic_batch_size(io, batch_size)`
        ======================= =====================================================

    :param int io: io address
    :param int batch_size: batch size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_rt.axclrtEngineSetDynamicBatchSize.restype = axclError
        libaxcl_rt.axclrtEngineSetDynamicBatchSize.argtypes=[c_void_p, c_uint32]
        c_batch_size = c_uint32(batch_size)
        if io:
            c_io = c_void_p(io)
            ret = libaxcl_rt.axclrtEngineSetDynamicBatchSize(c_io, c_batch_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_create_context(model_id: int) -> tuple[int, int]:
    """
    Create context

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineCreateContext(uint64_t modelId, uint64_t *contextId);`
        **python**              `context, ret = axcl.rt.engine_create_context(model_id)`
        ======================= =====================================================

    :param int model_id: model id
    :returns: tuple[int, int]

        - **context** (*int*) - context id
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    context_id = c_uint64(0)
    try:
        libaxcl_rt.axclrtEngineCreateContext.restype = axclError
        libaxcl_rt.axclrtEngineCreateContext.argtypes=[c_uint64, POINTER(c_uint64)]
        c_model_id = c_uint64(model_id)
        ret = libaxcl_rt.axclrtEngineCreateContext(c_model_id, byref(context_id))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return context_id.value, ret


def engine_execute(model_id: int, context_id: int, group: int, io: int) -> int:
    """
    Execute

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineExecute(uint64_t modelId, uint64_t contextId, uint32_t group, axclrtEngineIO io);`
        **python**              `ret = axcl.rt.engine_execute(model_id, context_id, group, io)`
        ======================= =====================================================

    :param int model_id: model id
    :param int context_id: context id
    :param int group: group
    :param int io: io address
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """

    ret = -1

    try:
        libaxcl_rt.axclrtEngineExecute.restype = axclError
        libaxcl_rt.axclrtEngineExecute.argtypes=[c_uint64, c_uint64, c_uint32, c_void_p]
        c_model_id = c_uint64(model_id)
        c_context_id = c_uint64(context_id)
        c_group = c_uint32(group)
        if io:
            c_io = c_void_p(io)
            ret = libaxcl_rt.axclrtEngineExecute(c_model_id, c_context_id, c_group, c_io)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def engine_execute_async(model_id: int, context_id: int, group: int, io: int, stream: int) -> int:
    """
    Execute async

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `axclError axclrtEngineExecuteAsync(uint64_t modelId, uint64_t contextId, uint32_t group, axclrtEngineIO io, axclrtStream stream);`
        **python**              `ret = axcl.rt.engine_execute_async(model_id, context_id, group, io, stream)`
        ======================= =====================================================

    :param int model_id: model id
    :param int context_id: context id
    :param int group: group
    :param int io: io address
    :param int stream: stream id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1

    try:
        libaxcl_rt.axclrtEngineExecuteAsync.restype = axclError
        libaxcl_rt.axclrtEngineExecuteAsync.argtypes=[c_uint64, c_uint64, c_uint32, c_void_p, c_void_p]
        c_model_id = c_uint64(model_id)
        c_context_id = c_uint64(context_id)
        c_group = c_uint32(group)
        if io and stream:
            c_io = c_void_p(io)
            c_stream = c_void_p(stream)
            ret = libaxcl_rt.axclrtEngineExecuteAsync(c_model_id, c_context_id, c_group, c_io, c_stream)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret
