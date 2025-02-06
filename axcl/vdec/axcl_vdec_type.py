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

from ctypes import Structure, c_int32, c_uint32, c_void_p, c_char, c_uint64
from enum import IntEnum
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.ax_global_type import *
from axcl.utils.axcl_basestructure import *

AX_VDEC_MAX_GRP_NUM = DEF_ALL_MOD_GRP_MAX
AX_VDEC_MAX_CHN_NUM = 3
AX_JDEC_MAX_CHN_NUM = 1
AX_DEC_MAX_CHN_NUM = AX_VDEC_MAX_CHN_NUM

AX_VDEC_MAX_WIDTH = 8192
AX_VDEC_MAX_HEIGHT = 8192
AX_VDEC_MIN_WIDTH = 144
AX_VDEC_MIN_HEIGHT = 144
AX_VDEC_OUTPUT_MIN_WIDTH = 48
AX_VDEC_OUTPUT_MIN_HEIGHT = 48

AX_VDEC_CH1_SCALE_MAX_WIDTH = 4096
AX_VDEC_CH1_SCALE_MAX_HEIGHT = 4096
AX_VDEC_CH2_SCALE_MAX_WIDTH = 1920
AX_VDEC_CH2_SCALE_MAX_HEIGHT = 1080

AX_JDEC_MAX_WIDTH = 32768
AX_JDEC_MAX_HEIGHT = 32768
AX_JDEC_MIN_WIDTH = 48
AX_JDEC_MIN_HEIGHT = 48

AX_VDEC_MAX_OUTPUT_FIFO_DEPTH = 34
AX_VDEC_MIN_OUTPUT_FIFO_DEPTH = 0

AX_VDEC_FBC_COMPRESS_LEVEL_MAX = 10

AX_MAX_VDEC_USER_DATA_SIZE = 2048

AX_MAX_VDEC_USER_DATA_CNT = 20

# 2 byte for length
AX_MAX_JDEC_USER_DATA_SIZE = 0xFFFF - 2

AX_VDEC_ALIGN_NUM = 8

AX_VDEC_GRP = AX_S32
AX_VDEC_CHN = AX_S32

AX_VDEC_ENABLE_MOD_E = AX_S32
"""
    Active module type.

    .. parsed-literal::

        AX_ENABLE_VDEC_NONE      = -1
        AX_ENABLE_BOTH_VDEC_JDEC = 0    # VDEC and JDEC
        AX_ENABLE_ONLY_VDEC      = 1
        AX_ENABLE_ONLY_JDEC      = 2
"""
AX_ENABLE_VDEC_NONE = -1
AX_ENABLE_BOTH_VDEC_JDEC = 0
AX_ENABLE_ONLY_VDEC = 1
AX_ENABLE_ONLY_JDEC = 2


class AX_VDEC_MOD_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_mod_attr = {
            "max_group_count": int,
            "dec_module": :class:`AX_VDEC_ENABLE_MOD_E <axcl.vdec.axcl_vdec_type.AX_VDEC_ENABLE_MOD_E>`,
            "vdec_mc": bool,
            "vdec_virt_chn": int
        }
    """
    _fields_ = [
        ("u32MaxGroupCount", AX_U32),
        ("enDecModule", AX_VDEC_ENABLE_MOD_E),
        ("bVdecMc", AX_BOOL),
        ("VdecVirtChn", AX_VDEC_CHN)
    ]
    field_aliases = {
        "u32MaxGroupCount": "max_group_count",
        "enDecModule": "dec_module",
        "bVdecMc": "vdec_mc",
        "VdecVirtChn": "vdec_virt_chn"
    }


AX_VDEC_INPUT_MODE_E = AX_S32
"""
    Input mode of stream.

    .. parsed-literal::

        AX_VDEC_INPUT_MODE_NAL    = 0
        AX_VDEC_INPUT_MODE_FRAME  = 1  # recommended
        AX_VDEC_INPUT_MODE_SLICE  = 2  # not support
        AX_VDEC_INPUT_MODE_STREAM = 3
        AX_VDEC_INPUT_MODE_COMPAT = 4  # not support
        AX_VDEC_INPUT_MODE_BUTT   = 5
