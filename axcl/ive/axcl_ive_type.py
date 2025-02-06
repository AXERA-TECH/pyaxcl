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

from ctypes import c_char, c_int8, c_uint8, c_int16, c_uint16, c_int32, c_uint32, c_int64, c_uint64, c_char_p, c_void_p, POINTER, byref, cast

from axcl.ax_global_type import *
from axcl.ax_base_type import *
from axcl.utils.axcl_basestructure import *

# u8bit
AX_U1Q7 = c_uint8
AX_U4Q4 = c_uint8

# u16bit
AX_U1Q10 = c_uint16
AX_U1Q15 = c_uint16

# u32bit
AX_U0Q20 = AX_U32
AX_U14Q4 = AX_U32

# s16bit
AX_S1Q7 = c_int16
AX_S1Q14 = c_int16

# s32bit
AX_S6Q10 = AX_S32

# IVE handle
AX_IVE_HANDLE = AX_S32

AX_IVE_MAX_REGION_NUM = 2048

AX_IVE_HIST_NUM = 256

# Type of the AX_IVE_IMAGE_T
AX_IVE_IMAGE_TYPE_E = AX_S32
"""
    ive image type

    .. parsed-literal::

        AX_IVE_IMAGE_TYPE_U8C1         = 0x0
        AX_IVE_IMAGE_TYPE_S8C1         = 0x1
        AX_IVE_IMAGE_TYPE_YUV420SP     = 0x2     # YUV420 SemiPlanar
        AX_IVE_IMAGE_TYPE_YUV422SP     = 0x3     # YUV422 SemiPlanar
        AX_IVE_IMAGE_TYPE_YUV420P      = 0x4     # YUV420 Planar
        AX_IVE_IMAGE_TYPE_YUV422P      = 0x5     # YUV422 planar
        AX_IVE_IMAGE_TYPE_S8C2_PACKAGE = 0x6
        AX_IVE_IMAGE_TYPE_S8C2_PLANAR  = 0x7
        AX_IVE_IMAGE_TYPE_S16C1        = 0x8
        AX_IVE_IMAGE_TYPE_U16C1        = 0x9
        AX_IVE_IMAGE_TYPE_U8C3_PACKAGE = 0xa
        AX_IVE_IMAGE_TYPE_U8C3_PLANAR  = 0xb
        AX_IVE_IMAGE_TYPE_S32C1        = 0xc
        AX_IVE_IMAGE_TYPE_U32C1        = 0xd
        AX_IVE_IMAGE_TYPE_S64C1        = 0xe
        AX_IVE_IMAGE_TYPE_U64C1        = 0xf
        AX_IVE_IMAGE_TYPE_BUTT         = 0x10
"""
AX_IVE_IMAGE_TYPE_U8C1         = 0x0
AX_IVE_IMAGE_TYPE_S8C1         = 0x1
AX_IVE_IMAGE_TYPE_YUV420SP     = 0x2             # YUV420 SemiPlanar
AX_IVE_IMAGE_TYPE_YUV422SP     = 0x3             # YUV422 SemiPlanar
AX_IVE_IMAGE_TYPE_YUV420P      = 0x4             # YUV420 Planar
AX_IVE_IMAGE_TYPE_YUV422P      = 0x5             # YUV422 planar
AX_IVE_IMAGE_TYPE_S8C2_PACKAGE = 0x6
AX_IVE_IMAGE_TYPE_S8C2_PLANAR  = 0x7
AX_IVE_IMAGE_TYPE_S16C1        = 0x8
AX_IVE_IMAGE_TYPE_U16C1        = 0x9
AX_IVE_IMAGE_TYPE_U8C3_PACKAGE = 0xa
AX_IVE_IMAGE_TYPE_U8C3_PLANAR  = 0xb
AX_IVE_IMAGE_TYPE_S32C1        = 0xc
AX_IVE_IMAGE_TYPE_U32C1        = 0xd
AX_IVE_IMAGE_TYPE_S64C1        = 0xe
AX_IVE_IMAGE_TYPE_U64C1        = 0xf
AX_IVE_IMAGE_TYPE_BUTT         = 0x10

# Definition of the AX_IVE_IMAGE_T
class ImageTypeUnion(BaseUnion):
    """
    .. parsed-literal::

        dict_imagetypeunion = {
            "type": :class:`AX_IVE_IMAGE_TYPE_E <axcl.ive.axcl_ive_type.AX_IVE_IMAGE_TYPE_E>`,
            "glb_type": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`
        }
    """
    _fields_ = [
        ("enType", AX_IVE_IMAGE_TYPE_E),         # RW;The type of the image
        ("enGlbType", AX_IMG_FORMAT_E)           # RW;The type of the global image
    ]
    field_aliases = {
        "enType": "type",
        "enGlbType": "glb_type"
    }

class AX_IVE_IMAGE_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_image = {
            "phy_addr": [int],
            "vir_addr": [int],
            "stride": [int],
            "width": int,
            "height": int,
            "image_type": :class:`ImageTypeUnion <axcl.ive.axcl_ive_type.ImageTypeUnion>`
        }
    """
    _fields_ = [
        ("au64PhyAddr", AX_U64 * 3),             # RW;The physical address of the image
        ("au64VirAddr", AX_U64 * 3),             # RW;The virtual address of the image
        ("au32Stride", AX_U32 * 3),              # RW;The stride of the image
        ("u32Width", AX_U32),                    # RW;The width of the image
        ("u32Height", AX_U32),                   # RW;The height of the image
        ("uImageType", ImageTypeUnion)           # image type
    ]
    field_aliases = {
        "au64PhyAddr": "phy_addr",
        "au64VirAddr": "vir_addr",
        "au32Stride": "stride",
        "u32Width": "width",
        "u32Height": "height",
        "uImageType": "image_type"
    }

AX_IVE_SRC_IMAGE_T = AX_IVE_IMAGE_T
AX_IVE_DST_IMAGE_T = AX_IVE_IMAGE_T

# Definition of the AX_IVE_MEM_INFO_T.
# This struct special purpose for input or ouput, such as Hist, CCL.
class AX_IVE_MEM_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_mem_info = {
            "phy_addr": int,
            "vir_addr": int,
            "size": int
        }
    """
    _fields_ = [
        ("u64PhyAddr", AX_U64),                  # RW;The physical address of the memory
        ("u64VirAddr", AX_U64),                  # RW;The virtual address of the memory
        ("u32Size", AX_U32)                      # RW;The size of memory
    ]
    field_aliases = {
        "u64PhyAddr": "phy_addr",
        "u64VirAddr": "vir_addr",
        "u32Size": "size"
    }

