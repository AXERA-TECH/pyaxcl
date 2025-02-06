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
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.ax_global_type import *
from axcl.sys.axcl_sys_type import *
from axcl.utils.axcl_basestructure import *

IVPS_SUCC = 0x00

AX_SUB_ID_IVPS = 0x01
AX_SUB_ID_RGN = 0x02
AX_SUB_ID_GDC = 0x03

# Error code definitions
def AX_ERROR_IVPS(e):
    return (0x80000000 | AX_SUB_ID_IVPS | e)

def AX_ERROR_RGN(e):
    return (0x80000000 | AX_SUB_ID_RGN | e)

def AX_ERROR_GDC(e):
    return (0x80000000 | AX_SUB_ID_GDC | e)

# IVPS ERROR CODE
AX_ERR_IVPS_INVALID_MODID = AX_ERROR_IVPS(0x01)  # Invalid module ID
AX_ERR_IVPS_INVALID_DEVID = AX_ERROR_IVPS(0x02)  # Invalid device ID
AX_ERR_IVPS_INVALID_CHNID = AX_ERROR_IVPS(0x03)  # Invalid channel ID
AX_ERR_IVPS_ILLEGAL_PARAM = AX_ERROR_IVPS(0x04)  # Illegal parameter
AX_ERR_IVPS_NULL_PTR = AX_ERROR_IVPS(0x05)       # Null pointer error
AX_ERR_IVPS_BAD_ADDR = AX_ERROR_IVPS(0x06)       # Bad address
AX_ERR_IVPS_SYS_NOTREADY = AX_ERROR_IVPS(0x07)   # System not ready
AX_ERR_IVPS_BUSY = AX_ERROR_IVPS(0x08)           # Channel is busy
AX_ERR_IVPS_NOT_INIT = AX_ERROR_IVPS(0x09)       # Not initialized
AX_ERR_IVPS_NOT_CONFIG = AX_ERROR_IVPS(0x0A)     # Not configured
AX_ERR_IVPS_NOT_SUPPORT = AX_ERROR_IVPS(0x0B)    # Operation not supported
AX_ERR_IVPS_NOT_PERM = AX_ERROR_IVPS(0x0C)       # Operation not permitted
AX_ERR_IVPS_EXIST = AX_ERROR_IVPS(0x0D)          # Channel exists
AX_ERR_IVPS_UNEXIST = AX_ERROR_IVPS(0x0E)        # Channel does not exist
AX_ERR_IVPS_NOMEM = AX_ERROR_IVPS(0x0F)          # Memory allocation failure
AX_ERR_IVPS_NOBUF = AX_ERROR_IVPS(0x10)          # No buffer available
AX_ERR_IVPS_BUF_EMPTY = AX_ERROR_IVPS(0x11)      # Buffer is empty
AX_ERR_IVPS_BUF_FULL = AX_ERROR_IVPS(0x12)       # Buffer is full
AX_ERR_IVPS_QUEUE_EMPTY = AX_ERROR_IVPS(0x13)    # Queue is empty
AX_ERR_IVPS_QUEUE_FULL = AX_ERROR_IVPS(0x14)     # Queue is full
AX_ERR_IVPS_TIMED_OUT = AX_ERROR_IVPS(0x15)      # Wait timed out
AX_ERR_IVPS_FLOW_END = AX_ERROR_IVPS(0x16)       # Process termination
AX_ERR_IVPS_UNKNOWN = AX_ERROR_IVPS(0x17)        # Unknown error

# IVPS RGN ERROR CODE
AX_ERR_IVPS_RGN_INVALID_GRPID = AX_ERROR_RGN(0x01)   # Invalid group ID
AX_ERR_IVPS_RGN_BUSY = AX_ERROR_RGN(0x02)             # Region is busy
AX_ERR_IVPS_RGN_UNEXIST = AX_ERROR_RGN(0x03)          # Region does not exist
AX_ERR_IVPS_RGN_ILLEGAL_PARAM = AX_ERROR_RGN(0x04)    # Illegal parameter
AX_ERR_IVPS_RGN_NOBUF = AX_ERROR_RGN(0x05)            # No buffer available

AX_IVPS_MIN_IMAGE_WIDTH = 8
AX_IVPS_MAX_IMAGE_WIDTH = 8192
AX_IVPS_MIN_IMAGE_HEIGHT = 8
AX_IVPS_MAX_IMAGE_HEIGHT = 8192
AX_IVPS_MAX_GRP_NUM = 256
"""
    .. _target to ax_ivps_max_grp_num:
"""
AX_IVPS_MAX_OUTCHN_NUM = 5
"""
    .. _target to ax_ivps_max_outchn_num:
"""
AX_IVPS_MAX_FILTER_NUM_PER_OUTCHN = 2
AX_IVPS_INVALID_FRMRATE = -1
AX_IVPS_MAX_POLYGON_POINT_NUM = 10
AX_IVPS_MIN_POLYGON_POINT_NUM = 4
AX_IVPS_USER_FRAME_RATE_NUM = 70

# Typedefs
IVPS_GRP = AX_S32
IVPS_CHN = AX_S32
IVPS_FILTER = AX_S32
IVPS_RGN_GRP = AX_S32
IVPS_RGB = AX_U32

AX_IVPS_CHN_FLIP_MODE_E = AX_S32
"""
    ivps chn flip mode

    .. parsed-literal::

        AX_IVPS_CHN_FLIP_NONE       = 0
        AX_IVPS_CHN_FLIP            = 1
        AX_IVPS_CHN_MIRROR          = 2
        AX_IVPS_CHN_FLIP_AND_MIRROR = 3
        AX_IVPS_CHN_FLIP_BUTT       = 4
"""
AX_IVPS_CHN_FLIP_NONE = 0
AX_IVPS_CHN_FLIP = 1
AX_IVPS_CHN_MIRROR = 2
AX_IVPS_CHN_FLIP_AND_MIRROR = 3
AX_IVPS_CHN_FLIP_BUTT = 4

class AX_IVPS_RECT_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rect = {
            "x": int,
            "y": int,
            "width": int,
            "height": int
        }
    """
    _fields_ = [
        ("nX", AX_S16),  # X-coordinate
        ("nY", AX_S16),  # Y-coordinate
        ("nW", AX_U16),  # Width
        ("nH", AX_U16)   # Height
    ]

    field_aliases = {
        "nX": "x",
        "nY": "y",
        "nW": "width",
        "nH": "height"
    }

class AX_IVPS_POINT_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_point = {
            "x": int,
            "y": int
        }
    """
    _fields_ = [
        ("nX", AX_S16),  # X-coordinate
        ("nY", AX_S16)   # Y-coordinate
    ]
    field_aliases = {
        "nX": "x",
        "nY": "y"
    }

class AX_IVPS_POINT_NICE_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_point_nice = {
            "x": int,
            "y": int
        }
    """
    _fields_ = [
        ("fX", AX_F32),  # X-coordinate
        ("fY", AX_F32)   # Y-coordinate
    ]
    field_aliases = {
        "fX": "x",
        "fY": "y"
    }

class AX_IVPS_SIZE_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_size = {
            "width": int,
            "height": int
        }
    """
    _fields_ = [
        ("nW", AX_U16),  # Width
        ("nH", AX_U16)   # Height
    ]
    field_aliases = {
        "nW": "width",
        "nH": "height"
    }

AX_IVPS_MOSAIC_BLK_SIZE_E = AX_S32
"""
    ivps mosaic blk size

    .. parsed-literal::

        AX_IVPS_MOSAIC_BLK_SIZE_2    = 0    # Block size 2x2
        AX_IVPS_MOSAIC_BLK_SIZE_4    = 1    # Block size 4x4
        AX_IVPS_MOSAIC_BLK_SIZE_8    = 2    # Block size 8x8
        AX_IVPS_MOSAIC_BLK_SIZE_16   = 3    # Block size 16x16
        AX_IVPS_MOSAIC_BLK_SIZE_32   = 4    # Block size 32x32
        AX_IVPS_MOSAIC_BLK_SIZE_64   = 5    # Block size 64x64
        AX_IVPS_MOSAIC_BLK_SIZE_BUTT = 6
"""
AX_IVPS_MOSAIC_BLK_SIZE_2 = 0  # Block size 2x2
AX_IVPS_MOSAIC_BLK_SIZE_4 = 1  # Block size 4x4
AX_IVPS_MOSAIC_BLK_SIZE_8 = 2  # Block size 8x8
AX_IVPS_MOSAIC_BLK_SIZE_16 = 3 # Block size 16x16
AX_IVPS_MOSAIC_BLK_SIZE_32 = 4 # Block size 32x32
AX_IVPS_MOSAIC_BLK_SIZE_64 = 5 # Block size 64x64
AX_IVPS_MOSAIC_BLK_SIZE_BUTT = 6

