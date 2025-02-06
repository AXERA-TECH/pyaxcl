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

from axcl.ax_global_type import *
from axcl.ax_codec_comm import *
from axcl.venc.axcl_venc_rc import *
from axcl.venc.axcl_venc_exif import *
from axcl.utils.axcl_logger import *
from axcl.utils.axcl_basestructure import *

VENC_QP_HISGRM_NUM = 52

MAX_VENC_CHN_NUM = 64

MAX_VENC_GRP_NUM = MAX_VENC_CHN_NUM // 2

MAX_VENC_ROI_NUM = 8
MAX_JENC_ROI_NUM = 8

VENC_MAX_NALU_NUM = 64

MIN_VENC_PIC_WIDTH = 128
MAX_VENC_PIC_WIDTH = 8192

MIN_VENC_PIC_HEIGHT = 128
MAX_VENC_PIC_HEIGHT = 8192

MIN_JENC_PIC_WIDTH = 32
MAX_JENC_PIC_WIDTH = 32768

MIN_JENC_PIC_HEIGHT = 32
MAX_JENC_PIC_HEIGHT = 32768

MIN_JENC_ROI_BLOCK_WIDTH = 16
MIN_JENC_ROI_BLOCK_HEIGHT = 16

MIN_JENC_QFACTOR = 1
MAX_JENC_QFACTOR = 99

MAX_VENC_USER_DATA_SIZE = 2048
MAX_JENC_USER_DATA_SIZE = 4096

VENC_CHN = AX_S32
VENC_GRP = AX_S32

# define for AX_VENC_ATTR_T::flag
AX_VENC_CHN_FLAGS_E = AX_S32
"""
    Channel flag attribute.

    .. parsed-literal::

        AX_VENC_FLAGS_NONE           = 0
        AX_VENC_CHN_ENABLE_MULTICORE = (1 << 0)     # enable multi-core
        AX_VENC_STREAM_CACHED        = (1 << 1)     # output cached stream
        AX_VENC_HEADER_ATTACH_TO_PB  = (1 << 2)     # insert sps/pps before I/P for h265 encoding
        AX_VENC_FLAGS_BUTT           = AX_VENC_HEADER_ATTACH_TO_PB + 1
"""
AX_VENC_FLAGS_NONE = 0
AX_VENC_CHN_ENABLE_MULTICORE = (1 << 0)
AX_VENC_STREAM_CACHED = (1 << 1)
AX_VENC_HEADER_ATTACH_TO_PB = (1 << 2)
AX_VENC_FLAGS_BUTT = AX_VENC_HEADER_ATTACH_TO_PB + 1

AX_VENC_LINK_MODE_E = AX_S32
"""
    Link or unlink mode for inputting frame.

    .. parsed-literal::

        AX_VENC_LINK_MODE   = 0     # link mode
        AX_VENC_UNLINK_MODE = 1     # unlink mode, invoke :func:`send_frame <axcl.venc.axcl_venc.send_frame>` to send frame manually.
"""
AX_VENC_LINK_MODE = 0
AX_VENC_UNLINK_MODE = 1


class AX_VENC_ATTR_H264_T(BaseStructure):
    """
    Attribute of h264 encoding.

    .. parsed-literal::

        dict_venc_attr_h264 = {
            "rcn_ref_share_buf": bool
        }
    """
    _fields_ = [
        ("bRcnRefShareBuf", AX_BOOL)  # Range:[0, 1]; Whether to enable the Share Buf of Rcn and Ref .
    ]
    field_aliases = {
        "bRcnRefShareBuf": "rcn_ref_share_buf"
    }


class AX_VENC_ATTR_H265_T(BaseStructure):
    """
    Attribute of h265 encoding.

    .. parsed-literal::

        dict_venc_attr_h265 = {
            "rcn_ref_share_buf": bool
        }
    """
    _fields_ = [
        ("bRcnRefShareBuf", AX_BOOL)  # Range:[0, 1]; Whether to enable the Share Buf of Rcn and Ref .
    ]
    field_aliases = {
        "bRcnRefShareBuf": "rcn_ref_share_buf"
    }


class AX_RECT_T(BaseStructure):
    """
    Rectangle definition.

    .. parsed-literal::

        dict_rect = {
            "x": int,
            "y": int,
            "width": int,
            "height": int
        }
    """
    _fields_ = [
        ("u32X", AX_U32),
        ("u32Y", AX_U32),
        ("u32Width", AX_U32),
        ("u32Height", AX_U32)
    ]
    field_aliases = {
        "u32X": "x",
        "u32Y": "y",
        "u32Width": "width",
        "u32Height": "height"
    }


class AX_VENC_JPEG_PARAM_T(BaseStructure):
    """
    JPEG parameters.

    .. parsed-literal::

        dict_venc_jpeg_param = {
            "q_factor": int,
            "y_qt": [int],
            "cbcr_qt": [int],
            "enable_roi": bool,
            "save_non_roi_qt": bool,
            "roi_q_factor": int,
            "roi_yqt": [int],
            "roi_cbcr_qt": [int],
            "enable": [bool],
            "roi_area": [:class:`AX_RECT_T <axcl.venc.axcl_venc_comm.AX_RECT_T>`],
            "mcu_per_ecs": int,
            "dblk_enable": bool
        }
    """
    _fields_ = [
        ("u32Qfactor", AX_U32),  # RW; Range:[1,99]; Qfactor value
        ("u8YQt", AX_U8 * 64),  # RW; Range:[1, 255]; Y quantization table
        ("u8CbCrQt", AX_U8 * 64),  # RW; Range:[1, 255]; CbCr quantization table
        ("bEnableRoi", AX_BOOL),  # RW; Range:[0, 1]; 0: Whether want to do ROI configuration
        ("bSaveNonRoiQt", AX_BOOL),  # RW; Range:[0, 1]; Which quantization table to save between RoiQt and nonRoiQt.
        ("u32RoiQfactor", AX_U32),  # RW; Range:[1,99]; Qfactor value
        ("u8RoiYQt", AX_U8 * 64),  # RW; Range:[1, 255]; Y quantization table
        ("u8RoiCbCrQt", AX_U8 * 64),  # RW; Range:[1, 255]; CbCr quantization table
        ("bEnable", AX_BOOL * MAX_VENC_ROI_NUM),  # RW; Range:[0, 1]; Whether to enable this ROI
        ("stRoiArea", AX_RECT_T * MAX_VENC_ROI_NUM),  # RW; Region of an ROI
        ("u32MCUPerECS", AX_U32),
        # RW; the max MCU number is (picwidth + 15) >> 4 x (picheight + 15) >> 4 x 2]; MCU number of one ECS
        ("bDblkEnable", AX_BOOL),  # JPEG AX_TRUE: enable Deblock;AX_FALSE: disable Deblock.
    ]
    field_aliases = {
        "u32Qfactor": "q_factor",
        "u8YQt": "y_qt",
        "u8CbCrQt": "cbcr_qt",
        "bEnableRoi": "enable_roi",
        "bSaveNonRoiQt": "save_non_roi_qt",
        "u32RoiQfactor": "roi_q_factor",
        "u8RoiYQt": "roi_yqt",
        "u8RoiCbCrQt": "roi_cbcr_qt",
        "bEnable": "enable",
        "stRoiArea": "roi_area",
        "u32MCUPerECS": "mcu_per_ecs",
        "bDblkEnable": "dblk_enable"
    }


class AX_VENC_MJPEG_PARAM_T(BaseStructure):
    """
    .. parsed-literal::

        dict_venc_mjpeg_param = {
            "y_qt": [int],
            "cb_qt": [int],
            "cr_qt": [int],
            "mcu_per_ecs": int
        }
    """
    _fields_ = [
        ("u8YQt", AX_U8 * 64),  # Range:[1, 255]; Y quantization table
        ("u8CbQt", AX_U8 * 64),  # Range:[1, 255]; Cb quantization table
        ("u8CrQt", AX_U8 * 64),  # Range:[1, 255]; Cr quantization table
        ("u32MCUPerECS", AX_U32)
        # the max MCU number is (picwidth + 15) >> 4 x (picheight + 15) >> 4 x 2]; MCU number of one ECS
    ]
    field_aliases = {
        "u8YQt": "y_qt",
        "u8CbQt": "cb_qt",
        "u8CrQt": "cr_qt",
        "u32MCUPerECS": "mcu_per_ecs"
    }


class AX_RES_SIZE_T(BaseStructure):
    """
    .. parsed-literal::

        dict_res_size = {
            "width": int,
            "height": int
        }
    """
    _fields_ = [
        ("u32Width", AX_U32),
        ("u32Height", AX_U32),
    ]
    field_aliases = {
        "u32Width": "width",
        "u32Height": "height"
    }


class AX_VENC_MPF_CFG_T(BaseStructure):
    """
    .. parsed-literal::

        dict_venc_mpf_cfg = {
            "large_thumb_nail_num": int,
            "large_thumb_nail_size": [:class:`AX_RES_SIZE_T <axcl.venc.axcl_venc_comm.AX_RES_SIZE_T>`]
        }
    """
    _fields_ = [
        ("u8LargeThumbNailNum", AX_U8),  # Range:[0,2]; the large thumbnail pic num of the MPF
        ("astLargeThumbNailSize", AX_RES_SIZE_T * 2),  # The resolution of large ThumbNail
    ]
    field_aliases = {
        "u8LargeThumbNailNum": "large_thumb_nail_num",
        "astLargeThumbNailSize": "large_thumb_nail_size"
    }


AX_VENC_PIC_RECEIVE_MODE_E = AX_S32
"""
    venc pic receive mode

    .. parsed-literal::

        AX_VENC_PIC_RECEIVE_SINGLE = 0    # single frame mode.
        AX_VENC_PIC_RECEIVE_MULTI  = 1    # multi slice mode
        AX_VENC_PIC_RECEIVE_BUTT   = 2
"""
AX_VENC_PIC_RECEIVE_SINGLE = 0  # single frame mode.
AX_VENC_PIC_RECEIVE_MULTI = 1  # multi slice mode
AX_VENC_PIC_RECEIVE_BUTT = 2


class AX_VENC_ATTR_JPEG_T(BaseStructure):
    """
    .. parsed-literal::

        dict_venc_attr_jpeg = {

        }
    """
    _fields_ = [
    ]
    field_aliases = {
    }


class AX_VENC_ATTR_MJPEG_T(BaseStructure):
    _fields_ = [
    ]
    field_aliases = {
    }


AX_VENC_PROFILE_E = AX_S32
"""
    Profile

    .. parsed-literal::

        AX_VENC_HEVC_MAIN_PROFILE               = 0
        AX_VENC_HEVC_MAIN_STILL_PICTURE_PROFILE = 1
        AX_VENC_HEVC_MAIN_10_PROFILE            = 2
        AX_VENC_HEVC_MAINREXT                   = 3
                                                        # H264 Defination
        AX_VENC_H264_BASE_PROFILE               = 9
        AX_VENC_H264_MAIN_PROFILE               = 10
        AX_VENC_H264_HIGH_PROFILE               = 11
        AX_VENC_H264_HIGH_10_PROFILE            = 12
"""
AX_VENC_HEVC_MAIN_PROFILE = 0
AX_VENC_HEVC_MAIN_STILL_PICTURE_PROFILE = 1
AX_VENC_HEVC_MAIN_10_PROFILE = 2
AX_VENC_HEVC_MAINREXT = 3

# H264 Defination
AX_VENC_H264_BASE_PROFILE = 9
AX_VENC_H264_MAIN_PROFILE = 10
AX_VENC_H264_HIGH_PROFILE = 11
AX_VENC_H264_HIGH_10_PROFILE = 12