AX_IVE_SRC_MEM_INFO_T = AX_IVE_MEM_INFO_T
AX_IVE_DST_MEM_INFO_T = AX_IVE_MEM_INFO_T

# Data struct
class AX_IVE_DATA_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_data = {
            "phy_addr": int,
            "vir_addr": int,
            "stride": int,
            "width": int,
            "height": int,
            "reserved": int
        }
    """
    _fields_ = [
        ("u64PhyAddr", AX_U64),                  # RW;The physical address of the data
        ("u64VirAddr", AX_U64),                  # RW;The virtaul address of the data
        ("u32Stride", AX_U32),                   # RW;The stride of 2D data by byte
        ("u32Width", AX_U32),                    # RW;The width of 2D data by byte
        ("u32Height", AX_U32),                   # RW;The height of 2D data by byte
        ("u32Reserved", AX_U32)                  # reserved
    ]
    field_aliases = {
        "u64PhyAddr": "phy_addr",
        "u64VirAddr": "vir_addr",
        "u32Stride": "stride",
        "u32Width": "width",
        "u32Height": "height",
        "u32Reserved": "reserved"
    }

AX_IVE_SRC_DATA_T = AX_IVE_DATA_T
AX_IVE_DST_DATA_T = AX_IVE_DATA_T

# Hardware Engine
AX_IVE_ENGINE_E = AX_S32
"""
    ive engine

    .. parsed-literal::

        AX_IVE_ENGINE_IVE  = 0
        AX_IVE_ENGINE_TDP  = 1
        AX_IVE_ENGINE_VGP  = 2
        AX_IVE_ENGINE_VPP  = 3
        AX_IVE_ENGINE_GDC  = 4
        AX_IVE_ENGINE_DSP  = 5
        AX_IVE_ENGINE_NPU  = 6
        AX_IVE_ENGINE_CPU  = 7
        AX_IVE_ENGINE_MAU  = 8
        AX_IVE_ENGINE_BUTT = 9
"""
AX_IVE_ENGINE_IVE  = 0
AX_IVE_ENGINE_TDP  = 1
AX_IVE_ENGINE_VGP  = 2
AX_IVE_ENGINE_VPP  = 3
AX_IVE_ENGINE_GDC  = 4
AX_IVE_ENGINE_DSP  = 5
AX_IVE_ENGINE_NPU  = 6
AX_IVE_ENGINE_CPU  = 7
AX_IVE_ENGINE_MAU  = 8
AX_IVE_ENGINE_BUTT = 9

# Definition of s16 point
class AX_IVE_POINT_S16_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_point_s16 = {
            "x": int,
            "y": int
        }
    """
    _fields_ = [
        ("s16X", AX_S16),                        # RW;The X coordinate of the point
        ("s16Y", AX_S16)                         # RW;The Y coordinate of the point
    ]
    field_aliases = {
        "s16X": "x",
        "s16Y": "y"
    }

# Definition of rectangle
class AX_IVE_RECT_U16_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_rect_u16 = {
            "x": int,
            "y": int,
            "w": int,
            "h": int
        }
    """
    _fields_ = [
        ("u16X", AX_U16),                        # RW;The location of X axis of the rectangle
        ("u16Y", AX_U16),                        # RW;The location of Y axis of the rectangle
        ("u16Width", AX_U16),                    # RW;The width of the rectangle
        ("u16Height", AX_U16)                    # RW;The height of the rectangle
    ]
    field_aliases = {
        "u16X": "x",
        "u16Y": "y",
        "u16Width": "w",
        "u16Height": "h"
    }

# Definition of error code
AX_IVE_ERR_CODE_E = AX_S32
"""
    ive err code

    .. parsed-literal::

        AX_ERR_IVE_OPEN_FAILED   = 0x50    # IVE open device failed
        AX_ERR_IVE_INIT_FAILED   = 0x51    # IVE init failed
        AX_ERR_IVE_NOT_INIT      = 0x52    # IVE not init error
        AX_ERR_IVE_SYS_TIMEOUT   = 0x53    # IVE process timeout
        AX_ERR_IVE_QUERY_TIMEOUT = 0x54    # IVE query timeout
        AX_ERR_IVE_BUS_ERR       = 0x55    # IVE bus error
"""
AX_ERR_IVE_OPEN_FAILED   = 0x50                  # IVE open device failed
AX_ERR_IVE_INIT_FAILED   = 0x51                  # IVE init failed
AX_ERR_IVE_NOT_INIT      = 0x52                  # IVE not init error
AX_ERR_IVE_SYS_TIMEOUT   = 0x53                  # IVE process timeout
AX_ERR_IVE_QUERY_TIMEOUT = 0x54                  # IVE query timeout
AX_ERR_IVE_BUS_ERR       = 0x55                  # IVE bus error

# MAU error code
AX_IVE_MAU_ERR_CODE_E = AX_S32
"""
    ive mau err code

    .. parsed-literal::

        AX_ERR_MAU_CREATE_HANDLE_ERROR  = 0x3    # Create handle error
        AX_ERR_MAU_DESTROY_HANDLE_ERROR = 0x4    # Destroy handle error
        AX_ERR_MAU_MATMUL_ERROR         = 0x5    # Matrix multiplication operation error
        AX_ERR_MAU_DRIVER_ERROR         = 0x6    # MAU driver error
        AX_ERR_MAU_TILE_ERROR           = 0x7    # Tile error, only for NPU engine
