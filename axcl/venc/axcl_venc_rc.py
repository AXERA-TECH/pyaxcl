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

from ctypes import Structure, Union
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.ax_global_type import *
from axcl.utils.axcl_basestructure import *


VENC_MIN_BITRATE = 3
VENC_MAX_BITRATE = 160 * 1000

VENC_BITRATE_RATIO = 1000
VENC_MIN_INTRADELTAQP = -51
VENC_MAX_INTRADELTAQP = 51

# IDR interval
VENC_MIN_IDR_INTERVAL = 1
VENC_MAX_IDR_INTERVAL = 65536

# qp range
VENC_MIN_FIXED_QP = -1
VENC_MIN_QP      = 0
VENC_MAX_QP      = 51
AX_VENC_IDR_DELTA_QP_MAX    = 10
AX_VENC_IDR_DELTA_QP_MIN    = 2

# frame rate range
VENC_MIN_FRAME_RATE = 1
VENC_MAX_FRAME_RATE = 240

MAX_EXTRA_BITRATE = 1000 * 1024

# I/P frame size proportion
VENC_MIN_I_PROP = 1
VENC_MAX_I_PROP = 100

# cvbr params
VENC_MIN_SHORT_TERM_STAT_TIME = 1   # in seconds
VENC_MAX_SHORT_TERM_STAT_TIME = 120 # in seconds

VENC_MIN_LONG_TERM_STAT_TIME = 1    # in seconds
VENC_MAX_LONG_TERM_STAT_TIME = 1440 # in seconds

VENC_MAX_LONG_TERM_BITRATE_LOW  = 2      # in kbps
VENC_MAX_LONG_TERM_BITRATE_HIGH = 614400 # in kbps

VENC_MIN_LONG_TERM_BITRATE_LOW  = 0      # in kbps
VENC_MIN_LONG_TERM_BITRATE_HIGH = 614400 # in kbps
# Difference between FrameLevelMinQp and MinQp
VENC_MIN_QP_DELTA_LOW  = 0
VENC_MIN_QP_DELTA_HIGH = 4
# Difference between FrameLevelMaxQp and MaxQp
VENC_MAX_QP_DELTA_LOW  = 0
VENC_MAX_QP_DELTA_HIGH = 4

VENC_MIN_CHANGE_POS = 20
VENC_MAX_CHANGE_POS = 100
VENC_DEF_CHANGE_POS = 90

VENC_MIN_STILL_PERCENT = 10
VENC_MAX_STILL_PERCENT = 100
VENC_DEF_STILL_PERCENT = 25

VENC_MAX_STILL_QP_DEF = 36

AX_VENC_RC_MODE_E = AX_S32
"""
    RC mode definition

    .. parsed-literal::

        AX_VENC_RC_MODE_H264CBR     = 1
        AX_VENC_RC_MODE_H264VBR     = 2
        AX_VENC_RC_MODE_H264AVBR    = 3
        AX_VENC_RC_MODE_H264QVBR    = 4
        AX_VENC_RC_MODE_H264CVBR    = 5
        AX_VENC_RC_MODE_H264FIXQP   = 6
        AX_VENC_RC_MODE_H264QPMAP   = 7
        AX_VENC_RC_MODE_MJPEGCBR    = 8
        AX_VENC_RC_MODE_MJPEGVBR    = 9
        AX_VENC_RC_MODE_MJPEGFIXQP  = 10
        AX_VENC_RC_MODE_H265CBR     = 11
        AX_VENC_RC_MODE_H265VBR     = 12
        AX_VENC_RC_MODE_H265AVBR    = 13
        AX_VENC_RC_MODE_H265QVBR    = 14
        AX_VENC_RC_MODE_H265CVBR    = 15
        AX_VENC_RC_MODE_H265FIXQP   = 16
        AX_VENC_RC_MODE_H265QPMAP   = 17
        AX_VENC_RC_MODE_BUTT        = 18
"""
AX_VENC_RC_MODE_H264CBR = 1
AX_VENC_RC_MODE_H264VBR = 2
AX_VENC_RC_MODE_H264AVBR = 3
AX_VENC_RC_MODE_H264QVBR = 4
AX_VENC_RC_MODE_H264CVBR = 5
AX_VENC_RC_MODE_H264FIXQP = 6
AX_VENC_RC_MODE_H264QPMAP = 7

AX_VENC_RC_MODE_MJPEGCBR = 8
AX_VENC_RC_MODE_MJPEGVBR = 9
AX_VENC_RC_MODE_MJPEGFIXQP = 10

AX_VENC_RC_MODE_H265CBR = 11
AX_VENC_RC_MODE_H265VBR = 12
AX_VENC_RC_MODE_H265AVBR = 13
AX_VENC_RC_MODE_H265QVBR = 14
AX_VENC_RC_MODE_H265CVBR = 15
AX_VENC_RC_MODE_H265FIXQP = 16
AX_VENC_RC_MODE_H265QPMAP = 17

AX_VENC_RC_MODE_BUTT = 18



AX_VENC_RC_QPMAP_MODE_E = AX_S32
"""
    RC QP mode definition

    .. parsed-literal::

        AX_VENC_RC_QPMAP_MODE_MEANQP = 0
        AX_VENC_RC_QPMAP_MODE_MINQP  = 1
        AX_VENC_RC_QPMAP_MODE_MAXQP  = 2
        AX_VENC_RC_QPMAP_MODE_BUTT   = 3
"""
AX_VENC_RC_QPMAP_MODE_MEANQP = 0
AX_VENC_RC_QPMAP_MODE_MINQP = 1
AX_VENC_RC_QPMAP_MODE_MAXQP = 2