AX_IVPS_ROTATION_E = AX_S32
"""
    ivps rotation

    .. parsed-literal::

        AX_IVPS_ROTATION_0    = 0    # No rotation
        AX_IVPS_ROTATION_90   = 1    # Rotate 90 degrees
        AX_IVPS_ROTATION_180  = 2    # Rotate 180 degrees
        AX_IVPS_ROTATION_270  = 3    # Rotate 270 degrees
        AX_IVPS_ROTATION_BUTT = 4
"""
AX_IVPS_ROTATION_0 = 0   # No rotation
AX_IVPS_ROTATION_90 = 1  # Rotate 90 degrees
AX_IVPS_ROTATION_180 = 2 # Rotate 180 degrees
AX_IVPS_ROTATION_270 = 3 # Rotate 270 degrees
AX_IVPS_ROTATION_BUTT = 4

AX_IVPS_ASPECT_RATIO_E = AX_S32
"""
    ivps aspect ratio

    .. parsed-literal::

        AX_IVPS_ASPECT_RATIO_STRETCH = 0    # Stretch to fill output size
        AX_IVPS_ASPECT_RATIO_AUTO    = 1    # Maintain aspect ratio
        AX_IVPS_ASPECT_RATIO_MANUAL  = 2    # Manual aspect ratio
        AX_IVPS_ASPECT_RATIO_BUTT    = 3
"""
AX_IVPS_ASPECT_RATIO_STRETCH = 0  # Stretch to fill output size
AX_IVPS_ASPECT_RATIO_AUTO = 1     # Maintain aspect ratio
AX_IVPS_ASPECT_RATIO_MANUAL = 2   # Manual aspect ratio
AX_IVPS_ASPECT_RATIO_BUTT = 3

AX_IVPS_ASPECT_RATIO_ALIGN_E = AX_S32
"""
    ivps aspect ratio align

    .. parsed-literal::

        AX_IVPS_ASPECT_RATIO_HORIZONTAL_CENTER = 0
        AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT   = 1
        AX_IVPS_ASPECT_RATIO_HORIZONTAL_RIGHT  = 2
        AX_IVPS_ASPECT_RATIO_VERTICAL_CENTER   = AX_IVPS_ASPECT_RATIO_HORIZONTAL_CENTER
        AX_IVPS_ASPECT_RATIO_VERTICAL_TOP      = AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT
        AX_IVPS_ASPECT_RATIO_VERTICAL_BOTTOM   = AX_IVPS_ASPECT_RATIO_HORIZONTAL_RIGHT
"""
AX_IVPS_ASPECT_RATIO_HORIZONTAL_CENTER = 0
AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT = 1
AX_IVPS_ASPECT_RATIO_HORIZONTAL_RIGHT = 2
AX_IVPS_ASPECT_RATIO_VERTICAL_CENTER = AX_IVPS_ASPECT_RATIO_HORIZONTAL_CENTER
AX_IVPS_ASPECT_RATIO_VERTICAL_TOP = AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT
AX_IVPS_ASPECT_RATIO_VERTICAL_BOTTOM = AX_IVPS_ASPECT_RATIO_HORIZONTAL_RIGHT

AX_IVPS_GDC_MAX_IMAGE_WIDTH = 8192
AX_IVPS_GDC_MAX_IMAGE_HEIGHT = 8192
AX_IVPS_GDC_MIN_IMAGE_WIDTH = 256
AX_IVPS_GDC_MIN_IMAGE_HEIGHT = 256
AX_IVPS_FISHEYE_MAX_RGN_NUM = 9
AX_IVPS_GDC_MAX_HANDLE_NUM = 32

GDC_HANDLE = AX_S32

AX_IVPS_GDC_TYPE_E = AX_S32
"""
    ivps gdc type

    .. parsed-literal::

        AX_IVPS_GDC_BYPASS   = 0    # no gdc correction for all whole frame
        AX_IVPS_GDC_FISHEYE  = 1    # gdc correction for fisheye
        AX_IVPS_GDC_MAP_USER = 2    # customize mesh table by user
        AX_IVPS_GDC_BUTT     = 3
"""
AX_IVPS_GDC_BYPASS = 0      # no gdc correction for all whole frame
AX_IVPS_GDC_FISHEYE = 1     # gdc correction for fisheye
AX_IVPS_GDC_MAP_USER = 2    # customize mesh table by user
AX_IVPS_GDC_BUTT = 3

AX_IVPS_FISHEYE_MOUNT_MODE_E = AX_S32
"""
    ivps fisheye mount mode

    .. parsed-literal::

        AX_IVPS_FISHEYE_MOUNT_MODE_DESKTOP = 0
        AX_IVPS_FISHEYE_MOUNT_MODE_CEILING = 1
        AX_IVPS_FISHEYE_MOUNT_MODE_WALL    = 2
        AX_IVPS_FISHEYE_MOUNT_MODE_BUTT    = 3
"""
AX_IVPS_FISHEYE_MOUNT_MODE_DESKTOP = 0
AX_IVPS_FISHEYE_MOUNT_MODE_CEILING = 1
AX_IVPS_FISHEYE_MOUNT_MODE_WALL = 2
AX_IVPS_FISHEYE_MOUNT_MODE_BUTT = 3

AX_IVPS_FISHEYE_VIEW_MODE_E = AX_S32
"""
    ivps fisheye view mode

    .. parsed-literal::

        AX_IVPS_FISHEYE_VIEW_MODE_PANORAMA = 0
        AX_IVPS_FISHEYE_VIEW_MODE_NORMAL   = 1
        AX_IVPS_FISHEYE_VIEW_MODE_BYPASS   = 2
        AX_IVPS_FISHEYE_VIEW_MODE_BUTT     = 3
"""
AX_IVPS_FISHEYE_VIEW_MODE_PANORAMA = 0
AX_IVPS_FISHEYE_VIEW_MODE_NORMAL = 1
AX_IVPS_FISHEYE_VIEW_MODE_BYPASS = 2
AX_IVPS_FISHEYE_VIEW_MODE_BUTT = 3