"""
AX_ERR_MAU_CREATE_HANDLE_ERROR  = 0x3            # Create handle error
AX_ERR_MAU_DESTROY_HANDLE_ERROR = 0x4            # Destroy handle error
AX_ERR_MAU_MATMUL_ERROR         = 0x5            # Matrix multiplication operation error
AX_ERR_MAU_DRIVER_ERROR         = 0x6            # MAU driver error
AX_ERR_MAU_TILE_ERROR           = 0x7            # Tile error, only for NPU engine

AX_ID_IVE_SMOD = 0x00
AX_ID_MAU_SMOD = 0x01

# IVE error code
# Invalid device ID
AX_ERR_IVE_INVALID_DEVID      = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_INVALID_MODID)
# Invalid channel ID
AX_ERR_IVE_INVALID_CHNID      = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_INVALID_CHNID)
# At least one parameter is illegal. For example, an illegal enumeration value exists.
AX_ERR_IVE_ILLEGAL_PARAM      = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_ILLEGAL_PARAM)
# The channel exists.
AX_ERR_IVE_EXIST              = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_EXIST)
# The UN exists.
AX_ERR_IVE_UNEXIST            = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_UNEXIST)
# A null point is used.
AX_ERR_IVE_NULL_PTR           = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_NULL_PTR)
# Try to enable or initialize the system, device, or channel before configuring attributes.
AX_ERR_IVE_NOT_CONFIG         = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_NOT_CONFIG)
# The operation is not supported currently.
AX_ERR_IVE_NOT_SURPPORT       = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_NOT_SUPPORT)
# The operation, changing static attributes for example, is not permitted.
AX_ERR_IVE_NOT_PERM           = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_NOT_PERM)
# A failure caused by the malloc memory occurs.
AX_ERR_IVE_NOMEM              = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_NOMEM)
# A failure caused by the malloc buffer occurs.
AX_ERR_IVE_NOBUF              = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_NOBUF)
# The buffer is empty.
AX_ERR_IVE_BUF_EMPTY          = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_BUF_EMPTY)
# No buffer is provided for storing new data.
AX_ERR_IVE_BUF_FULL           = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_BUF_FULL)
# The system is not ready because it may be not initialized or loaded. The error code is returned when a device file fails to be opened.
AX_ERR_IVE_NOTREADY           = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_SYS_NOTREADY)
# The resource is busy during the operations such as destroying a VENC channel without deregistering it.
AX_ERR_IVE_BUSY               = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_BUSY)
# IVE open device error
AX_ERR_IVE_OPEN_FAILED        = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_IVE_OPEN_FAILED)
# IVE init error
AX_ERR_IVE_INIT_FAILED        = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_IVE_INIT_FAILED)
# IVE not init error
AX_ERR_IVE_NOT_INIT           = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_IVE_NOT_INIT)
# IVE process timeout
AX_ERR_IVE_SYS_TIMEOUT        = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_IVE_SYS_TIMEOUT)
# IVE query timeout
AX_ERR_IVE_QUERY_TIMEOUT      = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_IVE_QUERY_TIMEOUT)
# IVE Bus error
AX_ERR_IVE_BUS_ERR            = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_IVE_BUS_ERR)
# IVE unknow error
AX_ERR_IVE_UNKNOWN            = AX_DEF_ERR(AX_ID_IVE, AX_ID_IVE_SMOD, AX_ERR_UNKNOWN)
# Create handle error
AX_ERR_IVE_MAU_CREATE_HANDLE  = AX_DEF_ERR(AX_ID_IVE, AX_ID_MAU_SMOD, AX_ERR_MAU_CREATE_HANDLE_ERROR)
# Destory handle error
AX_ERR_IVE_MAU_DESTROY_HANDLE = AX_DEF_ERR(AX_ID_IVE, AX_ID_MAU_SMOD, AX_ERR_MAU_DESTROY_HANDLE_ERROR)
# Matrix multiplication operation error
AX_ERR_IVE_MAU_MATMUL         = AX_DEF_ERR(AX_ID_IVE, AX_ID_MAU_SMOD, AX_ERR_MAU_MATMUL_ERROR)
# MAU driver error
AX_ERR_IVE_MAU_DRIVER         = AX_DEF_ERR(AX_ID_IVE, AX_ID_MAU_SMOD, AX_ERR_MAU_DRIVER_ERROR)
# Tile error, only for NPU engine
AX_ERR_IVE_MAU_TILE           = AX_DEF_ERR(AX_ID_IVE, AX_ID_MAU_SMOD, AX_ERR_MAU_TILE_ERROR)

# DMA mode
AX_IVE_DMA_MODE_E = AX_S32
"""
    ive dma mode

    .. parsed-literal::

        AX_IVE_DMA_MODE_DIRECT_COPY   = 0x0    # Direct copy mode
        AX_IVE_DMA_MODE_INTERVAL_COPY = 0x1    # Interval copy mode
        AX_IVE_DMA_MODE_SET_3BYTE     = 0x2    # Set 3-byte mode
        AX_IVE_DMA_MODE_SET_8BYTE     = 0x3    # Set 8-byte mode
        AX_IVE_DMA_MODE_BUTT          = 0x4