AX_VENC_RC_QPMAP_MODE_BUTT = 3


AX_VENC_RC_CTBRC_MODE_E = AX_S32
"""
    RC CTBRC mode definition

    .. parsed-literal::

        AX_VENC_RC_CTBRC_DISABLE      = 0    # Disable CTB QP adjustment.
        AX_VENC_RC_CTBRC_QUALITY      = 1    # CTB QP adjustment for Subjective Quality only.
        AX_VENC_RC_CTBRC_RATE         = 2    # CTB QP adjustment for Rate Control only.
        AX_VENC_RC_CTBRC_QUALITY_RATE = 3    # CTB QP adjustment for both Subjective Quality and Rate Control.
        AX_VENC_RC_CTBRC_BUTT         = 5
"""
AX_VENC_RC_CTBRC_DISABLE = 0      # Disable CTB QP adjustment.
AX_VENC_RC_CTBRC_QUALITY = 1      # CTB QP adjustment for Subjective Quality only.
AX_VENC_RC_CTBRC_RATE = 2         # CTB QP adjustment for Rate Control only.
AX_VENC_RC_CTBRC_QUALITY_RATE = 3 # CTB QP adjustment for both Subjective Quality and Rate Control.
AX_VENC_RC_CTBRC_BUTT = 5


AX_VENC_QPMAP_QP_TYPE_E = AX_S32
"""
    QP type definition

    .. parsed-literal::

        AX_VENC_QPMAP_QP_DISABLE = 0
        AX_VENC_QPMAP_QP_DELTA   = 1    # qp rang in [-31, 32]
        AX_VENC_QPMAP_QP_ABS     = 2    # qp range in [0, 51]
        AX_VENC_QPMAP_QP_BUTT    = 3
"""
AX_VENC_QPMAP_QP_DISABLE = 0
AX_VENC_QPMAP_QP_DELTA = 1 # qp rang in [-31, 32]
AX_VENC_QPMAP_QP_ABS = 2   # qp range in [0, 51]
AX_VENC_QPMAP_QP_BUTT = 3


AX_VENC_QPMAP_BLOCK_TYPE_E = AX_S32
"""
    QP map block type definition

    .. parsed-literal::

        AX_VENC_QPMAP_BLOCK_DISABLE = 0
        AX_VENC_QPMAP_BLOCK_SKIP    = 1
        AX_VENC_QPMAP_BLOCK_IPCM    = 2
        AX_VENC_QPMAP_BLOCK_BUTT    = 3
"""
AX_VENC_QPMAP_BLOCK_DISABLE = 0
AX_VENC_QPMAP_BLOCK_SKIP = 1
AX_VENC_QPMAP_BLOCK_IPCM = 2
AX_VENC_QPMAP_BLOCK_BUTT = 3

AX_VENC_QPMAP_BLOCK_UNIT_E  = AX_S32
"""
    QP map block definition

    .. parsed-literal::

        AX_VENC_QPMAP_BLOCK_UNIT_NONE  = -1
        AX_VENC_QPMAP_BLOCK_UNIT_64x64 = 0
        AX_VENC_QPMAP_BLOCK_UNIT_32x32 = 1
        AX_VENC_QPMAP_BLOCK_UNIT_16x16 = 2
        AX_VENC_QPMAP_BLOCK_UNIT_BUTT  = 3
"""
AX_VENC_QPMAP_BLOCK_UNIT_NONE = -1
AX_VENC_QPMAP_BLOCK_UNIT_64x64 = 0
AX_VENC_QPMAP_BLOCK_UNIT_32x32 = 1
AX_VENC_QPMAP_BLOCK_UNIT_16x16 = 2
AX_VENC_QPMAP_BLOCK_UNIT_BUTT = 3

class AX_VENC_QPMAP_META_T(BaseStructure):
    """
    Meta of QP map

    .. parsed-literal::

        dict_venc_qpmap_meta = {
            "ctb_rc_mode": int,
            "qpmap_qp_type": int,
            "qpmap_block_type": int,
            "qpmap_block_unit": int
        }
    """
    _fields_ = [
        ("enCtbRcMode", AX_S32),
        ("enQpmapQpType", AX_S32),
        ("enQpmapBlockType", AX_S32),
        ("enQpmapBlockUnit", AX_S32)
    ]
    field_aliases = {
        "enCtbRcMode": "ctb_rc_mode",
        "enQpmapQpType": "qpmap_qp_type",
        "enQpmapBlockType": "qpmap_block_type",
        "enQpmapBlockUnit": "qpmap_block_unit"
    }