class AX_IVPS_FISHEYE_RGN_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_fisheye_rgn_attr = {
            "view_mode": :class:`AX_IVPS_FISHEYE_VIEW_MODE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_FISHEYE_VIEW_MODE_E>`,
            "in_radius": int,
            "out_radius": int,
            "pan": int,
            "tilt": int,
            "center_x": int,
            "center_y": int,
            "hor_zoom": int,
            "ver_zoom": int,
            "out_rect": :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`
        }
    """
    _fields_ = [
        ("eViewMode", AX_IVPS_FISHEYE_VIEW_MODE_E),  # RW; range: [0, 3]; gdc view mode
        ("nInRadius", AX_U16),                        # RW; range: [0, nOutRadius); inner radius of gdc correction region
        ("nOutRadius", AX_U16),                       # RW; range: [0, 0.75 * MAX(width, height) of input picture]; out radius of gdc correction region
        ("nPan", AX_U16),                             # RW; range: [0, 360]; active if bRoiXY = 0
        ("nTilt", AX_U16),                            # RW; range: [0, 360]; active if bRoiXY = 0
        ("nCenterX", AX_U16),                         # RW; range: (0, width of input picture); x-coordinate of the centre point of correction region; active if bRoiXY = 1
        ("nCenterY", AX_U16),                         # RW; range: (0, height of input picture); y-coordinate of the centre point of correction region; active if bRoiXY = 1
        ("nHorZoom", AX_U16),                         # RW; range: [1, 5265] in normal mode, otherwise [1, 4095]; horizontal zoom of correction region
        ("nVerZoom", AX_U16),                         # RW; range: [1, 4095] vertical zoom of correction region
        ("tOutRect", AX_IVPS_RECT_T)                  # RW; out image rectangle attribute
    ]
    field_aliases = {
        "eViewMode": "view_mode",
        "nInRadius": "in_radius",
        "nOutRadius": "out_radius",
        "nPan": "pan",
        "nTilt": "tilt",
        "nCenterX": "center_x",
        "nCenterY": "center_y",
        "nHorZoom": "hor_zoom",
        "nVerZoom": "ver_zoom",
        "tOutRect": "out_rect"
    }

class AX_IVPS_FISHEYE_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_fisheye_attr = {
            "enable_bg_color": bool,
            "bg_color": int,
            "hor_offset": int,
            "ver_offset": int,
            "trapezoid_coef": int,
            "fan_strength": int,
            "mount_mode": :class:`AX_IVPS_FISHEYE_MOUNT_MODE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_FISHEYE_MOUNT_MODE_E>`,
            "region_num": int,
            "enable_rgn_update": bool,
            "rgn_update_idx": int,
            "enable_roi_xy": bool,
            "fisheye_rgn_attr": [:class:`AX_IVPS_FISHEYE_RGN_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_FISHEYE_RGN_ATTR_T>`]
        }
    """
    _fields_ = [
        ("bBgColor", AX_BOOL),                        # RW; range: [0, 1]; whether use background color or not; not support now
        ("nBgColor", AX_U32),                         # RW; range: [0, 0xffffff]; background color RGB888; not support now
        ("nHorOffset", AX_S16),                       # RW; range: [-511, 511]; the horizontal offset between image center and physical center of len
        ("nVerOffset", AX_S16),                       # RW; range: [-511, 511]; the vertical offset between image center and physical center of len
        ("nTrapezoidCoef", AX_U8),                    # RW; range: [0, 32]; strength coefficient of trapezoid correction
        ("nFanStrength", AX_S16),                     # RW; range: [-760, 760]; strength coefficient of fan correction
        ("eMountMode", AX_IVPS_FISHEYE_MOUNT_MODE_E), # RW; range: [0, 2]; gdc mount mode
        ("nRgnNum", AX_U8),                           # RW; range: [1, 9]; gdc correction region number
        ("bRgnUpdate", AX_BOOL),                      # RW; range: [0, 1]; whether update only one of gdc correction regions
        ("nRgnUpdateIdx", AX_U8),                     # RW; range: [0, 8]; gdc correction region update index
        ("bRoiXY", AX_BOOL),                          # RW; range: [0, 1]; 0: Polar coordinates with nPan and nTilt; 1: Planar coordinates with nCenterX and nCenterY
        ("tFisheyeRgnAttr", AX_IVPS_FISHEYE_RGN_ATTR_T * AX_IVPS_FISHEYE_MAX_RGN_NUM)           # RW; attribution of gdc correction region
    ]
    field_aliases = {
        "bBgColor": "enable_bg_color",
        "nBgColor": "bg_color",
        "nHorOffset": "hor_offset",
        "nVerOffset": "ver_offset",
        "nTrapezoidCoef": "trapezoid_coef",
        "nFanStrength": "fan_strength",
        "eMountMode": "mount_mode",
        "nRgnNum": "region_num",
        "bRgnUpdate": "enable_rgn_update",
        "nRgnUpdateIdx": "rgn_update_idx",
        "bRoiXY": "enable_roi_xy",
        "tFisheyeRgnAttr": "fisheye_rgn_attr"
    }

class AX_IVPS_MAP_USER_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_map_user_attr = {
            "mesh_start_x": int,
            "mesh_start_y": int,
            "mesh_width": int,
            "mesh_height": int,
            "mesh_num_horizontal": int,
            "mesh_num_vertical": int,
            "user_map_pointer": int,
            "mesh_table_physical_address": int
        }
    """
    _fields_ = [
        ("nMeshStartX", AX_U16),        # RW; range: [0, output width]; x-coordinate of output picture in the mesh table
        ("nMeshStartY", AX_U16),        # RW; range: [0, output height]; y-coordinate of output picture in the mesh table
        ("nMeshWidth", AX_U16),         # RW; range: [16, 256]; 16 aligned; width of mesh block
        ("nMeshHeight", AX_U16),        # RW; range: [16, 256]; 16 aligned; height of mesh block
        ("nMeshNumH", AX_U8),           # RW; range: [33, 64]; number of mesh block in horizontal direction, only support 33
        ("nMeshNumV", AX_U8),           # RW; range: [33, 64]; number of mesh block in vertical direction, only support 33
        ("pUserMap", POINTER(AX_S32)),  # RW; X-map and Y-map are crisscross arrangement; e.g. X-map[32bit] Y-map[32bit]...
        ("nMeshTablePhyAddr", AX_U64)   # RO; this variable is used internal
    ]
    field_aliases = {
        "nMeshStartX": "mesh_start_x",
        "nMeshStartY": "mesh_start_y",
        "nMeshWidth": "mesh_width",
        "nMeshHeight": "mesh_height",
        "nMeshNumH": "mesh_num_horizontal",
        "nMeshNumV": "mesh_num_vertical",
        "pUserMap": "user_map_pointer",
        "nMeshTablePhyAddr": "mesh_table_physical_address"
    }

class UNION_GDC_ATTR(BaseUnion):
    """
    .. parsed-literal::

        dict_union_gdc_attr = {
            "fisheye_attr": :class:`AX_IVPS_FISHEYE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_FISHEYE_ATTR_T>`,
            "map_user_attr": :class:`AX_IVPS_MAP_USER_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_MAP_USER_ATTR_T>`
        }
    """
    _fields_ = [
        ("tFisheyeAttr", AX_IVPS_FISHEYE_ATTR_T),  # RW; attribution of gdc fisheye
        ("tMapUserAttr", AX_IVPS_MAP_USER_ATTR_T),  # RW; attribution of gdc user map
    ]
    field_aliases = {
        "tFisheyeAttr": "fisheye_attr",
        "tMapUserAttr": "map_user_attr"
    }
    value_union_type_mapping = {
        AX_IVPS_GDC_FISHEYE: "tFisheyeAttr",
        AX_IVPS_GDC_MAP_USER: "tMapUserAttr"
    }


class AX_IVPS_GDC_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_gdc_attr = {
            "gdc_type": :class:`AX_IVPS_GDC_TYPE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_GDC_TYPE_E>`,
            "union_gdc_attr": :class:`UNION_GDC_ATTR <axcl.ivps.axcl_ivps_type.UNION_GDC_ATTR>`,
            "src_width": int,
            "src_height": int,
            "dst_stride": int,
            "dst_width": int,
            "dst_height": int,
            "dst_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`
        }
    """
    _fields_ = [
        ("eGdcType", AX_IVPS_GDC_TYPE_E),                     # GDC type
        ("tUnionGdcAttr", UNION_GDC_ATTR),
        ("nSrcWidth", AX_U16),                                # RW; range: [2, 8192]; 2 pixels aligned; width of input picture
        ("nSrcHeight", AX_U16),                               # RW; range: [2, 8192]; 2 pixels aligned; height of input picture
        ("nDstStride", AX_U16),                               # RW; range: [128, 8192]; 128 pixels aligned; format of output picture
        ("nDstWidth", AX_U16),                                # RW; range: [2, 8192]; 2 pixels aligned; width of output picture
        ("nDstHeight", AX_U16),                               # RW; range: [2, 8192]; 2 pixels aligned; height of output picture
        ("eDstFormat", AX_IMG_FORMAT_E)                       # RW; format of output picture; only support NV12/NV21
    ]
    field_aliases = {
        "eGdcType": "gdc_type",
        "tUnionGdcAttr": "union_gdc_attr",
        "nSrcWidth": "src_width",
        "nSrcHeight": "src_height",
        "nDstStride": "dst_stride",
        "nDstWidth": "dst_width",
        "nDstHeight": "dst_height",
        "eDstFormat": "dst_format"
    }
    name_union_type_mapping = {
        "tUnionGdcAttr": "eGdcType"
    }

AX_IVPS_DEWARP_TYPE_E = AX_S32
"""
    ivps dewarp type

    .. parsed-literal::

        AX_IVPS_DEWARP_BYPASS          = 0    # only support crop, rotation, mirror, flip or scaling
        AX_IVPS_DEWARP_MAP_USER        = 1    # user defined map
        AX_IVPS_DEWARP_PERSPECTIVE     = 2    # affine or perspective transformation
        AX_IVPS_DEWARP_LDC             = 3    # lens distortion correction
        AX_IVPS_DEWARP_LDC_V2          = 4    # lens distortion correction version 2
        AX_IVPS_DEWARP_LDC_PERSPECTIVE = 5    # LDC and PERSPECTIVE are done together
        AX_IVPS_DEWARP_BUTT            = 6