"""
AX_VDEC_INPUT_MODE_NAL = 0
AX_VDEC_INPUT_MODE_FRAME = 1
AX_VDEC_INPUT_MODE_SLICE = 2
AX_VDEC_INPUT_MODE_STREAM = 3
AX_VDEC_INPUT_MODE_COMPAT = 4
AX_VDEC_INPUT_MODE_BUTT = 5


class AX_VDEC_GRP_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_grp_attr = {
            "codec_type": :class:`AX_PAYLOAD_TYPE_E <axcl.ax_global_type.AX_PAYLOAD_TYPE_E>`,
            "input_mode": :class:`AX_VDEC_INPUT_MODE_E <axcl.vdec.axcl_vdec_type.AX_VDEC_INPUT_MODE_E>`,
            "max_pic_width": int,
            "max_pic_height": int,
            "stream_buf_size": int,
            "sdk_auto_frame_pool": bool,
            "skip_sdk_stream_pool": bool,
            "stream_buf_addr": :class:`AX_MEMORY_ADDR_T <axcl.ax_global_type.AX_MEMORY_ADDR_T>`
        }

    .. note::

        - `input_mode`: recommend to AX_VDEC_INPUT_MODE_FRAME
        - `stream_buf_size`: `max_pic_width` * `max_pic_height` * 2
        - `sdk_auto_frame_pool`: set 1 to uses private pool.
    """
    _fields_ = [
        ("enCodecType", AX_PAYLOAD_TYPE_E),
        ("enInputMode", AX_VDEC_INPUT_MODE_E),
        ("u32MaxPicWidth", AX_U32),
        ("u32MaxPicHeight", AX_U32),
        ("u32StreamBufSize", AX_U32),
        ("bSdkAutoFramePool", AX_BOOL),
        ("bSkipSdkStreamPool", AX_BOOL),
        ("stStreamBufAddr", AX_MEMORY_ADDR_T)
    ]
    field_aliases = {
        "enCodecType": "codec_type",
        "enInputMode": "input_mode",
        "u32MaxPicWidth": "max_pic_width",
        "u32MaxPicHeight": "max_pic_height",
        "u32StreamBufSize": "stream_buf_size",
        "bSdkAutoFramePool": "sdk_auto_frame_pool",
        "bSkipSdkStreamPool": "skip_sdk_stream_pool",
        "stStreamBufAddr": "stream_buf_addr"
    }


class AX_VDEC_STREAM_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_stream = {
            "pts": int,
            "private_data": int,
            "end_of_frame": bool,
            "end_of_stream": bool,
            "skip_display": bool,
            "stream_pack_len": int,
            "addr": int,
            "phy_addr": int,
            "user_data": int
        }

    .. note::

        - SDK bypass `pts` and `user_data` to next modules
        - If all streams have been sent, set `end_of_stream` to 1
    """
    _fields_ = [
        ("u64PTS", AX_U64),
        ("u64PrivateData", AX_U64),
        ("bEndOfFrame", AX_BOOL),
        ("bEndOfStream", AX_BOOL),
        ("bSkipDisplay", AX_BOOL),
        ("u32StreamPackLen", AX_U32),
        ("pu8Addr", POINTER(AX_U8)),
        ("u64PhyAddr", AX_U64),
        ("u64UserData", AX_U64)
    ]
    field_aliases = {
        "u64PTS": "pts",
        "u64PrivateData": "private_data",
        "bEndOfFrame": "end_of_frame",
        "bEndOfStream": "end_of_stream",
        "bSkipDisplay": "skip_display",
        "u32StreamPackLen": "stream_pack_len",
        "pu8Addr": "addr",
        "u64PhyAddr": "phy_addr",
        "u64UserData": "user_data"
    }


AX_VDEC_OUTPUT_ORDER_E = AX_S32
"""
    vdec output order

    .. parsed-literal::

        AX_VDEC_OUTPUT_ORDER_DISP = 0
        AX_VDEC_OUTPUT_ORDER_DEC  = 1
        AX_VDEC_OUTPUT_ORDER_BUTT = 2

    .. note::

        If decode and display sequence is same, recommend to AX_VDEC_OUTPUT_ORDER_DEC.
"""
AX_VDEC_OUTPUT_ORDER_DISP = 0
AX_VDEC_OUTPUT_ORDER_DEC = 1
AX_VDEC_OUTPUT_ORDER_BUTT = 2


AX_VDEC_MODE_E = AX_S32
"""
    vdec mode

    .. parsed-literal::

        VIDEO_DEC_MODE_IPB  = 0
        VIDEO_DEC_MODE_IP   = 1
        VIDEO_DEC_MODE_I    = 2
        VIDEO_DEC_MODE_GDR  = 3
        VIDEO_DEC_MODE_BUTT = 4
