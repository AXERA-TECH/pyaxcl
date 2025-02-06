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

from ctypes import c_void_p, POINTER,  CFUNCTYPE
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.ax_global_type import *
from axcl.ax_base_type import *
from axcl.utils.axcl_basestructure import *

AX_DMADIM_ENDIAN_E = AX_S32
"""
    dmadim endian

    .. parsed-literal::

        AX_DMADIM_ENDIAN_DEF = 0
        AX_DMADIM_ENDIAN_32 = 1
        AX_DMADIM_ENDIAN_16 = 2
        AX_DMADIM_ENDIAN_MAX = 2
"""
AX_DMADIM_ENDIAN_DEF = 0
AX_DMADIM_ENDIAN_32 = 1
AX_DMADIM_ENDIAN_16 = 2
AX_DMADIM_ENDIAN_MAX = 2

AX_DMADIM_XFER_MODE_E = AX_S32
"""
    dmadim xfer mode

    .. parsed-literal::
        AX_DMADIM_1D = 0
        AX_DMADIM_2D = 1
        AX_DMADIM_3D = 2
        AX_DMADIM_4D = 3
        AX_DMADIM_MEMORY_INIT = 4
        AX_DMADIM_CHECKSUM = 5
"""
AX_DMADIM_1D = 0
AX_DMADIM_2D = 1
AX_DMADIM_3D = 2
AX_DMADIM_4D = 3
AX_DMADIM_MEMORY_INIT = 4
AX_DMADIM_CHECKSUM = 5


class AX_DMADIM_XFER_STAT_T(BaseStructure):
    """
    .. parsed-literal::

        dict_dmadim_xfer_stat = {
            "id": int,
            "checksum": int,
            "stat": int
        }
    """
    _fields_ = [
        ("s32Id", AX_S32),
        ("u32CheckSum", AX_U32),
        ("u32Stat", AX_U32)
    ]
    field_aliases = {
        "s32Id": "id",
        "u32CheckSum": "checksum",
        "u32Stat": "stat"
    }

class AX_DMADIM_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_dmadim_info = {
            "phy_addr": int,
            "img_w": int,
            "stride": int
        }
    """
    _fields_ = [
        ("u64PhyAddr", AX_U64),
        ("u32Imgw", AX_U32),
        ("u32Stride", AX_U32 * 3)
    ]
    field_aliases = {
        "u64PhyAddr": "phy_addr",
        "u32Imgw": "img_w",
        "u32Stride": "stride"
    }

class AX_DMADIM_DESC_XD_T(BaseStructure):
    """
    .. parsed-literal::

        dict_dmadim_desc_xd = {
            "n_tiles": list[int, int, int],
            "src_info": :class:`AX_DMADIM_INFO_T <axcl.dmadim.axcl_dmadim_type.AX_DMADIM_INFO_T>`,
            "dst_info": :class:`AX_DMADIM_INFO_T <axcl.dmadim.axcl_dmadim_type.AX_DMADIM_INFO_T>`,
        }
    """
    _fields_ = [
        ("u16Ntiles", AX_U16 * 3),
        ("tSrcInfo", AX_DMADIM_INFO_T),
        ("tDstInfo", AX_DMADIM_INFO_T)
    ]
    field_aliases = {
        "u16Ntiles": "n_tiles",
        "tSrcInfo": "src_info",
        "tDstInfo": "dst_info"
    }

class AX_DMADIM_DESC_T(BaseStructure):
    """
    .. parsed-literal::

        dict_dmadim_desc = {
            "phy_src": int,
            "phy_dst": int,
            "size": int
        }
    """
    _fields_ = [
        ("u64PhySrc", AX_U64),
        ("u64PhyDst", AX_U64),
        ("u32Size", AX_U32)
    ]
    field_aliases = {
        "u64PhySrc": "phy_src",
        "u64PhyDst": "phy_dst",
        "u32Size": "size"
    }

class AX_DMADIM_MSG_T(BaseStructure):
    """
    .. parsed-literal::

        dict_dmadim_msg = {
            "desc_buf": list of dict_dmadim_desc, :class:`AX_DMADIM_DESC_T <axcl.dmadim.axcl_dmadim_type.AX_DMADIM_DESC_T>`,
            "endian": int,
            "desc_buf": int,
            "callback": callback funtion: def callback(stat, cb_arg)->None,  stat-:class:`AX_DMADIM_XFER_STAT_T <axcl.dmadim.axcl_dmadim_type.AX_DMADIM_XFER_STAT_T>`,
            "cb_arg": int,
            "dma_mode": int
        }
    """
    _fields_ = [
        ("u32DescNum", AX_U32),
        ("eEndian", AX_DMADIM_ENDIAN_E),
        ("pDescBuf", c_void_p),
        ("pfnCallBack",  CFUNCTYPE(None, POINTER(AX_DMADIM_XFER_STAT_T), c_void_p)),
        ("pCbArg", c_void_p),
        ("eDmaMode", AX_DMADIM_XFER_MODE_E)
    ]
    field_aliases = {
        "eEndian": "endian",
        "pDescBuf": "desc_buf",
        "pfnCallBack": "callback",
        "pCbArg": "cb_arg",
        "eDmaMode": "dma_mode"
    }