"""
AX_IVPS_DEWARP_BYPASS = 0  # only support crop, rotation, mirror, flip or scaling
AX_IVPS_DEWARP_MAP_USER = 1  # user defined map
AX_IVPS_DEWARP_PERSPECTIVE = 2  # affine or perspective transformation
AX_IVPS_DEWARP_LDC = 3  # lens distortion correction
AX_IVPS_DEWARP_LDC_V2 = 4  # lens distortion correction version 2
AX_IVPS_DEWARP_LDC_PERSPECTIVE = 5  # LDC and PERSPECTIVE are done together
AX_IVPS_DEWARP_BUTT = 6

class AX_IVPS_PERSPECTIVE_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_perspective_attr = {
            "matrix": [int]
        }
    """
    _fields_ = [
        ("nMatrix", AX_S64 * 9)  # Perspective Matrix
    ]
    field_aliases = {
        "nMatrix": "matrix"
    }

class AX_IVPS_LDC_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_ldc_attr = {
            "aspect_ratio_kept": bool,
            "x_ratio": int,
            "y_ratio": int,
            "xy_ratio": int,
            "center_x_offset": int,
            "center_y_offset": int,
            "distortion_ratio": int,
            "spread_coef": int
        }
    """
    _fields_ = [
        ("bAspect", AX_BOOL),                # whether aspect ratio is keep
        ("nXRatio", AX_S16),                 # Range: [0, 100], field angle ratio of horizontal, valid when bAspect = 0.
        ("nYRatio", AX_S16),                 # Range: [0, 100], field angle ratio of vertical, valid when bAspect = 0.
        ("nXYRatio", AX_S16),                # Range: [0, 100], field angle ratio of all, valid when bAspect = 1.
        ("nCenterXOffset", AX_S16),          # Range: [-511, 511], horizontal offset of the image distortion center relative to image center.
        ("nCenterYOffset", AX_S16),          # Range: [-511, 511], vertical offset of the image distortion center relative to image center.
        ("nDistortionRatio", AX_S16),        # Range: [-10000, 10000], LDC distortion ratio.
        ("nSpreadCoef", AX_S8)               # Range: [-18, 18], LDC spread coefficient
    ]
    field_aliases = {
        "bAspect": "aspect_ratio_kept",
        "nXRatio": "x_ratio",
        "nYRatio": "y_ratio",
        "nXYRatio": "xy_ratio",
        "nCenterXOffset": "center_x_offset",
        "nCenterYOffset": "center_y_offset",
        "nDistortionRatio": "distortion_ratio",
        "nSpreadCoef": "spread_coef"
    }

class AX_IVPS_LDC_V2_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_ldc_v2_attr = {
            "x_focus": int,
            "y_focus": int,
            "x_center": int,
            "y_center": int,
            "distortion_coefs": [int]
        }
    """
    _fields_ = [
        ("nXFocus", AX_U32),                  # Focus on X-axis
        ("nYFocus", AX_U32),                  # Focus on Y-axis
        ("nXCenter", AX_U32),                 # X-axis center
        ("nYCenter", AX_U32),                 # Y-axis center
        ("nDistortionCoeff", AX_S64 * 8)      # Distortion coefficients
    ]
    field_aliases = {
        "nXFocus": "x_focus",
        "nYFocus": "y_focus",
        "nXCenter": "x_center",
        "nYCenter": "y_center",
        "nDistortionCoeff": "distortion_coefs"
    }

class UNION_DEWARP_ATTR_T(BaseUnion):
    """
    .. parsed-literal::

        dict_union_dewarp_attr = {
            "map_user_attr": :class:`AX_IVPS_MAP_USER_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_MAP_USER_ATTR_T>`,
            "ldc_attr": :class:`AX_IVPS_LDC_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_LDC_ATTR_T>`,
            "ldc_v2_attr": :class:`AX_IVPS_LDC_V2_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_LDC_V2_ATTR_T>`
        }
    """
    _fields_ = [
        ("tMapUserAttr", AX_IVPS_MAP_USER_ATTR_T),  # User map attributes
        ("tLdcAttr", AX_IVPS_LDC_ATTR_T),           # LDC attributes
        ("tLdcV2Attr", AX_IVPS_LDC_V2_ATTR_T),      # LDC V2 attributes
    ]
    field_aliases = {
        "tMapUserAttr": "map_user_attr",
        "tLdcAttr": "ldc_attr",
        "tLdcV2Attr": "ldc_v2_attr"
    }
    value_union_type_mapping = {
        AX_IVPS_DEWARP_MAP_USER: "tMapUserAttr",
        AX_IVPS_DEWARP_LDC: "tLdcAttr",
        AX_IVPS_DEWARP_LDC_V2: "tLdcV2Attr"
    }

class AX_IVPS_GDC_CFG_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_gdc_cfg = {
            "dewarp_type": :class:`AX_IVPS_DEWARP_TYPE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_DEWARP_TYPE_E>`,
            "rotation_type": :class:`AX_IVPS_ROTATION_E <axcl.ivps.axcl_ivps_type.AX_IVPS_ROTATION_E>`,
            "hardware_rotation": bool,
            "vdsp_mode": :class:`AX_VDSP_MODE_E <axcl.ax_global_type.AX_VDSP_MODE_E>`,
            "mirror_enabled": bool,
            "flip_enabled": bool,
            "dewarp_attr": :class:`UNION_DEWARP_ATTR_T <axcl.ivps.axcl_ivps_type.UNION_DEWARP_ATTR_T>`,
            "perspective_attr": :class:`AX_IVPS_PERSPECTIVE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_PERSPECTIVE_ATTR_T>`
        }
    """
    _fields_ = [
        ("eDewarpType", AX_IVPS_DEWARP_TYPE_E),  # Dewarp type
        ("eRotation", AX_IVPS_ROTATION_E),        # Rotation type
        ("bHwRotation", AX_BOOL),                  # Only for DSP hardware Rotation
        ("eVdspMode", AX_VDSP_MODE_E),            # Only for DSP's core select
        ("bMirror", AX_BOOL),                      # Enable mirror
        ("bFlip", AX_BOOL),                        # Enable flip
        ("uDewarpAttr", UNION_DEWARP_ATTR_T),
        ("tPerspectiveAttr", AX_IVPS_PERSPECTIVE_ATTR_T)  # Perspective attributes
    ]
    field_aliases = {
        "eDewarpType": "dewarp_type",
        "eRotation": "rotation_type",
        "bHwRotation": "hardware_rotation",
        "eVdspMode": "vdsp_mode",
        "bMirror": "mirror_enabled",
        "bFlip": "flip_enabled",
        "uDewarpAttr": "dewarp_attr",
        "tPerspectiveAttr": "perspective_attr"
    }
    name_union_type_mapping = {
        "uDewarpAttr": "eDewarpType"
    }

class AX_IVPS_DEWARP_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_dewarp_attr = {
            "enable_crop": bool,
            "crop_rect": :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`,
            "dst_width": int,
            "dst_height": int,
            "dst_stride": int,
            "image_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "enable_perspective": bool,
            "perspective_attr": :class:`AX_IVPS_PERSPECTIVE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_PERSPECTIVE_ATTR_T>`
        }
    """
    _fields_ = [
        ("bCrop", AX_BOOL),                      # RW; whether crop function is enabled
        ("tCropRect", AX_IVPS_RECT_T),           # RW; 2 pixels aligned; crop rectangle info
        ("nDstWidth", AX_U16),                   # RW; range: [2, 8192]; 2 pixels aligned; width of output picture
        ("nDstHeight", AX_U16),                  # RW; range: [2, 8192]; 2 pixels aligned; height of output picture
        ("nDstStride", AX_U32),                  # RW; range: [128, 8192]; 128 pixels aligned; format of output picture
        ("eImgFormat", AX_IMG_FORMAT_E),         # RW; format of output picture; only support NV12
        ("bPerspective", AX_BOOL),               # Enable perspective
        ("tPerspectiveAttr", AX_IVPS_PERSPECTIVE_ATTR_T)  # Perspective attributes
    ]
    field_aliases = {
        "bCrop": "enable_crop",
        "tCropRect": "crop_rect",
        "nDstWidth": "dst_width",
        "nDstHeight": "dst_height",
        "nDstStride": "dst_stride",
        "eImgFormat": "image_format",
        "bPerspective": "enable_perspective",
        "tPerspectiveAttr": "perspective_attr"
    }