# Level for initialization
AX_VENC_LEVEL_E = AX_S32
"""
    Level

    .. parsed-literal::

        AX_VENC_HEVC_LEVEL_1    = 30
        AX_VENC_HEVC_LEVEL_2    = 60
        AX_VENC_HEVC_LEVEL_2_1  = 63
        AX_VENC_HEVC_LEVEL_3    = 90
        AX_VENC_HEVC_LEVEL_3_1  = 93
        AX_VENC_HEVC_LEVEL_4    = 120
        AX_VENC_HEVC_LEVEL_4_1  = 123
        AX_VENC_HEVC_LEVEL_5    = 150
        AX_VENC_HEVC_LEVEL_5_1  = 153
        AX_VENC_HEVC_LEVEL_5_2  = 156
        AX_VENC_HEVC_LEVEL_6    = 180
        AX_VENC_HEVC_LEVEL_6_1  = 183
        AX_VENC_HEVC_LEVEL_6_2  = 186

        AX_VENC_H264_LEVEL_1    = 10
        AX_VENC_H264_LEVEL_1_b  = 99
        AX_VENC_H264_LEVEL_1_1  = 11
        AX_VENC_H264_LEVEL_1_2  = 12
        AX_VENC_H264_LEVEL_1_3  = 13
        AX_VENC_H264_LEVEL_2    = 20
        AX_VENC_H264_LEVEL_2_1  = 21
        AX_VENC_H264_LEVEL_2_2  = 22
        AX_VENC_H264_LEVEL_3    = 30
        AX_VENC_H264_LEVEL_3_1  = 31
        AX_VENC_H264_LEVEL_3_2  = 32
        AX_VENC_H264_LEVEL_4    = 40
        AX_VENC_H264_LEVEL_4_1  = 41
        AX_VENC_H264_LEVEL_4_2  = 42
        AX_VENC_H264_LEVEL_5    = 50
        AX_VENC_H264_LEVEL_5_1  = 51
        AX_VENC_H264_LEVEL_5_2  = 52
        AX_VENC_H264_LEVEL_6    = 60
        AX_VENC_H264_LEVEL_6_1  = 61
        AX_VENC_H264_LEVEL_6_2  = 62
"""
AX_VENC_HEVC_LEVEL_1 = 30
AX_VENC_HEVC_LEVEL_2 = 60
AX_VENC_HEVC_LEVEL_2_1 = 63
AX_VENC_HEVC_LEVEL_3 = 90
AX_VENC_HEVC_LEVEL_3_1 = 93
AX_VENC_HEVC_LEVEL_4 = 120
AX_VENC_HEVC_LEVEL_4_1 = 123
AX_VENC_HEVC_LEVEL_5 = 150
AX_VENC_HEVC_LEVEL_5_1 = 153
AX_VENC_HEVC_LEVEL_5_2 = 156
AX_VENC_HEVC_LEVEL_6 = 180
AX_VENC_HEVC_LEVEL_6_1 = 183
AX_VENC_HEVC_LEVEL_6_2 = 186

# H264 Defination
AX_VENC_H264_LEVEL_1 = 10
AX_VENC_H264_LEVEL_1_b = 99
AX_VENC_H264_LEVEL_1_1 = 11
AX_VENC_H264_LEVEL_1_2 = 12
AX_VENC_H264_LEVEL_1_3 = 13
AX_VENC_H264_LEVEL_2 = 20
AX_VENC_H264_LEVEL_2_1 = 21
AX_VENC_H264_LEVEL_2_2 = 22
AX_VENC_H264_LEVEL_3 = 30
AX_VENC_H264_LEVEL_3_1 = 31
AX_VENC_H264_LEVEL_3_2 = 32
AX_VENC_H264_LEVEL_4 = 40
AX_VENC_H264_LEVEL_4_1 = 41
AX_VENC_H264_LEVEL_4_2 = 42
AX_VENC_H264_LEVEL_5 = 50
AX_VENC_H264_LEVEL_5_1 = 51
AX_VENC_H264_LEVEL_5_2 = 52
AX_VENC_H264_LEVEL_6 = 60
AX_VENC_H264_LEVEL_6_1 = 61
AX_VENC_H264_LEVEL_6_2 = 62

# Tier for initialization
AX_VENC_TIER_E = AX_S32
"""
    H265 tiler.

    .. parsed-literal::

        AX_VENC_HEVC_MAIN_TIER = 0
        AX_VENC_HEVC_HIGH_TIER = 1
"""
AX_VENC_HEVC_MAIN_TIER = 0
AX_VENC_HEVC_HIGH_TIER = 1

AX_VENC_STREAM_BIT_E = AX_S32
"""
    Stream bit

    .. parsed-literal::

        AX_VENC_STREAM_BIT_8  = 0
        AX_VENC_STREAM_BIT_10 = 1
        AX_VENC_STREAM_BUTT   = 2
"""
AX_VENC_STREAM_BIT_8 = 0
AX_VENC_STREAM_BIT_10 = 1
AX_VENC_STREAM_BUTT = 2

AX_VENC_DUMP_TYPE_E = AX_S32
"""
    Dump type.

    .. parsed-literal::

        AX_VENC_DUMP_NONE         = 0
        AX_VENC_DUMP_FRAME        = 1
        AX_VENC_DUMP_STREAM       = 2
        AX_VENC_DUMP_FRAME_STREAM = 3    # dump both frame and stream
"""
AX_VENC_DUMP_NONE = 0
AX_VENC_DUMP_FRAME = 1
AX_VENC_DUMP_STREAM = 2
AX_VENC_DUMP_FRAME_STREAM = 3

AX_VENC_ENCODER_TYPE_E = AX_S32
"""
    Encoder type

    .. parsed-literal::

        AX_VENC_VIDEO_ENCODER = 1    # enable h264/hevc encoder
        AX_VENC_JPEG_ENCODER  = 2    # enable jpeg/mjpeg encoder
        AX_VENC_MULTI_ENCODER = 3    # enable h264/h265/jpeg/mjpeg encoder
"""
AX_VENC_VIDEO_ENCODER = 1  # enable h264/hevc encoder
AX_VENC_JPEG_ENCODER = 2   # enable jpeg/mjpeg encoder
AX_VENC_MULTI_ENCODER = 3  # enable h264/h265/jpeg/mjpeg encoder

AX_VENC_THREAD_SCHED_POLICY_E = AX_S32
"""
    Internal encoding thread schedule type.

    .. parsed-literal::

        AX_VENC_SCHED_OTHER = 0    # default linux time-sharing scheduling
        AX_VENC_SCHED_FIFO  = 3    # First in-first out scheduling
        AX_VENC_SCHED_RR    = 4    # Round-robin scheduling
        AX_VENC_SCHED_BUTT  = 5
"""
AX_VENC_SCHED_OTHER = 0  # default linux time-sharing scheduling
AX_VENC_SCHED_FIFO = 3  # First in-first out scheduling
AX_VENC_SCHED_RR = 4  # Round-robin scheduling
AX_VENC_SCHED_BUTT = 5


class AX_VENC_ENCODE_THREAD_ATTR_T(BaseStructure):
    """
    Internal encoding thread attribute.

    .. parsed-literal::

        dict_venc_encodehread_attr = {
            "explicit_sched": bool,
            "sched_policy": :class:`AX_VENC_THREAD_SCHED_POLICY_E <axcl.venc.axcl_venc_comm.AX_VENC_THREAD_SCHED_POLICY_E>`,
            "sched_priority": int,
            "total_thread_num": int
        }
    """
    _fields_ = [
        # Range:[0, 1]; whether take scheduling attributes from the values specified by the attributes object or not,
        # only true user could change thread policy and priority
        # 0: inherit scheduling attributes from the creating thread,
        # 1: specified by attributes object.
        ("bExplicitSched", AX_BOOL),
        ("enSchedPolicy", AX_VENC_THREAD_SCHED_POLICY_E),  # encode thread sched policy
        ("u32SchedPriority", AX_U32),  # Range:[1, 99]; encode thread scheduling priority
        ("u32TotalThreadNum", AX_U32)  # Range:[1, 9]; thread number of encoding all venc channels
    ]
    field_aliases = {
        "bExplicitSched": "explicit_sched",
        "enSchedPolicy": "sched_policy",
        "u32SchedPriority": "sched_priority",
        "u32TotalThreadNum": "total_thread_num"
    }


class AX_VENC_MOD_ATTR_T(BaseStructure):
    """
    Encoder module attribute.

    .. parsed-literal::

        dict_venc_mod_attr = {
            "venc_type": :class:`AX_VENC_ENCODER_TYPE_E <axcl.venc.axcl_venc_comm.AX_VENC_ENCODER_TYPE_E>`,
            "mod_thd_attr": :class:`AX_VENC_ENCODE_THREAD_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_ENCODE_THREAD_ATTR_T>`
        }
    """
    _fields_ = [
        ("enVencType", AX_VENC_ENCODER_TYPE_E),
        ("stModThdAttr", AX_VENC_ENCODE_THREAD_ATTR_T)
    ]
    field_aliases = {
        "enVencType": "venc_type",
        "stModThdAttr": "mod_thd_attr"
    }


class AX_VENC_USR_DATA_T(BaseStructure):
    """
    User data parameters.

    .. parsed-literal::

        dict_venc_usr_data = {
            "enable": bool,
            "usr_data": int,
            "data_size": int
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),
        ("pu8UsrData", POINTER(AX_U8)),
        ("u32DataSize", AX_U32)
    ]
    field_aliases = {
        "bEnable": "enable",
        "pu8UsrData": "usr_data",
        "u32DataSize": "data_size"
    }


class AX_VENC_RECT_T(BaseStructure):
    """
    Rectangle definition.

    .. parsed-literal::

        dict_venc_rect = {
            "x": int,
            "y": int,
            "width": int,
            "height": int
        }
    """
    _fields_ = [
        ("s32X", AX_S32),
        ("s32Y", AX_S32),
        ("u32Width", AX_U32),
        ("u32Height", AX_U32)
    ]
    field_aliases = {
        "s32X": "x",
        "s32Y": "y",
        "u32Width": "width",
        "u32Height": "height"
    }


class AX_VENC_CROP_INFO_T(BaseStructure):
    """
    Crop information.

    .. parsed-literal::

        dict_venc_crop_info = {
            "enable": int,
            "rect": :class:`AX_VENC_RECT_T <axcl.venc.axcl_venc_comm.AX_VENC_RECT_T>`
        }
    """
    _fields_ = [
        ("bEnable", AX_S32),
        ("stRect", AX_VENC_RECT_T)
    ]
    field_aliases = {
        "bEnable": "enable",
        "stRect": "rect"
    }


class AX_VENC_ATTR_U(BaseUnion):
    """
    Codec attribute.

    .. parsed-literal::

        dict_venc_attr_u = {
            "attr_h264e": :class:`AX_VENC_ATTR_H264_T <axcl.venc.axcl_venc_comm.AX_VENC_ATTR_H264_T>`,
            "attr_h265e": :class:`AX_VENC_ATTR_H265_T <axcl.venc.axcl_venc_comm.AX_VENC_ATTR_H265_T>`,
            "attr_mjpege": :class:`AX_VENC_ATTR_MJPEG_T <axcl.venc.axcl_venc_comm.AX_VENC_ATTR_MJPEG_T>`,
            "attr_jpege": :class:`AX_VENC_ATTR_JPEG_T <axcl.venc.axcl_venc_comm.AX_VENC_ATTR_JPEG_T>`
        }
    """
    _fields_ = [
        ("stAttrH264e", AX_VENC_ATTR_H264_T),
        ("stAttrH265e", AX_VENC_ATTR_H265_T),
        ("stAttrMjpege", AX_VENC_ATTR_MJPEG_T),
        ("stAttrJpege", AX_VENC_ATTR_JPEG_T),
    ]
    field_aliases = {
        "stAttrH264e": "attr_h264e",
        "stAttrH265e": "attr_h265e",
        "stAttrMjpege": "attr_mjpege",
        "stAttrJpege": "attr_jpege"
    }
    value_union_type_mapping = {
        PT_H264: "stAttrH264e",
        PT_H265: "stAttrH265e",
        PT_MJPEG: "stAttrMjpege",
        PT_JPEG: "stAttrJpege",
    }


class AX_VENC_ATTR_T(BaseStructure):
    """
    Encoder attribute.

    .. parsed-literal::

        dict_venc_attr = {
            "type": :class:`AX_PAYLOAD_TYPE_E <axcl.ax_global_type.AX_PAYLOAD_TYPE_E>`,
            "max_pic_width": int,
            "max_pic_height": int,
            "mem_source": :class:`AX_MEMORY_SOURCE_E <axcl.ax_global_type.AX_MEMORY_SOURCE_E>`,
            "buf_size": int,
            "profile": :class:`AX_VENC_PROFILE_E <axcl.venc.axcl_venc_comm.AX_VENC_PROFILE_E>`,
            "level": :class:`AX_VENC_LEVEL_E <axcl.venc.axcl_venc_comm.AX_VENC_LEVEL_E>`,
            "tier": :class:`AX_VENC_TIER_E <axcl.venc.axcl_venc_comm.AX_VENC_TIER_E>`,
            "strm_bit_depth": :class:`AX_VENC_STREAM_BIT_E <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_BIT_E>`,
            "pic_width_src": int,
            "pic_height_src": int,
            "crop_cfg": :class:`AX_VENC_CROP_INFO_T <axcl.venc.axcl_venc_comm.AX_VENC_CROP_INFO_T>`,
            "link_mode": :class:`AX_VENC_LINK_MODE_E <axcl.venc.axcl_venc_comm.AX_VENC_LINK_MODE_E>`,
            "stop_wait_time": int,
            "in_fifo_depth": int,
            "out_fifo_depth": int,
            "flag": int,
            "attr": :class:`AX_VENC_ATTR_U <axcl.venc.axcl_venc_comm.AX_VENC_ATTR_U>`
        }
    """
    _fields_ = [
        ("enType", AX_PAYLOAD_TYPE_E),
        ("u32MaxPicWidth", AX_U32),
        ("u32MaxPicHeight", AX_U32),
        ("enMemSource", AX_MEMORY_SOURCE_E),
        ("u32BufSize", AX_U32),
        ("enProfile", AX_VENC_PROFILE_E),
        ("enLevel", AX_VENC_LEVEL_E),
        ("enTier", AX_VENC_TIER_E),
        ("enStrmBitDepth", AX_VENC_STREAM_BIT_E),
        ("u32PicWidthSrc", AX_U32),
        ("u32PicHeightSrc", AX_U32),
        ("stCropCfg", AX_VENC_CROP_INFO_T),
        ("enLinkMode", AX_VENC_LINK_MODE_E),
        ("s32StopWaitTime", AX_S32),
        ("u8InFifoDepth", AX_U8),
        ("u8OutFifoDepth", AX_U8),
        ("flag", AX_S32),
        ("uAttr", AX_VENC_ATTR_U),
    ]
    field_aliases = {
        "enType": "type",
        "u32MaxPicWidth": "max_pic_width",
        "u32MaxPicHeight": "max_pic_height",
        "enMemSource": "mem_source",
        "u32BufSize": "buf_size",
        "enProfile": "profile",
        "enLevel": "level",
        "enTier": "tier",
        "enStrmBitDepth": "strm_bit_depth",
        "u32PicWidthSrc": "pic_width_src",
        "u32PicHeightSrc": "pic_height_src",
        "stCropCfg": "crop_cfg",
        "enLinkMode": "link_mode",
        "s32StopWaitTime": "stop_wait_time",
        "u8InFifoDepth": "in_fifo_depth",
        "u8OutFifoDepth": "out_fifo_depth",
        "flag": "flag",
        "uAttr": "attr"
    }
    name_union_type_mapping = {
        "uAttr": "enType"
    }


AX_VENC_GOP_MODE_E = AX_S32
"""
    GOP mode type.

    .. parsed-literal::

        AX_VENC_GOPMODE_NORMALP = 0    # NORMALP
        AX_VENC_GOPMODE_ONELTR  = 1    # ONELTR
        AX_VENC_GOPMODE_SVC_T   = 2    # SVC-T
        AX_VENC_GOPMODE_BUTT    = 3