"""
AX_IVE_DMA_MODE_DIRECT_COPY   = 0x0              # Direct copy mode
AX_IVE_DMA_MODE_INTERVAL_COPY = 0x1              # Interval copy mode
AX_IVE_DMA_MODE_SET_3BYTE     = 0x2              # Set 3-byte mode
AX_IVE_DMA_MODE_SET_8BYTE     = 0x3              # Set 8-byte mode
AX_IVE_DMA_MODE_BUTT          = 0x4

# DMA control parameter
class AX_IVE_DMA_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_dma_ctrl = {
            "mode": :class:`AX_IVE_DMA_MODE_E <axcl.ive.axcl_ive_type.AX_IVE_DMA_MODE_E>`,
            "val": int,
            "hor_seg_size": int,
            "elem_size": int,
            "ver_seg_rows": int,
            "crp_x": int,
            "crp_y": int
        }
    """
    _fields_ = [
        ("enMode", AX_IVE_DMA_MODE_E),           # Used in memset mode
        ("u64Val", AX_U64),                      # Used in interval-copy mode, every row was segmented by hor_seg_size bytes
        ("u8HorSegSize", AX_U8),                 # Used in interval-copy mode, every row was segmented by hor_seg_size bytes
        ("u8ElemSize", AX_U8),                   # Used in interval-copy mode, the valid bytes copied in front of every segment in a valid row, which 0<elem_size<hor_seg_size
        ("u8VerSegRows", AX_U8),                 # Used in interval-copy mode, copy one row in every ver_seg_rows
        ("u16CrpX0", AX_U16),                    # Used in direct-copy mode, crop start point x-coordinate
        ("u16CrpY0", AX_U16)                     # Used in direct-copy mode, crop start point y-coordinate
    ]
    field_aliases = {
        "enMode": "mode",
        "u64Val": "val",
        "u8HorSegSize": "hor_seg_size",
        "u8ElemSize": "elem_size",
        "u8VerSegRows": "ver_seg_rows",
        "u16CrpX0": "crp_x",
        "u16CrpY0": "crp_y"
    }

# Add control parameters
class AX_IVE_ADD_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_add_ctrl = {
            "x": int,
            "y": int
        }
    """
    _fields_ = [
        ("u1q7X", AX_U1Q7),                      # x of "xA+yB"
        ("u1q7Y", AX_U1Q7)                       # y of "xA+yB"
    ]
    field_aliases = {
        "u1q7X": "x",
        "u1q7Y": "y"
    }

# Type of the Sub output results
AX_IVE_SUB_MODE_E = AX_S32
"""
    ive sub mode

    .. parsed-literal::

        AX_IVE_SUB_MODE_ABS   = 0x0    # Absolute value of the difference
        AX_IVE_SUB_MODE_SHIFT = 0x1    # The output result is obtained by shifting the result one digit right to reserve the signed bit.
        AX_IVE_SUB_MODE_BUTT  = 0x2
"""
AX_IVE_SUB_MODE_ABS   = 0x0                      # Absolute value of the difference
AX_IVE_SUB_MODE_SHIFT = 0x1                      # The output result is obtained by shifting the result one digit right to reserve the signed bit.
AX_IVE_SUB_MODE_BUTT  = 0x2

# Sub control parameters
class AX_IVE_SUB_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_sub_ctrl = {
            "mode": :class:`AX_IVE_SUB_MODE_E <axcl.ive.axcl_ive_type.AX_IVE_SUB_MODE_E>`
        }
    """
    _fields_ = [
        ("enMode", AX_IVE_SUB_MODE_E)            # sub output mode
    ]
    field_aliases = {
        "enMode": "mode"
    }

# Mse control parameters
class AX_IVE_MSE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_mse_ctrl = {
            "coef": int
        }
    """
    _fields_ = [
        ("u1q15MseCoef", AX_U1Q15)               # MSE coef, range: [0,65535]
    ]
    field_aliases = {
        "u1q15MseCoef": "coef"
    }

# HysEdge control struct
class AX_IVE_HYS_EDGE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_hys_edge_ctrl = {
            "low_thr": int,
            "high_thr": int
        }
    """
    _fields_ = [
        ("u16LowThr", AX_U16),
        ("u16HighThr", AX_U16)
    ]
    field_aliases = {
        "u16LowThr": "low_thr",
        "u16HighThr": "high_thr"
    }

# CannyEdge control struct
class AX_IVE_CANNY_EDGE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_canny_edge_ctrl = {
            "thr": int
        }
    """
    _fields_ = [
        ("u8Thr", AX_U8)
    ]
    field_aliases = {
        "u8Thr": "thr"
    }

# Region struct
class AX_IVE_REGION_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_region = {
            "label_status": int,
            "area": int,
            "left": int,
            "right": int,
            "top": int,
            "bottom": int
        }
    """
    _fields_ = [
        ("u8LabelStatus", AX_U8),                # 0: Labeled failed ; 1: Labeled successfully
        ("u32Area", AX_U32),                     # Represented by the pixel number
        ("u16Left", AX_U16),                     # Circumscribed rectangle left border
        ("u16Right", AX_U16),                    # Circumscribed rectangle right border
        ("u16Top", AX_U16),                      # Circumscribed rectangle top border
        ("u16Bottom", AX_U16)                    # Circumscribed rectangle bottom border
    ]
    field_aliases = {
        "u8LabelStatus": "label_status",
        "u32Area": "area",
        "u16Left": "left",
        "u16Right": "right",
        "u16Top": "top",
        "u16Bottom": "bottom"
    }

# CCBLOB struct
class AX_IVE_CCBLOB_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_ccblob = {
            "region": [:class:`AX_IVE_REGION_T <axcl.ive.axcl_ive_type.AX_IVE_REGION_T>`]
        }
    """
    _fields_ = [
        ("u16RegionNum", AX_U16),                               # Number of valid region
        ("astRegion", AX_IVE_REGION_T * AX_IVE_MAX_REGION_NUM)  # Valid regions with 'area>0' and 'label = ArrayIndex+1'
    ]
    field_aliases = {
        "astRegion": "region"
    }

# Type of the CCL
AX_IVE_CCL_MODE_E = AX_S32
"""
    ive ccl mode

    .. parsed-literal::

        AX_IVE_CCL_MODE_4C   = 0x0    # 4-connected
        AX_IVE_CCL_MODE_8C   = 0x1    # 8-connected
        AX_IVE_CCL_MODE_BUTT = 0x2