class AX_IVPS_ALPHA_LUT_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_alpha_lut = {
            "enable_alpha": bool,
            "reverse_alpha": bool,
            "physical_address": int
        }
    """
    _fields_ = [
        ("bAlphaEnable", AX_BOOL),           # Enable alpha
        ("bAlphaReverse", AX_BOOL),          # Reverse alpha
        ("u64PhyAddr", AX_U64)               # Physical address
    ]
    field_aliases = {
        "bAlphaEnable": "enable_alpha",
        "bAlphaReverse": "reverse_alpha",
        "u64PhyAddr": "physical_address"
    }

class AX_IVPS_POOL_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_pool_attr = {
            "pool_source": :class:`AX_POOL_SOURCE_E <axcl.sys.axcl_sys_type.AX_POOL_SOURCE_E>`,
            "frame_buf_num": int,
            "pool_id": int
        }
    """
    _fields_ = [
        ("ePoolSrc", AX_POOL_SOURCE_E),      # Pool allocation method
        ("nFrmBufNum", AX_U8),               # Private pool frame buffer count
        ("PoolId", AX_POOL)                  # User pool ID
    ]
    field_aliases = {
        "ePoolSrc": "pool_source",
        "nFrmBufNum": "frame_buf_num",
        "PoolId": "pool_id"
    }

class AX_IVPS_USER_FRAME_RATE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_user_frame_rate_ctrl = {
            "enable": bool,
            "array_number": int,
            "rate_control": [bool]
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),                     # Enable frame rate control
        ("nArryNum", AX_U8),                      # Number of items in rate control array
        ("bRateCtrl", AX_BOOL * AX_IVPS_USER_FRAME_RATE_NUM)  # Rate control flags
    ]
    field_aliases = {
        "bEnable": "enable",
        "nArryNum": "array_number",
        "bRateCtrl": "rate_control"
    }

AX_COORD_E = AX_S32
"""
    coord

    .. parsed-literal::

        AX_COORD_ABS   = 0
        AX_COORD_RATIO = 1    # In ratio mode: nX, nY: [0, 999]; nW, nH: [1, 1000]
        AX_COORD_BUTT  = 2
"""
AX_COORD_ABS = 0
AX_COORD_RATIO = 1           # In ratio mode: nX, nY: [0, 999]; nW, nH: [1, 1000]
AX_COORD_BUTT = 2

class AX_IVPS_CROP_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_crop_info = {
            "enable": bool,
            "coordinate_mode": :class:`AX_COORD_E <axcl.ivps.axcl_ivps_type.AX_COORD_E>`,
            "crop_rect": :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),                    # Enable cropping
        ("eCoordMode", AX_COORD_E),              # Coordinate mode
        ("tCropRect", AX_IVPS_RECT_T)            # Crop rectangle
    ]
    field_aliases = {
        "bEnable": "enable",
        "eCoordMode": "coordinate_mode",
        "tCropRect": "crop_rect"
    }

class AX_IVPS_CORNER_RECT_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_corner_rect_attr = {
            "enabled": bool,
            "hor_length": int,
            "ver_length": int
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),                    # Enable corner rectangle
        ("nHorLength", AX_U32),                  # Horizontal length
        ("nVerLength", AX_U32)                   # Vertical length
    ]
    field_aliases = {
        "bEnable": "enabled",
        "nHorLength": "hor_length",
        "nVerLength": "ver_length"
    }

AX_IVPS_SCALE_RANGE_TYPE_E = AX_S32
"""
    ivps scale range type

    .. parsed-literal::

        AX_IVPS_SCALE_RANGE_0    = 0    # scale range <  8/64
        AX_IVPS_SCALE_RANGE_1    = 1    # scale range >= 8/64
        AX_IVPS_SCALE_RANGE_2    = 2    # scale range >= 16/64
        AX_IVPS_SCALE_RANGE_3    = 3    # scale range >= 24/64
        AX_IVPS_SCALE_RANGE_4    = 4    # scale range >= 32/64
        AX_IVPS_SCALE_RANGE_5    = 5    # scale range >= 40/64
        AX_IVPS_SCALE_RANGE_6    = 6    # scale range >= 48/64
        AX_IVPS_SCALE_RANGE_7    = 7    # scale range >= 56/64
        AX_IVPS_SCALE_RANGE_8    = 8    # scale range > 1
        AX_IVPS_SCALE_RANGE_BUTT = 9
"""
AX_IVPS_SCALE_RANGE_0 = 0  # scale range <  8/64
AX_IVPS_SCALE_RANGE_1 = 1  # scale range >= 8/64
AX_IVPS_SCALE_RANGE_2 = 2  # scale range >= 16/64
AX_IVPS_SCALE_RANGE_3 = 3  # scale range >= 24/64
AX_IVPS_SCALE_RANGE_4 = 4  # scale range >= 32/64
AX_IVPS_SCALE_RANGE_5 = 5  # scale range >= 40/64
AX_IVPS_SCALE_RANGE_6 = 6  # scale range >= 48/64
AX_IVPS_SCALE_RANGE_7 = 7  # scale range >= 56/64
AX_IVPS_SCALE_RANGE_8 = 8  # scale range > 1
AX_IVPS_SCALE_RANGE_BUTT = 9

class AX_IVPS_SCALE_RANGE_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_scale_range = {
            "hor_scale_range": :class:`AX_IVPS_SCALE_RANGE_TYPE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_RANGE_TYPE_E>`,
            "ver_scale_range": :class:`AX_IVPS_SCALE_RANGE_TYPE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_RANGE_TYPE_E>`
        }
    """
    _fields_ = [
        ("eHorScaleRange", AX_IVPS_SCALE_RANGE_TYPE_E),  # Horizontal scale range
        ("eVerScaleRange", AX_IVPS_SCALE_RANGE_TYPE_E)   # Vertical scale range (Reserved)
    ]
    field_aliases = {
        "eHorScaleRange": "hor_scale_range",
        "eVerScaleRange": "ver_scale_range"
    }

AX_IVPS_COEF_LEVEL_E = AX_S32
"""
    ivps coef level

    .. parsed-literal::

        AX_IVPS_COEF_LEVEL_0    = 0    # Coefficient level 0
        AX_IVPS_COEF_LEVEL_1    = 1    # Coefficient level 1
        AX_IVPS_COEF_LEVEL_2    = 2    # Coefficient level 2
        AX_IVPS_COEF_LEVEL_3    = 3    # Coefficient level 3
        AX_IVPS_COEF_LEVEL_4    = 4    # Coefficient level 4
        AX_IVPS_COEF_LEVEL_5    = 5    # Coefficient level 5
        AX_IVPS_COEF_LEVEL_6    = 6    # Coefficient level 6
        AX_IVPS_COEF_LEVEL_BUTT = 7
"""
AX_IVPS_COEF_LEVEL_0 = 0  # Coefficient level 0
AX_IVPS_COEF_LEVEL_1 = 1  # Coefficient level 1
AX_IVPS_COEF_LEVEL_2 = 2  # Coefficient level 2
AX_IVPS_COEF_LEVEL_3 = 3  # Coefficient level 3
AX_IVPS_COEF_LEVEL_4 = 4  # Coefficient level 4
AX_IVPS_COEF_LEVEL_5 = 5  # Coefficient level 5
AX_IVPS_COEF_LEVEL_6 = 6  # Coefficient level 6
AX_IVPS_COEF_LEVEL_BUTT = 7

class AX_IVPS_SCALE_COEF_LEVEL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_scale_coef_level = {
            "hor_luma": :class:`AX_IVPS_COEF_LEVEL_E <axcl.ivps.axcl_ivps_type.AX_IVPS_COEF_LEVEL_E>`,
            "hor_chroma": :class:`AX_IVPS_COEF_LEVEL_E <axcl.ivps.axcl_ivps_type.AX_IVPS_COEF_LEVEL_E>`,
            "ver_luma": :class:`AX_IVPS_COEF_LEVEL_E <axcl.ivps.axcl_ivps_type.AX_IVPS_COEF_LEVEL_E>`,
            "ver_chroma": :class:`AX_IVPS_COEF_LEVEL_E <axcl.ivps.axcl_ivps_type.AX_IVPS_COEF_LEVEL_E>`
        }
    """
    _fields_ = [
        ("eHorLuma", AX_IVPS_COEF_LEVEL_E),    # Horizontal luminance coefficient level
        ("eHorChroma", AX_IVPS_COEF_LEVEL_E),  # Horizontal chrominance coefficient level (Reserved)
        ("eVerLuma", AX_IVPS_COEF_LEVEL_E),    # Vertical luminance coefficient level (Reserved)
        ("eVerChroma", AX_IVPS_COEF_LEVEL_E)   # Vertical chrominance coefficient level (Reserved)
    ]
    field_aliases = {
        "eHorLuma": "hor_luma",
        "eHorChroma": "hor_chroma",
        "eVerLuma": "ver_luma",
        "eVerChroma": "ver_chroma"
    }