"""
AX_VENC_GOPMODE_NORMALP = 0  # NORMALP
AX_VENC_GOPMODE_ONELTR = 1  # ONELTR
AX_VENC_GOPMODE_SVC_T = 2  # SVC-T
AX_VENC_GOPMODE_BUTT = 3


class AX_VENC_GOP_PIC_CONFIG_T(BaseStructure):
    """
    GOP picture configuration.

    .. parsed-literal::

        dict_venc_gop_pic_config = {
            "qp_offset": int,
            "qp_factor": int
        }
    """
    _fields_ = [
        ("s32QpOffset", AX_S32),  # QP offset will be added to the QP parameter to set the final QP
        ("f32QpFactor", AX_F32)
    ]
    field_aliases = {
        "s32QpOffset": "qp_offset",
        "f32QpFactor": "qp_factor"
    }


class AX_VENC_GOP_PIC_SPECIAL_CONFIG_T(BaseStructure):
    """
    GOP picture special configuration.

    .. parsed-literal::

        dict_venc_gop_pic_special_config = {
            "qp_offset": int,
            "qp_factor": int,
            "interval": int
        }
    """
    _fields_ = [
        ("s32QpOffset", AX_S32),  # QP offset will be added to the QP parameter to set the final QP
        ("f32QpFactor", AX_F32),
        ("s32Interval", AX_S32)
    ]
    field_aliases = {
        "s32QpOffset": "qp_offset",
        "f32QpFactor": "qp_factor",
        "s32Interval": "interval"
    }


class AX_VENC_GOP_NORMALP_T(BaseStructure):
    """
    NORMAL P gop mode parameters.

    .. parsed-literal::

        dict_venc_gop_normalp = {
            "pic_config": :class:`AX_VENC_GOP_PIC_CONFIG_T <axcl.venc.axcl_venc_comm.AX_VENC_GOP_PIC_CONFIG_T>`
        }
    """
    _fields_ = [
        ("stPicConfig", AX_VENC_GOP_PIC_CONFIG_T)  # normal P frame config
    ]
    field_aliases = {
        "stPicConfig": "pic_config"
    }


class AX_VENC_GOP_ONE_LTR_T(BaseStructure):
    """
    ONE LTE gop mode parameters.

    .. parsed-literal::

        dict_venc_gop_one_ltr = {
            "pic_config": :class:`AX_VENC_GOP_PIC_CONFIG_T <axcl.venc.axcl_venc_comm.AX_VENC_GOP_PIC_CONFIG_T>`,
            "pic_special_config": :class:`AX_VENC_GOP_PIC_SPECIAL_CONFIG_T <axcl.venc.axcl_venc_comm.AX_VENC_GOP_PIC_SPECIAL_CONFIG_T>`
        }
    """
    _fields_ = [
        ("stPicConfig", AX_VENC_GOP_PIC_CONFIG_T),  # normal P frame config
        ("stPicSpecialConfig", AX_VENC_GOP_PIC_SPECIAL_CONFIG_T)  # one long-term reference frame config
    ]
    field_aliases = {
        "stPicConfig": "pic_config",
        "stPicSpecialConfig": "pic_special_config"
    }


class AX_VENC_GOP_SVC_T_T(BaseStructure):
    """
    SVC_T gop mode parameters.

    .. parsed-literal::

        dict_venc_gop_svc = {
            "svc_t_cfg": :class:`POINTER(c_char_p) <POINTER(c_char_p)>`,
            "gop_size": int
        }
    """
    _fields_ = [
        ("s8SvcTCfg", POINTER(c_char_p)),
        ("u32GopSize", AX_U32)
    ]
    field_aliases = {
        "s8SvcTCfg": "svc_t_cfg",
        "u32GopSize": "gop_size"
    }


class AX_VENC_GOP_ATTR_UNION(BaseUnion):
    """
    .. parsed-literal::

        dict_venc_gop_attr_union = {
            "normal_p": :class:`AX_VENC_GOP_NORMALP_T <axcl.venc.axcl_venc_comm.AX_VENC_GOP_NORMALP_T>`,
            "one_ltr": :class:`AX_VENC_GOP_ONE_LTR_T <axcl.venc.axcl_venc_comm.AX_VENC_GOP_ONE_LTR_T>`,
            "svc_t": :class:`AX_VENC_GOP_SVC_T_T <axcl.venc.axcl_venc_comm.AX_VENC_GOP_SVC_T_T>`
        }
    """
    _fields_ = [
        ("stNormalP", AX_VENC_GOP_NORMALP_T),  # attributes of normal P
        ("stOneLTR", AX_VENC_GOP_ONE_LTR_T),  # attributes of one long-term reference frame
        ("stSvcT", AX_VENC_GOP_SVC_T_T)  # attributes of svc-t
    ]
    field_aliases = {
        "stNormalP": "normal_p",
        "stOneLTR": "one_ltr",
        "stSvcT": "svc_t"
    }
    value_union_type_mapping = {
        AX_VENC_GOPMODE_NORMALP: "stNormalP",
        AX_VENC_GOPMODE_ONELTR: "stOneLTR",
        AX_VENC_GOPMODE_SVC_T: "stSvcT"
    }


class AX_VENC_GOP_ATTR_T(BaseStructure):
    """
    GOP attribute.

    .. parsed-literal::

        dict_venc_gop_attr = {
            "gop_mode": :class:`AX_VENC_GOP_MODE_E <axcl.venc.axcl_venc_comm.AX_VENC_GOP_MODE_E>`,
            "gop_attr": :class:`AX_VENC_GOP_ATTR_UNION <axcl.venc.axcl_venc_comm.AX_VENC_GOP_ATTR_UNION>`
        }
    """
    _fields_ = [
        ("enGopMode", AX_VENC_GOP_MODE_E),
        ("uGopAttr", AX_VENC_GOP_ATTR_UNION)
    ]
    field_aliases = {
        "enGopMode": "gop_mode",
        "uGopAttr": "gop_attr"
    }
    name_union_type_mapping = {
        "uGopAttr": "enGopMode"
    }


class AX_VENC_CHN_ATTR_T(BaseStructure):
    """
    Encoder channel attribute.

    .. parsed-literal::

        dict_venc_chn_attr = {
            "venc_attr": :class:`AX_VENC_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_ATTR_T>`,
            "rc_attr": :class:`AX_VENC_RC_ATTR_T <axcl.venc.axcl_venc_rc.AX_VENC_RC_ATTR_T>`,
            "gop_attr": :class:`AX_VENC_GOP_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_GOP_ATTR_T>`
        }
    """
    _fields_ = [
        ("stVencAttr", AX_VENC_ATTR_T),  # the attribute of video encoder channel
        ("stRcAttr", AX_VENC_RC_ATTR_T),  # the attribute of rate  ctrl
        ("stGopAttr", AX_VENC_GOP_ATTR_T),  # the attribute of gop
    ]
    field_aliases = {
        "stVencAttr": "venc_attr",
        "stRcAttr": "rc_attr",
        "stGopAttr": "gop_attr"
    }


AX_VENC_HW_CLK_E = AX_S32
"""
    Encoder hardware clock type.

    .. parsed-literal::

        AX_VENC_CLK_FREQUENCY_624M = 0    # VENC hw mod clk frequency 624M
        AX_VENC_CLK_FREQUENCY_500M = 1    # VENC hw mod clk frequency 500M
        AX_VENC_CLK_FREQUENCY_400M = 2    # VENC hw mod clk frequency 400M
        AX_VENC_CLK_FREQUENCY_BUTT = 3