AX_VENC_VBR_QUALITY_LEVEL_E = AX_S32
"""
    Quality level definition of VBR

    .. parsed-literal::

        AX_VENC_VBR_QUALITY_LEVEL_INV  = 0
        AX_VENC_VBR_QUALITY_LEVEL_0    = 1
        AX_VENC_VBR_QUALITY_LEVEL_1    = 2
        AX_VENC_VBR_QUALITY_LEVEL_2    = 3
        AX_VENC_VBR_QUALITY_LEVEL_3    = 4
        AX_VENC_VBR_QUALITY_LEVEL_4    = 5
        AX_VENC_VBR_QUALITY_LEVEL_5    = 6
        AX_VENC_VBR_QUALITY_LEVEL_6    = 7
        AX_VENC_VBR_QUALITY_LEVEL_7    = 8
        AX_VENC_VBR_QUALITY_LEVEL_8    = 9
        AX_VENC_VBR_QUALITY_LEVEL_BUTT = 10
"""
AX_VENC_VBR_QUALITY_LEVEL_INV = 0
AX_VENC_VBR_QUALITY_LEVEL_0 = 1
AX_VENC_VBR_QUALITY_LEVEL_1 = 2
AX_VENC_VBR_QUALITY_LEVEL_2 = 3
AX_VENC_VBR_QUALITY_LEVEL_3 = 4
AX_VENC_VBR_QUALITY_LEVEL_4 = 5
AX_VENC_VBR_QUALITY_LEVEL_5 = 6
AX_VENC_VBR_QUALITY_LEVEL_6 = 7
AX_VENC_VBR_QUALITY_LEVEL_7 = 8
AX_VENC_VBR_QUALITY_LEVEL_8 = 9
AX_VENC_VBR_QUALITY_LEVEL_BUTT = 10


class AX_VENC_H264_CBR_T(BaseStructure):
    """
    CBR parameters

    .. parsed-literal::

        dict_venc_h264_cbr = {
            "gop": int,
            "start_time": int,
            "bitrate": int,
            "max_qp": int,
            "min_qp": int,
            "max_iqp": int,
            "min_iqp": int,
            "max_iprop": int,
            "min_iprop": int,
            "intra_qp_delta": int,
            "idr_qp_delta_range": int,
            "qpmap_info": :class:`AX_VENC_QPMAP_META_T <axcl.venc.axcl_venc_rc.AX_VENC_QPMAP_META_T>`
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),                     # Range:[1, 65536]; the interval of I Frame.
        ("u32StatTime", AX_U32),                # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32BitRate", AX_U32),                 # average bitrate(kbps)
        ("u32MaxQp", AX_U32),                   # Range:[0, 51]; the max QP value
        ("u32MinQp", AX_U32),                   # Range:[0, 51]; the min QP value
        ("u32MaxIQp", AX_U32),                  # Range:[0, 51]; the max I qp
        ("u32MinIQp", AX_U32),                  # Range:[0, 51]; the min I qp
        ("u32MaxIprop", AX_U32),                # Range:[1, 100]; the max I P size ratio
        ("u32MinIprop", AX_U32),                # Range:[1, u32MaxIprop]; the min I P size ratio
        ("s32IntraQpDelta", AX_S32),            # Range:[-51, 51]; QP difference between target QP and intra frame QP
        ("u32IdrQpDeltaRange", AX_U32),         # Range:[2, 10]; QP rang between CU QP and I frame QP
        ("stQpmapInfo", AX_VENC_QPMAP_META_T)   # Qpmap related info
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32StatTime": "start_time",
        "u32BitRate": "bitrate",
        "u32MaxQp": "max_qp",
        "u32MinQp": "min_qp",
        "u32MaxIQp": "max_iqp",
        "u32MinIQp": "min_iqp",
        "u32MaxIprop": "max_iprop",
        "u32MinIprop": "min_iprop",
        "s32IntraQpDelta": "intra_qp_delta",
        "u32IdrQpDeltaRange": "idr_qp_delta_range",
        "stQpmapInfo": "qpmap_info"
    }


class AX_VENC_H264_VBR_T(BaseStructure):
    """
    VBR parameters.

    .. parsed-literal::

        dict_venc_h264_vbr = {
            "gop": int,
            "stat_time": int,
            "max_bitrate": int,
            "vq": int,
            "max_qp": int,
            "min_qp": int,
            "max_iqp": int,
            "min_iqp": int,
            "intra_qp_delta": int,
            "idr_qp_delta_range": int,
            "qpmap_info": :class:`AX_VENC_QPMAP_META_T <axcl.venc.axcl_venc_rc.AX_VENC_QPMAP_META_T>`,
            "change_pos": int
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),                   # Range:[1, 65536]; the interval of I Frame.
        ("u32StatTime", AX_U32),              # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32MaxBitRate", AX_U32),            # the max bitrate(kbps)
        ("enVQ", AX_S32),                     # AX_VENC_VBR_QUALITY_LEVEL_E
        ("u32MaxQp", AX_U32),                 # Range:[0, 51]; the max QP value
        ("u32MinQp", AX_U32),                 # Range:[0, 51]; the min QP value
        ("u32MaxIQp", AX_U32),                # Range:[0, 51]; the max I qp
        ("u32MinIQp", AX_U32),                # Range:[0, 51]; the min I qp
        ("s32IntraQpDelta", AX_S32),          # Range:[-51, 51]; QP difference between target QP and intra frame QP
        ("u32IdrQpDeltaRange", AX_U32),       # Range:[2, 10]; QP rang between CU QP and I frame QP
        ("stQpmapInfo", AX_VENC_QPMAP_META_T),# Qpmap related info
        ("u32ChangePos", AX_U32)              # Range:[20, 100]
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32StatTime": "stat_time",
        "u32MaxBitRate": "max_bitrate",
        "enVQ": "vq",
        "u32MaxQp": "max_qp",
        "u32MinQp": "min_qp",
        "u32MaxIQp": "max_iqp",
        "u32MinIQp": "min_iqp",
        "s32IntraQpDelta": "intra_qp_delta",
        "u32IdrQpDeltaRange": "idr_qp_delta_range",
        "stQpmapInfo": "qpmap_info",
        "u32ChangePos": "change_pos"
    }