class AX_IVPS_SCALE_STEP_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_scale_step = {
            "enabled": bool,
            "scale_step_width": int,
            "scale_step_height": int
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),           # Enable scaling
        ("nScaleStepW", AX_U16),        # Scale step width
        ("nScaleStepH", AX_U16)         # Scale step height
    ]
    field_aliases = {
        "bEnable": "enabled",
        "nScaleStepW": "scale_step_width",
        "nScaleStepH": "scale_step_height"
    }

class AX_IVPS_ASPECT_RATIO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_aspect_ratio = {
            "aspect_ratio_mode": :class:`AX_IVPS_ASPECT_RATIO_E <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_E>`,
            "background_color": int,
            "alignments": [:class:`AX_IVPS_ASPECT_RATIO_ALIGN_E <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_ALIGN_E>`],
            "rectangle": :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`
        }
    """
    _fields_ = [
        ("eMode", AX_IVPS_ASPECT_RATIO_E),  # Aspect ratio mode
        ("nBgColor", AX_U32),                # Background color
        ("eAligns", AX_IVPS_ASPECT_RATIO_ALIGN_E * 2),  # Aspect ratio alignment
        ("tRect", AX_IVPS_RECT_T)            # Rectangle for manual mode
    ]
    field_aliases = {
        "eMode": "aspect_ratio_mode",
        "nBgColor": "background_color",
        "eAligns": "alignments",
        "tRect": "rectangle"
    }

AX_IVPS_ENGINE_E = AX_S32
"""
    ivps engine

    .. parsed-literal::

        AX_IVPS_ENGINE_SUBSIDIARY = 0    # do not create owner workqueue, subsidiary of the previous filter
        AX_IVPS_ENGINE_TDP        = 1
        AX_IVPS_ENGINE_GDC        = 2
        AX_IVPS_ENGINE_VPP        = 3
        AX_IVPS_ENGINE_VGP        = 4
        AX_IVPS_ENGINE_IVE        = 5
        AX_IVPS_ENGINE_VO         = 6
        AX_IVPS_ENGINE_DSP        = 7
        AX_IVPS_ENGINE_BUTT       = 8
"""
AX_IVPS_ENGINE_SUBSIDIARY = 0  #  do not create owner workqueue, subsidiary of the previous filter
AX_IVPS_ENGINE_TDP = 1
AX_IVPS_ENGINE_GDC = 2
AX_IVPS_ENGINE_VPP = 3
AX_IVPS_ENGINE_VGP = 4
AX_IVPS_ENGINE_IVE = 5
AX_IVPS_ENGINE_VO = 6
AX_IVPS_ENGINE_DSP = 7
AX_IVPS_ENGINE_BUTT = 8

AX_IVPS_PIPELINE_E = AX_S32
"""
    ivps pipeline

    .. parsed-literal::

        AX_IVPS_PIPELINE_DEFAULT = 0
        AX_IVPS_PIPELINE_BUTT    = 1
"""
AX_IVPS_PIPELINE_DEFAULT = 0
AX_IVPS_PIPELINE_BUTT = 1

class AX_IVPS_TDP_CFG_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivpsdp_cfg = {
            "rotation": :class:`AX_IVPS_ROTATION_E <axcl.ivps.axcl_ivps_type.AX_IVPS_ROTATION_E>`,
            "mirror": bool,
            "flip": bool
        }
    """
    _fields_ = [
        ("eRotation", AX_IVPS_ROTATION_E),   # Rotation attribute
        ("bMirror", AX_BOOL),                # Mirror attribute
        ("bFlip", AX_BOOL)                   # Flip attribute
    ]
    field_aliases = {
        "eRotation": "rotation",
        "bMirror": "mirror",
        "bFlip": "flip"
    }

AX_IVPS_SCALE_MODE_E = AX_S32
"""
    ivps scale mode

    .. parsed-literal::

        AX_IVPS_SCALE_NORMAL = 0
        AX_IVPS_SCALE_UP     = 1
        AX_IVPS_SCALE_DOWN   = 2
        AX_IVPS_SCALE_BUTT   = 3
"""
AX_IVPS_SCALE_NORMAL = 0
AX_IVPS_SCALE_UP = 1
AX_IVPS_SCALE_DOWN = 2
AX_IVPS_SCALE_BUTT = 3

class UNION_IVPS_FILTER_CFG_T(BaseUnion):
    """
    .. parsed-literal::

        dict_union_ivps_filter_cfg = {
            "tdp_cfg": :class:`AX_IVPS_TDP_CFG_T <axcl.ivps.axcl_ivps_type.AX_IVPS_TDP_CFG_T>`,
            "gdc_cfg": :class:`AX_IVPS_GDC_CFG_T <axcl.ivps.axcl_ivps_type.AX_IVPS_GDC_CFG_T>`
        }
    """
    _fields_ = [
        ("tTdpCfg", AX_IVPS_TDP_CFG_T),
        ("tGdcCfg", AX_IVPS_GDC_CFG_T),
    ]
    field_aliases = {
        "tTdpCfg": "tdp_cfg",
        "tGdcCfg": "gdc_cfg"
    }
    value_union_type_mapping = {
        AX_IVPS_ENGINE_TDP: "tTdpCfg",
        AX_IVPS_ENGINE_GDC: "tGdcCfg",
    }

class AX_IVPS_FILTER_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_filter = {
            "engaged": bool,
            "engine": :class:`AX_IVPS_ENGINE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_ENGINE_E>`,
            "frame_rate_control": :class:`AX_FRAME_RATE_CTRL_T <axcl.ax_global_type.AX_FRAME_RATE_CTRL_T>`,
            "crop": bool,
            "crop_rect": :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`,
            "dst_pic_width": int,
            "dst_pic_height": int,
            "dst_pic_stride": int,
            "dst_pic_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "compression_info": :class:`AX_FRAME_COMPRESS_INFO_T <axcl.ax_global_type.AX_FRAME_COMPRESS_INFO_T>`,
            "in_place": bool,
            "aspect_ratio": :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`,
            "engine_cfg": :class:`UNION_IVPS_FILTER_CFG_T <axcl.ivps.axcl_ivps_type.UNION_IVPS_FILTER_CFG_T>`,
            "reserved": int,
            "scale_mode": :class:`AX_IVPS_SCALE_MODE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_MODE_E>`
        }
    """
    _fields_ = [
        ("bEngage", AX_BOOL),                             # Engage filter
        ("eEngine", AX_IVPS_ENGINE_E),                   # Engine type
        ("tFRC", AX_FRAME_RATE_CTRL_T),                  # Frame rate control
        ("bCrop", AX_BOOL),                               # Enable cropping
        ("tCropRect", AX_IVPS_RECT_T),                   # Crop rectangle
        ("nDstPicWidth", AX_U32),                        # Destination picture width
        ("nDstPicHeight", AX_U32),                       # Destination picture height
        ("nDstPicStride", AX_U32),                       # Destination picture stride
        ("eDstPicFormat", AX_IMG_FORMAT_E),              # Destination picture format
        ("tCompressInfo", AX_FRAME_COMPRESS_INFO_T),    # Compression info
        ("bInplace", AX_BOOL),                            # In-place processing
        ("tAspectRatio", AX_IVPS_ASPECT_RATIO_T),        # Aspect ratio
        ("uEngineCfg", UNION_IVPS_FILTER_CFG_T),                    # Engine specific config data
        ("nFRC", AX_U32),                                # Reserved
        ("eScaleMode", AX_IVPS_SCALE_MODE_E)             # Scale mode
    ]
    field_aliases = {
        "bEngage": "engaged",
        "eEngine": "engine",
        "tFRC": "frame_rate_control",
        "bCrop": "crop",
        "tCropRect": "crop_rect",
        "nDstPicWidth": "dst_pic_width",
        "nDstPicHeight": "dst_pic_height",
        "nDstPicStride": "dst_pic_stride",
        "eDstPicFormat": "dst_pic_format",
        "tCompressInfo": "compression_info",
        "bInplace": "in_place",
        "tAspectRatio": "aspect_ratio",
        "uEngineCfg": "engine_cfg",
        "nFRC": "reserved",
        "eScaleMode": "scale_mode"
    }
    name_union_type_mapping = {
        "uEngineCfg": "eEngine"
    }

class AX_IVPS_PIPELINE_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_pipeline_attr = {
            "out_channel_num": int,
            "in_debug_fifo_depth": int,
            "out_fifo_depth": [int],
            "filters": [[:class:`AX_IVPS_FILTER_T <axcl.ivps.axcl_ivps_type.AX_IVPS_FILTER_T>`]]
        }
    """
    _fields_ = [
        ("nOutChnNum", AX_U8),                      # Output channel number
        ("nInDebugFifoDepth", AX_U16),              # Input debug FIFO depth
        ("nOutFifoDepth", AX_U8 * AX_IVPS_MAX_OUTCHN_NUM),  # Output FIFO depth
        ("tFilter", AX_IVPS_FILTER_T  * AX_IVPS_MAX_FILTER_NUM_PER_OUTCHN * (AX_IVPS_MAX_OUTCHN_NUM + 1))  # Filter attributes
    ]
    field_aliases = {
        "nOutChnNum": "out_channel_num",
        "nInDebugFifoDepth": "in_debug_fifo_depth",
        "nOutFifoDepth": "out_fifo_depth",
        "tFilter": "filters"
    }

class AX_IVPS_GRP_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_grp_attr = {
            "in_fifo_depth": int,
            "pipeline": :class:`AX_IVPS_PIPELINE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_PIPELINE_E>`
        }
    """
    _fields_ = [
        ("nInFifoDepth", AX_U8),            # Input FIFO depth
        ("ePipeline", AX_IVPS_PIPELINE_E)   # Pipeline type
    ]
    field_aliases = {
        "nInFifoDepth": "in_fifo_depth",
        "ePipeline": "pipeline"
    }

class AX_IVPS_CHN_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_chn_attr = {
            "frame_rate_control": :class:`AX_FRAME_RATE_CTRL_T <axcl.ax_global_type.AX_FRAME_RATE_CTRL_T>`,
            "dst_pic_width": int,
            "dst_pic_height": int,
            "dst_pic_stride": int,
            "dst_pic_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "aspect_ratio": :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`,
            "out_fifo_depth": int,
            "reserved": int
        }
    """
    _fields_ = [
        ("tFRC", AX_FRAME_RATE_CTRL_T),                # Frame rate control
        ("nDstPicWidth", AX_U32),                      # Destination picture width
        ("nDstPicHeight", AX_U32),                     # Destination picture height
        ("nDstPicStride", AX_U32),                     # Destination picture stride
        ("eDstPicFormat", AX_IMG_FORMAT_E),            # Destination picture format
        ("tAspectRatio", AX_IVPS_ASPECT_RATIO_T),      # Aspect ratio
        ("nOutFifoDepth", AX_U8),                      # Output FIFO depth
        ("nFRC", AX_U32)                               # Reserved
    ]
    field_aliases = {
        "tFRC": "frame_rate_control",
        "nDstPicWidth": "dst_pic_width",
        "nDstPicHeight": "dst_pic_height",
        "nDstPicStride": "dst_pic_stride",
        "eDstPicFormat": "dst_pic_format",
        "tAspectRatio": "aspect_ratio",
        "nOutFifoDepth": "out_fifo_depth",
        "nFRC": "reserved"
    }

class AX_IVPS_DUTY_CYCLE_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_duty_cycle_attr = {
            "tdp0_duty_cycle": int,
            "tdp1_duty_cycle": int,
            "gdc_duty_cycle": int,
            "vpp_duty_cycle": int,
            "vgp_duty_cycle": int,
            "vdsp0_duty_cycle": int,
            "vdsp1_duty_cycle": int
        }
    """
    _fields_ = [
        ("TDP0_duty_cycle", AX_U64),  # Duty cycle for TDP0, Range: [0, 100]
        ("TDP1_duty_cycle", AX_U64),  # Duty cycle for TDP1, Range: [0, 100]
        ("GDC_duty_cycle", AX_U64),   # Duty cycle for GDC, Range: [0, 100]
        ("VPP_duty_cycle", AX_U64),   # Duty cycle for VPP, Range: [0, 100]
        ("VGP_duty_cycle", AX_U64),   # Duty cycle for VGP, Range: [0, 100]
        ("VDSP0_duty_cycle", AX_U64), # Duty cycle for VDSP0, Range: [0, 100]
        ("VDSP1_duty_cycle", AX_U64)  # Duty cycle for VDSP1, Range: [0, 100]
    ]
    field_aliases = {
        "TDP0_duty_cycle": "tdp0_duty_cycle",
        "TDP1_duty_cycle": "tdp1_duty_cycle",
        "GDC_duty_cycle": "gdc_duty_cycle",
        "VPP_duty_cycle": "vpp_duty_cycle",
        "VGP_duty_cycle": "vgp_duty_cycle",
        "VDSP0_duty_cycle": "vdsp0_duty_cycle",
        "VDSP1_duty_cycle": "vdsp1_duty_cycle"
    }