"""
VIDEO_DEC_MODE_IPB = 0
VIDEO_DEC_MODE_IP = 1
VIDEO_DEC_MODE_I = 2
VIDEO_DEC_MODE_GDR = 3
VIDEO_DEC_MODE_BUTT = 4


class AX_VDEC_PARAM_VIDEO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_param_video = {
            "output_order": :class:`AX_VDEC_OUTPUT_ORDER_E <axcl.vdec.axcl_vdec_type.AX_VDEC_OUTPUT_ORDER_E>`,
            "vdec_mode": :class:`AX_VDEC_MODE_E <axcl.vdec.axcl_vdec_type.AX_VDEC_MODE_E>`
        }
    """
    _fields_ = [
        ("enOutputOrder", AX_VDEC_OUTPUT_ORDER_E),
        ("enVdecMode", AX_VDEC_MODE_E)
    ]
    field_aliases = {
        "enOutputOrder": "output_order",
        "enVdecMode": "vdec_mode"
    }


class AX_VDEC_GRP_PARAM_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_grp_param = {
            "vdec_video_param": :class:`AX_VDEC_PARAM_VIDEO_T <axcl.vdec.axcl_vdec_type.AX_VDEC_PARAM_VIDEO_T>`,
            "src_frm_rate": int
        }
    """
    _fields_ = [
        ("stVdecVideoParam", AX_VDEC_PARAM_VIDEO_T),
        ("f32SrcFrmRate", AX_F32)
    ]
    field_aliases = {
        "stVdecVideoParam": "vdec_video_param",
        "f32SrcFrmRate": "src_frm_rate"
    }


class AX_VDEC_RECV_PIC_PARAM_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_recv_pic_param = {
            "recv_pic_num": int
        }
    """
    _fields_ = [
        ("s32RecvPicNum", AX_S32)
    ]
    field_aliases = {
        "s32RecvPicNum": "recv_pic_num"
    }


AX_VDEC_OUTPUT_MODE_E = AX_S32
"""
    vdec output mode

    .. parsed-literal::

        AX_VDEC_OUTPUT_ORIGINAL  = 0
        AX_VDEC_OUTPUT_CROP      = 1
        AX_VDEC_OUTPUT_SCALE     = 2
        AX_VDEC_OUTPUT_MODE_BUTT = 3

    .. seealso::

        For limitation of channel output mode, refer to :func:`set_chn_attr <axcl.vdec.axcl_vdec.set_chn_attr>`
"""
AX_VDEC_OUTPUT_ORIGINAL = 0
AX_VDEC_OUTPUT_CROP = 1
AX_VDEC_OUTPUT_SCALE = 2
AX_VDEC_OUTPUT_MODE_BUTT = 3