class AX_VENC_H264_CVBR_T(BaseStructure):
    """
    CVBR parameters.

    .. parsed-literal::

        dict_venc_h264_cvbr = {
            "gop": int,
            "stat_time": int,
            "max_qp": int,
            "min_qp": int,
            "max_iqp": int,
            "min_iqp": int,
            "min_qp_delta": int,
            "max_qp_delta": int,
            "max_iprop": int,
            "min_iprop": int,
            "max_bitrate": int,
            "short_term_stat_time": int,
            "long_term_stat_time": int,
            "long_term_max_bitrate": int,
            "long_term_min_bitrate": int,
            "qpmap_info": :class:`AX_VENC_QPMAP_META_T <axcl.venc.axcl_venc_rc.AX_VENC_QPMAP_META_T>`,
            "extra_bit_percent": int,
            "long_term_stat_time_unit": int,
            "intra_qp_delta": int,
            "idr_qp_delta_range": int
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),                    # Range:[1, 65536]; the interval of I Frame.
        ("u32StatTime", AX_U32),               # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32MaxQp", AX_U32),                  # Range:[0, 51]; the max QP value
        ("u32MinQp", AX_U32),                  # Range:[0, 51]; the min QP value
        ("u32MaxIQp", AX_U32),                 # Range:[0, 51]; the max I qp
        ("u32MinIQp", AX_U32),                 # Range:[0, 51]; the min I qp
        ("u32MinQpDelta", AX_S32),              # Range:[0, 4];Difference between FrameLevelMinQp and MinQp, FrameLevelMinQp = MinQp(or MinIQp) + MinQpDelta
        ("u32MaxQpDelta", AX_U32),             # Range:[0, 4];Difference between FrameLevelMaxQp and MaxQp, FrameLevelMaxQp = MaxQp(or MaxIQp) - MaxQpDelta
        ("u32MaxIprop", AX_U32),               # Range:[1, 100]; the max I P size ratio
        ("u32MinIprop", AX_U32),               # Range:[1, u32MaxIprop]; the min I P size ratio
        ("u32MaxBitRate", AX_U32),             # the max bitrate, the unit is kbps
        ("u32ShortTermStatTime", AX_U32),      # Range:[1, 120]; the short-term rate statistic time, the unit is second (s)
        ("u32LongTermStatTime", AX_U32),       # Range:[1, 1440]; the long-term rate statistic time, the unit is second (s)
        ("u32LongTermMaxBitrate", AX_U32),     # Range:[2, 614400];the long-term target max bitrate, can not be larger than u32MaxBitRate,the unit is kbps
        ("u32LongTermMinBitrate", AX_U32),     # Range:[0, 614400];the long-term target min bitrate,  can not be larger than u32LongTermMaxBitrate,the unit is kbps
        ("stQpmapInfo", AX_VENC_QPMAP_META_T), # Qpmap related info
        ("u32ExtraBitPercent", AX_U32),        # unsupported
        ("u32LongTermStatTimeUnit", AX_U32),   # unsupported
        ("s32IntraQpDelta", AX_U32),           # Range:[-51, 51];To Alleviate Breath_effect
        ("u32IdrQpDeltaRange", AX_U32)         # Range:[2, 10]; QP rang between CU QP and I frame QP
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32StatTime": "stat_time",
        "u32MaxQp": "max_qp",
        "u32MinQp": "min_qp",
        "u32MaxIQp": "max_iqp",
        "u32MinIQp": "min_iqp",
        "u32MinQpDelta": "min_qp_delta",
        "u32MaxQpDelta": "max_qp_delta",
        "u32MaxIprop": "max_iprop",
        "u32MinIprop": "min_iprop",
        "u32MaxBitRate": "max_bitrate",
        "u32ShortTermStatTime": "short_term_stat_time",
        "u32LongTermStatTime": "long_term_stat_time",
        "u32LongTermMaxBitrate": "long_term_max_bitrate",
        "u32LongTermMinBitrate": "long_term_min_bitrate",
        "stQpmapInfo": "qpmap_info",
        "u32ExtraBitPercent": "extra_bit_percent",
        "u32LongTermStatTimeUnit": "long_term_stat_time_unit",
        "s32IntraQpDelta": "intra_qp_delta",
        "u32IdrQpDeltaRange": "idr_qp_delta_range"
    }


class AX_VENC_H264_AVBR_T(BaseStructure):
    """
    AVBR parameters.

    .. parsed-literal::

        dict_venc_h264_avbr = {
            "gop": int,
            "stat_time": int,
            "max_bitrate": int,
            "max_qp": int,
            "min_qp": int,
            "max_iqp": int,
            "min_iqp": int,
            "intra_qp_delta": int,
            "idr_qp_delta_range": int,
            "qpmap_info": :class:`AX_VENC_QPMAP_META_T <axcl.venc.axcl_venc_rc.AX_VENC_QPMAP_META_T>`,
            "change_pos": int,
            "min_still_percent": int,
            "max_still_qp": int
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),                     # Range:[1, 65536]; the interval of ISLICE.
        ("u32StatTime", AX_U32),                # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32MaxBitRate", AX_U32),              # the max bitrate, the unit is kbps
        ("u32MaxQp", AX_U32),                   # Range:[0, 51]; the max QP value
        ("u32MinQp", AX_U32),                   # Range:[0, 51]; the min QP value
        ("u32MaxIQp", AX_U32),                  # Rangeb:[0, 51]; the max I qp
        ("u32MinIQp", AX_U32),                  # Range:[0, 51]; the min I qp
        ("s32IntraQpDelta", AX_S32),            # Range:[-51, 51]; QP difference between target QP and intra frame QP
        ("u32IdrQpDeltaRange", AX_U32),         # Range:[2, 10]; QP rang between CU QP and I frame QP
        ("stQpmapInfo", AX_VENC_QPMAP_META_T),  # Qpmap related info
        ("u32ChangePos", AX_U32),               # Range:[20, 100]
        ("u32MinStillPercent", AX_U32),         # Range:[10, 100]
        ("u32MaxStillQp", AX_U32)               # Range:[u32MinIQp, u32MaxIQp]; def 36
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32StatTime": "stat_time",
        "u32MaxBitRate": "max_bitrate",
        "u32MaxQp": "max_qp",
        "u32MinQp": "min_qp",
        "u32MaxIQp": "max_iqp",
        "u32MinIQp": "min_iqp",
        "s32IntraQpDelta": "intra_qp_delta",
        "u32IdrQpDeltaRange": "idr_qp_delta_range",
        "stQpmapInfo": "qpmap_info",
        "u32ChangePos": "change_pos",
        "u32MinStillPercent": "min_still_percent",
        "u32MaxStillQp": "max_still_qp"
    }