"""
AX_IVE_CCL_MODE_4C    = 0x0                      # 4-connected
AX_IVE_CCL_MODE_8C    = 0x1                      # 8-connected
AX_IVE_CCL_MODE_BUTT  = 0x2

# CCL control struct
class AX_IVE_CCL_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_ccl_ctrl = {
            "mode": :class:`AX_IVE_CCL_MODE_E <axcl.ive.axcl_ive_type.AX_IVE_CCL_MODE_E>`
        }
    """
    _fields_ = [
        ("enMode", AX_IVE_CCL_MODE_E)            # ccl mode
    ]
    field_aliases = {
        "enMode": "mode"
    }

# Erode control parameter
class AX_IVE_ERODE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_erode_ctrl = {
            "mask": [int]
        }
    """
    _fields_ = [
        ("au8Mask", AX_U8 * 25)                  # The template parameter value must be 0 or 255.
    ]
    field_aliases = {
        "au8Mask": "mask"
    }

# Dilate control parameters
class AX_IVE_DILATE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_dilate_ctrl = {
            "mask": [int]
        }
    """
    _fields_ = [
        ("au8Mask", AX_U8 * 25)                  # The template parameter value must be 0 or 255.
    ]
    field_aliases = {
        "au8Mask": "mask"
    }

# Filter control parameters
# You need to set these parameters when using the filter operator.
class AX_IVE_FILTER_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_filter_ctrl = {
            "mask": [int]
        }
    """
    _fields_ = [
        ("as6q10Mask", AX_S6Q10 * 25)            # Template parameter filter coefficient
    ]
    field_aliases = {
        "as6q10Mask": "mask"
    }

# Equalizehist control parameters
class AX_IVE_EQUALIZE_HIST_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_equalize_hist_ctrl = {
            "coef": int
        }
    """
    _fields_ = [
        ("u0q20HistEqualCoef", AX_U0Q20)         # range: [0,1048575]
    ]
    field_aliases = {
        "u0q20HistEqualCoef": "coef"
    }

# Type of the Integ output results
AX_IVE_INTEG_OUT_CTRL_E = AX_S32
"""
    ive integ out ctrl

    .. parsed-literal::

        AX_IVE_INTEG_OUT_CTRL_COMBINE = 0x0
        AX_IVE_INTEG_OUT_CTRL_SUM     = 0x1
        AX_IVE_INTEG_OUT_CTRL_SQSUM   = 0x2
        AX_IVE_INTEG_OUT_CTRL_BUTT    = 0x3
"""
AX_IVE_INTEG_OUT_CTRL_COMBINE = 0x0
AX_IVE_INTEG_OUT_CTRL_SUM     = 0x1
AX_IVE_INTEG_OUT_CTRL_SQSUM   = 0x2
AX_IVE_INTEG_OUT_CTRL_BUTT    = 0x3

# Integ control parameters
class AX_IVE_INTEG_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_integ_ctrl = {
            "ctrl": :class:`AX_IVE_INTEG_OUT_CTRL_E <axcl.ive.axcl_ive_type.AX_IVE_INTEG_OUT_CTRL_E>`
        }
    """
    _fields_ = [
        ("enOutCtrl", AX_IVE_INTEG_OUT_CTRL_E)
    ]
    field_aliases = {
        "enOutCtrl": "ctrl"
    }

# SOBEL control parameter
class AX_IVE_SOBEL_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_sobel_ctrl = {
            "mask": [int]
        }
    """
    _fields_ = [
        ("as6q10Mask", AX_S6Q10 * 25)            # Template parameter sobel coefficient
    ]
    field_aliases = {
        "as6q10Mask": "mask"
    }

# GMM control struct
class AX_IVE_GMM_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_gmm_ctrl = {
            "init_var": int,
            "min_var": int,
            "init_weight": int,
            "learn_rate": int,
            "bg_ratio": int,
            "var_thr": int,
            "thr": int
        }
    """
    _fields_ = [
        ("u14q4InitVar", AX_U14Q4),              # Initial Variance, range: [0,262143]
        ("u14q4MinVar", AX_U14Q4),               # Min Variance, range: [0,262143]
        ("u1q10InitWeight", AX_U1Q10),           # Initial Weight, range: [0,1024]
        ("u1q7LearnRate", AX_U1Q7),              # Learning rate, range: [0,128]
        ("u1q7BgRatio", AX_U1Q7),                # Background ratio, range: [0,128]
        ("u4q4VarThr", AX_U4Q4),                 # Variance Threshold, range: [0,255]
        ("u8Thr", AX_U8)                         # Output Threshold, range: [1,255]
    ]
    field_aliases = {
        "u14q4InitVar": "init_var",
        "u14q4MinVar": "min_var",
        "u1q10InitWeight": "init_weight",
        "u1q7LearnRate": "learn_rate",
        "u1q7BgRatio": "bg_ratio",
        "u4q4VarThr": "var_thr",
        "u8Thr": "thr"
    }

# GMM2 control struct
class AX_IVE_GMM2_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_gmm2_ctrl = {
            "init_var": int,
            "min_var": int,
            "max_var": int,
            "learn_rate": int,
            "bg_ratio": int,
            "var_thr": int,
            "var_thr_check": int,
            "ct": int,
            "thr": int
        }
    """
    _fields_ = [
        ("u14q4InitVar", AX_U14Q4),              # Initial Variance, range: [0,262143]
        ("u14q4MinVar", AX_U14Q4),               # Min Variance, range: [0,262143]
        ("u14q4MaxVar", AX_U14Q4),               # Max Variance, range: [0,262143]
        ("u1q7LearnRate", AX_U1Q7),              # Learning rate, range: [0,128]
        ("u1q7BgRatio", AX_U1Q7),                # Background ratio, range: [0,128]
        ("u4q4VarThr", AX_U4Q4),                 # Variance Threshold, range: [0,255]
        ("u4q4VarThrCheck", AX_U4Q4),            # Variance Threshold Check, range: [0,255]
        ("s1q7CT", AX_S1Q7),                     # range: [-255,255]
        ("u8Thr", AX_U8)                         # Output Threshold, range: [1,255]
    ]
    field_aliases = {
        "u14q4InitVar": "init_var",
        "u14q4MinVar": "min_var",
        "u14q4MaxVar": "max_var",
        "u1q7LearnRate": "learn_rate",
        "u1q7BgRatio": "bg_ratio",
        "u4q4VarThr": "var_thr",
        "u4q4VarThrCheck": "var_thr_check",
        "s1q7CT": "ct",
        "u8Thr": "thr"
    }