class AX_VDEC_FRAME_RATE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_frame_rate_ctrl = {
            "dst_frm_rate": int,
            "frm_rate_ctrl": bool
        }
    """
    _fields_ = [
        ("f32DstFrmRate", AX_F32),
        ("bFrmRateCtrl", AX_BOOL)
    ]
    field_aliases = {
        "f32DstFrmRate": "dst_frm_rate",
        "bFrmRateCtrl": "frm_rate_ctrl"
    }


class AX_VDEC_CHN_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_chn_attr = {
            "pic_width": int,
            "pic_height": int,
            "frame_stride": int,
            "frame_padding": int,
            "crop_x": int,
            "crop_y": int,
            "scale_ratio_x": int,
            "scale_ratio_y": int,
            "output_fifo_depth": int,
            "frame_buf_cnt": int,
            "frame_buf_size": int,
            "output_mode": :class:`AX_VDEC_OUTPUT_MODE_E <axcl.vdec.axcl_vdec_type.AX_VDEC_OUTPUT_MODE_E>`,
            "img_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "compress_info": :class:`AX_FRAME_COMPRESS_INFO_T <axcl.ax_global_type.AX_FRAME_COMPRESS_INFO_T>`,
            "output_frm_rate": :class:`AX_VDEC_FRAME_RATE_CTRL_T <axcl.vdec.axcl_vdec_type.AX_VDEC_FRAME_RATE_CTRL_T>`
        }

    .. note::

        - `frame_stride` must be aligned to 256.
        - `output_fifo_depth` must be greater than 1.
    """
    _fields_ = [
        ("u32PicWidth", AX_U32),
        ("u32PicHeight", AX_U32),
        ("u32FrameStride", AX_U32),
        ("u32FramePadding", AX_U32),
        ("u32CropX", AX_U32),
        ("u32CropY", AX_U32),
        ("u32ScaleRatioX", AX_U32),
        ("u32ScaleRatioY", AX_U32),
        ("u32OutputFifoDepth", AX_U32),
        ("u32FrameBufCnt", AX_U32),
        ("u32FrameBufSize", AX_U32),
        ("enOutputMode", AX_VDEC_OUTPUT_MODE_E),
        ("enImgFormat", AX_IMG_FORMAT_E),
        ("stCompressInfo", AX_FRAME_COMPRESS_INFO_T),
        ("stOutputFrmRate", AX_VDEC_FRAME_RATE_CTRL_T)
    ]
    field_aliases = {
        "u32PicWidth": "pic_width",
        "u32PicHeight": "pic_height",
        "u32FrameStride": "frame_stride",
        "u32FramePadding": "frame_padding",
        "u32CropX": "crop_x",
        "u32CropY": "crop_y",
        "u32ScaleRatioX": "scale_ratio_x",
        "u32ScaleRatioY": "scale_ratio_y",
        "u32OutputFifoDepth": "output_fifo_depth",
        "u32FrameBufCnt": "frame_buf_cnt",
        "u32FrameBufSize": "frame_buf_size",
        "enOutputMode": "output_mode",
        "enImgFormat": "img_format",
        "stCompressInfo": "compress_info",
        "stOutputFrmRate": "output_frm_rate"
    }


class AX_VDEC_DECODE_ERROR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_decode_error = {
            "format_err": int,
            "pic_size_err_set": int,
            "stream_unsprt": int,
            "pack_err": int,
            "ref_err_set": int,
            "pic_buf_size_err_set": int,
            "stream_size_over": int,
            "vdec_stream_not_release": int
        }
    """
    _fields_ = [
        ("s32FormatErr", AX_S32),
        ("s32PicSizeErrSet", AX_S32),
        ("s32StreamUnsprt", AX_S32),
        ("s32PackErr", AX_S32),
        ("s32RefErrSet", AX_S32),
        ("s32PicBufSizeErrSet", AX_S32),
        ("s32StreamSizeOver", AX_S32),
        ("s32VdecStreamNotRelease", AX_S32)
    ]
    field_aliases = {
        "s32FormatErr": "format_err",
        "s32PicSizeErrSet": "pic_size_err_set",
        "s32StreamUnsprt": "stream_unsprt",
        "s32PackErr": "pack_err",
        "s32RefErrSet": "ref_err_set",
        "s32PicBufSizeErrSet": "pic_buf_size_err_set",
        "s32StreamSizeOver": "stream_size_over",
        "s32VdecStreamNotRelease": "vdec_stream_not_release"
    }


class AX_VDEC_GRP_STATUS_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_grp_status = {
            "codec_type": :class:`AX_PAYLOAD_TYPE_E <axcl.ax_global_type.AX_PAYLOAD_TYPE_E>`,
            "left_stream_bytes": int,
            "left_stream_frames": int,
            "left_pics": [int],
            "start_recv_stream": bool,
            "recv_stream_frames": int,
            "decode_stream_frames": int,
            "pic_width": int,
            "pic_height": int,
            "input_fifo_is_full": bool,
            "vdec_dec_err": :class:`AX_VDEC_DECODE_ERROR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_DECODE_ERROR_T>`
        }
    """
    _fields_ = [
        ("enCodecType", AX_PAYLOAD_TYPE_E),
        ("u32LeftStreamBytes", AX_U32),
        ("u32LeftStreamFrames", AX_U32),
        ("u32LeftPics", AX_U32 * AX_DEC_MAX_CHN_NUM),
        ("bStartRecvStream", AX_BOOL),
        ("u32RecvStreamFrames", AX_U32),
        ("u32DecodeStreamFrames", AX_U32),
        ("u32PicWidth", AX_U32),
        ("u32PicHeight", AX_U32),
        ("bInputFifoIsFull", AX_BOOL),
        ("stVdecDecErr", AX_VDEC_DECODE_ERROR_T)
    ]
    field_aliases = {
        "enCodecType": "codec_type",
        "u32LeftStreamBytes": "left_stream_bytes",
        "u32LeftStreamFrames": "left_stream_frames",
        "u32LeftPics": "left_pics",
        "bStartRecvStream": "start_recv_stream",
        "u32RecvStreamFrames": "recv_stream_frames",
        "u32DecodeStreamFrames": "decode_stream_frames",
        "u32PicWidth": "pic_width",
        "u32PicHeight": "pic_height",
        "bInputFifoIsFull": "input_fifo_is_full",
        "stVdecDecErr": "vdec_dec_err"
    }