"""
AX_VENC_CLK_FREQUENCY_624M = 0  # VENC hw mod clk frequency 624M
AX_VENC_CLK_FREQUENCY_500M = 1  # VENC hw mod clk frequency 500M
AX_VENC_CLK_FREQUENCY_400M = 2  # VENC hw mod clk frequency 400M
AX_VENC_CLK_FREQUENCY_BUTT = 3


class AX_VENC_MOD_PARAM_T(BaseStructure):
    """
    Encoder module parameters.

    .. parsed-literal::

        dict_venc_mod_param = {
            "hw_clk": :class:`AX_VENC_HW_CLK_E <axcl.venc.axcl_venc_comm.AX_VENC_HW_CLK_E>`
        }
    """
    _fields_ = [
        ("enVencHwClk", AX_VENC_HW_CLK_E)  # VENC Hw mod clk frequency
    ]
    field_aliases = {
        "enVencHwClk": "hw_clk"
    }


class AX_VENC_VUI_ASPECT_RATIO_T(BaseStructure):
    """
    vui.aspect.ratio parameters

    .. parsed-literal::

        dict_venc_vui_aspect_ratio = {
            "aspect_ratio_info_present_flag": int,
            "aspect_ratio_idc": int,
            "overscan_info_present_flag": int,
            "overscan_appropriate_flag": int,
            "sar_width": int,
            "sar_height": int
        }
    """
    _fields_ = [
        ("aspect_ratio_info_present_flag", AX_U8),
        # RW; Range:[0,1]; If 1, aspectratio info belows will be encoded into vui
        ("aspect_ratio_idc", AX_U8),  # RW; Range:[0,255]; 17~254 is reserved,see the protocol for the meaning.
        ("overscan_info_present_flag", AX_U8),  # RW; Range:[0,1]; If 1, oversacan info belows will be encoded into vui.
        ("overscan_appropriate_flag", AX_U8),  # RW; Range:[0,1]; see the protocol for the meaning.
        ("sar_width", AX_U16),  # RW; Range:(0, 65535]; see the protocol for the meaning.
        ("sar_height", AX_U16)  # RW; Range:(0, 65535]; see the protocol for the meaning.
    ]
    field_aliases = {
        "aspect_ratio_info_present_flag": "aspect_ratio_info_present_flag",
        "aspect_ratio_idc": "aspect_ratio_idc",
        "overscan_info_present_flag": "overscan_info_present_flag",
        "overscan_appropriate_flag": "overscan_appropriate_flag",
        "sar_width": "sar_width",
        "sar_height": "sar_height"
    }


class AX_VENC_VUI_TIME_INFO_T(BaseStructure):
    """
    vui.time.info parameters

    .. parsed-literal::

        dict_venc_vui_time_info = {
            "timing_info_present_flag": int,
            "num_units_in_tick": int,
            "time_scale": int,
            "fixed_frame_rate_flag": int,
            "num_ticks_poc_diff_one_minus1": int
        }
    """
    _fields_ = [
        ("timing_info_present_flag", AX_U8),  # RW; Range:[0,1]; If 1, timing info belows will be encoded into vui.
        ("num_units_in_tick", AX_U32),  # RW; Range:(0,4294967295]; see the H.264/H.265 protocol for the meaning
        ("time_scale", AX_U32),  # RW; Range:(0,4294967295]; see the H.264/H.265 protocol for the meaning
        ("fixed_frame_rate_flag", AX_U8),  # RW; Range:[0,1]; see the H.264 protocol for the meaning.
        ("num_ticks_poc_diff_one_minus1", AX_U32)  # RW; Range:(0,4294967294]; see the H.265 protocol for the meaning
    ]
    field_aliases = {
        "timing_info_present_flag": "timing_info_present_flag",
        "num_units_in_tick": "num_units_in_tick",
        "time_scale": "time_scale",
        "fixed_frame_rate_flag": "fixed_frame_rate_flag",
        "num_ticks_poc_diff_one_minus1": "num_ticks_poc_diff_one_minus1"
    }


class AX_VENC_VUI_VIDEO_SIGNAL_T(BaseStructure):
    """
    vui.video.signal parameters.

    .. parsed-literal::

        dict_venc_vui_video_signal = {
            "video_signal_type_present_flag": int,
            "video_format": int,
            "video_full_range_flag": int,
            "colour_description_present_flag": int,
            "colour_primaries": int,
            "transfer_characteristics": int,
            "matrix_coefficients": int
        }
    """
    _fields_ = [
        ("video_signal_type_present_flag", AX_U8),
        # RW; Range:[0,1]; If 1, video singnal info will be encoded into vui.
        ("video_format", AX_U8),  # RW; H.264e Range:[0,7], H.265e Range:[0,5]; see the protocol for the meaning.
        ("video_full_range_flag", AX_U8),  # RW; Range: {0,1}; see the protocol for the meaning.
        ("colour_description_present_flag", AX_U8),  # RO; Range: {0,1}; see the protocol for the meaning.
        ("colour_primaries", AX_U8),  # RO; Range: [0,255]; see the protocol for the meaning.
        ("transfer_characteristics", AX_U8),  # RO; Range: [0,255]; see the protocol for the meaning.
        ("matrix_coefficients", AX_U8)  # RO; Range:[0,255]; see the protocol for the meaning.
    ]
    field_aliases = {
        "video_signal_type_present_flag": "video_signal_type_present_flag",
        "video_format": "video_format",
        "video_full_range_flag": "video_full_range_flag",
        "colour_description_present_flag": "colour_description_present_flag",
        "colour_primaries": "colour_primaries",
        "transfer_characteristics": "transfer_characteristics",
        "matrix_coefficients": "matrix_coefficients"
    }


class AX_VENC_VUI_BITSTREAM_RESTRIC_T(BaseStructure):
    """
    vui.bitstream.restric parameters.

    .. parsed-literal::

        dict_venc_vui_bitstream_restric = {
            "bitstream_restriction_flag": int
        }
    """
    _fields_ = [
        ("bitstream_restriction_flag", AX_U8)  # RW; Range: {0,1}; see the protocol for the meaning.
    ]
    field_aliases = {
        "bitstream_restriction_flag": "bitstream_restriction_flag"
    }


class AX_VENC_VUI_PARAM_T(BaseStructure):
    """
    vui parameters.

    .. parsed-literal::

        dict_venc_vui_param = {
            "vui_aspect_ratio": :class:`AX_VENC_VUI_ASPECT_RATIO_T <axcl.venc.axcl_venc_comm.AX_VENC_VUI_ASPECT_RATIO_T>`,
            "vui_time_info": :class:`AX_VENC_VUI_TIME_INFO_T <axcl.venc.axcl_venc_comm.AX_VENC_VUI_TIME_INFO_T>`,
            "vui_video_signal": :class:`AX_VENC_VUI_VIDEO_SIGNAL_T <axcl.venc.axcl_venc_comm.AX_VENC_VUI_VIDEO_SIGNAL_T>`,
            "vui_bitstream_restric": :class:`AX_VENC_VUI_BITSTREAM_RESTRIC_T <axcl.venc.axcl_venc_comm.AX_VENC_VUI_BITSTREAM_RESTRIC_T>`
        }
    """
    _fields_ = [
        ("stVuiAspectRatio", AX_VENC_VUI_ASPECT_RATIO_T),
        ("stVuiTimeInfo", AX_VENC_VUI_TIME_INFO_T),
        ("stVuiVideoSignal", AX_VENC_VUI_VIDEO_SIGNAL_T),
        ("stVuiBitstreamRestric", AX_VENC_VUI_BITSTREAM_RESTRIC_T),
    ]
    field_aliases = {
        "stVuiAspectRatio": "vui_aspect_ratio",
        "stVuiTimeInfo": "vui_time_info",
        "stVuiVideoSignal": "vui_video_signal",
        "stVuiBitstreamRestric": "vui_bitstream_restric"
    }


AX_H264E_NALU_TYPE_E = AX_S32
"""
    H264 NALU type

    .. parsed-literal::

        AX_H264E_NALU_BSLICE    = 0     # B SLICE types
        AX_H264E_NALU_PSLICE    = 1     # P SLICE types
        AX_H264E_NALU_ISLICE    = 2     # I SLICE types
        AX_H264E_NALU_IDRSLICE  = 5     # IDR SLICE types
        AX_H264E_NALU_SEI       = 6     # SEI types
        AX_H264E_NALU_SPS       = 7     # SPS types
        AX_H264E_NALU_PPS       = 8     # PPS types
        AX_H264E_NALU_PREFIX_14 = 14    # Prefix NAL unit
        AX_H264E_NALU_BUTT      = 15
"""
AX_H264E_NALU_BSLICE = 0  # B SLICE types
AX_H264E_NALU_PSLICE = 1  # P SLICE types
AX_H264E_NALU_ISLICE = 2  # I SLICE types
AX_H264E_NALU_IDRSLICE = 5  # IDR SLICE types
AX_H264E_NALU_SEI = 6  # SEI types
AX_H264E_NALU_SPS = 7  # SPS types
AX_H264E_NALU_PPS = 8  # PPS types
AX_H264E_NALU_PREFIX_14 = 14  # Prefix NAL unit
AX_H264E_NALU_BUTT = 15

# the nalu type of H265E
AX_H265E_NALU_TYPE_E = AX_S32
"""
    H265 NALU type

    .. parsed-literal::

        AX_H265E_NALU_BSLICE = 0    # B SLICE types
        AX_H265E_NALU_PSLICE = 1    # P SLICE types
        AX_H265E_NALU_ISLICE = 2    # I SLICE types
"""
AX_H265E_NALU_BSLICE = 0  # B SLICE types
AX_H265E_NALU_PSLICE = 1  # P SLICE types
AX_H265E_NALU_ISLICE = 2  # I SLICE types

AX_H265E_NALU_TSA_R = 3

AX_H265E_NALU_IDRSLICE = 19  # IDR SLICE types
AX_H265E_NALU_VPS = 32  # VPS types
AX_H265E_NALU_SPS = 33  # SPS types
AX_H265E_NALU_PPS = 34  # PPS types
AX_H265E_NALU_SEI = 39  # SEI types

AX_H265E_NALU_BUTT = 40

# Picture type for encoding
AX_VENC_PICTURE_CODING_TYPE_E = AX_S32
"""
    Picture coding type.

    .. parsed-literal::

        AX_VENC_INTRA_FRAME           = 0    # I Frame
        AX_VENC_PREDICTED_FRAME       = 1    # P Frame
        AX_VENC_BIDIR_PREDICTED_FRAME = 2    # B Frame
        AX_VENC_VIRTUAL_INTRA_FRAME   = 3    # virtual I frame
        AX_VENC_NOTCODED_FRAME        = 4    # Used just as a return value
"""
AX_VENC_INTRA_FRAME = 0  # I Frame
AX_VENC_PREDICTED_FRAME = 1  # P Frame
AX_VENC_BIDIR_PREDICTED_FRAME = 2  # B Frame
AX_VENC_VIRTUAL_INTRA_FRAME = 3  # virtual I frame
AX_VENC_NOTCODED_FRAME = 4  # Used just as a return value

# the pack type of JPEGE
AX_JPEGE_PACK_TYPE_E = AX_S32
"""
    JPEG pack type.

    .. parsed-literal::

        AX_JPEGE_PACK_ECS     = 5     # ECS types
        AX_JPEGE_PACK_APP     = 6     # APP types
        AX_JPEGE_PACK_VDO     = 7     # VDO types
        AX_JPEGE_PACK_PIC     = 8     # PIC types
        AX_JPEGE_PACK_DCF     = 9     # DCF types
        AX_JPEGE_PACK_DCF_PIC = 10    # DCF PIC types
        AX_JPEGE_PACK_BUTT    = 11
"""
AX_JPEGE_PACK_ECS = 5  # ECS types
AX_JPEGE_PACK_APP = 6  # APP types
AX_JPEGE_PACK_VDO = 7  # VDO types
AX_JPEGE_PACK_PIC = 8  # PIC types
AX_JPEGE_PACK_DCF = 9  # DCF types
AX_JPEGE_PACK_DCF_PIC = 10  # DCF PIC types
AX_JPEGE_PACK_BUTT = 11


# the data type of VENC
class AX_VENC_DATA_TYPE_U(BaseUnion):
    """
    Encoder data type.

    .. parsed-literal::

        dict_venc_dataype_u = {
            "h264e_type": :class:`AX_H264E_NALU_TYPE_E <axcl.venc.axcl_venc_comm.AX_H264E_NALU_TYPE_E>`,
            "jpege_type": :class:`AX_JPEGE_PACK_TYPE_E <axcl.venc.axcl_venc_comm.AX_JPEGE_PACK_TYPE_E>`,
            "h265e_type": :class:`AX_H265E_NALU_TYPE_E <axcl.venc.axcl_venc_comm.AX_H265E_NALU_TYPE_E>`
        }
    """
    _fields_ = [
        ("enH264EType", AX_H264E_NALU_TYPE_E),  # R; H264E NALU types
        ("enJPEGEType", AX_JPEGE_PACK_TYPE_E),  # R; JPEGE pack types
        ("enH265EType", AX_H265E_NALU_TYPE_E),  # R; H264E NALU types
    ]
    field_aliases = {
        "enH264EType": "h264e_type",
        "enJPEGEType": "jpege_type",
        "enH265EType": "h265e_type"
    }
    value_union_type_mapping = {
        PT_H264: "enH264EType",
        PT_JPEG: "enJPEGEType",
        PT_H265: "enH265EType",
    }


class AX_VENC_NALU_INFO_T(BaseStructure):
    """
    NALU information.

    .. parsed-literal::

        dict_venc_nalu_info = {
            "nalu_type": :class:`AX_VENC_DATA_TYPE_U <axcl.venc.axcl_venc_comm.AX_VENC_DATA_TYPE_U>`,
            "nalu_offset": int,
            "nalu_length": int
        }
    """
    _fields_ = [
        ("unNaluType", AX_VENC_DATA_TYPE_U),  # R; the nalu type
        ("u32NaluOffset", AX_U32),
        ("u32NaluLength", AX_U32)
    ]
    field_aliases = {
        "unNaluType": "nalu_type",
        "u32NaluOffset": "nalu_offset",
        "u32NaluLength": "nalu_length"
    }


class AX_CHN_STREAM_STATUS_T(BaseStructure):
    """
    Channel stream status.

    .. parsed-literal::

        dict_chn_stream_status = {
            "total_chn_num": int,
            "chn_index": [int],
            "chn_codec_type": [:class:`AX_PAYLOAD_TYPE_E <axcl.ax_global_type.AX_PAYLOAD_TYPE_E>`]
        }
    """
    _fields_ = [
        ("u32TotalChnNum", AX_U32),  # Range:[0, MAX_VENC_CHN_NUM], how many channels have stream.
        ("au32ChnIndex", AX_U32 * MAX_VENC_CHN_NUM),  # the channel id set of venc channel that has stream
        ("aenChnCodecType", AX_PAYLOAD_TYPE_E * MAX_VENC_CHN_NUM),  # channel payload type
    ]
    field_aliases = {
        "u32TotalChnNum": "total_chn_num",
        "au32ChnIndex": "chn_index",
        "aenChnCodecType": "chn_codec_type"
    }


class AX_VENC_SELECT_GRP_PARAM_T(BaseStructure):
    """
    Select group parameters.

    .. parsed-literal::

        dict_venc_select_grp_param = {
            "total_chn_num": int,
            "chn_in_grp": [int]
        }
    """
    _fields_ = [
        ("u16TotalChnNum", AX_U16),  # Range:[0, MAX_VENC_CHN_NUM), how many channels in grp.
        ("u16ChnInGrp", AX_U16 * MAX_VENC_CHN_NUM)  # the channel id set of group
    ]
    field_aliases = {
        "u16TotalChnNum": "total_chn_num",
        "u16ChnInGrp": "chn_in_grp"
    }


class AX_VENC_PACK_T(BaseStructure):
    """
    Packed stream parameters.

    .. parsed-literal::

        dict_venc_pack = {
            "phy_addr": int,
            "vir_addr": int,
            "len": int,
            "pts": int,
            "seq_num": int,
            "user_data": int,
            "type": :class:`AX_PAYLOAD_TYPE_E <axcl.ax_global_type.AX_PAYLOAD_TYPE_E>`,
            "coding_Type": :class:`AX_VENC_PICTURE_CODING_TYPE_E <axcl.venc.axcl_venc_comm.AX_VENC_PICTURE_CODING_TYPE_E>`,
            "temporal_id": int,
            "nalu_num": int,
            "nalu_info": [:class:`AX_VENC_NALU_INFO_T <axcl.venc.axcl_venc_comm.AX_VENC_NALU_INFO_T>`]
        }
    """
    _fields_ = [
        ("ulPhyAddr", AX_U64),
        ("pu8Addr", POINTER(AX_U8)),
        ("u32Len", AX_U32),
        ("u64PTS", AX_U64),
        ("u64SeqNum", AX_U64),
        ("u64UserData", AX_U64),
        ("enType", AX_PAYLOAD_TYPE_E),
        ("enCodingType", AX_VENC_PICTURE_CODING_TYPE_E),
        ("u32TemporalID", AX_U32),
        ("u32NaluNum", AX_U32),
        ("stNaluInfo", AX_VENC_NALU_INFO_T * VENC_MAX_NALU_NUM)
    ]
    field_aliases = {
        "ulPhyAddr": "phy_addr",
        "pu8Addr": "vir_addr",
        "u32Len": "len",
        "u64PTS": "pts",
        "u64SeqNum": "seq_num",
        "u64UserData": "user_data",
        "enType": "type",
        "enCodingType": "coding_Type",
        "u32TemporalID": "temporal_id",
        "u32NaluNum": "nalu_num",
        "stNaluInfo": "nalu_info"
    }


AX_H264E_REF_TYPE_E = AX_S32
"""
    H264/H265 ref. type

    .. parsed-literal::

        AX_BASE_IDRSLICE               = 0    # the Idr frame at Base layer
        AX_BASE_PSLICE_REFTOIDR        = 1    # the P frame at Base layer, referenced by other frames at Base layer and reference to Idr frame
        AX_BASE_PSLICE_REFBYBASE       = 2    # the P frame at Base layer, referenced by other frames at Base layer
        AX_BASE_PSLICE_REFBYENHANCE    = 3    # the P frame at Base layer, referenced by other frames at Enhance layer
        AX_ENHANCE_PSLICE_REFBYENHANCE = 4    # the P frame at Enhance layer, referenced by other frames at Enhance layer
        AX_ENHANCE_PSLICE_NOTFORREF    = 5    # the P frame at Enhance layer ,not referenced
        AX_ENHANCE_PSLICE_BUTT         = 6