IVPS_RGN_HANDLE = AX_S32

AX_IVPS_MAX_RGN_HANDLE_NUM = 384
AX_IVPS_INVALID_REGION_HANDLE = IVPS_RGN_HANDLE(-1)
AX_IVPS_REGION_MAX_DISP_NUM = 32

AX_IVPS_RGN_TYPE_E = AX_S32
"""
    ivps rgn type

    .. parsed-literal::

        AX_IVPS_RGN_TYPE_LINE    = 0
        AX_IVPS_RGN_TYPE_RECT    = 1
        AX_IVPS_RGN_TYPE_POLYGON = 2    # Convex quadrilateral
        AX_IVPS_RGN_TYPE_MOSAIC  = 3
        AX_IVPS_RGN_TYPE_OSD     = 4
        AX_IVPS_RGN_TYPE_BUTT    = 5
"""
AX_IVPS_RGN_TYPE_LINE = 0
AX_IVPS_RGN_TYPE_RECT = 1
AX_IVPS_RGN_TYPE_POLYGON = 2  # Convex quadrilateral
AX_IVPS_RGN_TYPE_MOSAIC = 3
AX_IVPS_RGN_TYPE_OSD = 4
AX_IVPS_RGN_TYPE_BUTT = 5

class AX_IVPS_RGN_CHN_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rgn_chn_attr = {
            "z_index": int,
            "single_canvas": bool,
            "alpha": int,
            "format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "bit_color": :class:`AX_BITCOLOR_T <axcl.ax_global_type.AX_BITCOLOR_T>`,
            "color_key": :class:`AX_COLORKEY_T <axcl.ax_global_type.AX_COLORKEY_T>`
        }
    """
    _fields_ = [
        ("nZindex", AX_S32),           # RW; Z index for OSD
        ("bSingleCanvas", AX_BOOL),    # RW; AX_TRUE: single canvas; AX_FALSE: double canvas
        ("nAlpha", AX_U16),            # RW; range: (0, 255]; 0: transparent, 255: opaque
        ("eFormat", AX_IMG_FORMAT_E),  # Image format
        ("nBitColor", AX_BITCOLOR_T),  # RW; only for bitmap
        ("nColorKey", AX_COLORKEY_T)   # Color key
    ]
    field_aliases = {
        "nZindex": "z_index",
        "bSingleCanvas": "single_canvas",
        "nAlpha": "alpha",
        "eFormat": "format",
        "nBitColor": "bit_color",
        "nColorKey": "color_key"
    }

class AX_IVPS_RGN_LINE_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rgn_line = {
            "points": [:class:`AX_POINT_T <axcl.ax_global_type.AX_POINT_T>`],
            "line_width": int,
            "color": :class:`ctypes.c_uint`,
            "alpha": int
        }
    """
    _fields_ = [
        ("tPTs", AX_POINT_T * 2),      # RW; fixed two point coordinates
        ("nLineWidth", AX_U32),        # RW; range: [1, 16]
        ("nColor", IVPS_RGB),          # RGB Color: 0xRRGGBB
        ("nAlpha", AX_U8)              # RW; range: (0, 255]; 0: transparent, 255: opaque
    ]
    field_aliases = {
        "tPTs": "points",
        "nLineWidth": "line_width",
        "nColor": "color",
        "nAlpha": "alpha"
    }

