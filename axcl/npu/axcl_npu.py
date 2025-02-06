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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.lib.axcl_lib import libaxcl_npu
from axcl.npu.axcl_npu_type import *
from axcl.ax_global_type import *


def get_version() -> str:
    """
    Get NPU engine lib version

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `const AX_CHAR* AX_ENGINE_GetVersion(AX_VOID);`
        **python**              `version = axcl.npu.get_version()`
        ======================= =====================================================

    :returns: **version** (*str*) - the version string of the npu lib
    """
    try:
        libaxcl_npu.AXCL_ENGINE_GetVersion.restype = c_char_p
        version = libaxcl_npu.AXCL_ENGINE_GetVersion()

        return version.decode("utf-8") if version else ""
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
        return ""


def npu_reset() -> None:
    """
    Reset the NPU engine

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID AX_ENGINE_NPUReset(AX_VOID);`
        **python**              `axcl.npu.npu_reset()`
        ======================= =====================================================

    :returns: None
    """
    try:
        libaxcl_npu.AXCL_ENGINE_NPUReset.restype = None
        libaxcl_npu.AXCL_ENGINE_NPUReset.argtypes = None
        libaxcl_npu.AXCL_ENGINE_NPUReset()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())


def init(npu_attr: dict) -> int:
    """
    Initialize the NPU engine with attributes.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_Init(AX_ENGINE_NPU_ATTR_T* pNpuAttr);`
        **python**              `ret = axcl.npu.init(npu_attr)`
        ======================= =====================================================

    :param dict npu_attr: NPU attributes to initialize, see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_NPU_ATTR_T`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        c_npu_attr = AX_ENGINE_NPU_ATTR_T()
        c_npu_attr.dict2struct(npu_attr)

        libaxcl_npu.AXCL_ENGINE_Init.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_Init.argtypes = [POINTER(AX_ENGINE_NPU_ATTR_T)]
        ret = libaxcl_npu.AXCL_ENGINE_Init(byref(c_npu_attr))
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def get_npu_attr() -> tuple[dict, int]:
    """
    Retrieve the attributes of the NPU.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetVNPUAttr(AX_ENGINE_NPU_ATTR_T* pNpuAttr);`
        **python**              `npu_attr, ret = axcl.npu.get_npu_attr()`
        ======================= =====================================================

    :returns: **npu_attr** (*dict*) - attributes(see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_NPU_ATTR_T`) of the NPU, **ret** (*int*) - result code
    """
    ret = -1
    npu_attr = {}
    try:
        c_npu_attr = AX_ENGINE_NPU_ATTR_T()

        libaxcl_npu.AXCL_ENGINE_GetVNPUAttr.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetVNPUAttr.argtypes = [POINTER(AX_ENGINE_NPU_ATTR_T)]
        ret = libaxcl_npu.AXCL_ENGINE_GetVNPUAttr(byref(c_npu_attr))

        if ret == AX_SUCCESS:
            npu_attr = c_npu_attr.struct2dict()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return npu_attr, ret


def deinit() -> int:
    """
    Deinitialize the NPU engine.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_Deinit(AX_VOID);`
        **python**              `ret = axcl.npu.deinit()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_npu.AXCL_ENGINE_Deinit.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_Deinit.argtypes = None
        ret = libaxcl_npu.AXCL_ENGINE_Deinit()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def get_model_type(ptr: int, size: int) -> tuple[int, int]:
    """
    Get the model type from the provided data.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetModelType(const AX_VOID* pData, AX_U32 nDataSize, AX_ENGINE_MODEL_TYPE_T* pModelType);`
        **python**              `model_type, ret = axcl.npu.get_model_type(ptr, size)`
        ======================= =====================================================

    :param int ptr: Pointer to the data
    :param int size: Size of the data
    :returns: **model_type** (*int*) - the type (see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_MODEL_TYPE_T`) of the model, **ret** (*int*) - result code
    """
    ret = -1
    model_type = AX_ENGINE_MODEL_TYPE0
    try:
        c_buffer_ptr = cast(c_void_p(ptr), c_void_p) if isinstance(ptr, int) else ptr
        c_model_type = AX_ENGINE_MODEL_TYPE_T(AX_ENGINE_MODEL_TYPE0)

        libaxcl_npu.AXCL_ENGINE_GetModelType.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetModelType.argtypes = [
            c_void_p,
            c_uint32,
            POINTER(AX_ENGINE_MODEL_TYPE_T),
        ]

        ret = libaxcl_npu.AXCL_ENGINE_GetModelType(
            c_buffer_ptr, AX_U32(size), byref(c_model_type)
        )

        if ret == AX_SUCCESS:
            model_type = c_model_type.value
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return model_type, ret


