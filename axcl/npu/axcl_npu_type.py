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
from axcl.utils.axcl_basestructure import *

# Typedefs
AX_ENGINE_HANDLE = c_void_p
AX_ENGINE_CONTEXT_T = c_void_p
AX_ENGINE_EXECUTION_CONTEXT = c_void_p
AX_ENGINE_NPU_SET_T = c_uint32

# Enumerations
AX_ENGINE_TENSOR_LAYOUT_T = c_int32
"""
    tensor layout type

    .. parsed-literal::

        AX_ENGINE_TENSOR_LAYOUT_UNKNOWN  = 0x0
        AX_ENGINE_TENSOR_LAYOUT_NHWC     = 0x1
        AX_ENGINE_TENSOR_LAYOUT_NCHW     = 0x2
"""
AX_ENGINE_TENSOR_LAYOUT_UNKNOWN = 0
AX_ENGINE_TENSOR_LAYOUT_NHWC = 1
AX_ENGINE_TENSOR_LAYOUT_NCHW = 2


AX_ENGINE_MEMORY_TYPE_T = c_int32
"""
    tensor memory type

    .. parsed-literal::

        AX_ENGINE_MT_PHYSICAL  = 0x0
        AX_ENGINE_MT_VIRTUAL   = 0x1
        AX_ENGINE_MT_OCM       = 0x2
"""
AX_ENGINE_MT_PHYSICAL = 0
AX_ENGINE_MT_VIRTUAL = 1
AX_ENGINE_MT_OCM = 2


AX_ENGINE_DATA_TYPE_T = c_int32
"""
    tensor data type

    .. parsed-literal::

        AX_ENGINE_DT_UNKNOWN  = 0x0
        AX_ENGINE_DT_UINT8    = 0x1
        AX_ENGINE_DT_UINT16   = 0x2
        AX_ENGINE_DT_FLOAT32  = 0x3
        AX_ENGINE_DT_SINT16   = 0x4
        AX_ENGINE_DT_SINT8    = 0x5
        AX_ENGINE_DT_SINT32   = 0x6
        AX_ENGINE_DT_UINT32   = 0x7
        AX_ENGINE_DT_FLOAT64  = 0x8
        AX_ENGINE_DT_UINT10_PACKED = 100
        AX_ENGINE_DT_UINT12_PACKED = 101
        AX_ENGINE_DT_UINT14_PACKED = 102
        AX_ENGINE_DT_UINT16_PACKED = 103
"""
AX_ENGINE_DT_UNKNOWN = 0
AX_ENGINE_DT_UINT8 = 1
AX_ENGINE_DT_UINT16 = 2
AX_ENGINE_DT_FLOAT32 = 3
AX_ENGINE_DT_SINT16 = 4
AX_ENGINE_DT_SINT8 = 5
AX_ENGINE_DT_SINT32 = 6
AX_ENGINE_DT_UINT32 = 7
AX_ENGINE_DT_FLOAT64 = 8
AX_ENGINE_DT_UINT10_PACKED = 100
AX_ENGINE_DT_UINT12_PACKED = 101
AX_ENGINE_DT_UINT14_PACKED = 102
AX_ENGINE_DT_UINT16_PACKED = 103