class AX_VDEC_USERDATA_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_userdata = {
            "phy_addr": int,
            "user_data_cnt": int,
            "len": int,
            "buf_size": int,
            "data_len": [int],
            "valid": bool,
            "addr": int
        }
    """
    _fields_ = [
        ("u64PhyAddr", AX_U64),
        ("u32UserDataCnt", AX_U32),
        ("u32Len", AX_U32),
        ("u32BufSize", AX_U32),
        ("u32DataLen", AX_U32 * AX_MAX_VDEC_USER_DATA_CNT),
        ("bValid", AX_BOOL),
        ("pu8Addr", POINTER(AX_U8))
    ]
    field_aliases = {
        "u64PhyAddr": "phy_addr",
        "u32UserDataCnt": "user_data_cnt",
        "u32Len": "len",
        "u32BufSize": "buf_size",
        "u32DataLen": "data_len",
        "bValid": "valid",
        "pu8Addr": "addr"
    }


AX_VDEC_DISPLAY_MODE_E = AX_S32
"""
    vdec display mode

    .. parsed-literal::

        AX_VDEC_DISPLAY_MODE_PREVIEW  = 0
        AX_VDEC_DISPLAY_MODE_PLAYBACK = 1
        AX_VDEC_DISPLAY_MODE_BUTT     = 2
"""
AX_VDEC_DISPLAY_MODE_PREVIEW = 0
AX_VDEC_DISPLAY_MODE_PLAYBACK = 1
AX_VDEC_DISPLAY_MODE_BUTT = 2


class AX_VDEC_GRP_CHN_SET(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_grp_chn_set = {
            "grp": int,
            "chn_count": int,
            "chn": [int],
            "chn_frame_num": [int]
        }
    """
    _fields_ = [
        ("VdGrp", AX_VDEC_GRP),
        ("u32ChnCount", AX_U32),
        ("VdChn", AX_VDEC_CHN * AX_DEC_MAX_CHN_NUM),
        ("u64ChnFrameNum", AX_U64 * AX_DEC_MAX_CHN_NUM)
    ]
    field_aliases = {
        "VdGrp": "grp",
        "u32ChnCount": "chn_count",
        "VdChn": "chn",
        "u64ChnFrameNum": "chn_frame_num"
    }


class AX_VDEC_GRP_SET_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_grp_set_info = {
            "grp_count": int,
            "chn_set": [:class:`AX_VDEC_GRP_CHN_SET <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_CHN_SET>`]
        }
    """
    _fields_ = [
        ("u32GrpCount", AX_U32),
        ("stChnSet", AX_VDEC_GRP_CHN_SET * AX_VDEC_MAX_GRP_NUM)
    ]
    field_aliases = {
        "u32GrpCount": "grp_count",
        "stChnSet": "chn_set"
    }


class AX_VDEC_DEC_ONE_FRM_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_dec_one_frm = {
            "stream": :class:`AX_VDEC_STREAM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_STREAM_T>`,
            "frame": :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`,
            "output_mode": :class:`AX_VDEC_OUTPUT_MODE_E <axcl.vdec.axcl_vdec_type.AX_VDEC_OUTPUT_MODE_E>`,
            "img_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`
        }
    """
    _fields_ = [
        ("stStream", AX_VDEC_STREAM_T),
        ("stFrame", AX_VIDEO_FRAME_T),
        ("enOutputMode", AX_VDEC_OUTPUT_MODE_E),
        ("enImgFormat", AX_IMG_FORMAT_E)
    ]
    field_aliases = {
        "stStream": "stream",
        "stFrame": "frame",
        "enOutputMode": "output_mode",
        "enImgFormat": "img_format"
    }