class AX_VENC_H264_FIXQP_T(BaseStructure):
    """
    Fix QP parameters.

    .. parsed-literal::

        dict_venc_h264_fixqp = {
            "gop": int,
            "iqp": int,
            "pqp": int,
            "bqp": int
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),     # Range:[1, 65536]; the interval of ISLICE.
        ("u32IQp", AX_U32),     # Range:[0, 51]; qp of the i frame
        ("u32PQp", AX_U32),     # Range:[0, 51]; qp of the p frame
        ("u32BQp", AX_U32)      # Range:[0, 51]; qp of the b frame
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32IQp": "iqp",
        "u32PQp": "pqp",
        "u32BQp": "bqp"
    }


class AX_VENC_H264_QPMAP_T(BaseStructure):
    """
    H264 QP map parameters.

    .. parsed-literal::

        dict_venc_h264_qpmap = {
            "gop": int,
            "stat_time": int,
            "target_bitrate": int,
            "qpmap_info": :class:`AX_VENC_QPMAP_META_T <axcl.venc.axcl_venc_rc.AX_VENC_QPMAP_META_T>`
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),                     # Range:[1, 65536]; the interval of ISLICE.
        ("u32StatTime", AX_U32),                # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32TargetBitRate", AX_U32),           # the target bitrate, the unit is kbps
        ("stQpmapInfo", AX_VENC_QPMAP_META_T)   # Qpmap related info
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32StatTime": "stat_time",
        "u32TargetBitRate": "target_bitrate",
        "stQpmapInfo": "qpmap_info"
    }