# Type of the Integ output results
AX_IVE_THRESH_MODE_E = AX_S32
"""
    ive thresh mode

    .. parsed-literal::

        AX_IVE_THRESH_MODE_BINARY      = 0x0    # srcVal <= lowThr, dstVal = minVal; srcVal > lowThr, dstVal = maxVal.
        AX_IVE_THRESH_MODE_TRUNC       = 0x1    # srcVal <= lowThr, dstVal = srcVal; srcVal > lowThr, dstVal = maxVal.
        AX_IVE_THRESH_MODE_TO_MINVAL   = 0x2    # srcVal <= lowThr, dstVal = minVal; srcVal > lowThr, dstVal = srcVal.
        AX_IVE_THRESH_MODE_MIN_MID_MAX = 0x3    # srcVal <= lowThr, dstVal = minVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = maxVal.
        AX_IVE_THRESH_MODE_ORI_MID_MAX = 0x4    # srcVal <= lowThr, dstVal = srcVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = maxVal.
        AX_IVE_THRESH_MODE_MIN_MID_ORI = 0x5    # srcVal <= lowThr, dstVal = minVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = srcVal.
        AX_IVE_THRESH_MODE_MIN_ORI_MAX = 0x6    # srcVal <= lowThr, dstVal = minVal; lowThr < srcVal <= highThr, dstVal = srcVal; srcVal > highThr, dstVal = maxVal.
        AX_IVE_THRESH_MODE_ORI_MID_ORI = 0x7    # srcVal <= lowThr, dstVal = srcVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = srcVal.
        AX_IVE_THRESH_MODE_BUTT        = 0x8
"""
AX_IVE_THRESH_MODE_BINARY      = 0x0             # srcVal <= lowThr, dstVal = minVal; srcVal > lowThr, dstVal = maxVal.
AX_IVE_THRESH_MODE_TRUNC       = 0x1             # srcVal <= lowThr, dstVal = srcVal; srcVal > lowThr, dstVal = maxVal.
AX_IVE_THRESH_MODE_TO_MINVAL   = 0x2             # srcVal <= lowThr, dstVal = minVal; srcVal > lowThr, dstVal = srcVal.
AX_IVE_THRESH_MODE_MIN_MID_MAX = 0x3             # srcVal <= lowThr, dstVal = minVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = maxVal.
AX_IVE_THRESH_MODE_ORI_MID_MAX = 0x4             # srcVal <= lowThr, dstVal = srcVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = maxVal.
AX_IVE_THRESH_MODE_MIN_MID_ORI = 0x5             # srcVal <= lowThr, dstVal = minVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = srcVal.
AX_IVE_THRESH_MODE_MIN_ORI_MAX = 0x6             # srcVal <= lowThr, dstVal = minVal; lowThr < srcVal <= highThr, dstVal = srcVal; srcVal > highThr, dstVal = maxVal.
AX_IVE_THRESH_MODE_ORI_MID_ORI = 0x7             # srcVal <= lowThr, dstVal = srcVal; lowThr < srcVal <= highThr, dstVal = midVal; srcVal > highThr, dstVal = srcVal.
AX_IVE_THRESH_MODE_BUTT        = 0x8

# Thresh control parameters.
class AX_IVE_THRESH_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivehresh_ctrl = {
            "mode": :class:`AX_IVE_THRESH_MODE_E <axcl.ive.axcl_ive_type.AX_IVE_THRESH_MODE_E>`,
            "low_thr": int,
            "high_thr": int,
            "min_val": int,
            "mid_val": int,
            "max_val": int
        }
    """
    _fields_ = [
        ("enMode", AX_IVE_THRESH_MODE_E),
        ("u8LowThr", AX_U8),                     # user-defined threshold,  0<=low_thr<=255
        ("u8HighThr", AX_U8),                    # user-defined threshold, if mode<AX_IVE_THRESH_MODE_MIN_MID_MAX, high_thr is not used, else 0<=low_thr<=high_thr<=255;
        ("u8MinVal", AX_U8),                     # Minimum value when tri-level thresholding
        ("u8MidVal", AX_U8),                     # Middle value when tri-level thresholding, if mode<2, u32MidVal is not used;
        ("u8MaxVal", AX_U8)                      # Maxmum value when tri-level thresholding
    ]
    field_aliases = {
        "enMode": "mode",
        "u8LowThr": "low_thr",
        "u8HighThr": "high_thr",
        "u8MinVal": "min_val",
        "u8MidVal": "mid_val",
        "u8MaxVal": "max_val"
    }

# Mode of 16BitTo8Bit
AX_IVE_16BIT_TO_8BIT_MODE_E = AX_S32
"""
    ive 16bit to 8bit mode

    .. parsed-literal::

        AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_S8      = 0x0
        AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_U8_ABS  = 0x1
        AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_U8_BIAS = 0x2
        AX_IVE_16BIT_TO_8BIT_MODE_U16_TO_U8      = 0x3
        AX_IVE_16BIT_TO_8BIT_MODE_BUTT           = 0x4