AX_ENGINE_COLOR_SPACE_T = c_int32
"""
    tensor color space type

    .. parsed-literal::

        AX_ENGINE_CS_FEATUREMAP = 0
        AX_ENGINE_CS_RAW10      = 1
        AX_ENGINE_CS_RAW12      = 2
        AX_ENGINE_CS_RAW16      = 3
        AX_ENGINE_CS_NV12       = 4
        AX_ENGINE_CS_NV21       = 5
        AX_ENGINE_CS_RGB        = 6
        AX_ENGINE_CS_BGR        = 7
        AX_ENGINE_CS_RGBA       = 8
        AX_ENGINE_CS_GRAY       = 9
        AX_ENGINE_CS_YUV444     = 10
        AX_ENGINE_CS_RAW14      = 11
        AX_ENGINE_CS_RAW8       = 12
"""
AX_ENGINE_CS_FEATUREMAP = 0
AX_ENGINE_CS_RAW8 = 12
AX_ENGINE_CS_RAW10 = 1
AX_ENGINE_CS_RAW12 = 2
AX_ENGINE_CS_RAW14 = 11
AX_ENGINE_CS_RAW16 = 3
AX_ENGINE_CS_NV12 = 4
AX_ENGINE_CS_NV21 = 5
AX_ENGINE_CS_RGB = 6
AX_ENGINE_CS_BGR = 7
AX_ENGINE_CS_RGBA = 8
AX_ENGINE_CS_GRAY = 9
AX_ENGINE_CS_YUV444 = 10


AX_ENGINE_NPU_MODE_T = c_int32
"""
    vnpu type

    .. parsed-literal::

        AX_ENGINE_VIRTUAL_NPU_DISABLE    = 0
        AX_ENGINE_VIRTUAL_NPU_STD        = 1
        AX_ENGINE_VIRTUAL_NPU_BIG_LITTLE = 2
        AX_ENGINE_VIRTUAL_NPU_LITTLE_BIG = 3
        AX_ENGINE_VIRTUAL_NPU_BUTT       = 4
"""
AX_ENGINE_VIRTUAL_NPU_DISABLE = 0
AX_ENGINE_VIRTUAL_NPU_STD = 1
AX_ENGINE_VIRTUAL_NPU_BIG_LITTLE = 2
AX_ENGINE_VIRTUAL_NPU_LITTLE_BIG = 3
AX_ENGINE_VIRTUAL_NPU_BUTT = 4


AX_ENGINE_MODEL_TYPE_T = c_int32
"""
    model type

    .. parsed-literal::

        AX_ENGINE_MODEL_TYPE0     = 0
        AX_ENGINE_MODEL_TYPE1     = 1
        AX_ENGINE_MODEL_TYPE2     = 2
        AX_ENGINE_MODEL_TYPE_BUTT = 3
"""
AX_ENGINE_MODEL_TYPE0 = 0
AX_ENGINE_MODEL_TYPE1 = 1
AX_ENGINE_MODEL_TYPE2 = 2
AX_ENGINE_MODEL_TYPE_BUTT = 3


# Structures
class AX_ENGINE_NPU_ATTR_T(BaseStructure):
    """
    NPU attributes structure.

    .. parsed-literal::

        dict_npu_attr = {
            "hard_mode": :class:`AX_ENGINE_NPU_MODE_T <axcl.npu.axcl_npu_type.AX_ENGINE_NPU_MODE_T>`,
            "reserved": [int]
        }
    """
    _fields_ = [
        ("eHardMode", AX_ENGINE_NPU_MODE_T),  # NPU mode
        ("reserve", c_uint32 * 8)  # Reserved
    ]
    field_aliases = {
        "eHardMode": "hard_mode",
        "reserve": "reserved"
    }


class AX_ENGINE_IOMETA_EX_T(BaseStructure):
    """
    Extended IO metadata structure.

    .. parsed-literal::

        dict_io_meta_ex = {
            "color_space": :class:`AX_ENGINE_COLOR_SPACE_T <axcl.npu.axcl_npu_type.AX_ENGINE_COLOR_SPACE_T>`,
            "reserved": [int]
        }
    """
    _fields_ = [
        ("eColorSpace", AX_ENGINE_COLOR_SPACE_T),  # Color space
        ("u64Reserved", c_uint64 * 18)  # Reserved
    ]
    field_aliases = {
        "eColorSpace": "color_space",
        "u64Reserved": "reserved"
    }