"""
AX_BASE_IDRSLICE = 0  # the Idr frame at Base layer
AX_BASE_PSLICE_REFTOIDR = 1  # the P frame at Base layer, referenced by other frames at Base layer and reference to Idr frame
AX_BASE_PSLICE_REFBYBASE = 2  # the P frame at Base layer, referenced by other frames at Base layer
AX_BASE_PSLICE_REFBYENHANCE = 3  # the P frame at Base layer, referenced by other frames at Enhance layer
AX_ENHANCE_PSLICE_REFBYENHANCE = 4  # the P frame at Enhance layer, referenced by other frames at Enhance layer
AX_ENHANCE_PSLICE_NOTFORREF = 5  # the P frame at Enhance layer ,not referenced
AX_ENHANCE_PSLICE_BUTT = 6

AX_H265E_REF_TYPE_E = AX_H264E_REF_TYPE_E


# Defines the features of an H.264 stream
class AX_VENC_STREAM_INFO_H264_T(BaseStructure):
    """
    H264 stream information.

    .. parsed-literal::

        dict_venc_stream_info_h264 = {
            "pic_bytes_num": int,
            "inter_16x16mb_num": int,
            "inter_8x8mb_num": int,
            "intra_16mb_num": int,
            "intra_8mb_num": int,
            "intra_4mb_num": int,
            "ref_type": :class:`AX_H264E_REF_TYPE_E <axcl.venc.axcl_venc_comm.AX_H264E_REF_TYPE_E>`,
            "update_attr_cnt": int,
            "start_qp": int,
            "mean_qp": int,
            "p_skip": bool
        }
    """
    _fields_ = [
        ("u32PicBytesNum", AX_U32),
        ("u32Inter16x16MbNum", AX_U32),
        ("u32Inter8x8MbNum", AX_U32),
        ("u32Intra16MbNum", AX_U32),
        ("u32Intra8MbNum", AX_U32),
        ("u32Intra4MbNum", AX_U32),
        ("enRefType", AX_H264E_REF_TYPE_E),
        ("u32UpdateAttrCnt", AX_U32),
        ("u32StartQp", AX_U32),
        ("u32MeanQp", AX_U32),
        ("bPSkip", AX_BOOL)
    ]
    field_aliases = {
        "u32PicBytesNum": "pic_bytes_num",
        "u32Inter16x16MbNum": "inter_16x16mb_num",
        "u32Inter8x8MbNum": "inter_8x8mb_num",
        "u32Intra16MbNum": "intra_16mb_num",
        "u32Intra8MbNum": "intra_8mb_num",
        "u32Intra4MbNum": "intra_4mb_num",
        "enRefType": "ref_type",
        "u32UpdateAttrCnt": "update_attr_cnt",
        "u32StartQp": "start_qp",
        "u32MeanQp": "mean_qp",
        "bPSkip": "p_skip"
    }


class AX_VENC_STREAM_INFO_H265_T(BaseStructure):
    """
    H265 stream information.

    .. parsed-literal::

        dict_venc_stream_info_h265 = {
            "pic_bytes_num": int,
            "inter_64x64cu_num": int,
            "inter_32x32cu_num": int,
            "inter_16x16cu_num": int,
            "inter_8x8cu_num": int,
            "intra_32x32cu_num": int,
            "intra_16x16cu_num": int,
            "intra_8x8cu_num": int,
            "intra_4x4cu_num": int,
            "ref_type": :class:`AX_H265E_REF_TYPE_E <axcl.venc.axcl_venc_comm.AX_H265E_REF_TYPE_E>`,
            "update_attr_cnt": int,
            "start_qp": int,
            "mean_qp": int,
            "p_skip": bool
        }
    """
    _fields_ = [
        ("u32PicBytesNum", AX_U32),
        ("u32Inter64x64CuNum", AX_U32),
        ("u32Inter32x32CuNum", AX_U32),
        ("u32Inter16x16CuNum", AX_U32),
        ("u32Inter8x8CuNum", AX_U32),
        ("u32Intra32x32CuNum", AX_U32),
        ("u32Intra16x16CuNum", AX_U32),
        ("u32Intra8x8CuNum", AX_U32),
        ("u32Intra4x4CuNum", AX_U32),
        ("enRefType", AX_H265E_REF_TYPE_E),
        ("u32UpdateAttrCnt", AX_U32),
        ("u32StartQp", AX_U32),
        ("u32MeanQp", AX_U32),
        ("bPSkip", AX_BOOL)
    ]
    field_aliases = {
        "u32PicBytesNum": "pic_bytes_num",
        "u32Inter64x64CuNum": "inter_64x64cu_num",
        "u32Inter32x32CuNum": "inter_32x32cu_num",
        "u32Inter16x16CuNum": "inter_16x16cu_num",
        "u32Inter8x8CuNum": "inter_8x8cu_num",
        "u32Intra32x32CuNum": "intra_32x32cu_num",
        "u32Intra16x16CuNum": "intra_16x16cu_num",
        "u32Intra8x8CuNum": "intra_8x8cu_num",
        "u32Intra4x4CuNum": "intra_4x4cu_num",
        "enRefType": "ref_type",
        "u32UpdateAttrCnt": "update_attr_cnt",
        "u32StartQp": "start_qp",
        "u32MeanQp": "mean_qp",
        "bPSkip": "p_skip"
    }


class AX_VENC_SSE_INFO_T(BaseStructure):
    """
    SSE information.

    .. parsed-literal::

        dict_venc_sse_info = {
            "sse_en": bool,
            "sse_val": int
        }
    """
    _fields_ = [
        ("bSSEEn", AX_BOOL),
        ("u32SSEVal", AX_U32)
    ]
    field_aliases = {
        "bSSEEn": "sse_en",
        "u32SSEVal": "sse_val"
    }


class AX_VENC_STREAM_ADVANCE_INFO_H264_T(BaseStructure):
    """
    H264 advance stream information.

    .. parsed-literal::

        dict_venc_stream_advance_info_h264 = {
            "residual_bit_num": int,
            "head_bit_num": int,
            "madi_val": int,
            "madp_val": int,
            "psnr_val": int,
            "mse_lcu_cnt": int,
            "mse_sum": int,
            "sse_info": [:class:`AX_VENC_SSE_INFO_T <axcl.venc.axcl_venc_comm.AX_VENC_SSE_INFO_T>`],
            "qp_hstgrm": [int],
            "move_scene_16x16_num": int,
            "move_scene_bits": int
        }
    """
    _fields_ = [
        ("u32ResidualBitNum", AX_U32),
        ("u32HeadBitNum", AX_U32),
        ("u32MadiVal", AX_U32),
        ("u32MadpVal", AX_U32),
        ("f64PSNRVal", AX_F64),
        ("u32MseLcuCnt", AX_U32),
        ("u32MseSum", AX_U32),
        ("stSSEInfo", AX_VENC_SSE_INFO_T * 8),
        ("u32QpHstgrm", AX_U32 * VENC_QP_HISGRM_NUM),
        ("u32MoveScene16x16Num", AX_U32),
        ("u32MoveSceneBits", AX_U32)
    ]
    field_aliases = {
        "u32ResidualBitNum": "residual_bit_num",
        "u32HeadBitNum": "head_bit_num",
        "u32MadiVal": "madi_val",
        "u32MadpVal": "madp_val",
        "f64PSNRVal": "psnr_val",
        "u32MseLcuCnt": "mse_lcu_cnt",
        "u32MseSum": "mse_sum",
        "stSSEInfo": "sse_info",
        "u32QpHstgrm": "qp_hstgrm",
        "u32MoveScene16x16Num": "move_scene_16x16_num",
        "u32MoveSceneBits": "move_scene_bits"
    }


class AX_VENC_STREAM_ADVANCE_INFO_H265_T(BaseStructure):
    """
    H265 advance stream information.

    .. parsed-literal::

        dict_venc_stream_advance_info_h265 = {
            "residual_bit_num": int,
            "head_bit_num": int,
            "madi_val": int,
            "madp_val": int,
            "psnr_val": int,
            "mse_lcu_cnt": int,
            "mse_sum": int,
            "sse_info": [:class:`AX_VENC_SSE_INFO_T <axcl.venc.axcl_venc_comm.AX_VENC_SSE_INFO_T>`],
            "qp_hstgrm": [int],
            "move_scene_32x32_num": int,
            "move_scene_bits": int
        }
    """
    _fields_ = [
        ("u32ResidualBitNum", AX_U32),  # the residual num
        ("u32HeadBitNum", AX_U32),  # the head bit num
        ("u32MadiVal", AX_U32),  # the madi value
        ("u32MadpVal", AX_U32),  # the madp value
        ("f64PSNRVal", AX_F64),  # the PSNR value
        ("u32MseLcuCnt", AX_U32),  # the lcu cnt of the mse
        ("u32MseSum", AX_U32),  # the sum of the mse
        ("stSSEInfo", AX_VENC_SSE_INFO_T * 8),  # the information of the sse
        ("u32QpHstgrm", AX_U32 * VENC_QP_HISGRM_NUM),  # the Qp histogram value
        ("u32MoveScene32x32Num", AX_U32),  # the 32x32 cu num of the move scene
        ("u32MoveSceneBits", AX_U32)  # the stream bit num of the move scene
    ]
    field_aliases = {
        "u32ResidualBitNum": "residual_bit_num",
        "u32HeadBitNum": "head_bit_num",
        "u32MadiVal": "madi_val",
        "u32MadpVal": "madp_val",
        "f64PSNRVal": "psnr_val",
        "u32MseLcuCnt": "mse_lcu_cnt",
        "u32MseSum": "mse_sum",
        "stSSEInfo": "sse_info",
        "u32QpHstgrm": "qp_hstgrm",
        "u32MoveScene32x32Num": "move_scene_32x32_num",
        "u32MoveSceneBits": "move_scene_bits"
    }


# Defines the features of an jpege stream
class AX_VENC_STREAM_INFO_JPEG_T(BaseStructure):
    """
    JPEG stream information.

    .. parsed-literal::

        dict_venc_stream_info_jpeg = {
            "pic_bytes_num": int,
            "update_attr_cnt": int,
            "q_factor": int
        }
    """
    _fields_ = [
        ("u32PicBytesNum", AX_U32),  # the coded picture stream byte number
        ("u32UpdateAttrCnt", AX_U32),
        # Number of times that channel attributes or parameters (including RC parameters) are set
        ("u32Qfactor", AX_U32)  # image quality
    ]
    field_aliases = {
        "u32PicBytesNum": "pic_bytes_num",
        "u32UpdateAttrCnt": "update_attr_cnt",
        "u32Qfactor": "q_factor"
    }


class AX_VENC_STREAM_ADVANCE_INFO_JPEG_T(BaseStructure):
    """
    JPEG advance stream information.

    .. parsed-literal::

        dict_venc_stream_advance_info_jpeg = {

        }
    """
    _fields_ = [
    ]
    field_aliases = {
    }


class AX_VENC_STREAM_INFO_U(BaseUnion):
    """
    .. parsed-literal::

        dict_venc_stream_info_u = {
            "h264_info": :class:`AX_VENC_STREAM_INFO_H264_T <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_INFO_H264_T>`,
            "jpeg_info": :class:`AX_VENC_STREAM_INFO_JPEG_T <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_INFO_JPEG_T>`,
            "h265_info": :class:`AX_VENC_STREAM_INFO_H265_T <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_INFO_H265_T>`
        }
    """
    _fields_ = [
        ("stH264Info", AX_VENC_STREAM_INFO_H264_T),
        ("stJpegInfo", AX_VENC_STREAM_INFO_JPEG_T),
        ("stH265Info", AX_VENC_STREAM_INFO_H265_T)
    ]
    field_aliases = {
        "stH264Info": "h264_info",
        "stJpegInfo": "jpeg_info",
        "stH265Info": "h265_info"
    }
    value_union_type_mapping = {
        PT_H264: "stH264Info",
        PT_JPEG: "stJpegInfo",
        PT_H265: "stH265Info"
    }


class AX_VENC_STREAM_ADVANCE_INFO_U(BaseUnion):
    """
    .. parsed-literal::

        dict_venc_stream_advance_info_u = {
            "advance_h264_info": :class:`AX_VENC_STREAM_ADVANCE_INFO_H264_T <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_ADVANCE_INFO_H264_T>`,
            "advance_jpeg_info": :class:`AX_VENC_STREAM_ADVANCE_INFO_JPEG_T <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_ADVANCE_INFO_JPEG_T>`,
            "advance_h265_info": :class:`AX_VENC_STREAM_ADVANCE_INFO_H265_T <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_ADVANCE_INFO_H265_T>`
        }
    """
    _fields_ = [
        ("stAdvanceH264Info", AX_VENC_STREAM_ADVANCE_INFO_H264_T),  # the stream info of h264
        ("stAdvanceJpegInfo", AX_VENC_STREAM_ADVANCE_INFO_JPEG_T),  # the stream info of jpeg
        ("stAdvanceH265Info", AX_VENC_STREAM_ADVANCE_INFO_H265_T)  # the stream info of h265
    ]
    field_aliases = {
        "stAdvanceH264Info": "advance_h264_info",
        "stAdvanceJpegInfo": "advance_jpeg_info",
        "stAdvanceH265Info": "advance_h265_info"
    }
    value_union_type_mapping = {
        PT_H264: "stAdvanceH264Info",
        PT_JPEG: "stAdvanceJpegInfo",
        PT_H265: "stAdvanceH265Info"
    }


class AX_VENC_STREAM_T(BaseStructure):
    """
    Encoded stream information.

    .. parsed-literal::

        dict_venc_stream = {
            "pack": :class:`AX_VENC_PACK_T <axcl.venc.axcl_venc_comm.AX_VENC_PACK_T>`,
            "info": :class:`AX_VENC_STREAM_INFO_U <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_INFO_U>`,
            "advance_info": :class:`AX_VENC_STREAM_ADVANCE_INFO_U <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_ADVANCE_INFO_U>`
        }
    """
    _fields_ = [
        ("stPack", AX_VENC_PACK_T),
        ("uInfo", AX_VENC_STREAM_INFO_U),
        ("uAdvanceInfo", AX_VENC_STREAM_ADVANCE_INFO_U)
    ]
    field_aliases = {
        "stPack": "pack",
        "uInfo": "info",
        "uAdvanceInfo": "advance_info"
    }


class AX_VENC_RECV_PIC_PARAM_T(BaseStructure):
    """
    Receive parameters.

    .. parsed-literal::

        dict_venc_recv_pic_param = {
            "recv_pic_num": int
        }
    """
    _fields_ = [
        ("s32RecvPicNum", AX_S32)
    ]
    field_aliases = {
        "s32RecvPicNum": "recv_pic_num"
    }


class AX_VENC_STREAM_BUF_INFO_T(BaseStructure):
    """
    Stream buffer information.

    .. parsed-literal::

        dict_venc_stream_buf_info = {
            "phy_addr": int,
            "user_addr": int,
            "buf_size": int
        }
    """
    _fields_ = [
        ("u64PhyAddr", AX_U64),
        ("pUserAddr", c_void_p),
        ("u32BufSize", AX_U32)
    ]
    field_aliases = {
        "u64PhyAddr": "phy_addr",
        "pUserAddr": "user_addr",
        "u32BufSize": "buf_size"
    }


class AX_VENC_ROI_ATTR_T(BaseStructure):
    """
    ROI attribute.

    .. parsed-literal::

        dict_venc_roi_attr = {
            "index": int,
            "enable": bool,
            "abs_qp": bool,
            "roi_qp": int,
            "roi_area": :class:`AX_RECT_T <axcl.venc.axcl_venc_comm.AX_RECT_T>`
        }
    """
    _fields_ = [
        ("u32Index", AX_U32),  # RW; Range:[0, 7]; Index of an ROI. The system supports indexes ranging from 0 to 7
        ("bEnable", AX_BOOL),  # RW; Range:[0, 1]; Whether to enable this ROI
        ("bAbsQp", AX_BOOL),  # RW; Range:[0, 1]; QP mode of an ROI. 0: relative QP. 1: absolute QP. (only for venc)
        ("s32RoiQp", AX_S32),  # RW; Range: [-51, 51] when bAbsQp==0; [0, 51] when bAbsQp==1;  (only for venc)
        ("stRoiArea", AX_RECT_T),  # RW; Region of an ROI
    ]
    field_aliases = {
        "u32Index": "index",
        "bEnable": "enable",
        "bAbsQp": "abs_qp",
        "s32RoiQp": "roi_qp",
        "stRoiArea": "roi_area"
    }


class AX_VENC_ROI_ATTR_EX_T(BaseStructure):
    """
    ROI attribute.

    .. parsed-literal::

        dict_venc_roi_attr_ex = {
            "index": int,
            "enable": [bool],
            "abs_qp": [bool],
            "qp": [int],
            "rect": [:class:`AX_RECT_T <axcl.venc.axcl_venc_comm.AX_RECT_T>`]
        }
    """
    _fields_ = [
        ("u32Index", AX_U32),  # Range:[0, 7]; Index of an ROI. The system supports indexes ranging from 0 to 7
        ("bEnable", AX_BOOL * 3),
        # Range:[0, 1]; Subscript of array   0: I Frame; 1: P/B Frame; 2: VI Frame; other params are the same.
        ("bAbsQp", AX_BOOL * 3),  # Range:[0, 1]; QP mode of an ROI. AX_FALSE: relative QP. AX_TURE: absolute QP.
        ("s32Qp", AX_S32 * 3),  # Range:[-51, 51]; QP value,only relative mode can QP value less than 0.
        ("stRect", AX_RECT_T * 3)  # Region of an ROI
    ]
    field_aliases = {
        "u32Index": "index",
        "bEnable": "enable",
        "bAbsQp": "abs_qp",
        "s32Qp": "qp",
        "stRect": "rect"
    }


class AX_JPEG_ROI_ATTR_T(BaseStructure):
    """
    JPEG ROI attribute.

    .. parsed-literal::

        dict_jpeg_roi_attr = {
            "index": int,
            "enable": bool,
            "roi_area": :class:`AX_RECT_T <axcl.venc.axcl_venc_comm.AX_RECT_T>`
        }
    """
    _fields_ = [
        ("u32Index", AX_U32),  # RW; Range:[0, 7]; Index of an ROI. The system supports indexes ranging from 0 to 7
        ("bEnable", AX_BOOL),  # RW; Range:[0, 1]; Whether to enable this ROI
        ("stRoiArea", AX_RECT_T)  # RW; Region of an ROI
    ]
    field_aliases = {
        "u32Index": "index",
        "bEnable": "enable",
        "stRoiArea": "roi_area"
    }


class AX_VENC_CHN_STATUS_T(BaseStructure):
    """
    Channel status.

    .. parsed-literal::

        dict_venc_chn_status = {
            "left_pics": int,
            "left_stream_bytes": int,
            "left_stream_frames": int,
            "cur_packs": int,
            "left_recv_pics": int,
            "left_enc_pics": int,
            "reserved": int
        }
    """
    _fields_ = [
        ("u32LeftPics", AX_U32),  # Number of frames yet to encode (until fifo empty)
        ("u32LeftStreamBytes", AX_U32),  # Number of bytes remaining in the bitstream buffer
        ("u32LeftStreamFrames", AX_U32),  # Number of frames remaining in the bitstream buffer
        ("u32CurPacks", AX_U32),  # Number of current stream packets. not support now
        ("u32LeftRecvPics", AX_U32),
        # Number of frames yet to recieve (total number specified at start). not support now
        ("u32LeftEncPics", AX_U32),  # Number of frames yet to encode (total number specified at start). not support now
        ("u32Reserved", AX_U32)  # Reserved
    ]
    field_aliases = {
        "u32LeftPics": "left_pics",
        "u32LeftStreamBytes": "left_stream_bytes",
        "u32LeftStreamFrames": "left_stream_frames",
        "u32CurPacks": "cur_packs",
        "u32LeftRecvPics": "left_recv_pics",
        "u32LeftEncPics": "left_enc_pics",
        "u32Reserved": "reserved"
    }


class AX_USER_RC_INFO_T(BaseStructure):
    """
    User RC information.

    .. parsed-literal::

        dict_user_rc_info = {
            "qp_map_valid": bool,
            "ipc_mmap_valid": bool,
            "blk_start_qp": int,
            "qp_map_phy_addr": int,
            "qp_map_vir_addr": int,
            "ipcm_map_phy_addr": int,
            "frame_type": :class:`AX_FRAME_TYPE_E <axcl.ax_codec_comm.AX_FRAME_TYPE_E>`,
            "roi_map_delta_size": int
        }
    """
    _fields_ = [
        ("bQpMapValid", AX_BOOL),  # Range:[0,1]; Indicates whether the QpMap mode is valid for the current frame
        ("bIPCMMapValid", AX_BOOL),  # Range:[0,1]; Indicates whether the IpcmMap mode is valid for the current frame
        ("u32BlkStartQp", AX_U32),  # Range:[0,51];QP value of the first 16 x 16 block in QpMap mode
        ("u64QpMapPhyAddr", AX_U64),  # Physical address of the QP table in QpMap mode
        ("pQpMapVirAddr", POINTER(AX_S8)),  # virtaul address of the qpMap
        ("u64IpcmMapPhyAddr", AX_U64),  # Physical address of the IPCM table in QpMap mode
        ("enFrameType", AX_FRAME_TYPE_E),  # Encoding frame type of the current frame
        ("u32RoiMapDeltaSize", AX_U32)  # size of QpDelta map (per frame)
    ]
    field_aliases = {
        "bQpMapValid": "qp_map_valid",
        "bIPCMMapValid": "ipc_mmap_valid",
        "u32BlkStartQp": "blk_start_qp",
        "u64QpMapPhyAddr": "qp_map_phy_addr",
        "pQpMapVirAddr": "qp_map_vir_addr",
        "u64IpcmMapPhyAddr": "ipcm_map_phy_addr",
        "enFrameType": "frame_type",
        "u32RoiMapDeltaSize": "roi_map_delta_size"
    }


class AX_USER_FRAME_INFO_T(BaseStructure):
    """
    User frame information.

    .. parsed-literal::

        dict_user_frame_info = {
            "user_frame": :class:`AX_VIDEO_FRAME_INFO_T <axcl.ax_global_type.AX_VIDEO_FRAME_INFO_T>`,
            "user_rc_info": :class:`AX_USER_RC_INFO_T <axcl.venc.axcl_venc_comm.AX_USER_RC_INFO_T>`,
            "user_exif_info": :class:`AX_USER_EXIF_INFO_T <axcl.venc.axcl_venc_exif.AX_USER_EXIF_INFO_T>`
        }
    """
    _fields_ = [
        ("stUserFrame", AX_VIDEO_FRAME_INFO_T),
        ("stUserRcInfo", AX_USER_RC_INFO_T),
        ("stUserExifInfo", AX_USER_EXIF_INFO_T)
    ]
    field_aliases = {
        "stUserFrame": "user_frame",
        "stUserRcInfo": "user_rc_info",
        "stUserExifInfo": "user_exif_info"
    }


AX_ENC_ERR_CODE_E = AX_S32
AX_ERR_ENC_CREATE_CHAN_ERR = 0x80  # create encoder channel failed
AX_ERR_ENC_SET_PRIORITY_FAIL = 0x81  # set encoder thread priority failed

AX_VENC_STREAM_BUF_TYPE_E = AX_S32
"""
    Strean buffer type.

    .. parsed-literal::

        AX_STREAM_BUF_NON_CACHE = 0
        AX_STREAM_BUF_CACHE     = 1