"""
AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_S8      = 0x0
AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_U8_ABS  = 0x1
AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_U8_BIAS = 0x2
AX_IVE_16BIT_TO_8BIT_MODE_U16_TO_U8      = 0x3
AX_IVE_16BIT_TO_8BIT_MODE_BUTT           = 0x4

# 16BitTo8Bit control parameters
class AX_IVE_16BIT_TO_8BIT_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_16bito_8bit_ctrl = {
            "mode": :class:`AX_IVE_16BIT_TO_8BIT_MODE_E <axcl.ive.axcl_ive_type.AX_IVE_16BIT_TO_8BIT_MODE_E>`,
            "gain": int,
            "bias": int
        }
    """
    _fields_ = [
        ("enMode", AX_IVE_16BIT_TO_8BIT_MODE_E),
        ("s1q14Gain", AX_S1Q14),                 # range: [-16383,16383]
        ("s16Bias", AX_S16)                      # range: [-16384,16383]
    ]
    field_aliases = {
        "enMode": "mode",
        "s1q14Gain": "gain",
        "s16Bias": "bias"
    }

# Crop image control parameter
class AX_IVE_CROP_IMAGE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_crop_image_ctrl = {
            "num": int
        }
    """
    _fields_ = [
        ("u16Num", AX_U16)
    ]
    field_aliases = {
        "u16Num": "num"
    }

# Aspect ratio align mode
AX_IVE_ASPECT_RATIO_ALIGN_MODE_E = AX_S32
"""
    ive aspect ratio align mode

    .. parsed-literal::

        AX_IVE_ASPECT_RATIO_FORCE_RESIZE      = 0                                        # Without keeping aspect ratio, others keep aspect ratio.
        AX_IVE_ASPECT_RATIO_HORIZONTAL_LEFT   = 1                                        # Border on the right of the image.
        AX_IVE_ASPECT_RATIO_HORIZONTAL_CENTER = 2                                        # Border on both sides of the image.
        AX_IVE_ASPECT_RATIO_HORIZONTAL_RIGHT  = 3                                        # Border on the left of the image.
        AX_IVE_ASPECT_RATIO_VERTICAL_TOP      = AX_IVE_ASPECT_RATIO_HORIZONTAL_LEFT      # Border on the bottom of the image.
        AX_IVE_ASPECT_RATIO_VERTICAL_CENTER   = AX_IVE_ASPECT_RATIO_HORIZONTAL_CENTER    # Border on both sides of the image.
        AX_IVE_ASPECT_RATIO_VERTICAL_BOTTOM   = AX_IVE_ASPECT_RATIO_HORIZONTAL_RIGHT     # Border on the top of the image.
        AX_IVE_ASPECT_RATIO_BUTT              = 4
"""
AX_IVE_ASPECT_RATIO_FORCE_RESIZE      = 0        # Without keeping aspect ratio, others keep aspect ratio.
AX_IVE_ASPECT_RATIO_HORIZONTAL_LEFT   = 1        # Border on the right of the image.
AX_IVE_ASPECT_RATIO_HORIZONTAL_CENTER = 2        # Border on both sides of the image.
AX_IVE_ASPECT_RATIO_HORIZONTAL_RIGHT  = 3        # Border on the left of the image.
AX_IVE_ASPECT_RATIO_VERTICAL_TOP      = AX_IVE_ASPECT_RATIO_HORIZONTAL_LEFT    # Border on the bottom of the image.
AX_IVE_ASPECT_RATIO_VERTICAL_CENTER   = AX_IVE_ASPECT_RATIO_HORIZONTAL_CENTER  # Border on both sides of the image.
AX_IVE_ASPECT_RATIO_VERTICAL_BOTTOM   = AX_IVE_ASPECT_RATIO_HORIZONTAL_RIGHT   # Border on the top of the image.
AX_IVE_ASPECT_RATIO_BUTT              = 4

# CropResize control parameter
class AX_IVE_CROP_RESIZE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_crop_resize_ctrl = {
            "num": int,
            "align": [:class:`AX_IVE_ASPECT_RATIO_ALIGN_MODE_E <axcl.ive.axcl_ive_type.AX_IVE_ASPECT_RATIO_ALIGN_MODE_E>`],
            "border_color": int
        }
    """
    _fields_ = [
        ("u16Num", AX_U16),
        ("enAlign", AX_IVE_ASPECT_RATIO_ALIGN_MODE_E * 2),
        ("u32BorderColor", AX_U32)
    ]
    field_aliases = {
        "u16Num": "num",
        "enAlign": "align",
        "u32BorderColor": "border_color"
    }

# MAU and NPU data BaseStructure
# MatMul handle
AX_IVE_MATMUL_HANDLE = c_void_p

# MAU engine id
AX_IVE_MAU_ID_E = AX_S32
"""
    ive mau id

    .. parsed-literal::

        AX_IVE_MAU_ID_0    = 0
        AX_IVE_MAU_ID_BUTT = 1
"""
AX_IVE_MAU_ID_0    = 0
AX_IVE_MAU_ID_BUTT = 1

# MAU order
AX_IVE_MAU_ORDER_E = AX_S32
"""
    ive mau order

    .. parsed-literal::

        AX_IVE_MAU_ORDER_ASCEND  = 0
        AX_IVE_MAU_ORDER_DESCEND = 1
        AX_IVE_MAU_ORDER_BUTT    = 2
"""
AX_IVE_MAU_ORDER_ASCEND  = 0
AX_IVE_MAU_ORDER_DESCEND = 1
AX_IVE_MAU_ORDER_BUTT    = 2