class AX_ENGINE_IOMETA_T(BaseStructure):
    """
    IO metadata structure.

    .. parsed-literal::

        dict_io_meta = {
            "name": str,
            "shape": [int],
            "shape_size": int,
            "layout": :class:`AX_ENGINE_TENSOR_LAYOUT_T <axcl.npu.axcl_npu_type.AX_ENGINE_TENSOR_LAYOUT_T>`,
            "memory_type": :class:`AX_ENGINE_MEMORY_TYPE_T <axcl.npu.axcl_npu_type.AX_ENGINE_MEMORY_TYPE_T>`,
            "data_type": :class:`AX_ENGINE_DATA_TYPE_T <axcl.npu.axcl_npu_type.AX_ENGINE_DATA_TYPE_T>`,
            "extra_meta": :class:`AX_ENGINE_IOMETA_EX_T <axcl.npu.axcl_npu_type.AX_ENGINE_IOMETA_EX_T>`,
            "size": int,
            "quantization_value": int,
            "stride": [int],
            "reserved": [int]
        }
    """
    _fields_ = [
        ("pName", c_char_p),  # Tensor name
        ("pShape", POINTER(c_int32)),  # Shape (pointer to int array)
        ("nShapeSize", c_uint8),  # Number of dimensions
        ("eLayout", AX_ENGINE_TENSOR_LAYOUT_T),  # Tensor layout
        ("eMemoryType", AX_ENGINE_MEMORY_TYPE_T),  # Memory type
        ("eDataType", AX_ENGINE_DATA_TYPE_T),  # Data type
        ("pExtraMeta", POINTER(AX_ENGINE_IOMETA_EX_T)),  # Extra metadata
        ("nSize", c_uint32),  # Total size
        ("nQuantizationValue", c_uint32),  # Quantization value
        ("pStride", POINTER(c_int32)),  # Stride (pointer to int array)
        ("u64Reserved", c_uint64 * 9)  # Reserved
    ]
    field_aliases = {
        "pName": "name",
        "pShape": "shape",
        "nShapeSize": "shape_size",
        "eLayout": "layout",
        "eMemoryType": "memory_type",
        "eDataType": "data_type",
        "pExtraMeta": "extra_meta",
        "nSize": "size",
        "nQuantizationValue": "quantization_value",
        "pStride": "stride",
        "u64Reserved": "reserved"
    }