"""
AX_STREAM_BUF_NON_CACHE = 0
AX_STREAM_BUF_CACHE = 1


class AX_JPEG_ENCODE_ONCE_PARAMS_T(BaseStructure):
    """
    JPEG encoding parameters.

    .. parsed-literal::

        dict_jpeg_encode_once_params = {
            "width": int,
            "height": int,
            "img_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "pic_stride": [int],
            "phy_addr": [int],
            "vir_addr": [int],
            "crop_x": int,
            "crop_y": int,
            "crop_width": int,
            "crop_height": int,
            "header_size": [int],
            "compress_info": :class:`AX_FRAME_COMPRESS_INFO_T <axcl.ax_global_type.AX_FRAME_COMPRESS_INFO_T>`,
            "output_phy_addr": int,
            "output_vir_addr": int,
            "output_len": int,
            "strm_buf_type": :class:`AX_VENC_STREAM_BUF_TYPE_E <axcl.venc.axcl_venc_comm.AX_VENC_STREAM_BUF_TYPE_E>`,
            "jpeg_param": :class:`AX_VENC_JPEG_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_JPEG_PARAM_T>`,
            "thumb_enable": bool,
            "thumb_width": int,
            "thumb_height": int
        }
    """
    _fields_ = [
        ("u32Width", AX_U32),
        ("u32Height", AX_U32),
        ("enImgFormat", AX_IMG_FORMAT_E),
        ("u32PicStride", AX_U32 * 3),
        ("u64PhyAddr", AX_U64 * 3),
        ("u64VirAddr", AX_U64 * 3),
        ("s16CropX", AX_S16),
        ("s16CropY", AX_S16),
        ("s16CropWidth", AX_S16),
        ("s16CropHeight", AX_S16),
        ("u32HeaderSize", AX_U32 * AX_MAX_COLOR_COMPONENT),
        ("stCompressInfo", AX_FRAME_COMPRESS_INFO_T),
        ("ulPhyAddr", AX_U64),
        ("pu8Addr", POINTER(AX_U8)),
        ("u32Len", AX_U32),
        ("enStrmBufType", AX_VENC_STREAM_BUF_TYPE_E),
        ("stJpegParam", AX_VENC_JPEG_PARAM_T),
        ("bThumbEnable", AX_BOOL),
        ("u32ThumbWidth", AX_U32),
        ("u32ThumbHeight", AX_U32)
    ]
    field_aliases = {
        "u32Width": "width",
        "u32Height": "height",
        "enImgFormat": "img_format",
        "u32PicStride": "pic_stride",
        "u64PhyAddr": "phy_addr",
        "u64VirAddr": "vir_addr",
        "s16CropX": "crop_x",
        "s16CropY": "crop_y",
        "s16CropWidth": "crop_width",
        "s16CropHeight": "crop_height",
        "u32HeaderSize": "header_size",
        "stCompressInfo": "compress_info",
        "ulPhyAddr": "output_phy_addr",
        "pu8Addr": "output_vir_addr",
        "u32Len": "output_len",
        "enStrmBufType": "strm_buf_type",
        "stJpegParam": "jpeg_param",
        "bThumbEnable": "thumb_enable",
        "u32ThumbWidth": "thumb_width",
        "u32ThumbHeight": "thumb_height"
    }


AX_VENC_INTRA_REFRESH_MODE_E = AX_S32
"""
    Instra refresh mode

    .. parsed-literal::

        AX_VENC_INTRA_REFRESH_ROW    = 0
        AX_VENC_INTRA_REFRESH_COLUMN = 1
        AX_VENC_INTRA_REFRESH_BUTT   = 2