def create_handle(ptr: int, size: int) -> tuple[int, int]:
    """
    Create a handle for the model.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_CreateHandle(AX_ENGINE_HANDLE* pHandle, const AX_VOID* pData, AX_U32 nDataSize);`
        **python**              `handle, ret = axcl.npu.create_handle(ptr, size)`
        ======================= =====================================================

    :param int ptr: Pointer to the data
    :param int size: Size of the data
    :returns: **handle** (*int*) - the created handle, **ret** (*int*) - result code
    """
    ret = -1
    handle = None
    try:
        c_handle = AX_ENGINE_HANDLE()
        c_buffer_ptr = cast(c_void_p(ptr), c_void_p) if isinstance(ptr, int) else ptr

        libaxcl_npu.AXCL_ENGINE_CreateHandle.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_CreateHandle.argtypes = [
            POINTER(AX_ENGINE_HANDLE),
            c_void_p,
            c_uint32,
        ]

        ret = libaxcl_npu.AXCL_ENGINE_CreateHandle(
            byref(c_handle), c_buffer_ptr, AX_U32(size)
        )

        if ret == AX_SUCCESS:
            handle = c_handle.value
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return handle, ret


def create_handle_v2(ptr: int, size: int, extra: dict) -> tuple[int, int]:
    """
    Create a handle for the model with additional parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_CreateHandleV2(AX_ENGINE_HANDLE* pHandle, const AX_VOID* pData, AX_U32 nDataSize, AX_ENGINE_HANDLE_EXTRA_T* pExtra);`
        **python**              `handle, ret = axcl.npu.create_handle_v2(ptr, size, extra)`
        ======================= =====================================================

    :param int ptr: Pointer to the data
    :param int size: Size of the data
    :param dict extra: Additional parameters for handle creation, see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_HANDLE_EXTRA_T`
    :returns: **handle** (*int*) - the created handle, **ret** (*int*) - result code
    """
    ret = -1
    handle = None
    try:
        c_handle = AX_ENGINE_HANDLE()
        c_buffer_ptr = cast(c_void_p(ptr), c_void_p) if isinstance(ptr, int) else ptr
        c_extra = AX_ENGINE_HANDLE_EXTRA_T()
        c_extra.dict2struct(extra)

        libaxcl_npu.AXCL_ENGINE_CreateHandleV2.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_CreateHandleV2.argtypes = [
            POINTER(AX_ENGINE_HANDLE),
            c_void_p,
            c_uint32,
            POINTER(AX_ENGINE_HANDLE_EXTRA_T),
        ]

        ret = libaxcl_npu.AXCL_ENGINE_CreateHandleV2(
            byref(c_handle), c_buffer_ptr, AX_U32(size), c_extra
        )

        if ret == AX_SUCCESS:
            handle = c_handle.value
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return handle, ret