class AX_ENGINE_IO_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_engine_io_info = {
            "inputs": :class:`AX_ENGINE_IOMETA_T <axcl.npu.axcl_npu_type.AX_ENGINE_IOMETA_T>`,
            "input_size": int,
            "outputs": :class:`AX_ENGINE_IOMETA_T <axcl.npu.axcl_npu_type.AX_ENGINE_IOMETA_T>`,
            "output_size": int,
            "max_batch_size": int,
            "dynamic_batch_size": int,
            "reserved": [int]
        }
    """
    _fields_ = [
        ("pInputs", POINTER(AX_ENGINE_IOMETA_T)),  # Pointer to inputs
        ("nInputSize", c_uint32),  # Number of inputs
        ("pOutputs", POINTER(AX_ENGINE_IOMETA_T)),  # Pointer to outputs
        ("nOutputSize", c_uint32),  # Number of outputs
        ("nMaxBatchSize", c_uint32),  # Max batch size (0 for unlimited)
        ("bDynamicBatchSize", c_int32),  # Dynamic batch size support
        ("u64Reserved", c_uint64 * 11)  # Reserved
    ]
    field_aliases = {
        "pInputs": "inputs",
        "nInputSize": "input_size",
        "pOutputs": "outputs",
        "nOutputSize": "output_size",
        "nMaxBatchSize": "max_batch_size",
        "bDynamicBatchSize": "dynamic_batch_size",
        "u64Reserved": "reserved"
    }


class AX_ENGINE_IO_BUFFER_T(BaseStructure):
    """
    .. parsed-literal::

        dict_engine_io_buffer = {
            "physical_address": int,
            "virtual_address": pointer,
            "size": int,
            "stride": [int],
            "stride_size": int,
            "reserved": [int]
        }
    """
    _fields_ = [
        ("phyAddr", c_uint64),  # Physical address
        ("pVirAddr", c_void_p),  # Virtual address
        ("nSize", c_uint32),  # Total memory size
        ("pStride", POINTER(c_int32)),  # Pointer to stride array
        ("nStrideSize", c_uint8),  # Number of strides
        ("u64Reserved", c_uint64 * 11)  # Reserved
    ]
    field_aliases = {
        "phyAddr": "physical_address",
        "pVirAddr": "virtual_address",
        "nSize": "size",
        "pStride": "stride",
        "nStrideSize": "stride_size",
        "u64Reserved": "reserved"
    }


class AX_ENGINE_IO_SETTING_T(BaseStructure):
    """
    .. parsed-literal::

        dict_engine_io_setting = {
            "wbt_index": int,
            "reserved": [int]
        }
    """
    _fields_ = [
        ("nWbtIndex", c_uint32),  # WB index
        ("u64Reserved", c_uint64 * 7)  # Reserved
    ]
    field_aliases = {
        "nWbtIndex": "wbt_index",
        "u64Reserved": "reserved"
    }


class AX_ENGINE_IO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_engine_io = {
            "inputs": :class:`AX_ENGINE_IO_BUFFER_T <axcl.npu.axcl_npu_type.AX_ENGINE_IO_BUFFER_T>`,
            "input_size": int,
            "outputs": :class:`AX_ENGINE_IO_BUFFER_T <axcl.npu.axcl_npu_type.AX_ENGINE_IO_BUFFER_T>`,
            "output_size": int,
            "batch_size": int,
            "io_setting": :class:`AX_ENGINE_IO_SETTING_T <axcl.npu.axcl_npu_type.AX_ENGINE_IO_SETTING_T>`,
            "parallel_run": int,
            "reserved": [int]
        }
    """
    _fields_ = [
        ("pInputs", POINTER(AX_ENGINE_IO_BUFFER_T)),  # Pointer to input buffers
        ("nInputSize", c_uint32),  # Number of inputs
        ("pOutputs", POINTER(AX_ENGINE_IO_BUFFER_T)),  # Pointer to output buffers
        ("nOutputSize", c_uint32),  # Number of outputs
        ("nBatchSize", c_uint32),  # Batch size
        ("pIoSetting", POINTER(AX_ENGINE_IO_SETTING_T)),  # IO settings
        ("nParallelRun", c_uint32),  # Parallel run flag
        ("u64Reserved", c_uint64 * 10)  # Reserved
    ]
    field_aliases = {
        "pInputs": "inputs",
        "nInputSize": "input_size",
        "pOutputs": "outputs",
        "nOutputSize": "output_size",
        "nBatchSize": "batch_size",
        "pIoSetting": "io_setting",
        "nParallelRun": "parallel_run",
        "u64Reserved": "reserved"
    }


class AX_ENGINE_HANDLE_EXTRA_T(BaseStructure):
    """
    .. parsed-literal::

        dict_engine_handle_extra = {
            "npu_set": int,
            "name": str,
            "reserved": [int]
        }
    """
    _fields_ = [
        ("nNpuSet", AX_ENGINE_NPU_SET_T),  # NPU set
        ("pName", c_char_p),  # Name
        ("reserve", c_uint32 * 8)  # Reserved
    ]
    field_aliases = {
        "nNpuSet": "npu_set",
        "pName": "name",
        "reserve": "reserved"
    }


class AX_ENGINE_CMM_INFO(BaseStructure):
    """
    .. parsed-literal::

        dict_engine_cmm_info = {
            "cmm_size": int,
        }
    """
    _fields_ = [
        ("nCMMSize", c_uint32),  # Size of CMM
    ]
    field_aliases = {
        "nCMMSize": "cmm_size"
    }