class AX_VENC_H264_QVBR_T(BaseStructure):
    """
    QVBR parameters.

    .. parsed-literal::

        dict_venc_h264_qvbr = {
            "gop": int,
            "stat_time": int,
            "target_bitrate": int
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),           # Range:[1, 65536];the interval of ISLICE.
        ("u32StatTime", AX_U32),      # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32TargetBitRate", AX_U32)  # the target bitrate, the unit is kbps
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32StatTime": "stat_time",
        "u32TargetBitRate": "target_bitrate"
    }


class AX_VENC_H265_QPMAP_T(BaseStructure):
    """
    H265 QP map parameters.

    .. parsed-literal::

        dict_venc_h265_qpmap = {
            "gop": int,
            "stat_time": int,
            "target_bitrate": int,
            "qpmap_info": :class:`AX_VENC_QPMAP_META_T <axcl.venc.axcl_venc_rc.AX_VENC_QPMAP_META_T>`
        }
    """
    _fields_ = [
        ("u32Gop", AX_U32),                     # Range:[1, 65536]; the interval of ISLICE.
        ("u32StatTime", AX_U32),                # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32TargetBitRate", AX_U32),           # the target bitrate, the unit is kbps
        ("stQpmapInfo", AX_VENC_QPMAP_META_T)   # Qpmap related info
    ]
    field_aliases = {
        "u32Gop": "gop",
        "u32StatTime": "stat_time",
        "u32TargetBitRate": "target_bitrate",
        "stQpmapInfo": "qpmap_info"
    }


AX_VENC_H265_CBR_T = AX_VENC_H264_CBR_T
AX_VENC_H265_VBR_T = AX_VENC_H264_VBR_T
AX_VENC_H265_AVBR_T = AX_VENC_H264_AVBR_T
AX_VENC_H265_FIXQP_T = AX_VENC_H264_FIXQP_T
AX_VENC_H265_QVBR_T = AX_VENC_H264_QVBR_T
AX_VENC_H265_CVBR_T = AX_VENC_H264_CVBR_T


class AX_VENC_MJPEG_FIXQP_T(BaseStructure):
    """
    MJPEG fix QP parameters.

    .. parsed-literal::

        dict_venc_mjpeg_fixqp = {
            "fixed_qp": int
        }
    """
    _fields_ = [
        # Range:[-1, 51]; Fixed qp for every frame.
        # -1: disable fixed qp mode.
        # [0, 51]: value of fixed qp.
        ("s32FixedQp", AX_S32)
    ]
    field_aliases = {
        "s32FixedQp": "fixed_qp"
    }


class AX_VENC_MJPEG_CBR_T(BaseStructure):
    """
    MJPEG CBR parameters.

    .. parsed-literal::

        dict_venc_mjpeg_cbr = {
            "stat_time": int,
            "bitrate": int,
            "max_qp": int,
            "min_qp": int
        }
    """
    _fields_ = [
        ("u32StatTime", AX_U32),   # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32BitRate", AX_U32),    # average bitrate ,the unit is kbps*/
        ("u32MaxQp", AX_U32),      # Range:[0, 51]; the max Qfactor value*/
        ("u32MinQp", AX_U32)       # Range:[0, 51]; the min Qfactor value ,can not be larger than u32MaxQfactor
    ]
    field_aliases = {
        "u32StatTime": "stat_time",
        "u32BitRate": "bitrate",
        "u32MaxQp": "max_qp",
        "u32MinQp": "min_qp"
    }


class AX_VENC_MJPEG_VBR_T(BaseStructure):
    """
    MJPEG VBR parameters.

    .. parsed-literal::

        dict_venc_mjpeg_vbr = {
            "stat_time": int,
            "max_bitrate": int,
            "max_qp": int,
            "min_qp": int
        }
    """
    _fields_ = [
        ("u32StatTime", AX_U32),   # Range:[1, 60]; the rate statistic time, the unit is senconds(s)
        ("u32MaxBitRate", AX_U32), # the max bitrate ,the unit is kbps*/
        ("u32MaxQp", AX_U32),      # Range:[0, 51]; max image quailty allowed
        ("u32MinQp", AX_U32)      # Range:[0, 51]; min image quality allowed ,can not be larger than u32MaxQfactor*/
    ]
    field_aliases = {
        "u32StatTime": "stat_time",
        "u32MaxBitRate": "max_bitrate",
        "u32MaxQp": "max_qp",
        "u32MinQp": "min_qp"
    }


class AX_VENC_RC_ATTR_U(BaseUnion):
    """
    RC definition.

    .. parsed-literal::

        dict_venc_rc_attr_u = {
            "h264_cbr_rc_attr": :class:`AX_VENC_H264_CBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_CBR_T>`,
            "h264_vbr_rc_attr": :class:`AX_VENC_H264_VBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_VBR_T>`,
            "h264_avbr_rc_attr": :class:`AX_VENC_H264_AVBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_AVBR_T>`,
            "h264_qvbr_rc_attr": :class:`AX_VENC_H264_QVBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_QVBR_T>`,
            "h264_cvbr_rc_attr": :class:`AX_VENC_H264_CVBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_CVBR_T>`,
            "h264_fix_qp_rc_attr": :class:`AX_VENC_H264_FIXQP_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_FIXQP_T>`,
            "h264_qp_map_rc_attr": :class:`AX_VENC_H264_QPMAP_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_QPMAP_T>`,
            "h265_cbr_rc_attr": :class:`AX_VENC_H265_CBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_CBR_T>`,
            "h265_vbr_rc_attr": :class:`AX_VENC_H265_VBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_VBR_T>`,
            "h265_avbr_rc_attr": :class:`AX_VENC_H265_AVBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_AVBR_T>`,
            "h265_qvbr_rc_attr": :class:`AX_VENC_H265_QVBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_QVBR_T>`,
            "h265_cvbr_rc_attr": :class:`AX_VENC_H265_CVBR_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_CVBR_T>`,
            "h265_fix_qp_rc_attr": :class:`AX_VENC_H265_FIXQP_T <axcl.venc.axcl_venc_rc.AX_VENC_H264_FIXQP_T>`,
            "h265_qp_map_rc_attr": :class:`AX_VENC_H265_QPMAP_T <axcl.venc.axcl_venc_rc.AX_VENC_H265_QPMAP_T>`,
            "mjpeg_cbr_rc_attr": :class:`AX_VENC_MJPEG_CBR_T <axcl.venc.axcl_venc_rc.AX_VENC_MJPEG_CBR_T>`,
            "mjpeg_vbr_rc_attr": :class:`AX_VENC_MJPEG_VBR_T <axcl.venc.axcl_venc_rc.AX_VENC_MJPEG_VBR_T>`,
            "mjpeg_fix_qp_rc_attr": :class:`AX_VENC_MJPEG_FIXQP_T <axcl.venc.axcl_venc_rc.AX_VENC_MJPEG_FIXQP_T>`
        }
    """
    _fields_ = [
        ("stH264Cbr", AX_VENC_H264_CBR_T),
        ("stH264Vbr", AX_VENC_H264_VBR_T),
        ("stH264AVbr", AX_VENC_H264_AVBR_T),
        ("stH264QVbr", AX_VENC_H264_QVBR_T),
        ("stH264CVbr", AX_VENC_H264_CVBR_T),
        ("stH264FixQp", AX_VENC_H264_FIXQP_T),
        ("stH264QpMap", AX_VENC_H264_QPMAP_T),
        ("stH265Cbr", AX_VENC_H265_CBR_T),
        ("stH265Vbr", AX_VENC_H265_VBR_T),
        ("stH265AVbr", AX_VENC_H265_AVBR_T),
        ("stH265QVbr", AX_VENC_H265_QVBR_T),
        ("stH265CVbr", AX_VENC_H265_CVBR_T),
        ("stH265FixQp", AX_VENC_H265_FIXQP_T),
        ("stH265QpMap", AX_VENC_H265_QPMAP_T),
        ("stMjpegCbr", AX_VENC_MJPEG_CBR_T),
        ("stMjpegVbr", AX_VENC_MJPEG_VBR_T),
        ("stMjpegFixQp", AX_VENC_MJPEG_FIXQP_T)
    ]
    field_aliases = {
        "stH264Cbr": "h264_cbr_rc_attr",
        "stH264Vbr": "h264_vbr_rc_attr",
        "stH264AVbr": "h264_avbr_rc_attr",
        "stH264QVbr": "h264_qvbr_rc_attr",
        "stH264CVbr": "h264_cvbr_rc_attr",
        "stH264FixQp": "h264_fix_qp_rc_attr",
        "stH264QpMap": "h264_qp_map_rc_attr",
        "stH265Cbr": "h265_cbr_rc_attr",
        "stH265Vbr": "h265_vbr_rc_attr",
        "stH265AVbr": "h265_avbr_rc_attr",
        "stH265QVbr": "h265_qvbr_rc_attr",
        "stH265CVbr": "h265_cvbr_rc_attr",
        "stH265FixQp": "h265_fix_qp_rc_attr",
        "stH265QpMap": "h265_qp_map_rc_attr",
        "stMjpegCbr": "mjpeg_cbr_rc_attr",
        "stMjpegVbr": "mjpeg_vbr_rc_attr",
        "stMjpegFixQp": "mjpeg_fix_qp_rc_attr"
    }
    value_union_type_mapping = {
        AX_VENC_RC_MODE_H264CBR: "stH264Cbr",
        AX_VENC_RC_MODE_H264VBR: "stH264Vbr",
        AX_VENC_RC_MODE_H264AVBR: "stH264AVbr",
        AX_VENC_RC_MODE_H264QVBR: "stH264QVbr",
        AX_VENC_RC_MODE_H264CVBR: "stH264CVbr",
        AX_VENC_RC_MODE_H264FIXQP: "stH264FixQp",
        AX_VENC_RC_MODE_H264QPMAP: "stH264QpMap",
        AX_VENC_RC_MODE_H265CBR: "stH265Cbr",
        AX_VENC_RC_MODE_H265VBR: "stH265Vbr",
        AX_VENC_RC_MODE_H265AVBR: "stH265AVbr",
        AX_VENC_RC_MODE_H265QVBR: "stH265QVbr",
        AX_VENC_RC_MODE_H265CVBR: "stH265CVbr",
        AX_VENC_RC_MODE_H265FIXQP: "stH265FixQp",
        AX_VENC_RC_MODE_H265QPMAP: "stH265QpMap",
        AX_VENC_RC_MODE_MJPEGCBR: "stMjpegCbr",
        AX_VENC_RC_MODE_MJPEGVBR: "stMjpegVbr",
        AX_VENC_RC_MODE_MJPEGFIXQP: "stMjpegFixQp"
    }


class AX_VENC_RC_ATTR_T(BaseStructure):
    """
    RC attribute.

    .. parsed-literal::

        dict_venc_rc_attr = {
            "rc_mode": :class:`AX_VENC_RC_MODE_E <axcl.venc.axcl_venc_rc.AX_VENC_RC_MODE_E>`,
            "first_frame_start_qp": int,
            "frame_rate": :class:`AX_FRAME_RATE_CTRL_T <axcl.ax_global_type.AX_FRAME_RATE_CTRL_T>`,
            "attr": :class:`AX_VENC_RC_ATTR_U <axcl.venc.axcl_venc_rc.AX_VENC_RC_ATTR_U>`
        }
    """
    _fields_ = [
        ("enRcMode", AX_VENC_RC_MODE_E),
        ("s32FirstFrameStartQp", AX_S32),       # Range[-1, 51]; Start QP value of the first frame.  -1: Encoder calculates initial QP.
        ("stFrameRate", AX_FRAME_RATE_CTRL_T),  # use nSrcFrameRate and nDstFrameRate include in struct.
        ("uAttr", AX_VENC_RC_ATTR_U)
    ]
    field_aliases = {
        "enRcMode": "rc_mode",
        "s32FirstFrameStartQp": "first_frame_start_qp",
        "stFrameRate": "frame_rate",
        "uAttr": "attr"
    }
    name_union_type_mapping = {
        "uAttr": "enRcMode"
    }


class AX_VENC_SCENE_CHANGE_DETECT_T(BaseStructure):
    """
    Scene change detection parameters.

    .. parsed-literal::

        dict_venc_scene_change_detect = {
            "detect_scene_change": bool,
            "adaptive_insert_idr_frame": bool
        }
    """
    _fields_ = [
        ("bDetectSceneChange", AX_BOOL),      # Range:[0, 1]; enable detect scene change.*/
        ("bAdaptiveInsertIDRFrame", AX_BOOL)  # Range:[0, 1]; enable a daptive insertIDR frame.*/
    ]
    field_aliases = {
        "bDetectSceneChange": "detect_scene_change",
        "bAdaptiveInsertIDRFrame": "adaptive_insert_idr_frame"
    }


class AX_VENC_RC_PARAM_T(BaseStructure):
    """
    RC parameters.

    .. parsed-literal::

        dict_venc_rc_param = {
            "row_qp_delta": int,
            "first_frame_start_qp": int,
            "scene_change_detect": :class:`AX_VENC_SCENE_CHANGE_DETECT_T <axcl.venc.axcl_venc_rc.AX_VENC_SCENE_CHANGE_DETECT_T>`,
            "rc_mode": :class:`AX_VENC_RC_MODE_E <axcl.venc.axcl_venc_rc.AX_VENC_RC_MODE_E>`,
            "frame_rate": :class:`AX_FRAME_RATE_CTRL_T <axcl.ax_global_type.AX_FRAME_RATE_CTRL_T>`,
            "attr": :class:`AX_VENC_RC_ATTR_U <axcl.venc.axcl_venc_rc.AX_VENC_RC_ATTR_U>`
        }
    """
    _fields_ = [
        ("u32RowQpDelta", AX_U32),          # Range:[0, 10];the start QP value of each macroblock row relative to the start QP value
        ("s32FirstFrameStartQp", AX_S32),   # Range:[-1, 51];Start QP value of the first frame*/
        ("stSceneChangeDetect", AX_VENC_SCENE_CHANGE_DETECT_T),
        ("enRcMode", AX_VENC_RC_MODE_E),
        ("stFrameRate", AX_FRAME_RATE_CTRL_T),
        ("uAttr", AX_VENC_RC_ATTR_U)
    ]
    field_aliases = {
        "u32RowQpDelta": "row_qp_delta",
        "s32FirstFrameStartQp": "first_frame_start_qp",
        "stSceneChangeDetect": "scene_change_detect",
        "enRcMode": "rc_mode",
        "stFrameRate": "frame_rate",
        "uAttr": "attr"
    }
    name_union_type_mapping = {
        "uAttr": "enRcMode"
    }


AX_VENC_DROPFRAME_MODE_E = AX_S32
"""
    Drop frame mode definition.

    .. parsed-literal::

        AX_VENC_DROPFRM_NORMAL = 0    # normal mode
        AX_VENC_DROPFRM_PSKIP  = 1    # pskip
        AX_VENC_DROPFRM_BUTT   = 2