"""
AX_VENC_INTRA_REFRESH_ROW = 0
AX_VENC_INTRA_REFRESH_COLUMN = 1
AX_VENC_INTRA_REFRESH_BUTT = 2


class AX_VENC_INTRA_REFRESH_T(BaseStructure):
    """
    Intra. refresh parameters.

    .. parsed-literal::

        dict_venc_intra_refresh = {
            "refresh": bool,
            "refresh_num": int,
            "req_iqp": int,
            "intra_refresh_mode": :class:`AX_VENC_INTRA_REFRESH_MODE_E <axcl.venc.axcl_venc_comm.AX_VENC_INTRA_REFRESH_MODE_E>`
        }
    """
    _fields_ = [
        ("bRefresh", AX_BOOL),
        ("u32RefreshNum", AX_U32),  # Range:[1, gopLen]; how many frames it will take to do GDR
        ("u32ReqIQp", AX_U32),
        ("enIntraRefreshMode", AX_VENC_INTRA_REFRESH_MODE_E)
    ]
    field_aliases = {
        "bRefresh": "refresh",
        "u32RefreshNum": "refresh_num",
        "u32ReqIQp": "req_iqp",
        "enIntraRefreshMode": "intra_refresh_mode"
    }


class AX_VENC_SLICE_SPLIT_T(BaseStructure):
    """
    Slice split parameters.

    .. parsed-literal::

        dict_venc_slice_split = {
            "split": bool,
            "lcu_line_num": int
        }
    """
    _fields_ = [
        ("bSplit", AX_BOOL),
        ("u32LcuLineNum", AX_U32)  # [1, align_up(picHeight)/BLK_SIZE]: a slice should contain how many MCU/MB/CTU lines
    ]
    field_aliases = {
        "bSplit": "split",
        "u32LcuLineNum": "lcu_line_num"
    }


AX_ID_VENC_COMMON = 0x02
AX_ERR_VENC_CREATE_CHAN_ERR = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_ENC_CREATE_CHAN_ERR)
AX_ERR_VENC_SET_PRIORITY_FAIL = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_ENC_SET_PRIORITY_FAIL)
AX_ERR_VENC_NULL_PTR = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_NULL_PTR)
AX_ERR_VENC_ILLEGAL_PARAM = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_ILLEGAL_PARAM)
AX_ERR_VENC_BAD_ADDR = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_BAD_ADDR)
AX_ERR_VENC_NOT_SUPPORT = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_NOT_SUPPORT)
AX_ERR_VENC_NOT_INIT = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_NOT_INIT)
AX_ERR_VENC_BUF_EMPTY = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_BUF_EMPTY)
AX_ERR_VENC_BUF_FULL = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_BUF_FULL)
AX_ERR_VENC_QUEUE_EMPTY = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_QUEUE_EMPTY)
AX_ERR_VENC_QUEUE_FULL = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_QUEUE_FULL)
AX_ERR_VENC_EXIST = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_EXIST)
AX_ERR_VENC_UNEXIST = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_UNEXIST)
AX_ERR_VENC_NOT_PERMIT = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_NOT_PERM)
AX_ERR_VENC_TIMEOUT = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_TIMED_OUT)
AX_ERR_VENC_FLOW_END = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_FLOW_END)
AX_ERR_VENC_ATTR_NOT_CFG = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_NOT_CONFIG)
AX_ERR_VENC_SYS_NOTREADY = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_SYS_NOTREADY)
AX_ERR_VENC_INVALID_CHNID = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_INVALID_CHNID)
AX_ERR_VENC_NOMEM = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_NOMEM)
AX_ERR_VENC_NOT_MATCH = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_NOT_MATCH)
AX_ERR_VENC_INVALID_GRPID = AX_DEF_ERR(AX_ID_VENC, AX_ID_VENC_COMMON, AX_ERR_INVALID_GRPID)


def ax_venc_pack_to_dict(c_pack, pack):
    pack['phy_addr'] = c_pack.ulPhyAddr
    pack['vir_addr'] = cast(c_pack.pu8Addr, c_void_p).value
    pack['len'] = c_pack.u32Len
    pack['pts'] = c_pack.u64PTS
    pack['seq_num'] = c_pack.u64SeqNum
    pack['usr_data'] = c_pack.u64UserData
    pack['type'] = c_pack.enType
    pack['coding_type'] = c_pack.enCodingType
    pack['temporal_id'] = c_pack.u32TemporalID
    pack['nalu_num'] = c_pack.u32NaluNum
    pack['nalu_info'] = []
    for i in range(c_pack.u32NaluNum if c_pack.u32NaluNum <= VENC_MAX_NALU_NUM else VENC_MAX_NALU_NUM):
        if c_pack.enType == PT_H264:
            nalu_type = c_pack.stNaluInfo[i].unNaluType.enH264EType
        elif c_pack.enType == PT_H265:
            nalu_type = c_pack.stNaluInfo[i].unNaluType.enH265EType
        elif c_pack.enType == PT_JPEG:
            nalu_type = c_pack.stNaluInfo[i].unNaluType.enJPEGEType
        pack['nalu_info'].append({'nalu_type': nalu_type,
                                  'nalu_offset': c_pack.stNaluInfo[i].u32NaluOffset,
                                  'nalu_length': c_pack.stNaluInfo[i].u32NaluLength})


def dict_to_ax_venc_pack(pack, c_pack):
    c_pack.ulPhyAddr = pack.get('phy_addr', 0)
    c_pack.pu8Addr = cast(pack.get('vir_addr', 0), POINTER(AX_U8))
    c_pack.u32Len = pack.get('len', 0)
    c_pack.u64PTS = pack.get('pts', 0)
    c_pack.u64SeqNum = pack.get('seq_num', 0)
    c_pack.u64UserData = pack.get('usr_data', 0)
    c_pack.enType = pack.get('type', 0)
    c_pack.enCodingType = pack.get('coding_type', 0)
    c_pack.u32TemporalID = pack.get('temporal_id', 0)
    nalu_info = pack.get('nalu_info')
    if nalu_info and isinstance(nalu_info, list):
        c_pack.u32NaluNum = len(nalu_info)
        for i in range(c_pack.u32NaluNum if c_pack.u32NaluNum <= VENC_MAX_NALU_NUM else VENC_MAX_NALU_NUM):
            if c_pack.enType == PT_H264:
                c_pack.stNaluInfo[i].unNaluType.enH264EType = nalu_info[i].get('nalu_type', 0)
            elif c_pack.enType == PT_H265:
                c_pack.stNaluInfo[i].unNaluType.enH265EType = nalu_info[i].get('nalu_type', 0)
            elif c_pack.enType == PT_JPEG:
                c_pack.stNaluInfo[i].unNaluType.enJPEGEType = nalu_info[i].get('nalu_type', 0)

            c_pack.stNaluInfo[i].u32NaluOffset = nalu_info[i].get('nalu_offset', 0)
            c_pack.stNaluInfo[i].u32NaluLength = nalu_info[i].get('nalu_length', 0)


def ax_venc_stream_info_u_to_dict(type, c_u_info, info):
    if type == PT_H264:
        h264_info = {}
        info['h264_info'] = h264_info
        h264_info['pic_bytes_num'] = c_u_info.stH264Info.u32PicBytesNum
        h264_info['inter_16x16mb_num'] = c_u_info.stH264Info.u32Inter16x16MbNum
        h264_info['inter_8x8mb_num'] = c_u_info.stH264Info.u32Inter8x8MbNum
        h264_info['intra_16mb_num'] = c_u_info.stH264Info.u32Intra16MbNum
        h264_info['intra_8mb_num'] = c_u_info.stH264Info.u32Intra8MbNum
        h264_info['intra_4mb_num'] = c_u_info.stH264Info.u32Intra4MbNum
        h264_info['ref_type'] = c_u_info.stH264Info.enRefType
        h264_info['update_attr_cnt'] = c_u_info.stH264Info.u32UpdateAttrCnt
        h264_info['start_qp'] = c_u_info.stH264Info.u32StartQp
        h264_info['mean_qp'] = c_u_info.stH264Info.u32MeanQp
        h264_info['p_skip'] = c_u_info.stH264Info.bPSkip
    elif type == PT_JPEG:
        jpeg_info = {}
        info['jpeg_info'] = jpeg_info
        jpeg_info['pic_bytes_num'] = c_u_info.stJpegInfo.u32PicBytesNum
        jpeg_info['update_attr_cnt'] = c_u_info.stJpegInfo.u32UpdateAttrCnt
        jpeg_info['q_factor'] = c_u_info.stJpegInfo.u32Qfactor
    elif type == PT_H265:
        h265_info = {}
        info['h265_info'] = h265_info
        h265_info['pic_bytes_num'] = c_u_info.stH265Info.u32PicBytesNum
        h265_info['inter_64x64cu_num'] = c_u_info.stH265Info.u32Inter64x64CuNum
        h265_info['inter_32x32cu_num'] = c_u_info.stH265Info.u32Inter32x32CuNum
        h265_info['inter_16x16cu_num'] = c_u_info.stH265Info.u32Inter16x16CuNum
        h265_info['inter_8x8cu_num'] = c_u_info.stH265Info.u32Inter8x8CuNum
        h265_info['intra_32x32cu_num'] = c_u_info.stH265Info.u32Intra32x32CuNum
        h265_info['intra_16x16cu_num'] = c_u_info.stH265Info.u32Intra16x16CuNum
        h265_info['intra_8x8cu_num'] = c_u_info.stH265Info.u32Intra8x8CuNum
        h265_info['intra_4x4cu_num'] = c_u_info.stH265Info.u32Intra4x4CuNum
        h265_info['ref_type'] = c_u_info.stH265Info.enRefType
        h265_info['update_attr_cnt'] = c_u_info.stH265Info.u32UpdateAttrCnt
        h265_info['start_qp'] = c_u_info.stH265Info.u32StartQp
        h265_info['mean_qp'] = c_u_info.stH265Info.u32MeanQp
        h265_info['p_skip'] = c_u_info.stH265Info.bPSkip


def dict_to_ax_venc_stream_info_u(type, info, c_u_info):
    if type == PT_H264:
        h264_info = info['h264_info']
        c_u_info.stH264Info.u32PicBytesNum = h264_info['pic_bytes_num']
        c_u_info.stH264Info.u32Inter16x16MbNum = h264_info['inter_16x16mb_num']
        c_u_info.stH264Info.u32Inter8x8MbNum = h264_info['inter_8x8mb_num']
        c_u_info.stH264Info.u32Intra16MbNum = h264_info['intra_16mb_num']
        c_u_info.stH264Info.u32Intra8MbNum = h264_info['intra_8mb_num']
        c_u_info.stH264Info.u32Intra4MbNum = h264_info['intra_4mb_num']
        c_u_info.stH264Info.enRefType = h264_info['ref_type']
        c_u_info.stH264Info.u32UpdateAttrCnt = h264_info['update_attr_cnt']
        c_u_info.stH264Info.u32StartQp = h264_info['start_qp']
        c_u_info.stH264Info.u32MeanQp = h264_info['mean_qp']
        c_u_info.stH264Info.bPSkip = h264_info['p_skip']
    elif type == PT_JPEG:
        jpeg_info = info['jpeg_info']
        c_u_info.stJpegInfo.u32PicBytesNum = jpeg_info['pic_bytes_num']
        c_u_info.stJpegInfo.u32UpdateAttrCnt = jpeg_info['update_attr_cnt']
        c_u_info.stJpegInfo.u32Qfactor = jpeg_info['q_factor']
    elif type == PT_H265:
        h265_info = info['h265_info']
        c_u_info.stH265Info.u32PicBytesNum = h265_info['pic_bytes_num']
        c_u_info.stH265Info.u32Inter64x64CuNum = h265_info['inter_64x64cu_num']
        c_u_info.stH265Info.u32Inter32x32CuNum = h265_info['inter_32x32cu_num']
        c_u_info.stH265Info.u32Inter16x16CuNum = h265_info['inter_16x16cu_num']
        c_u_info.stH265Info.u32Inter8x8CuNum = h265_info['inter_8x8cu_num']
        c_u_info.stH265Info.u32Intra32x32CuNum = h265_info['intra_32x32cu_num']
        c_u_info.stH265Info.u32Intra16x16CuNum = h265_info['intra_16x16cu_num']
        c_u_info.stH265Info.u32Intra8x8CuNum = h265_info['intra_8x8cu_num']
        c_u_info.stH265Info.u32Intra4x4CuNum = h265_info['intra_4x4cu_num']
        c_u_info.stH265Info.enRefType = h265_info['ref_type']
        c_u_info.stH265Info.u32UpdateAttrCnt = h265_info['update_attr_cnt']
        c_u_info.stH265Info.u32StartQp = h265_info['start_qp']
        c_u_info.stH265Info.u32MeanQp = h265_info['mean_qp']
        c_u_info.stH265Info.bPSkip = h265_info['p_skip']


def ax_venc_stream_advance_info_u_to_dict(type, c_advance_u_info, info):
    if type == PT_H264:
        advance_h264_info = {}
        info['advance_h264_info'] = advance_h264_info
        advance_h264_info['residual_bit_num'] = c_advance_u_info.stAdvanceH264Info.u32ResidualBitNum
        advance_h264_info['head_bit_num'] = c_advance_u_info.stAdvanceH264Info.u32HeadBitNum
        advance_h264_info['madi_val'] = c_advance_u_info.stAdvanceH264Info.u32MadiVal
        advance_h264_info['madp_val'] = c_advance_u_info.stAdvanceH264Info.u32MadpVal
        advance_h264_info['psnr_val'] = c_advance_u_info.stAdvanceH264Info.f64PSNRVal
        advance_h264_info['mse_lcu_cnt'] = c_advance_u_info.stAdvanceH264Info.u32MseLcuCnt
        advance_h264_info['mse_sum'] = c_advance_u_info.stAdvanceH264Info.u32MseSum
        advance_h264_info['sse_info'] = []
        for sse in c_advance_u_info.stAdvanceH264Info.stSSEInfo:
            sse_dict = {
                "sse_en": False if sse.bSSEEn == AX_FALSE else True,
                "sse_val": sse.u32SSEVal
            }
            advance_h264_info['sse_info'].append(sse_dict)
        advance_h264_info['qp_hst_grm'] = list(c_advance_u_info.stAdvanceH264Info.u32QpHstgrm)
        advance_h264_info['move_scene_16x16_num'] = c_advance_u_info.stAdvanceH264Info.u32MoveScene16x16Num
        advance_h264_info['move_scene_bits'] = c_advance_u_info.stAdvanceH264Info.u32MoveSceneBits
    elif type == PT_JPEG:
        info['advance_jpeg_info'] = {}
    elif type == PT_H265:
        advance_h265_info = {}
        info['advance_h265_info'] = advance_h265_info
        advance_h265_info['residual_bit_num'] = c_advance_u_info.stAdvanceH265Info.u32ResidualBitNum
        advance_h265_info['head_bit_num'] = c_advance_u_info.stAdvanceH265Info.u32HeadBitNum
        advance_h265_info['madi_val'] = c_advance_u_info.stAdvanceH265Info.u32MadiVal
        advance_h265_info['madp_val'] = c_advance_u_info.stAdvanceH265Info.u32MadpVal
        advance_h265_info['psnr_val'] = c_advance_u_info.stAdvanceH265Info.f64PSNRVal
        advance_h265_info['mse_lcu_cnt'] = c_advance_u_info.stAdvanceH265Info.u32MseLcuCnt
        advance_h265_info['mse_sum'] = c_advance_u_info.stAdvanceH265Info.u32MseSum
        advance_h265_info['sse_info'] = []
        for sse in c_advance_u_info.stAdvanceH265Info.stSSEInfo:
            sse_dict = {
                "sse_en": False if sse.bSSEEn == AX_FALSE else True,
                "sse_val": sse.u32SSEVal
            }
            advance_h265_info['sse_info'].append(sse_dict)
        advance_h265_info['qp_hst_grm'] = list(c_advance_u_info.stAdvanceH265Info.u32QpHstgrm)
        advance_h265_info['move_scene_32x32_num'] = c_advance_u_info.stAdvanceH265Info.u32MoveScene32x32Num
        advance_h265_info['move_scene_bits'] = c_advance_u_info.stAdvanceH265Info.u32MoveSceneBits


def dict_to_ax_venc_stream_advance_info_u(type, info, c_advance_u_info):
    if type == PT_H264:
        h264_advance_info = info['advance_h264_info']
        c_advance_u_info.stAdvanceH264Info.u32ResidualBitNum = h264_advance_info['residual_bit_num']
        c_advance_u_info.stAdvanceH264Info.u32HeadBitNum = h264_advance_info['head_bit_num']
        c_advance_u_info.stAdvanceH264Info.u32MadiVal = h264_advance_info['madi_val']
        c_advance_u_info.stAdvanceH264Info.u32MadpVal = h264_advance_info['madp_val']
        c_advance_u_info.stAdvanceH264Info.f64PSNRVal = h264_advance_info['psnr_val']
        c_advance_u_info.stAdvanceH264Info.u32MseLcuCnt = h264_advance_info['mse_lcu_cnt']
        c_advance_u_info.stAdvanceH264Info.u32MseSum = h264_advance_info['mse_sum']
        for i in range(8):
            c_advance_u_info.stAdvanceH264Info.stSSEInfo[i].bSSEEn = h264_advance_info['sse_info'][i]['sse_en']
            c_advance_u_info.stAdvanceH264Info.stSSEInfo[i].u32SSEVal = h264_advance_info['sse_info'][i]['sse_val']
        for i in range(VENC_QP_HISGRM_NUM):
            c_advance_u_info.stAdvanceH264Info.u32QpHstgrm[i] = h264_advance_info['qp_hst_grm'][i]
        c_advance_u_info.stAdvanceH264Info.u32MoveScene16x16Num = h264_advance_info['move_scene_16x16_num']
        c_advance_u_info.stAdvanceH264Info.u32MoveSceneBits = h264_advance_info['move_scene_bits']
    elif type == PT_JPEG:
        pass
    elif type == PT_H265:
        h265_advance_info = info['advance_h265_info']
        c_advance_u_info.stAdvanceH265Info.u32ResidualBitNum = h265_advance_info['residual_bit_num']
        c_advance_u_info.stAdvanceH265Info.u32HeadBitNum = h265_advance_info['head_bit_num']
        c_advance_u_info.stAdvanceH265Info.u32MadiVal = h265_advance_info['madi_val']
        c_advance_u_info.stAdvanceH265Info.u32MadpVal = h265_advance_info['madp_val']
        c_advance_u_info.stAdvanceH265Info.f64PSNRVal = h265_advance_info['psnr_val']
        c_advance_u_info.stAdvanceH265Info.u32MseLcuCnt = h265_advance_info['mse_lcu_cnt']
        c_advance_u_info.stAdvanceH265Info.u32MseSum = h265_advance_info['mse_sum']
        for i in range(8):
            c_advance_u_info.stAdvanceH265Info.stSSEInfo[i].bSSEEn = h265_advance_info['sse_info'][i]['sse_en']
            c_advance_u_info.stAdvanceH265Info.stSSEInfo[i].u32SSEVal = h265_advance_info['sse_info'][i]['sse_val']
        for i in range(VENC_QP_HISGRM_NUM):
            c_advance_u_info.stAdvanceH265Info.u32QpHstgrm[i] = h265_advance_info['qp_hst_grm'][i]
        c_advance_u_info.stAdvanceH265Info.u32MoveScene32x32Num = h265_advance_info['move_scene_32x32_num']
        c_advance_u_info.stAdvanceH265Info.u32MoveSceneBits = h265_advance_info['move_scene_bits']


def ax_venc_stream_to_dict(c_stream, stream):
    pack = {}
    stream['pack'] = pack
    ax_venc_pack_to_dict(c_stream.stPack, pack)
    ax_venc_stream_info_u_to_dict(c_stream.stPack.enType, c_stream.uInfo, stream)
    ax_venc_stream_advance_info_u_to_dict(c_stream.stPack.enType, c_stream.uAdvanceInfo, stream)


def dict_to_ax_venc_stream(stream, c_stream):
    pack = stream.get('pack')
    if pack:
        dict_to_ax_venc_pack(pack, c_stream.stPack)
    dict_to_ax_venc_stream_info_u(c_stream.stPack.enType, stream, c_stream.uInfo)
    dict_to_ax_venc_stream_advance_info_u(c_stream.stPack.enType, stream, c_stream.uAdvanceInfo)