class AX_VDEC_STREAM_BUF_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_stream_buf_info = {
            "phy_start": int,
            "vir_start": int,
            "total_size": int,
            "readable_size": int,
            "writeable_size": int,
            "read_offset": int,
            "write_offset": int
        }
    """
    _fields_ = [
        ("phyStart", AX_U64),
        ("virStart", POINTER(AX_U8)),
        ("totalSize", AX_U32),
        ("readAbleSize", AX_U32),
        ("writeAbleSize", AX_U32),
        ("readOffset", AX_U32),
        ("writeOffset", AX_U32)
    ]
    field_aliases = {
        "phyStart": "phy_start",
        "virStart": "vir_start",
        "totalSize": "total_size",
        "readAbleSize": "readable_size",
        "writeAbleSize": "writeable_size",
        "readOffset": "read_offset",
        "writeOffset": "write_offset"
    }


AX_VDEC_SUB_ID_E = AX_S32
AX_ID_VDEC_NULL = 1
AX_VDEC_SUB_ID_E = 2


class AX_VDEC_VUI_ASPECT_RATIO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_vui_aspect_ratio = {
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
        ("aspect_ratio_idc", AX_U8),
        ("overscan_info_present_flag", AX_U8),
        ("overscan_appropriate_flag", AX_U8),
        ("sar_width", AX_U16),
        ("sar_height", AX_U16)
    ]
    field_aliases = {
        "aspect_ratio_info_present_flag": "aspect_ratio_info_present_flag",
        "aspect_ratio_idc": "aspect_ratio_idc",
        "overscan_info_present_flag": "overscan_info_present_flag",
        "overscan_appropriate_flag": "overscan_appropriate_flag",
        "sar_width": "sar_width",
        "sar_height": "sar_height"
    }


class AX_VDEC_VUI_TIME_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_vuiime_info = {
            "timing_info_present_flag": int,
            "num_units_in_tick": int,
            "time_scale": int,
            "fixed_frame_rate_flag": int,
            "num_ticks_poc_diff_one_minus1": int
        }
    """
    _fields_ = [
        ("timing_info_present_flag", AX_U8),
        ("num_units_in_tick", AX_U32),
        ("time_scale", AX_U32),
        ("fixed_frame_rate_flag", AX_U8),
        ("num_ticks_poc_diff_one_minus1", AX_U32)
    ]
    field_aliases = {
        "timing_info_present_flag": "timing_info_present_flag",
        "num_units_in_tick": "num_units_in_tick",
        "time_scale": "time_scale",
        "fixed_frame_rate_flag": "fixed_frame_rate_flag",
        "num_ticks_poc_diff_one_minus1": "num_ticks_poc_diff_one_minus1"
    }