"""
AX_VENC_DROPFRM_NORMAL = 0  # normal mode
AX_VENC_DROPFRM_PSKIP = 1   # pskip
AX_VENC_DROPFRM_BUTT = 2


class AX_VENC_RATE_JAM_CFG_T(BaseStructure):
    """
    Bitrate jam configuration parameters.

    .. parsed-literal::

        dict_venc_rate_jam_cfg = {
            "drop_frm_en": bool,
            "drop_frm_thr_bps": int,
            "drop_frm_mode": :class:`AX_VENC_DROPFRAME_MODE_E <axcl.venc.axcl_venc_rc.AX_VENC_DROPFRAME_MODE_E>`,
            "enc_frm_gaps": int
        }
    """
    _fields_ = [
        ("bDropFrmEn", AX_BOOL),                        # Range:[0,1];Indicates whether to enable rate jam stragety
        ("u32DropFrmThrBps", AX_U32),                   # Range:[64k, 163840k];the instant bit rate threshold
        ("enDropFrmMode", AX_VENC_DROPFRAME_MODE_E),    # drop frame mode
        ("u32EncFrmGaps", AX_U32)                       # Range:[0, 65535]; the continue frame numbers to do rate jam stragegy
    ]
    field_aliases = {
        "bDropFrmEn": "drop_frm_en",
        "u32DropFrmThrBps": "drop_frm_thr_bps",
        "enDropFrmMode": "drop_frm_mode",
        "u32EncFrmGaps": "enc_frm_gaps"
    }


AX_VENC_RC_PRIORITY_E = AX_S32
"""
    RC priority definition.

    .. parsed-literal::

        AX_VENC_RC_PRIORITY_FRAMEBITS_FIRST = 0    # framebits first
        AX_VENC_RC_PRIORITY_BITRATE_FIRST   = 1    # bitrate first
        AX_VENC_RC_PRIORITY_BUTT            = 2