# Data type for matrix manipulation
AX_IVE_MAU_DATA_TYPE_E = AX_S32
"""
    ive mau data type

    .. parsed-literal::

        AX_IVE_MAU_DT_UNKNOWN  = 0
        AX_IVE_MAU_DT_UINT8    = 1
        AX_IVE_MAU_DT_UINT16   = 2
        AX_IVE_MAU_DT_FLOAT32  = 3
        AX_IVE_MAU_DT_SINT16   = 4
        AX_IVE_MAU_DT_SINT8    = 5
        AX_IVE_MAU_DT_SINT32   = 6
        AX_IVE_MAU_DT_UINT32   = 7
        AX_IVE_MAU_DT_FLOAT64  = 8
        AX_IVE_MAU_DT_FLOAT16  = 9
        AX_IVE_MAU_DT_UINT64   = 10
        AX_IVE_MAU_DT_SINT64   = 11
        AX_IVE_MAU_DT_BFLOAT16 = 12
        AX_IVE_MAU_DT_BUTT     = 13
"""
AX_IVE_MAU_DT_UNKNOWN  = 0
AX_IVE_MAU_DT_UINT8    = 1
AX_IVE_MAU_DT_UINT16   = 2
AX_IVE_MAU_DT_FLOAT32  = 3
AX_IVE_MAU_DT_SINT16   = 4
AX_IVE_MAU_DT_SINT8    = 5
AX_IVE_MAU_DT_SINT32   = 6
AX_IVE_MAU_DT_UINT32   = 7
AX_IVE_MAU_DT_FLOAT64  = 8
AX_IVE_MAU_DT_FLOAT16  = 9
AX_IVE_MAU_DT_UINT64   = 10
AX_IVE_MAU_DT_SINT64   = 11
AX_IVE_MAU_DT_BFLOAT16 = 12
AX_IVE_MAU_DT_BUTT     = 13

# MatMul control parameter for NPU engine
class AX_IVE_NPU_MATMUL_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_npu_matmul_ctrl = {
            "pch_mode_dir": int,
            "type": :class:`AX_IVE_MAU_DATA_TYPE_E <axcl.ive.axcl_ive_type.AX_IVE_MAU_DATA_TYPE_E>`,
            "ksize": int
        }
    """
    _fields_ = [
        ("pchModelDir", POINTER(AX_CHAR)),
        ("enDataType", AX_IVE_MAU_DATA_TYPE_E),
        ("s32KSize", AX_S32)
    ]
    field_aliases = {
        "pchModelDir": "pch_mode_dir",
        "enDataType": "type",
        "s32KSize": "ksize"
    }

# MatMul control parameter for MAU engine
class AX_IVE_MAU_MATMUL_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_mau_matmul_ctrl = {
            "id": :class:`AX_IVE_MAU_ID_E <axcl.ive.axcl_ive_type.AX_IVE_MAU_ID_E>`,
            "ddr_read_bandwidth_limit": int,
            "is_enable_mul_res": bool,
            "is_enable_top_n_res": bool,
            "order": :class:`AX_IVE_MAU_ORDER_E <axcl.ive.axcl_ive_type.AX_IVE_MAU_ORDER_E>`,
            "top_n": int
        }
    """
    _fields_ = [
        ("enMauId", AX_IVE_MAU_ID_E),
        ("s32DdrReadBandwidthLimit", AX_S32),
        ("bEnableMulRes", AX_BOOL),
        ("bEnableTopNRes", AX_BOOL),
        ("enOrder", AX_IVE_MAU_ORDER_E),
        ("s32TopN", AX_S32)
    ]
    field_aliases = {
        "enMauId": "id",
        "s32DdrReadBandwidthLimit": "ddr_read_bandwidth_limit",
        "bEnableMulRes": "is_enable_mul_res",
        "bEnableTopNRes": "is_enable_top_n_res",
        "enOrder": "order",
        "s32TopN": "top_n"
    }

# Blob data(tensor) for matrix manipulation
class AX_IVE_MAU_BLOB_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_mau_blob = {
            "phy_addr": int,
            "vir_addr": int,
            "shape": int,
            "type": :class:`AX_IVE_MAU_DATA_TYPE_E <axcl.ive.axcl_ive_type.AX_IVE_MAU_DATA_TYPE_E>`
        }
    """
    _fields_ = [
        ("u64PhyAddr", AX_U64),
        ("pVirAddr", c_void_p),
        ("pShape", POINTER(AX_S32)),
        ("u8ShapeSize", AX_U8),
        ("enDataType", AX_IVE_MAU_DATA_TYPE_E)
    ]
    field_aliases = {
        "u64PhyAddr": "phy_addr",
        "pVirAddr": "vir_addr",
        "pShape": "shape",
        "enDataType": "type"
    }

# Input data for MatMul
class AX_IVE_MAU_MATMUL_INPUT_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_mau_matmul_input = {
            "mat_q": :class:`AX_IVE_MAU_BLOB_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_BLOB_T>`,
            "mat_b": :class:`AX_IVE_MAU_BLOB_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_BLOB_T>`
        }
    """
    _fields_ = [
        ("stMatQ", AX_IVE_MAU_BLOB_T),
        ("stMatB", AX_IVE_MAU_BLOB_T)
    ]
    field_aliases = {
        "stMatQ": "mat_q",
        "stMatB": "mat_b"
    }

# Output data for MatMul
class AX_IVE_MAU_MATMUL_OUTPUT_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ive_mau_matmul_output = {
            "mul_res": :class:`AX_IVE_MAU_BLOB_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_BLOB_T>`,
            "top_n_res": :class:`AX_IVE_MAU_BLOB_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_BLOB_T>`
        }
    """
    _fields_ = [
        ("stMulRes", AX_IVE_MAU_BLOB_T),
        ("stTopNRes", AX_IVE_MAU_BLOB_T)         # NPU engine no need
    ]
    field_aliases = {
        "stMulRes": "mul_res",
        "stTopNRes": "top_n_res"
    }