class AX_VDEC_VUI_VIDEO_SIGNAL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_vui_video_signal = {
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
        ("video_format", AX_U8),
        ("video_full_range_flag", AX_U8),
        ("colour_description_present_flag", AX_U8),
        ("colour_primaries", AX_U8),
        ("transfer_characteristics", AX_U8),
        ("matrix_coefficients", AX_U8)
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


class AX_VDEC_VUI_BITSTREAM_RESTRIC_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_vui_bitstream_restric = {
            "bitstream_restriction_flag": int
        }
    """
    _fields_ = [
        ("bitstream_restriction_flag", AX_U8)
    ]
    field_aliases = {
        "bitstream_restriction_flag": "bitstream_restriction_flag"
    }


class AX_VDEC_VUI_PARAM_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_vui_param = {
            "vui_aspect_ratio": :class:`AX_VDEC_VUI_ASPECT_RATIO_T <axcl.vdec.axcl_vdec_type.AX_VDEC_VUI_ASPECT_RATIO_T>`,
            "vui_time_info": :class:`AX_VDEC_VUI_TIME_INFO_T <axcl.vdec.axcl_vdec_type.AX_VDEC_VUI_TIME_INFO_T>`,
            "vui_video_signal": :class:`AX_VDEC_VUI_VIDEO_SIGNAL_T <axcl.vdec.axcl_vdec_type.AX_VDEC_VUI_VIDEO_SIGNAL_T>`,
            "vui_bit_stream_restric": :class:`AX_VDEC_VUI_BITSTREAM_RESTRIC_T <axcl.vdec.axcl_vdec_type.AX_VDEC_VUI_BITSTREAM_RESTRIC_T>`
        }
    """
    _fields_ = [
        ("stVuiAspectRatio", AX_VDEC_VUI_ASPECT_RATIO_T),
        ("stVuiTimeInfo", AX_VDEC_VUI_TIME_INFO_T),
        ("stVuiVideoSignal", AX_VDEC_VUI_VIDEO_SIGNAL_T),
        ("stVuiBitstreamRestric", AX_VDEC_VUI_BITSTREAM_RESTRIC_T)
    ]
    field_aliases = {
        "stVuiAspectRatio": "vui_aspect_ratio",
        "stVuiTimeInfo": "vui_time_info",
        "stVuiVideoSignal": "vui_video_signal",
        "stVuiBitstreamRestric": "vui_bit_stream_restric"
    }


class AX_VDEC_USRPIC_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_usrpic = {
            "frm_info": [:class:`AX_VIDEO_FRAME_INFO_T <axcl.ax_global_type.AX_VIDEO_FRAME_INFO_T>`],
            "instant": bool,
            "enable": [bool]
        }
    """
    _fields_ = [
        ("stFrmInfo", AX_VIDEO_FRAME_INFO_T * AX_DEC_MAX_CHN_NUM),
        ("bInstant", AX_BOOL),
        ("bEnable", AX_BOOL * AX_DEC_MAX_CHN_NUM)
    ]
    field_aliases = {
        "stFrmInfo": "frm_info",
        "bInstant": "instant",
        "bEnable": "enable"
    }


class AX_VDEC_BITSTREAM_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_vdec_bitstream_info = {
            "width": int,
            "height": int,
            "ref_frames_num": int,
            "bit_depth_y": int,
            "bit_depth_c": int
        }
    """
    _fields_ = [
        ("u32Width", AX_U32),
        ("u32Height", AX_U32),
        ("u32RefFramesNum", AX_U32),
        ("u32BitDepthY", AX_U32),
        ("u32BitDepthC", AX_U32)
    ]
    field_aliases = {
        "u32Width": "width",
        "u32Height": "height",
        "u32RefFramesNum": "ref_frames_num",
        "u32BitDepthY": "bit_depth_y",
        "u32BitDepthC": "bit_depth_c"
    }

AX_ERR_VDEC_INVALID_GRPID = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_INVALID_GRPID)
AX_ERR_VDEC_INVALID_CHNID = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_INVALID_CHNID)
AX_ERR_VDEC_ILLEGAL_PARAM = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_ILLEGAL_PARAM)
AX_ERR_VDEC_NULL_PTR = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NULL_PTR)
AX_ERR_VDEC_BAD_ADDR = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_BAD_ADDR)
AX_ERR_VDEC_SYS_NOTREADY = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_SYS_NOTREADY)
AX_ERR_VDEC_BUSY  = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_BUSY)
AX_ERR_VDEC_NOT_INIT = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NOT_INIT)
AX_ERR_VDEC_NOT_CONFIG = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NOT_CONFIG)
AX_ERR_VDEC_NOT_SUPPORT = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NOT_SUPPORT)
AX_ERR_VDEC_NOT_PERM = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NOT_PERM)
AX_ERR_VDEC_EXIST = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_EXIST)
AX_ERR_VDEC_UNEXIST = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_UNEXIST)
AX_ERR_VDEC_NOMEM = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NOMEM)
AX_ERR_VDEC_NOBUF = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NOBUF)
AX_ERR_VDEC_NOT_MATCH = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_NOT_MATCH)
AX_ERR_VDEC_BUF_EMPTY = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_BUF_EMPTY)
AX_ERR_VDEC_BUF_FULL = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_BUF_FULL)
AX_ERR_VDEC_QUEUE_EMPTY = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_QUEUE_EMPTY)
AX_ERR_VDEC_QUEUE_FULL = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_QUEUE_FULL)
AX_ERR_VDEC_TIMED_OUT = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_TIMED_OUT)
AX_ERR_VDEC_FLOW_END = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_FLOW_END)
AX_ERR_VDEC_UNKNOWN = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_UNKNOWN)
AX_ERR_VDEC_OS = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, AX_ERR_OS_FAIL)
AX_ERR_VDEC_RUN_ERROR = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, 0x80)
AX_ERR_VDEC_STRM_ERROR = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, 0x81)
AX_ERR_VDEC_NEED_REALLOC_BUF = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, 0x82)
AX_ERR_VDEC_NO_AVAILABLE_GRP = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, 0x83)
AX_ERR_VDEC_MAX_ERR_DEF  = AX_DEF_ERR(AX_ID_VDEC, AX_ID_VDEC_NULL, 0xFF)