"""
AX_VENC_RC_PRIORITY_FRAMEBITS_FIRST = 0  # framebits first
AX_VENC_RC_PRIORITY_BITRATE_FIRST = 1    # bitrate first
AX_VENC_RC_PRIORITY_BUTT = 2


class AX_VENC_SUPERFRAME_CFG_T(BaseStructure):
    """
    Super frame configuration.

    .. parsed-literal::

        dict_venc_superframe_cfg = {
            "strategy_en": bool,
            "super_i_frm_bits_thr": int,
            "super_p_frm_bits_thr": int,
            "super_b_frm_bits_thr": int,
            "rc_priority": :class:`AX_VENC_RC_PRIORITY_E <axcl.venc.axcl_venc_rc.AX_VENC_RC_PRIORITY_E>`
        }
    """
    _fields_ = [
        ("bStrategyEn", AX_BOOL),               # super frame strategy enable
        ("u32SuperIFrmBitsThr", AX_U32),        # Range:[0, 4294967295];Indicate the threshold of the super I frame for enabling the super frame processing mode
        ("u32SuperPFrmBitsThr", AX_U32),        # Range:[0, 4294967295];Indicate the threshold of the super P frame for enabling the super frame processing mode
        ("u32SuperBFrmBitsThr", AX_U32),        # Range:[0, 4294967295];Indicate the threshold of the super B frame for enabling the super frame processing mode
        ("enRcPriority", AX_VENC_RC_PRIORITY_E) # rate control priority
    ]
    field_aliases = {
        "bStrategyEn": "strategy_en",
        "u32SuperIFrmBitsThr": "super_i_frm_bits_thr",
        "u32SuperPFrmBitsThr": "super_p_frm_bits_thr",
        "u32SuperBFrmBitsThr": "super_b_frm_bits_thr",
        "enRcPriority": "rc_priority"
    }