def destroy_handle(handle: int) -> int:
    """
    Destroy the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_DestroyHandle(AX_ENGINE_HANDLE nHandle);`
        **python**              `ret = axcl.npu.destroy_handle(handle)`
        ======================= =====================================================

    :param int handle: The handle to be destroyed
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        c_handle = cast(c_void_p(handle), c_void_p)

        libaxcl_npu.AXCL_ENGINE_DestroyHandle.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_DestroyHandle.argtypes = [AX_ENGINE_HANDLE]
        ret = libaxcl_npu.AXCL_ENGINE_DestroyHandle(c_handle)
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def get_handle_model_type(handle: int) -> tuple[int, int]:
    """
    Get the model type associated with the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetHandleModelType(AX_ENGINE_HANDLE nHandle, AX_ENGINE_MODEL_TYPE_T* pModelType);`
        **python**              `model_type, ret = axcl.npu.get_handle_model_type(handle)`
        ======================= =====================================================

    :param int handle: The handle to query
    :returns: **model_type** (*int*) - the type(see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_MODEL_TYPE_T`) of the model, **ret** (*int*) - result code
    """
    ret = -1
    model_type = AX_ENGINE_MODEL_TYPE0
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_model_type = AX_ENGINE_MODEL_TYPE_T()

        libaxcl_npu.AXCL_ENGINE_GetHandleModelType.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetHandleModelType.argtypes = [
            AX_ENGINE_HANDLE,
            POINTER(AX_ENGINE_MODEL_TYPE_T),
        ]

        ret = libaxcl_npu.AXCL_ENGINE_GetHandleModelType(c_handle, byref(c_model_type))

        if ret == AX_SUCCESS:
            model_type = c_model_type.value
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return model_type, ret


def _info2dict(c_io_info: AX_ENGINE_IO_INFO_T) -> dict:
    io_info = c_io_info.struct2dict()

    inputs = []
    for i in range(c_io_info.nInputSize):
        inputs.append(c_io_info.pInputs[i].struct2dict())
    io_info["inputs"] = inputs

    outputs = []
    for i in range(c_io_info.nOutputSize):
        outputs.append(c_io_info.pOutputs[i].struct2dict())
    io_info["outputs"] = outputs

    return io_info


def get_io_info(handle: int) -> tuple[dict, int]:
    """
    Retrieve IO information for the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetIOInfo(AX_ENGINE_HANDLE nHandle, AX_ENGINE_IO_INFO_T** pIO);`
        **python**              `io_info, ret = axcl.npu.get_io_info(handle)`
        ======================= =====================================================

    :param int handle: The handle to query
    :returns: **io_info** (*dict*) - IO information(see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_IO_INFO_T`), **ret** (*int*) - result code
    """
    ret = -1
    io_info = {}
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_io_info_ptr = POINTER(AX_ENGINE_IO_INFO_T)()

        libaxcl_npu.AXCL_ENGINE_GetIOInfo.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetIOInfo.argtypes = [
            AX_ENGINE_HANDLE,
            POINTER(POINTER(AX_ENGINE_IO_INFO_T)),
        ]

        ret = libaxcl_npu.AXCL_ENGINE_GetIOInfo(c_handle, byref(c_io_info_ptr))

        if ret == AX_SUCCESS and c_io_info_ptr:
            io_info = _info2dict(c_io_info_ptr.contents)

    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return io_info, ret


def get_group_io_info_count(handle: int) -> tuple[int, int]:
    """
    Get the count of IO information groups for the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetGroupIOInfoCount(AX_ENGINE_HANDLE nHandle, AX_U32* pCount);`
        **python**              `count, ret = axcl.npu.get_group_io_info_count(handle)`
        ======================= =====================================================

    :param int handle: The handle to query
    :returns: **count** (*int*) - number of IO information groups, **ret** (*int*) - result code
    """
    ret = -1
    count = 0
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_count = c_uint32()

        libaxcl_npu.AXCL_ENGINE_GetGroupIOInfoCount.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetGroupIOInfoCount.argtypes = [
            AX_ENGINE_HANDLE,
            POINTER(c_uint32),
        ]

        ret = libaxcl_npu.AXCL_ENGINE_GetGroupIOInfoCount(c_handle, byref(c_count))

        if ret == AX_SUCCESS:
            count = c_count.value
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return count, ret


def get_group_io_info(handle: int, index: int) -> tuple[dict, int]:
    """
    Get IO information for a specific group index.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetGroupIOInfo(AX_ENGINE_HANDLE nHandle, AX_U32 nIndex, AX_ENGINE_IO_INFO_T** pIO);`
        **python**              `io_info, ret = axcl.npu.get_group_io_info(handle, index)`
        ======================= =====================================================

    :param int handle: The handle to query
    :param int index: The index of the group
    :returns: **io_info** (*dict*) - IO information(see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_IO_INFO_T`) for the group, **ret** (*int*) - result code
    """
    ret = -1
    io_info = {}
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_io_info_ptr = POINTER(AX_ENGINE_IO_INFO_T)()

        libaxcl_npu.AXCL_ENGINE_GetGroupIOInfo.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetGroupIOInfo.argtypes = [
            AX_ENGINE_HANDLE,
            c_uint32,
            POINTER(POINTER(AX_ENGINE_IO_INFO_T)),
        ]

        ret = libaxcl_npu.AXCL_ENGINE_GetGroupIOInfo(
            c_handle, c_uint32(index), byref(c_io_info_ptr)
        )

        if ret == AX_SUCCESS and c_io_info_ptr:
            io_info = _info2dict(c_io_info_ptr.contents)

    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return io_info, ret


def create_context(handle: int) -> int:
    """
    Create a context for the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_CreateContext(AX_ENGINE_HANDLE handle);`
        **python**              `ret = axcl.npu.create_context(handle)`
        ======================= =====================================================

    :param int handle: The handle for which to create a context
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        c_handle = cast(c_void_p(handle), c_void_p)

        libaxcl_npu.AXCL_ENGINE_CreateContext.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_CreateContext.argtypes = [AX_ENGINE_HANDLE]
        ret = libaxcl_npu.AXCL_ENGINE_CreateContext(c_handle)
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def create_context_v2(handle: int) -> tuple[int, int]:
    """
    Create a context for the specified handle, returning the context.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_CreateContextV2(AX_ENGINE_HANDLE handle, AX_ENGINE_CONTEXT_T* pContext);`
        **python**              `ctx, ret = axcl.npu.create_context_v2(handle)`
        ======================= =====================================================

    :param int handle: The handle for which to create a context
    :returns: **ctx** (*int*) - the created context, **ret** (*int*) - result code
    """
    ret = -1
    ctx = None
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_ctx = AX_ENGINE_CONTEXT_T()

        libaxcl_npu.AXCL_ENGINE_CreateContextV2.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_CreateContextV2.argtypes = [
            AX_ENGINE_HANDLE,
            POINTER(AX_ENGINE_CONTEXT_T),
        ]
        ret = libaxcl_npu.AXCL_ENGINE_CreateContextV2(c_handle, byref(c_ctx))
        if ret == AX_SUCCESS:
            ctx = c_ctx.value
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ctx, ret


def _meta_array_dict2struct(meta: list[dict]) -> Array[AX_ENGINE_IO_BUFFER_T]:
    c_meta_array = (AX_ENGINE_IO_BUFFER_T * len(meta))()
    for i, m in enumerate(meta):
        buf = AX_ENGINE_IO_BUFFER_T()
        buf.dict2struct(m)
        c_meta_array[i] = buf
    return c_meta_array


def _io_dict2struct(io: dict) -> AX_ENGINE_IO_T:
    _io = io.copy()
    inputs_dict = io.get("inputs")
    outputs_dict = io.get("outputs")
    _io["inputs"] = _meta_array_dict2struct(inputs_dict)
    _io["outputs"] = _meta_array_dict2struct(outputs_dict)
    c_io = AX_ENGINE_IO_T()
    c_io.dict2struct(_io)
    return c_io


def run_sync(handle: int, io: dict) -> int:
    """
    Execute synchronous operation with the provided IO.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_RunSync(AX_ENGINE_HANDLE handle, AX_ENGINE_IO_T* pIO);`
        **python**              `ret = axcl.npu.run_sync(handle, io)`
        ======================= =====================================================

    :param int handle: The handle to execute the operation
    :param dict io: Input and output data for the operation, see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_IO_T`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_io = _io_dict2struct(io)

        libaxcl_npu.AXCL_ENGINE_RunSync.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_RunSync.argtypes = [
            AX_ENGINE_HANDLE,
            POINTER(AX_ENGINE_IO_T),
        ]
        ret = libaxcl_npu.AXCL_ENGINE_RunSync(c_handle, byref(c_io))
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def run_sync_v2(handle: int, context: int, io: dict) -> int:
    """
    Execute synchronous operation with context and provided IO.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_RunSyncV2(AX_ENGINE_HANDLE handle, AX_ENGINE_CONTEXT_T context, AX_ENGINE_IO_T* pIO);`
        **python**              `ret = axcl.npu.run_sync_v2(handle, context, io)`
        ======================= =====================================================

    :param int handle: The handle to execute the operation
    :param int context: The context for the operation
    :param dict io: Input and output data for the operation, see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_IO_T`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_context = cast(c_void_p(context), c_void_p)
        c_io = _io_dict2struct(io)

        libaxcl_npu.AXCL_ENGINE_RunSyncV2.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_RunSyncV2.argtypes = [
            AX_ENGINE_HANDLE,
            AX_ENGINE_CONTEXT_T,
            POINTER(AX_ENGINE_IO_T),
        ]
        ret = libaxcl_npu.AXCL_ENGINE_RunSyncV2(c_handle, c_context, byref(c_io))
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def run_group_io_sync(handle: int, context: int, index: int, io: dict) -> int:
    """
    Execute synchronous operation for a specific group with context.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_RunGroupIOSync(AX_ENGINE_HANDLE handle, AX_ENGINE_CONTEXT_T context, AX_U32 nIndex, AX_ENGINE_IO_T* pIO);`
        **python**              `ret = axcl.npu.run_group_io_sync(handle, context, index, io)`
        ======================= =====================================================

    :param int handle: The handle to execute the operation
    :param int context: The context for the operation
    :param int index: The index of the group
    :param dict io: Input and output data for the operation, see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_IO_T`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_context = cast(c_void_p(context), c_void_p)
        c_io = AX_ENGINE_IO_T()
        c_io.dict2struct(io)

        libaxcl_npu.AXCL_ENGINE_RunGroupIOSync.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_RunGroupIOSync.argtypes = [
            AX_ENGINE_HANDLE,
            AX_ENGINE_CONTEXT_T,
            c_uint32,
            POINTER(AX_ENGINE_IO_T),
        ]
        ret = libaxcl_npu.AXCL_ENGINE_RunGroupIOSync(
            c_handle, c_context, c_uint32(index), byref(c_io)
        )
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def get_affinity(handle: int) -> tuple[int, int]:
    """
    Retrieve the affinity of the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetAffinity(AX_ENGINE_HANDLE nHandle, AX_ENGINE_NPU_SET_T* pNpuSet);`
        **python**              `affinity, ret = axcl.npu.get_affinity(handle)`
        ======================= =====================================================

    :param int handle: The handle to query
    :returns: **affinity** (*int*) - the affinity value, **ret** (*int*) - result code
    """
    ret = -1
    affinity = 0
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_affinity = AX_ENGINE_NPU_SET_T()

        libaxcl_npu.AXCL_ENGINE_GetAffinity.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetAffinity.argtypes = [
            AX_ENGINE_HANDLE,
            POINTER(AX_ENGINE_NPU_SET_T),
        ]
        ret = libaxcl_npu.AXCL_ENGINE_GetAffinity(c_handle, byref(c_affinity))

        if ret == AX_SUCCESS:
            affinity = c_affinity.value
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return affinity, ret


def set_affinity(handle: int, npu_set: int) -> int:
    """
    Set the affinity for the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_SetAffinity(AX_ENGINE_HANDLE nHandle, AX_ENGINE_NPU_SET_T nNpuSet);`
        **python**              `ret = axcl.npu.set_affinity(handle, npu_set)`
        ======================= =====================================================

    :param int handle: The handle to set the affinity for
    :param int npu_set: The NPU set to assign
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        c_handle = cast(c_void_p(handle), c_void_p)

        libaxcl_npu.AXCL_ENGINE_SetAffinity.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_SetAffinity.argtypes = [
            AX_ENGINE_HANDLE,
            AX_ENGINE_NPU_SET_T,
        ]
        ret = libaxcl_npu.AXCL_ENGINE_SetAffinity(
            c_handle, AX_ENGINE_NPU_SET_T(npu_set)
        )
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return ret


def get_cmm_usage(handle: int) -> tuple[dict, int]:
    """
    Retrieve CMM usage information for the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_ENGINE_GetCMMUsage(AX_ENGINE_HANDLE nHandle, AX_ENGINE_CMM_INFO* pCMMInfo);`
        **python**              `cmm_info, ret = axcl.npu.get_cmm_usage(handle)`
        ======================= =====================================================

    :param int handle: The handle to query
    :returns: **cmm_info** (*dict*) - CMM usage information(see :class:`axcl.npu.axcl_npu_type.AX_ENGINE_CMM_INFO`), **ret** (*int*) - result code
    """
    ret = -1
    cmm_info = {}
    try:
        c_handle = cast(c_void_p(handle), c_void_p)
        c_cmm_info = AX_ENGINE_CMM_INFO()

        libaxcl_npu.AXCL_ENGINE_GetCMMUsage.restype = c_int32
        libaxcl_npu.AXCL_ENGINE_GetCMMUsage.argtypes = [
            AX_ENGINE_HANDLE,
            POINTER(AX_ENGINE_CMM_INFO),
        ]
        ret = libaxcl_npu.AXCL_ENGINE_GetCMMUsage(c_handle, byref(c_cmm_info))

        if ret == AX_SUCCESS:
            cmm_info = c_cmm_info.struct2dict()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
    finally:
        return cmm_info, ret


def get_model_tools_version(handle: int) -> str:
    """
    Retrieve the model tools version for the specified handle.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `const AX_CHAR* AX_ENGINE_GetModelToolsVersion(AX_ENGINE_HANDLE nHandle);`
        **python**              `version = axcl.npu.get_model_tools_version(handle)`
        ======================= =====================================================

    :param int handle: The handle to query
    :returns: **version** (*str*) - the version string of the model tools
    """
    try:
        c_handle = cast(c_void_p(handle), c_void_p)

        libaxcl_npu.AXCL_ENGINE_GetModelToolsVersion.restype = c_char_p
        libaxcl_npu.AXCL_ENGINE_GetModelToolsVersion.argtypes = [AX_ENGINE_HANDLE]

        version = libaxcl_npu.AXCL_ENGINE_GetModelToolsVersion(c_handle)
        return version.decode("utf-8") if version else ""
    except:
        print(sys.exc_info())
        print(traceback.format_exc())
        return ""