class UNION_RGN_POLYGON_T(BaseUnion):
    """
    .. parsed-literal::

        dict_union_rgn_polygon = {
            "rect": :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`,
            "points": [:class:`AX_IVPS_POINT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_T>`]
        }
    """
    _fields_ = [
        ("tRect", AX_IVPS_RECT_T),  # Rectangle info
        ("tPTs", AX_IVPS_POINT_T * AX_IVPS_MAX_POLYGON_POINT_NUM),  # RW; polygon coordinates
    ]
    field_aliases = {
        "tRect": "rect",
        "tPTs": "points"
    }
    value_union_type_mapping = {
        AX_IVPS_RGN_TYPE_RECT: "tRect",
        AX_IVPS_RGN_TYPE_POLYGON: "tPTs",
    }

class AX_IVPS_RGN_POLYGON_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rgn_polygon = {
            "rgn_polygon": :class:`UNION_RGN_POLYGON_T <axcl.ivps.axcl_ivps_type.UNION_RGN_POLYGON_T>`,
            "point_number": int,
            "line_width": int,
            "color": int,
            "alpha": int,
            "solid_fill": bool,
            "corner_rect": :class:`AX_IVPS_CORNER_RECT_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_CORNER_RECT_ATTR_T>`
        }
    """
    _fields_ = [
        ("uRgnPolygon", UNION_RGN_POLYGON_T),
        ("nPointNum", AX_U8),       # RW; range: [4, 10]
        ("nLineWidth", AX_U32),     # RW; range: [1, 16]
        ("nColor", IVPS_RGB),       # RW; range: [0, 0xffffff]; color RGB888
        ("nAlpha", AX_U8),          # RW; range: (0, 255]; 0: transparent, 255: opaque
        ("bSolid", AX_BOOL),        # Fill the rect with nColor if AX_TRUE
        ("tCornerRect", AX_IVPS_CORNER_RECT_ATTR_T)  # Corner rectangle attributes
    ]
    field_aliases = {
        "uRgnPolygon": "rgn_polygon",
        "nPointNum": "point_number",
        "nLineWidth": "line_width",
        "nColor": "color",
        "nAlpha": "alpha",
        "bSolid": "solid_fill",
        "tCornerRect": "corner_rect"
    }
    name_union_type_mapping = {
        "uRgnPolygon": "eType"
    }

class AX_IVPS_RGN_MOSAIC_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rgn_mosaic = {
            "rect": :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`,
            "block_size": :class:`AX_IVPS_MOSAIC_BLK_SIZE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_MOSAIC_BLK_SIZE_E>`
        }
    """
    _fields_ = [
        ("tRect", AX_IVPS_RECT_T),                  # Rectangle
        ("eBklSize", AX_IVPS_MOSAIC_BLK_SIZE_E)     # Mosaic block size
    ]
    field_aliases = {
        "tRect": "rect",
        "eBklSize": "block_size"
    }

AX_IVPS_RGN_OSD_T = AX_OSD_BMP_ATTR_T  # OSD attributes (Alias)

class AX_IVPS_RGN_DISP_U(BaseUnion):
    """
    .. parsed-literal::

        dict_ivps_rgn_disp_u = {
            "line_attr": :class:`AX_IVPS_RGN_LINE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_LINE_T>`,
            "polygon_attr": :class:`AX_IVPS_RGN_POLYGON_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_POLYGON_T>`,
            "mosaic_attr": :class:`AX_IVPS_RGN_MOSAIC_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_MOSAIC_T>`,
            "osd_attr": :class:`AX_OSD_BMP_ATTR_T <axcl.ax_global_type.AX_OSD_BMP_ATTR_T>`
        }
    """
    _fields_ = [
        ("tLine", AX_IVPS_RGN_LINE_T),          # Line attributes
        ("tPolygon", AX_IVPS_RGN_POLYGON_T),    # Polygon attributes
        ("tMosaic", AX_IVPS_RGN_MOSAIC_T),      # Mosaic attributes
        ("tOSD", AX_IVPS_RGN_OSD_T)             # OSD attributes
    ]
    field_aliases = {
        "tLine": "line_attr",
        "tPolygon": "polygon_attr",
        "tMosaic": "mosaic_attr",
        "tOSD": "osd_attr"
    }
    value_union_type_mapping = {
        AX_IVPS_RGN_TYPE_LINE: "tLine",
        AX_IVPS_RGN_TYPE_RECT: "tPolygon",
        AX_IVPS_RGN_TYPE_POLYGON: "tPolygon",
        AX_IVPS_RGN_TYPE_MOSAIC: "tMosaic",
        AX_IVPS_RGN_TYPE_OSD: "tOSD",
    }

class AX_IVPS_RGN_DISP_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rgn_disp = {
            "show": bool,
            "type": :class:`AX_IVPS_RGN_TYPE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_TYPE_E>`,
            "display": :class:`AX_IVPS_RGN_DISP_U <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_DISP_U>`
        }
    """
    _fields_ = [
        ("bShow", AX_BOOL),                     # Show/Hide
        ("eType", AX_IVPS_RGN_TYPE_E),          # Region type
        ("uDisp", AX_IVPS_RGN_DISP_U)           # Display union
    ]
    field_aliases = {
        "bShow": "show",
        "eType": "type",
        "uDisp": "display"
    }
    name_union_type_mapping = {
        "uDisp": "eType"
    }

class AX_IVPS_RGN_DISP_GROUP_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rgn_disp_group = {
            "number_of_regions": int,
            "channel_attr": :class:`AX_IVPS_RGN_CHN_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_CHN_ATTR_T>`,
            "display_attr_array": [:class:`AX_IVPS_RGN_DISP_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_DISP_T>`]
        }
    """
    _fields_ = [
        ("nNum", AX_U32),                          # Number of regions
        ("tChnAttr", AX_IVPS_RGN_CHN_ATTR_T),      # Channel attributes
        ("arrDisp", AX_IVPS_RGN_DISP_T * AX_IVPS_REGION_MAX_DISP_NUM)  # Array of display attributes
    ]
    field_aliases = {
        "nNum": "number_of_regions",
        "tChnAttr": "channel_attr",
        "arrDisp": "display_attr_array"
    }

class AX_IVPS_GDI_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_gdi_attr = {
            "thickness": int,
            "alpha": int,
            "color": int,
            "solid_fill": bool,
            "absolute_coordinate": bool,
            "corner_rect": :class:`AX_IVPS_CORNER_RECT_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_CORNER_RECT_ATTR_T>`
        }
    """
    _fields_ = [
        ("nThick", AX_U16),                             # Thickness
        ("nAlpha", AX_U16),                             # Alpha value
        ("nColor", AX_U32),                             # Color
        ("bSolid", AX_BOOL),                            # Fill the rect if AX_TRUE
        ("bAbsCoo", AX_BOOL),                           # Is absolute coordinate
        ("tCornerRect", AX_IVPS_CORNER_RECT_ATTR_T)     # Corner rectangle attributes
    ]
    field_aliases = {
        "nThick": "thickness",
        "nAlpha": "alpha",
        "nColor": "color",
        "bSolid": "solid_fill",
        "bAbsCoo": "absolute_coordinate",
        "tCornerRect": "corner_rect"
    }

class AX_IVPS_RGN_CANVAS_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_ivps_rgn_canvas_info = {
            "physical_address": int,
            "virtual_address": int,
            "uv_offset": int,
            "stride": int,
            "width": int,
            "height": int,
            "format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`
        }
    """
    _fields_ = [
        ("nPhyAddr", AX_U64),           # Physical address
        ("pVirAddr", c_void_p),         # Virtual address
        ("nUVOffset", AX_U32),          # Y and UV offset
        ("nStride", AX_U32),            # Stride
        ("nW", AX_U16),                 # Width
        ("nH", AX_U16),                 # Height
        ("eFormat", AX_IMG_FORMAT_E)    # Image Format
    ]
    field_aliases = {
        "nPhyAddr": "physical_address",
        "pVirAddr": "virtual_address",
        "nUVOffset": "uv_offset",
        "nStride": "stride",
        "nW": "width",
        "nH": "height",
        "eFormat": "format"
    }