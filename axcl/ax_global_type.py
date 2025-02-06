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

from ctypes import Structure, c_void_p, Union, POINTER

import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.ax_base_type import *
from axcl.utils.axcl_basestructure import *

DEF_ALL_MOD_GRP_MAX = 164
DEF_ALL_MOD_CHN_MAX = 128
AX_LINK_DEST_MAXNUM = 6
AX_MAX_COLOR_COMPONENT = 3  # VENC support Y/U/V three planes come from external input
AX_MAX_COMPRESS_LOSSY_LEVEL = 10
AX_INVALID_ID = -1
AX_SUCCESS = 0


AX_INVALID_FRMRATE = 0.0

class AX_FRAME_RATE_CTRL_T(BaseStructure):
    """
    .. parsed-literal::

        dict_frame_rate_ctrl = {
            "src_frame_rate": int,
            "dst_frame_rate": int
        }
    """
    _fields_ = [
        ("fSrcFrameRate", AX_F32),
        ("fDstFrameRate", AX_F32)
    ]
    field_aliases = {
        "fSrcFrameRate": "src_frame_rate",
        "fDstFrameRate": "dst_frame_rate"
    }


AX_LOG_LEVEL_E = AX_S32
SYS_LOG_MIN         = -1
SYS_LOG_EMERGENCY   = 0
SYS_LOG_ALERT       = 1
SYS_LOG_CRITICAL    = 2
SYS_LOG_ERROR       = 3
SYS_LOG_WARN        = 4
SYS_LOG_NOTICE      = 5
SYS_LOG_INFO        = 6
SYS_LOG_DEBUG       = 7
SYS_LOG_MAX         = 8

AX_LOG_TARGET_E = AX_S32
SYS_LOG_TARGET_MIN    = 0
SYS_LOG_TARGET_STDERR = 1
SYS_LOG_TARGET_SYSLOG = 2
SYS_LOG_TARGET_NULL   = 3
SYS_LOG_TARGET_MAX    = 4


AX_CHIP_TYPE_E = AX_S32
"""
    chip type

    .. parsed-literal::

        NONE_CHIP_TYPE = 0x0
        AX650A_CHIP    = 0x1
        AX650N_CHIP    = 0x2
        AX650C_CHIP    = 0x3
        AX750_CHIP     = 0x4
        AX650_CHIP_MAX = 0x5
"""
NONE_CHIP_TYPE = 0x0
AX650A_CHIP    = 0x1
AX650N_CHIP    = 0x2
AX650C_CHIP    = 0x3
AX750_CHIP     = 0x4
AX650_CHIP_MAX = 0x5

AX_PAYLOAD_TYPE_E = AX_S32
"""
    payload type

    .. parsed-literal::

        PT_PCMU         = 0
        PT_1016         = 1
        PT_G721         = 2
        PT_GSM          = 3
        PT_G723         = 4
        PT_DVI4_8K      = 5
        PT_DVI4_16K     = 6
        PT_LPC          = 7
        PT_PCMA         = 8
        PT_G722         = 9
        PT_S16BE_STEREO = 10
        PT_S16BE_MONO   = 11
        PT_QCELP        = 12
        PT_CN           = 13
        PT_MPEGAUDIO    = 14
        PT_G728         = 15
        PT_DVI4_3       = 16
        PT_DVI4_4       = 17
        PT_G729         = 18
        PT_G711A        = 19
        PT_G711U        = 20
        PT_G726         = 21
        PT_G729A        = 22
        PT_LPCM         = 23
        PT_CelB         = 25
        PT_JPEG         = 26
        PT_CUSM         = 27
        PT_NV           = 28
        PT_PICW         = 29
        PT_CPV          = 30
        PT_H261         = 31
        PT_MPEGVIDEO    = 32
        PT_MPEG2TS      = 33
        PT_H263         = 34
        PT_SPEG         = 35
        PT_MPEG2VIDEO   = 36
        PT_AAC          = 37
        PT_WMA9STD      = 38
        PT_HEAAC        = 39
        PT_PCM_VOICE    = 40
        PT_PCM_AUDIO    = 41
        PT_AACLC        = 42
        PT_MP3          = 43
        PT_ADPCMA       = 49
        PT_AEC          = 50
        PT_X_LD         = 95
        PT_H264         = 96
        PT_D_GSM_HR     = 200
        PT_D_GSM_EFR    = 201
        PT_D_L8         = 202
        PT_D_RED        = 203
        PT_D_VDVI       = 204
        PT_D_BT656      = 220
        PT_D_H263_1998  = 221
        PT_D_MP1S       = 222
        PT_D_MP2P       = 223
        PT_D_BMPEG      = 224
        PT_MP4VIDEO     = 230
        PT_MP4AUDIO     = 237
        PT_VC1          = 238
        PT_JVC_ASF      = 255
        PT_D_AVI        = 256
        PT_DIVX3        = 257
        PT_AVS          = 258
        PT_REAL8        = 259
        PT_REAL9        = 260
        PT_VP6          = 261
        PT_VP6F         = 262
        PT_VP6A         = 263
        PT_SORENSON     = 264
        PT_H265         = 265
        PT_VP8          = 266
        PT_MVC          = 267
        PT_PNG          = 268
        PT_AVS2         = 269
        PT_VP7          = 270
        PT_VP9          = 271
        PT_AMR          = 1001
        PT_MJPEG        = 1002
        PT_AMRWB        = 1003
        PT_PRORES       = 1006
        PT_OPUS         = 1007
        PT_BUTT         = 1008
"""
PT_PCMU             = 0
PT_1016             = 1
PT_G721             = 2
PT_GSM              = 3
PT_G723             = 4
PT_DVI4_8K          = 5
PT_DVI4_16K         = 6
PT_LPC              = 7
PT_PCMA             = 8
PT_G722             = 9
PT_S16BE_STEREO     = 10
PT_S16BE_MONO       = 11
PT_QCELP            = 12
PT_CN               = 13
PT_MPEGAUDIO        = 14
PT_G728             = 15
PT_DVI4_3           = 16
PT_DVI4_4           = 17
PT_G729             = 18
PT_G711A            = 19
PT_G711U            = 20
PT_G726             = 21
PT_G729A            = 22
PT_LPCM             = 23
PT_CelB             = 25
PT_JPEG             = 26
PT_CUSM             = 27
PT_NV               = 28
PT_PICW             = 29
PT_CPV              = 30
PT_H261             = 31
PT_MPEGVIDEO        = 32
PT_MPEG2TS          = 33
PT_H263             = 34
PT_SPEG             = 35
PT_MPEG2VIDEO       = 36
PT_AAC              = 37
PT_WMA9STD          = 38
PT_HEAAC            = 39
PT_PCM_VOICE        = 40
PT_PCM_AUDIO        = 41
PT_AACLC            = 42
PT_MP3              = 43
PT_ADPCMA           = 49
PT_AEC              = 50
PT_X_LD             = 95
PT_H264             = 96
PT_D_GSM_HR         = 200
PT_D_GSM_EFR        = 201
PT_D_L8             = 202
PT_D_RED            = 203
PT_D_VDVI           = 204
PT_D_BT656          = 220
PT_D_H263_1998      = 221
PT_D_MP1S           = 222
PT_D_MP2P           = 223
PT_D_BMPEG          = 224
PT_MP4VIDEO         = 230
PT_MP4AUDIO         = 237
PT_VC1              = 238
PT_JVC_ASF          = 255
PT_D_AVI            = 256
PT_DIVX3            = 257
PT_AVS              = 258
PT_REAL8            = 259
PT_REAL9            = 260
PT_VP6              = 261
PT_VP6F             = 262
PT_VP6A             = 263
PT_SORENSON         = 264
PT_H265             = 265
PT_VP8              = 266
PT_MVC              = 267
PT_PNG              = 268
PT_AVS2             = 269
PT_VP7              = 270
PT_VP9              = 271
PT_AMR              = 1001
PT_MJPEG            = 1002
PT_AMRWB            = 1003
PT_PRORES           = 1006
PT_OPUS             = 1007
PT_BUTT             = 1008

AX_VSCAN_FORMAT_E = AX_S32
"""
    vscan format

    .. parsed-literal::

        AX_VSCAN_FORMAT_RASTER = 0    # video raster scan mode
        AX_VSCAN_FORMAT_BUTT   = 1
"""
AX_VSCAN_FORMAT_RASTER = 0       # video raster scan mode
AX_VSCAN_FORMAT_BUTT = 1


AX_COMPRESS_MODE_E = AX_S32
"""
    compress mode

    .. parsed-literal::

        AX_COMPRESS_MODE_NONE     = 0    # no compress
        AX_COMPRESS_MODE_LOSSLESS = 1
        AX_COMPRESS_MODE_LOSSY    = 2
        AX_COMPRESS_MODE_BUTT     = 3
"""
AX_COMPRESS_MODE_NONE = 0   # no compress
AX_COMPRESS_MODE_LOSSLESS = 1
AX_COMPRESS_MODE_LOSSY = 2
AX_COMPRESS_MODE_BUTT = 3


class AX_FRAME_COMPRESS_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_frame_compress_info = {
            "compress_mode": :class:`AX_COMPRESS_MODE_E <axcl.ax_global_type.AX_COMPRESS_MODE_E>`,
            "compress_level": int
        }
    """
    _fields_ = [
        ("enCompressMode", AX_COMPRESS_MODE_E),
        ("u32CompressLevel", AX_U32)
    ]
    field_aliases = {
        "enCompressMode": "compress_mode",
        "u32CompressLevel": "compress_level"
    }

AX_DYNAMIC_RANGE_E = AX_S32
"""
    dynamic range

    .. parsed-literal::

        AX_DYNAMIC_RANGE_SDR8  = 0
        AX_DYNAMIC_RANGE_SDR10 = 1
        AX_DYNAMIC_RANGE_HDR10 = 2
        AX_DYNAMIC_RANGE_HLG   = 3
        AX_DYNAMIC_RANGE_SLF   = 4
        AX_DYNAMIC_RANGE_XDR   = 5
        AX_DYNAMIC_RANGE_BUTT  = 6
"""
AX_DYNAMIC_RANGE_SDR8 = 0
AX_DYNAMIC_RANGE_SDR10 = 1
AX_DYNAMIC_RANGE_HDR10 = 2
AX_DYNAMIC_RANGE_HLG = 3
AX_DYNAMIC_RANGE_SLF = 4
AX_DYNAMIC_RANGE_XDR = 5
AX_DYNAMIC_RANGE_BUTT = 6


AX_COLOR_GAMUT_E = AX_S32
"""
    color gamut

    .. parsed-literal::

        AX_COLOR_GAMUT_BT601  = 0
        AX_COLOR_GAMUT_BT709  = 1
        AX_COLOR_GAMUT_BT2020 = 2
        AX_COLOR_GAMUT_USER   = 3
        AX_COLOR_GAMUT_BUTT   = 4
"""
AX_COLOR_GAMUT_BT601 = 0
AX_COLOR_GAMUT_BT709 = 1
AX_COLOR_GAMUT_BT2020 = 2
AX_COLOR_GAMUT_USER = 3
AX_COLOR_GAMUT_BUTT = 4


AX_IMG_FORMAT_E = AX_S32
"""
    Image format

    .. parsed-literal::

        AX_FORMAT_INVALID                            = -1
                                                                               # YUV400 8 bit
        AX_FORMAT_YUV400                             = 0x0                     # Y...
        AX_FORMAT_YUV420_PLANAR                      = 0x1                     # YYYY... UUUU... VVVV...   I420/YU12
        AX_FORMAT_YUV420_PLANAR_VU                   = 0x2                     # YYYY... VVVV... UUUU...  YV12
        AX_FORMAT_YUV420_SEMIPLANAR                  = 0x3                     # YYYY... UVUVUV...       NV12
        AX_FORMAT_YUV420_SEMIPLANAR_VU               = 0x4                     # YYYY... VUVUVU...      NV21
                                                                               # YUV422 8 bit
        AX_FORMAT_YUV422_PLANAR                      = 0x8                     # YYYY... UUUU... VVVV...   I422
        AX_FORMAT_YUV422_PLANAR_VU                   = 0x9                     # YYYY... VVVV... UUUU...  YV16
        AX_FORMAT_YUV422_SEMIPLANAR                  = 0xA                     # YYYY... UVUVUV...       NV16
        AX_FORMAT_YUV422_SEMIPLANAR_VU               = 0xB                     # YYYY... VUVUVU...       NV61
        AX_FORMAT_YUV422_INTERLEAVED_YUVY            = 0xC                     # YUVYYUVY...           YUVY
        AX_FORMAT_YUV422_INTERLEAVED_YUYV            = 0xD                     # YUYVYUYV...           YUYV
        AX_FORMAT_YUV422_INTERLEAVED_UYVY            = 0xE                     # UYVYUYVY...           UYVY
        AX_FORMAT_YUV422_INTERLEAVED_VYUY            = 0xF                     # VYUYVYUY...           VYUY
        AX_FORMAT_YUV422_INTERLEAVED_YVYU            = 0x10                    # VYUYVYUY...           YVYU
                                                                               # YUV444 8 bit
        AX_FORMAT_YUV444_PLANAR                      = 0x14                    # YYYY... UUUU... VVVV...   I444
        AX_FORMAT_YUV444_PLANAR_VU                   = 0x15                    # YYYY... VVVV... UUUU...  YV24
        AX_FORMAT_YUV444_SEMIPLANAR                  = 0x16                    # YYYY... UVUVUV...       NV24
        AX_FORMAT_YUV444_SEMIPLANAR_VU               = 0x17                    # YYYY... VUVUVU...      NV42
        AX_FORMAT_YUV444_PACKED                      = 0x18                    # YUV YUV YUV ...
                                                                               # YUV 10 bit
        AX_FORMAT_YUV400_10BIT                       = 0x20
        AX_FORMAT_YUV420_PLANAR_10BIT_UV_PACKED_4Y5B = 0x24                    # YYYY... UUUU... VVVV... , 4 Y pixels in 5 bytes, UV packed
        AX_FORMAT_YUV420_PLANAR_10BIT_I010           = 0x25                    # 16 bit pixel, low 10bits valid, high 6 bits invalid
        AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P101010    = 0x28                    # YYYY... UVUVUV... ,  Y/U/V 4 pixels in 5 bytes
        AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P010       = 0x2A                    # 16 bit pixel, high 10bits valid, low 6 bits invalid
        AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P016       = 0x2C                    # 16 bit pixel, low 10bits valid, high 6 bits invalid
        AX_FORMAT_YUV420_SEMIPLANAR_10BIT_I016       = 0x2E                    # 16 bit pixel, high 10bits valid, low 6 bits invalid
        AX_FORMAT_YUV420_SEMIPLANAR_10BIT_12P16B     = 0x2F                    # 12 pixels in 16bytes, low 120bits valid, high 8 bits invalid
        AX_FORMAT_YUV444_PACKED_10BIT_P010           = 0x30                    # YUV YUV YUV ... , 16 bit pixel, high 10bits valid, low 6 bits invalid
        AX_FORMAT_YUV444_PACKED_10BIT_P101010        = 0x32                    # YUV YUV YUV ... , 4 pixels storage in 5 bytes
        AX_FORMAT_YUV422_SEMIPLANAR_10BIT_P101010    = 0x33                    # YYYY... UVUVUV... ,  Y/U/V 4 pixels in 5 bytes
        AX_FORMAT_YUV422_SEMIPLANAR_10BIT_P010       = 0x34                    # 16 bit pixel, high 10bits valid, low 6 bits invalid
                                                                               # BAYER RAW
        AX_FORMAT_BAYER_RAW_8BPP                     = 0x80
        AX_FORMAT_BAYER_RAW_10BPP                    = 0x81
        AX_FORMAT_BAYER_RAW_12BPP                    = 0x82
        AX_FORMAT_BAYER_RAW_14BPP                    = 0x83
        AX_FORMAT_BAYER_RAW_16BPP                    = 0x84
        AX_FORMAT_BAYER_RAW_10BPP_PACKED             = 0x85
        AX_FORMAT_BAYER_RAW_12BPP_PACKED             = 0x86
        AX_FORMAT_BAYER_RAW_14BPP_PACKED             = 0x87
                                                                               # RGB Format
        AX_FORMAT_RGB565                             = 0xA0                    # BGRBGR..., RGB565 16bpp
        AX_FORMAT_RGB888                             = 0xA1                    # BGRBGR..., RGB888 24bpp
        AX_FORMAT_KRGB444                            = 0xA2
        AX_FORMAT_KRGB555                            = 0xA3
        AX_FORMAT_KRGB888                            = 0xA4
        AX_FORMAT_BGR888                             = 0xA5                    # RGBRGB..., BGR888 32bpp
        AX_FORMAT_BGR565                             = 0xA6                    # RGBRGB..., BGR565 16bpp
        AX_FORMAT_ARGB4444                           = 0xC5                    # BGRABGRA..., ARGB4444 16bpp
        AX_FORMAT_ARGB1555                           = 0xC6                    # BGRABGRA..., ARGB1555 16bpp
        AX_FORMAT_ARGB8888                           = 0xC7                    # BGRABGRA..., ARGB8888 32bpp
        AX_FORMAT_ARGB8565                           = 0xC8                    # BGRABGRA..., ARGB8565 24bpp
        AX_FORMAT_RGBA8888                           = 0xC9                    # ABGRABGR..., RGBA8888 32bpp
        AX_FORMAT_RGBA5551                           = 0xCA                    # ABGRABGR..., RGBA5551 16bpp
        AX_FORMAT_RGBA4444                           = 0xCB                    # ABGRABGR..., RGBA4444 16bpp
        AX_FORMAT_RGBA5658                           = 0xCC                    # ABGRABGR..., RGBA5658 24bpp
        AX_FORMAT_ABGR4444                           = 0xCD                    # RGBARGBA..., ABGR4444 16bpp
        AX_FORMAT_ABGR1555                           = 0xCE                    # RGBARGBA..., ABGR1555 16bpp
        AX_FORMAT_ABGR8888                           = 0xCF                    # RGBARGBA..., ABGR8888 32bpp
        AX_FORMAT_ABGR8565                           = 0xD0                    # RGBARGBA..., ABGR8565 24bpp
        AX_FORMAT_BGRA8888                           = 0xD1                    # ARGBARGB..., BGRA8888 32bpp
        AX_FORMAT_BGRA5551                           = 0xD2                    # ARGBARGB..., BGRA5551 16bpp
        AX_FORMAT_BGRA4444                           = 0xD3                    # ARGBARGB..., BGRA4444 16bpp
        AX_FORMAT_BGRA5658                           = 0xD4                    # ARGBARGB..., BGRA5658 24bpp
        AX_FORMAT_BITMAP                             = 0xE0
        AX_FORMAT_MAX                                = AX_FORMAT_BITMAP + 1
"""
AX_FORMAT_INVALID                               = -1
# YUV400 8 bit
AX_FORMAT_YUV400                                = 0x0       # Y...
# YUV420 8 bit
AX_FORMAT_YUV420_PLANAR                         = 0x1       # YYYY... UUUU... VVVV...   I420/YU12
AX_FORMAT_YUV420_PLANAR_VU                      = 0x2       # YYYY... VVVV... UUUU...  YV12
AX_FORMAT_YUV420_SEMIPLANAR                     = 0x3       # YYYY... UVUVUV...       NV12
AX_FORMAT_YUV420_SEMIPLANAR_VU                  = 0x4       # YYYY... VUVUVU...      NV21
# YUV422 8 bit
AX_FORMAT_YUV422_PLANAR                         = 0x8       # YYYY... UUUU... VVVV...   I422
AX_FORMAT_YUV422_PLANAR_VU                      = 0x9       # YYYY... VVVV... UUUU...  YV16
AX_FORMAT_YUV422_SEMIPLANAR                     = 0xA       # YYYY... UVUVUV...       NV16
AX_FORMAT_YUV422_SEMIPLANAR_VU                  = 0xB       # YYYY... VUVUVU...       NV61
AX_FORMAT_YUV422_INTERLEAVED_YUVY               = 0xC       # YUVYYUVY...           YUVY
AX_FORMAT_YUV422_INTERLEAVED_YUYV               = 0xD       # YUYVYUYV...           YUYV
AX_FORMAT_YUV422_INTERLEAVED_UYVY               = 0xE       # UYVYUYVY...           UYVY
AX_FORMAT_YUV422_INTERLEAVED_VYUY               = 0xF       # VYUYVYUY...           VYUY
AX_FORMAT_YUV422_INTERLEAVED_YVYU               = 0x10      # VYUYVYUY...           YVYU
# YUV444 8 bit
AX_FORMAT_YUV444_PLANAR                         = 0x14      # YYYY... UUUU... VVVV...   I444
AX_FORMAT_YUV444_PLANAR_VU                      = 0x15      # YYYY... VVVV... UUUU...  YV24
AX_FORMAT_YUV444_SEMIPLANAR                     = 0x16      # YYYY... UVUVUV...       NV24
AX_FORMAT_YUV444_SEMIPLANAR_VU                  = 0x17      # YYYY... VUVUVU...      NV42
AX_FORMAT_YUV444_PACKED                         = 0x18           # YUV YUV YUV ...
# YUV 10 bit
AX_FORMAT_YUV400_10BIT                          = 0x20
AX_FORMAT_YUV420_PLANAR_10BIT_UV_PACKED_4Y5B    = 0x24      # YYYY... UUUU... VVVV... , 4 Y pixels in 5 bytes, UV packed
AX_FORMAT_YUV420_PLANAR_10BIT_I010              = 0x25      #  16 bit pixel, low 10bits valid, high 6 bits invalid
AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P101010       = 0x28      # YYYY... UVUVUV... ,  Y/U/V 4 pixels in 5 bytes
AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P010          = 0x2A      # 16 bit pixel, high 10bits valid, low 6 bits invalid
AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P016          = 0x2C      # 16 bit pixel, low 10bits valid, high 6 bits invalid
AX_FORMAT_YUV420_SEMIPLANAR_10BIT_I016          = 0x2E      # 16 bit pixel, high 10bits valid, low 6 bits invalid
AX_FORMAT_YUV420_SEMIPLANAR_10BIT_12P16B        = 0x2F      # 12 pixels in 16bytes, low 120bits valid, high 8 bits invalid
AX_FORMAT_YUV444_PACKED_10BIT_P010              = 0x30      # YUV YUV YUV ... , 16 bit pixel, high 10bits valid, low 6 bits invalid
AX_FORMAT_YUV444_PACKED_10BIT_P101010           = 0x32      # YUV YUV YUV ... , 4 pixels storage in 5 bytes
AX_FORMAT_YUV422_SEMIPLANAR_10BIT_P101010       = 0x33      # YYYY... UVUVUV... ,  Y/U/V 4 pixels in 5 bytes
AX_FORMAT_YUV422_SEMIPLANAR_10BIT_P010          = 0x34      # 16 bit pixel, high 10bits valid, low 6 bits invalid
# BAYER RAW
AX_FORMAT_BAYER_RAW_8BPP                        = 0x80
AX_FORMAT_BAYER_RAW_10BPP                       = 0x81
AX_FORMAT_BAYER_RAW_12BPP                       = 0x82
AX_FORMAT_BAYER_RAW_14BPP                       = 0x83
AX_FORMAT_BAYER_RAW_16BPP                       = 0x84
AX_FORMAT_BAYER_RAW_10BPP_PACKED                = 0x85
AX_FORMAT_BAYER_RAW_12BPP_PACKED                = 0x86
AX_FORMAT_BAYER_RAW_14BPP_PACKED                = 0x87
# RGB Format
AX_FORMAT_RGB565                                = 0xA0       # BGRBGR..., RGB565 16bpp
AX_FORMAT_RGB888                                = 0xA1       # BGRBGR..., RGB888 24bpp
AX_FORMAT_KRGB444                               = 0xA2
AX_FORMAT_KRGB555                               = 0xA3
AX_FORMAT_KRGB888                               = 0xA4
AX_FORMAT_BGR888                                = 0xA5       # RGBRGB..., BGR888 32bpp
AX_FORMAT_BGR565                                = 0xA6       # RGBRGB..., BGR565 16bpp
AX_FORMAT_ARGB4444                              = 0xC5       # BGRABGRA..., ARGB4444 16bpp
AX_FORMAT_ARGB1555                              = 0xC6       # BGRABGRA..., ARGB1555 16bpp
AX_FORMAT_ARGB8888                              = 0xC7       # BGRABGRA..., ARGB8888 32bpp
AX_FORMAT_ARGB8565                              = 0xC8       # BGRABGRA..., ARGB8565 24bpp
AX_FORMAT_RGBA8888                              = 0xC9       # ABGRABGR..., RGBA8888 32bpp
AX_FORMAT_RGBA5551                              = 0xCA       # ABGRABGR..., RGBA5551 16bpp
AX_FORMAT_RGBA4444                              = 0xCB       # ABGRABGR..., RGBA4444 16bpp
AX_FORMAT_RGBA5658                              = 0xCC       # ABGRABGR..., RGBA5658 24bpp
AX_FORMAT_ABGR4444                              = 0xCD       # RGBARGBA..., ABGR4444 16bpp
AX_FORMAT_ABGR1555                              = 0xCE       # RGBARGBA..., ABGR1555 16bpp
AX_FORMAT_ABGR8888                              = 0xCF       # RGBARGBA..., ABGR8888 32bpp
AX_FORMAT_ABGR8565                              = 0xD0       # RGBARGBA..., ABGR8565 24bpp
AX_FORMAT_BGRA8888                              = 0xD1       # ARGBARGB..., BGRA8888 32bpp
AX_FORMAT_BGRA5551                              = 0xD2       # ARGBARGB..., BGRA5551 16bpp
AX_FORMAT_BGRA4444                              = 0xD3       # ARGBARGB..., BGRA4444 16bpp
AX_FORMAT_BGRA5658                              = 0xD4       # ARGBARGB..., BGRA5658 24bpp
AX_FORMAT_BITMAP                                = 0xE0
AX_FORMAT_MAX                                   = AX_FORMAT_BITMAP + 1


AX_FRAME_FLAG_E = AX_S32
"""
    frame flag

    .. parsed-literal::

        AX_FRM_FLG_NONE    = 0x0
        AX_FRM_FLG_USR_PIC = (0x1 << 0)                # for vdec user picture
        AX_FRM_FLG_FR_CTRL = (0x1 << 1)                # for vo frame ctrl
        AX_FRM_FLG_BUTT    = AX_FRM_FLG_FR_CTRL + 1
"""
AX_FRM_FLG_NONE  = 0x0
AX_FRM_FLG_USR_PIC  = (0x1 << 0) # for vdec user picture
AX_FRM_FLG_FR_CTRL  = (0x1 << 1) # for vo frame ctrl
AX_FRM_FLG_BUTT = AX_FRM_FLG_FR_CTRL + 1



class AX_VIDEO_FRAME_T(BaseStructure):
    """
    .. parsed-literal::

        dict_video_frame = {
            "width": int,
            "height": int,
            "img_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "vscan_format": :class:`AX_VSCAN_FORMAT_E <axcl.ax_global_type.AX_VSCAN_FORMAT_E>`,
            "compress_info": :class:`AX_FRAME_COMPRESS_INFO_T <axcl.ax_global_type.AX_FRAME_COMPRESS_INFO_T>`,
            "dynamic_range": :class:`AX_DYNAMIC_RANGE_E <axcl.ax_global_type.AX_DYNAMIC_RANGE_E>`,
            "color_gamut": :class:`AX_COLOR_GAMUT_E <axcl.ax_global_type.AX_COLOR_GAMUT_E>`,
            "pic_stride": [int],
            "ext_stride": [int],
            "phy_addr": [int],
            "vir_addr": [int],
            "ext_phy_addr": [int],
            "ext_vir_addr": [int],
            "header_size": [int],
            "blk_id": [int],
            "crop_x": int,
            "crop_y": int,
            "crop_width": int,
            "crop_height": int,
            "time_ref": int,
            "pts": int,
            "seq_num": int,
            "user_data": int,
            "private_data": int,
            "frame_flag": int,
            "frame_size": int
        }
    """
    _fields_ = [
        ("u32Width", AX_U32),
        ("u32Height", AX_U32),

        ("enImgFormat", AX_IMG_FORMAT_E),
        ("enVscanFormat", AX_VSCAN_FORMAT_E),
        ("stCompressInfo", AX_FRAME_COMPRESS_INFO_T),
        ("stDynamicRange", AX_DYNAMIC_RANGE_E),
        ("stColorGamut", AX_COLOR_GAMUT_E),
        ("u32PicStride", AX_U32 * AX_MAX_COLOR_COMPONENT),
        ("u32ExtStride", AX_U32 * AX_MAX_COLOR_COMPONENT),
        ("u64PhyAddr", AX_U64 * AX_MAX_COLOR_COMPONENT),
        ("u64VirAddr", AX_U64 * AX_MAX_COLOR_COMPONENT),
        ("u64ExtPhyAddr", AX_U64 * AX_MAX_COLOR_COMPONENT),
        ("u64ExtVirAddr", AX_U64 * AX_MAX_COLOR_COMPONENT),
        ("u32HeaderSize", AX_U32 * AX_MAX_COLOR_COMPONENT),
        ("u32BlkId", AX_U32 * AX_MAX_COLOR_COMPONENT),

        ("s16CropX", AX_S16),
        ("s16CropY", AX_S16),
        ("s16CropWidth", AX_S16),
        ("s16CropHeight", AX_S16),

        ("u32TimeRef", AX_U32),
        ("u64PTS", AX_U64),                  # Payload TimeStamp
        ("u64SeqNum", AX_U64),               # input frame sequence number
        ("u64UserData", AX_U64),             # Reserved for user, sdk do not use

        ("u64PrivateData", AX_U64),           # SDK reserved, user do not use

        # FRAME_FLAG_E, can be OR operation.
        # Can only be assigned as a member of the AX_FRAME_FLAG_E enum.
        ("u32FrameFlag", AX_U32),

        ("u32FrameSize", AX_U32)              # FRAME Size, for isp raw and yuv.
    ]

    field_aliases = {
        "u32Width": "width",
        "u32Height": "height",
        "enImgFormat": "img_format",
        "enVscanFormat": "vscan_format",
        "stCompressInfo": "compress_info",
        "stDynamicRange": "dynamic_range",
        "stColorGamut": "color_gamut",
        "u32PicStride": "pic_stride",
        "u32ExtStride": "ext_stride",
        "u64PhyAddr": "phy_addr",
        "u64VirAddr": "vir_addr",
        "u64ExtPhyAddr": "ext_phy_addr",
        "u64ExtVirAddr": "ext_vir_addr",
        "u32HeaderSize": "header_size",
        "u32BlkId": "blk_id",
        "s16CropX": "crop_x",
        "s16CropY": "crop_y",
        "s16CropWidth": "crop_width",
        "s16CropHeight": "crop_height",
        "u32TimeRef": "time_ref",
        "u64PTS": "pts",
        "u64SeqNum": "seq_num",
        "u64UserData": "user_data",
        "u64PrivateData": "private_data",
        "u32FrameFlag": "frame_flag",
        "u32FrameSize": "frame_size"
    }

AX_MOD_ID_E    = AX_S32
"""
    module id

    .. parsed-literal::

        AX_ID_MIN      = 0x00
        AX_ID_ISP      = 0x01
        AX_ID_CE       = 0x02
        AX_ID_VO       = 0x03
        AX_ID_VDSP     = 0x04
        AX_ID_EFUSE    = 0x05
        AX_ID_NPU      = 0x06
        AX_ID_VENC     = 0x07
        AX_ID_VDEC     = 0x08
        AX_ID_JENC     = 0x09
        AX_ID_JDEC     = 0x0a
        AX_ID_SYS      = 0x0b
        AX_ID_AENC     = 0x0c
        AX_ID_IVPS     = 0x0d
        AX_ID_MIPI     = 0x0e
        AX_ID_ADEC     = 0x0f
        AX_ID_DMA      = 0x10
        AX_ID_VIN      = 0x11
        AX_ID_USER     = 0x12
        AX_ID_IVES     = 0x13
        AX_ID_SKEL     = 0x14
        AX_ID_IVE      = 0x15
        AX_ID_AVS      = 0x16
        AX_ID_AVSCALI  = 0x17
        AX_ID_3A       = 0X19
        AX_ID_AUDIO    = 0x1a
        AX_ID_PYRALITE = 0x1b
        AX_ID_SIF      = 0x1c
        AX_ID_ENGINE   = 0x1d
        AX_ID_GDC_LITE = 0x1e
        AX_ID_AI       = 0X20
        AX_ID_AO       = 0X21
        AX_ID_SENSOR   = 0x22
        AX_ID_NT       = 0x23
        AX_ID_TDP      = 0X24
        AX_ID_VPP      = 0X25
        AX_ID_VGP      = 0X26
        AX_ID_GDC      = 0x27
        AX_ID_BASE     = 0x28
        AX_ID_ALGO     = 0x29
                                 # reserve
        AX_ID_RESERVE  = 0x2a
        AX_ID_BUTT     = 0x2b
                                 # for customer
        AX_ID_CUST_MIN = 0x80    # 128
        AX_ID_MAX      = 0xFF    # 255
"""
AX_ID_MIN      = 0x00
AX_ID_ISP      = 0x01
AX_ID_CE       = 0x02
AX_ID_VO       = 0x03
AX_ID_VDSP     = 0x04
AX_ID_EFUSE    = 0x05
AX_ID_NPU      = 0x06
AX_ID_VENC     = 0x07
AX_ID_VDEC     = 0x08
AX_ID_JENC     = 0x09
AX_ID_JDEC     = 0x0a
AX_ID_SYS      = 0x0b
AX_ID_AENC     = 0x0c
AX_ID_IVPS     = 0x0d
AX_ID_MIPI     = 0x0e
AX_ID_ADEC     = 0x0f
AX_ID_DMA      = 0x10
AX_ID_VIN      = 0x11
AX_ID_USER     = 0x12
AX_ID_IVES     = 0x13
AX_ID_SKEL     = 0x14
AX_ID_IVE      = 0x15
AX_ID_AVS      = 0x16
AX_ID_AVSCALI  = 0x17
AX_ID_3A       = 0X19
AX_ID_AUDIO    = 0x1a
AX_ID_PYRALITE = 0x1b
AX_ID_SIF      = 0x1c
AX_ID_ENGINE   = 0x1d
AX_ID_GDC_LITE = 0x1e
AX_ID_AI       = 0X20
AX_ID_AO       = 0X21
AX_ID_SENSOR   = 0x22
AX_ID_NT       = 0x23
AX_ID_TDP      = 0X24
AX_ID_VPP      = 0X25
AX_ID_VGP      = 0X26
AX_ID_GDC      = 0x27
AX_ID_BASE     = 0x28
AX_ID_ALGO     = 0x29
# reserve
AX_ID_RESERVE  = 0x2a
AX_ID_BUTT     = 0x2b
# for customer
AX_ID_CUST_MIN = 0x80 # 128
AX_ID_MAX      = 0xFF  # 255

AX_LINK_MODE_E = AX_S32
"""
    link mode

    .. parsed-literal::

        AX_UNLINK_MODE = 0
        AX_LINK_MODE   = 1
"""
AX_UNLINK_MODE = 0
AX_LINK_MODE = 1


AX_AUDIO_BIT_WIDTH_E = AX_S32
AX_AUDIO_BIT_WIDTH_8    = 0    # 8bit width
AX_AUDIO_BIT_WIDTH_16   = 1    # 16bit width
AX_AUDIO_BIT_WIDTH_24   = 2    # 24bit width
AX_AUDIO_BIT_WIDTH_32   = 3    # 32bit width
AX_AUDIO_BIT_WIDTH_BUTT = 4

AX_AUDIO_SOUND_MODE_E = AX_S32
AX_AUDIO_SOUND_MODE_MONO   = 0  # mono
AX_AUDIO_SOUND_MODE_STEREO = 1  # stereo
AX_AUDIO_SOUND_MODE_BUTT   = 2

class AX_AUDIO_FRAME_T(BaseStructure):
    _fields_ = [
        ("enBitwidth", AX_AUDIO_BIT_WIDTH_E),
        ("enSoundmode", AX_AUDIO_SOUND_MODE_E),
        ("u64VirAddr", POINTER(AX_U8)),
        ("u64PhyAddr", AX_U64),
        ("u64TimeStamp", AX_U64),
        ("u32Seq", AX_U32),
        ("u32Len", AX_U32),
        ("u32PoolId", AX_U32 * 2),
        ("bEof", AX_BOOL),
        ("u32BlkId", AX_U32)
    ]

class AX_AUDIO_FRAME_INFO_T(BaseStructure):
    _fields_ = [
        ("stAFrame", AX_AUDIO_FRAME_T),
        ("enModId", AX_MOD_ID_E),
        ("bEndOfStream", AX_BOOL)
    ]

class AX_VIDEO_FRAME_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_video_frame_info = {
            "video_frame": :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`,
            "mod_id": :class:`AX_MOD_ID_E <axcl.ax_global_type.AX_MOD_ID_E>`,
            "is_end_of_stream": bool
        }
    """
    _fields_ = [
        ("stVFrame", AX_VIDEO_FRAME_T),
        ("enModId", AX_MOD_ID_E),
        ("bEndOfStream", AX_BOOL)
    ]
    field_aliases = {
        "stVFrame": "video_frame",
        "enModId": "mod_id",
        "bEndOfStream": "is_end_of_stream",
    }

AX_NOTIFY_EVENT_E = AX_S32
AX_NOTIFY_EVENT_SLEEP   = 0
AX_NOTIFY_EVENT_WAKEUP  = 1
AX_NOTIFY_EVENT_MAX     = 2

AX_SYS_CLK_LEVEL_E = AX_S32
"""
    sys clk level

    .. parsed-literal::

        AX_SYS_CLK_HIGH_MODE            = 0
        AX_SYS_CLK_HIGH_HOTBALANCE_MODE = 1
        AX_SYS_CLK_MID_MODE             = 2
        AX_SYS_CLK_MID_HOTBALANCE_MODE  = 3
        AX_SYS_CLK_MAX_MODE             = 4
"""
AX_SYS_CLK_HIGH_MODE             = 0
AX_SYS_CLK_HIGH_HOTBALANCE_MODE  = 1
AX_SYS_CLK_MID_MODE              = 2
AX_SYS_CLK_MID_HOTBALANCE_MODE   = 3
AX_SYS_CLK_MAX_MODE              = 4


AX_SYS_CLK_ID_E = AX_S32
"""
    sys clk id

    .. parsed-literal::

        AX_CPU_CLK_ID     = 0
        AX_BUS_CLK_ID     = 1
        AX_NPU_CLK_ID     = 2
        AX_ISP_CLK_ID     = 3
        AX_MM_CLK_ID      = 4
        AX_VPU_CLK_ID     = 5
        AX_SYS_CLK_MAX_ID = 6
"""
AX_CPU_CLK_ID       = 0
AX_BUS_CLK_ID       = 1
AX_NPU_CLK_ID       = 2
AX_ISP_CLK_ID       = 3
AX_MM_CLK_ID        = 4
AX_VPU_CLK_ID       = 5
AX_SYS_CLK_MAX_ID   = 6


class AX_MOD_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_mod_info = {
            "mod_id": :class:`AX_MOD_ID_E <axcl.ax_global_type.AX_MOD_ID_E>`,
            "grp_id": int,
            "chn_id": int
        }
    """
    _fields_ = [
        ("enModId", AX_MOD_ID_E),
        ("s32GrpId", AX_S32),
        ("s32ChnId", AX_S32)
    ]
    field_aliases = {
        "enModId": "mod_id",
        "s32GrpId": "grp_id",
        "s32ChnId": "chn_id"
    }

class AX_LINK_DEST_T(BaseStructure):
    """
    .. parsed-literal::

        dict_link_dest = {
            "dest_num": int,
            "dest_mod": [:class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`]
        }
    """
    _fields_ = [
        ("u32DestNum", AX_U32),
        ("astDestMod", AX_MOD_INFO_T * AX_LINK_DEST_MAXNUM)
    ]
    field_aliases = {
        "u32DestNum": "dest_num",
        "astDestMod": "dest_mod"
    }

AX_MEMORY_SOURCE_E = AX_S32
"""
    memory source

    .. parsed-literal::

        AX_MEMORY_SOURCE_CMM  = 0
        AX_MEMORY_SOURCE_POOL = 1
        AX_MEMORY_SOURCE_OS   = 2
        AX_MEMORY_SOURCE_BUTT = 3
"""
AX_MEMORY_SOURCE_CMM  = 0
AX_MEMORY_SOURCE_POOL = 1
AX_MEMORY_SOURCE_OS   = 2
AX_MEMORY_SOURCE_BUTT = 3


class AX_MEMORY_ADDR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_memory_addr = {
            "phy_addr": int,
            "vir_addr": int
        }
    """
    _fields_ = [
        ("u64PhyAddr", AX_U64),
        ("pVirAddr", c_void_p)
    ]
    field_aliases = {
        "u64PhyAddr": "phy_addr",
        "pVirAddr": "vir_addr"
    }

# OSD attribute extend
class AX_OSD_BMP_ATTR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_osd_bmp_attr = {
            "alpha": int,
            "rgb_format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "bitmap_p": int,
            "phy_addr": int,
            "bmp_width": int,
            "bmp_height": int,
            "dst_x_offset": int,
            "dst_y_offset": int,
            "color": int,
            "enable_color_inv": bool,
            "color_inv": int,
            "color_inv_thr": int
        }
    """
    _fields_ = [
        ("u16Alpha", AX_U16),
        ("enRgbFormat", AX_IMG_FORMAT_E),
        ("pBitmap", POINTER(AX_U8)),   # pointer to OSD template
        ("u64PhyAddr", AX_U64),        # physical address of OSD template
        ("u32BmpWidth", AX_U32),        # template width
        ("u32BmpHeight", AX_U32),       # template height

        ("u32DstXoffset", AX_U32),     # where to overlay, x0
        ("u32DstYoffset", AX_U32),     # where to overlay, y0

        # the below variables are only for bitmap-1 format
        ("u32Color", AX_U32),          # RW; range: [0, 0xffffff]; color RGB888; 0xRRGGBB
        ("bColorInv", AX_BOOL),          # RW; range: [0, 1]; whether use background color or not
        ("u32ColorInv", AX_U32),       # RW; range: [0, 0xffffff]; inverse color RGB888; 0xRRGGBB
        ("u32ColorInvThr", AX_U32),    # RW; range: [0, 0xffffff]; threshold of color difference with background; 0xRRGGBB
    ]

    field_aliases = {
        "u16Alpha": "alpha",
        "enRgbFormat": "rgb_format",
        "pBitmap": "bitmap_p",
        "u64PhyAddr": "phy_addr",
        "u32BmpWidth": "bmp_width",
        "u32BmpHeight": "bmp_height",
        "u32DstXoffset": "dst_x_offset",
        "u32DstYoffset": "dst_y_offset",
        "u32Color": "color",
        "bColorInv": "enable_color_inv",
        "u32ColorInv": "color_inv",
        "u32ColorInvThr": "color_inv_thr"
    }

AX_ERR_CODE_E = AX_S32
"""
    error code

    .. parsed-literal::

        AX_ERR_INVALID_MODID       = 0x01    # invalid module id
        AX_ERR_INVALID_DEVID       = 0x02    # invalid device id
        AX_ERR_INVALID_GRPID       = 0x03    # invalid group id
        AX_ERR_INVALID_CHNID       = 0x04    # invalid channel id
        AX_ERR_INVALID_PIPEID      = 0x05    # invalid pipe id
        AX_ERR_INVALID_STITCHGRPID = 0x06    # invalid stitch group id
                                             # reserved
        AX_ERR_ILLEGAL_PARAM       = 0x0A    # at lease one input value is out of range
        AX_ERR_NULL_PTR            = 0x0B    # at lease one input pointer is null
        AX_ERR_BAD_ADDR            = 0x0C    # at lease one input address is invalid
                                             # reserved
        AX_ERR_SYS_NOTREADY        = 0x10    # a driver is required but not loaded
        AX_ERR_BUSY                = 0x11    # a resource is busy, probably locked by other users
        AX_ERR_NOT_INIT            = 0x12    # module is not initialized
        AX_ERR_NOT_CONFIG          = 0x13    # module is not configured
        AX_ERR_NOT_SUPPORT         = 0x14    # requested function is not supported on this platform
        AX_ERR_NOT_PERM            = 0x15    # requested operation is not permitted in this state
        AX_ERR_EXIST               = 0x16    # target object already exists
        AX_ERR_UNEXIST             = 0x17    # target object does not exist
        AX_ERR_NOMEM               = 0x18    # failed to allocate memory from heap
        AX_ERR_NOBUF               = 0x19    # failed to borrow buffer from pool
        AX_ERR_NOT_MATCH           = 0x1A    # inconsistent parameter configuration between interfaces
                                             # reserved
        AX_ERR_BUF_EMPTY           = 0x20    # buffer contains no data
        AX_ERR_BUF_FULL            = 0x21    # buffer contains fresh data
        AX_ERR_QUEUE_EMPTY         = 0x22    # failed to read as queue is empty
        AX_ERR_QUEUE_FULL          = 0x23    # failed to write as queue is full
                                             # reserved
        AX_ERR_TIMED_OUT           = 0x27    # operation timeout
        AX_ERR_FLOW_END            = 0x28    # END signal detected in data stream, processing terminated
        AX_ERR_UNKNOWN             = 0x29    # unexpected failure, please contact manufacturer support
                                             # reserved
"""
AX_ERR_INVALID_MODID        = 0x01  # invalid module id
AX_ERR_INVALID_DEVID        = 0x02  # invalid device id
AX_ERR_INVALID_GRPID        = 0x03  # invalid group id
AX_ERR_INVALID_CHNID        = 0x04  # invalid channel id
AX_ERR_INVALID_PIPEID       = 0x05  # invalid pipe id
AX_ERR_INVALID_STITCHGRPID  = 0x06  # invalid stitch group id
# reserved
AX_ERR_ILLEGAL_PARAM        = 0x0A  # at lease one input value is out of range
AX_ERR_NULL_PTR             = 0x0B  # at lease one input pointer is null
AX_ERR_BAD_ADDR             = 0x0C  # at lease one input address is invalid
#reserved
AX_ERR_SYS_NOTREADY         = 0x10  # a driver is required but not loaded
AX_ERR_BUSY                 = 0x11  # a resource is busy, probably locked by other users
AX_ERR_NOT_INIT             = 0x12  # module is not initialized
AX_ERR_NOT_CONFIG           = 0x13  # module is not configured
AX_ERR_NOT_SUPPORT          = 0x14  # requested function is not supported on this platform
AX_ERR_NOT_PERM             = 0x15  # requested operation is not permitted in this state
AX_ERR_EXIST                = 0x16  # target object already exists
AX_ERR_UNEXIST              = 0x17  # target object does not exist
AX_ERR_NOMEM                = 0x18  # failed to allocate memory from heap
AX_ERR_NOBUF                = 0x19  # failed to borrow buffer from pool
AX_ERR_NOT_MATCH            = 0x1A  # inconsistent parameter configuration between interfaces
#reserved
AX_ERR_BUF_EMPTY            = 0x20  # buffer contains no data
AX_ERR_BUF_FULL             = 0x21  # buffer contains fresh data
AX_ERR_QUEUE_EMPTY          = 0x22  # failed to read as queue is empty
AX_ERR_QUEUE_FULL           = 0x23  # failed to write as queue is full
#reserved
AX_ERR_TIMED_OUT            = 0x27  # operation timeout
AX_ERR_FLOW_END             = 0x28  # END signal detected in data stream, processing terminated
AX_ERR_UNKNOWN              = 0x29  # unexpected failure, please contact manufacturer support
#reserved

AX_ERR_OS_FAIL              = 0x30  # os failure, please contact manufacturer support

AX_ERR_BUTT                 = 0x7F  # maxium code, private error code of all modules
                                    # must be greater than it


#
# |----------------------------------------------------------------|
# ||   FIXED   |   MOD_ID    | SUB_MODULE_ID |   ERR_ID            |
# |----------------------------------------------------------------|
# |<--8bits----><----8bits---><-----8bits---><------8bits------->|

def AX_DEF_ERR( module, sub_module, errid):
    return AX_S32(((0x80000000) | ((module) << 16 ) | ((sub_module)<<8) | (errid)))


class AX_POINT_T(BaseStructure):
    """
    .. parsed-literal::

        dict_point = {
            "x": int,
            "y": int
        }
    """
    _fields_ = [
        ("nX", AX_S16),
        ("nY", AX_S16)
    ]
    field_aliases = {
        "nX": "x",
        "nY": "y"
    }

class AX_BGCOLOR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_bgcolor = {
            "enable": bool,
            "bg_color": int
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),  # RW; range: [0, 1]; whether use background color or not;
        ("nBgColor", AX_U32) # RW; range: [0, 0xffffff]; background color RGB888;
    ]
    field_aliases = {
        "bEnable": "enable",
        "nBgColor": "bg_color"
    }

class AX_COLORKEY_T(BaseStructure):
    """
    .. parsed-literal::

        dict_colorkey = {
            "enable": int,
            "inv": int,
            "key_low": int,
            "key_high": int
        }
    """
    _fields_ = [
        ("u16Enable", AX_U16),
        ("u16Inv", AX_U16),      # RW; 0: winin threshold, 1: outside threshold
        ("u32KeyLow", AX_U32),   # RW; min value of color key 0xRRGGBB
        ("u32KeyHigh", AX_U32)   # RW; max value of color key; 0xRRGGBB
    ]
    field_aliases = {
        "u16Enable": "enable",
        "u16Inv": "inv",
        "u32KeyLow": "key_low",
        "u32KeyHigh": "key_high"
    }

class AX_BITCOLOR_T(BaseStructure):
    """
    .. parsed-literal::

        dict_bitcolor = {
            "color": int,
            "enable_color_inv": bool,
            "color_inv": int,
            "color_inv_thr": int
        }
    """
    _fields_ = [
        ("nColor", AX_U32),       # RW; range: [0, 0xffffff]; color RGB888; 0xRRGGBB
        ("bColorInvEn", AX_BOOL),   # RW; range: [0, 1]; whether use background color inv or not
        ("nColorInv", AX_U32),    # RW; range: [0, 0xffffff]; inverse color RGB888; 0xRRGGBB
        ("nColorInvThr", AX_U32)  # RW; range: [0, 0xffffff]; threshold of color difference with background; 0xRRGGBB
    ]
    field_aliases = {
        "nColor": "color",
        "bColorInvEn": "enable_color_inv",
        "nColorInv": "color_inv",
        "nColorInvThr": "color_inv_thr"
    }


class AX_OVERLAY_T(BaseStructure):
    """
    .. parsed-literal::

        dict_overlay = {
            "enable": bool,
            "width": int,
            "height": int,
            "stride": int,
            "format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "phy_addr": [int],
            "compress_info": :class:`AX_FRAME_COMPRESS_INFO_T <axcl.ax_global_type.AX_FRAME_COMPRESS_INFO_T>`,
            "alpha": :class:`ctypes.c_ubyte`,
            "offset": :class:`AX_POINT_T <axcl.ax_global_type.AX_POINT_T>`,
            "color_key": :class:`AX_COLORKEY_T <axcl.ax_global_type.AX_COLORKEY_T>`,
            "bit_color": :class:`AX_BITCOLOR_T <axcl.ax_global_type.AX_BITCOLOR_T>`
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),
        ("nWidth", AX_U16),
        ("nHeight", AX_U16),
        ("nStride", AX_U32),
        ("eFormat", AX_IMG_FORMAT_E),
        ("u64PhyAddr", AX_U64 * 2),
        ("stCompressInfo", AX_FRAME_COMPRESS_INFO_T),
        ("nAlpha", c_uint8),
        ("tOffset", AX_POINT_T),
        ("tColorKey", AX_COLORKEY_T),
        ("tBitColor", AX_BITCOLOR_T)
    ]
    field_aliases = {
        "bEnable": "enable",
        "nWidth": "width",
        "nHeight": "height",
        "nStride": "stride",
        "eFormat": "format",
        "u64PhyAddr": "phy_addr",
        "stCompressInfo": "compress_info",
        "nAlpha": "alpha",
        "tOffset": "offset",
        "tColorKey": "color_key",
        "tBitColor": "bit_color"
    }


AX_PYRA_MODE_E = AX_S32
"""
    pyra mode

    .. parsed-literal::

        AX_PYRA_MODE_GEN  = 0
        AX_PYRA_MODE_RCN  = 1
        AX_PYRA_MODE_BUTT = 2
"""
AX_PYRA_MODE_GEN = 0
AX_PYRA_MODE_RCN = 1
AX_PYRA_MODE_BUTT = 2

class AX_PYRA_FRAME_T(BaseStructure):
    """
    .. parsed-literal::

        dict_pyra_frame = {
            "enable": bool,
            "width": int,
            "height": int,
            "stride": int,
            "format": :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`,
            "phy_addr": [int],
            "compress_info": :class:`AX_FRAME_COMPRESS_INFO_T <axcl.ax_global_type.AX_FRAME_COMPRESS_INFO_T>`,
            "pixel_format": int,
            "enable_crop": bool,
            "crop_x_0": int,
            "crop_y_0": int,
            "crop_width": int,
            "crop_height": int
        }
    """
    _fields_ = [
        ("bEnable", AX_BOOL),
        ("nWidth", AX_U16),
        ("nHeight", AX_U16),
        ("nStride", AX_U32),
        ("eFormat", AX_IMG_FORMAT_E),
        ("u64PhyAddr", AX_U64 * 2),
        ("stCompressInfo", AX_FRAME_COMPRESS_INFO_T),
        ("PixelFormat", AX_U8),

        ("bCropEnable", AX_BOOL),
        ("nCropX0", AX_S16),
        ("nCropY0", AX_S16),
        ("nCropWidth", AX_U16),
        ("nCropHeight", AX_U16)
    ]
    field_aliases = {
        "bEnable": "enable",
        "nWidth": "width",
        "nHeight": "height",
        "nStride": "stride",
        "eFormat": "format",
        "u64PhyAddr": "phy_addr",
        "stCompressInfo": "compress_info",
        "PixelFormat": "pixel_format",
        "bCropEnable": "enable_crop",
        "nCropX0": "crop_x_0",
        "nCropY0": "crop_y_0",
        "nCropWidth": "crop_width",
        "nCropHeight": "crop_height"
    }

AX_GDC_MODE_E = AX_S32
"""
    gdc mode

    .. parsed-literal::

        AX_GDC_MODE_CORE0 = 0    # core 0
        AX_GDC_MODE_MAX   = 1
"""
AX_GDC_MODE_CORE0     = 0   # core 0
AX_GDC_MODE_MAX       = 1


AX_VDSP_MODE_E = AX_S32
"""
    vdsp mode

    .. parsed-literal::

        AX_VDSP_MODE_CORE0 = 0    # core 0
        AX_VDSP_MODE_CORE1 = 1    # core 1
        AX_VDSP_MODE_AUTO  = 2    # core0/1 balance
        AX_VDSP_MODE_MAX   = 3
"""
AX_VDSP_MODE_CORE0     = 0    # core 0
AX_VDSP_MODE_CORE1     = 1    # core 1
AX_VDSP_MODE_AUTO      = 2    # core0/1 balance
AX_VDSP_MODE_MAX       = 3


AX_WARP_ENGINE_E  = AX_S32
"""
    warp engine

    .. parsed-literal::

        AX_WARP_ENGINE_GDC  = 0
        AX_WARP_ENGINE_VDSP = 1
        AX_WARP_ENGINE_MAX  = 2
"""
AX_WARP_ENGINE_GDC     = 0
AX_WARP_ENGINE_VDSP    = 1
AX_WARP_ENGINE_MAX     = 2

class AX_WARP_MODE_U(Union):
    _fields_ = [
        ("eGdcMode", AX_GDC_MODE_E),
        ("eVdspMode", AX_VDSP_MODE_E)
    ]

def ax_video_frame_to_dict(frame, dict):
    dict['width'] = frame.u32Width
    dict['height'] = frame.u32Height
    dict['img_format'] = frame.enImgFormat
    dict['vscan_format'] = frame.enVscanFormat
    dict['compress_info'] = {}
    dict['compress_info']['compress_mode'] = frame.stCompressInfo.enCompressMode
    dict['compress_info']['compress_level'] = frame.stCompressInfo.u32CompressLevel
    dict['dynamic_range'] = frame.stDynamicRange
    dict['color_gamut'] = frame.stColorGamut
    dict['pic_stride'] = [frame.u32PicStride[0], frame.u32PicStride[1], frame.u32PicStride[2]]
    dict['ext_stride'] = [frame.u32ExtStride[0], frame.u32ExtStride[1], frame.u32ExtStride[2]]
    dict['phy_addr'] = [frame.u64PhyAddr[0], frame.u64PhyAddr[1], frame.u64PhyAddr[2]]
    dict['vir_addr'] = [frame.u64VirAddr[0], frame.u64VirAddr[1], frame.u64VirAddr[2]]
    dict['ext_phy_addr'] = [frame.u64ExtPhyAddr[0], frame.u64ExtPhyAddr[1], frame.u64ExtPhyAddr[2]]
    dict['ext_vir_addr'] = [frame.u64ExtVirAddr[0], frame.u64ExtVirAddr[1], frame.u64ExtVirAddr[2]]
    dict['header_size'] = [frame.u32HeaderSize[0], frame.u32HeaderSize[1], frame.u32HeaderSize[2]]
    dict['blk_id'] = [frame.u32BlkId[0], frame.u32BlkId[1], frame.u32BlkId[2]]
    dict['crop_x'] = frame.s16CropX
    dict['crop_y'] = frame.s16CropY
    dict['crop_width'] = frame.s16CropWidth
    dict['crop_height'] = frame.s16CropHeight
    dict['time_ref'] = frame.u32TimeRef
    dict['pts'] = frame.u64PTS
    dict['seq_num'] = frame.u64SeqNum
    dict['user_data'] = frame.u64UserData
    dict['private_data'] = frame.u64PrivateData
    dict['frame_flag'] = frame.u32FrameFlag
    dict['frame_size'] = frame.u32FrameSize

def dict_to_ax_video_frame(dict, frame):
    frame.u32Width = AX_U32(dict.get('width', 0))
    frame.u32Height = AX_U32(dict.get('height', 0))
    frame.enImgFormat = AX_IMG_FORMAT_E(dict.get('img_format', 0))

    frame.enVscanFormat = AX_VSCAN_FORMAT_E(dict.get('vscan_format', 0))
    compress_info = dict.get('compress_info')
    if compress_info:
        frame.stCompressInfo.enCompressMode = AX_COMPRESS_MODE_E(compress_info.get('compress_mode', 0))
        frame.stCompressInfo.u32CompressLevel = AX_U32(compress_info.get('compress_level', 0))
    frame.stDynamicRange = AX_S32(dict.get('dynamic_range', 0))
    frame.stColorGamut = AX_S32(dict.get('color_gamut', 0))

    pic_stride = dict.get('pic_stride')
    if pic_stride and isinstance(pic_stride, list):
        for i in range(len(pic_stride)):
            frame.u32PicStride[i] = AX_U32(pic_stride[i])

    ext_stride = dict.get('ext_stride')
    if ext_stride and isinstance(ext_stride, list):
        for i in range(len(ext_stride)):
            frame.u32ExtStride[i] = AX_U32(ext_stride[i])

    phy_addr = dict.get('phy_addr')
    if phy_addr and isinstance(phy_addr, list):
        for i in range(len(phy_addr)):
            frame.u64PhyAddr[i] = AX_U64(phy_addr[i])

    vir_addr = dict.get('vir_addr')
    if vir_addr and isinstance(vir_addr, list):
        for i in range(len(vir_addr)):
            frame.u64VirAddr[i] = AX_U64(vir_addr[i])

    ext_phy_addr = dict.get('ext_phy_addr')
    if ext_phy_addr and isinstance(ext_phy_addr, list):
        for i in range(len(ext_phy_addr)):
            frame.u64ExtPhyAddr[i] = AX_U64(ext_phy_addr[i])

    ext_vir_addr = dict.get('ext_vir_addr')
    if ext_vir_addr and isinstance(ext_vir_addr, list):
        for i in range(len(ext_vir_addr)):
            frame.u64ExtVirAddr[i] = AX_U64(ext_vir_addr[i])

    header_size = dict.get('header_size')
    if header_size and isinstance(header_size, list):
        for i in range(len(header_size)):
            frame.u32HeaderSize[i] = AX_U64(header_size[i])

    blk_id = dict.get('blk_id')
    if blk_id and isinstance(blk_id, list):
        for i in range(len(blk_id)):
            frame.u32BlkId[i] = AX_U32(blk_id[i])

    frame.s16CropX = AX_S16(dict.get('crop_x', 0))
    frame.s16CropY = AX_S16(dict.get('crop_y', 0))
    frame.s16CropWidth = AX_S16(dict.get('crop_width', 0))
    frame.s16CropHeight = AX_S16(dict.get('crop_height', 0))
    frame.u32TimeRef = AX_U32(dict.get('time_ref', 0))
    frame.u64PTS = AX_U64(dict.get('pts', 0))
    frame.u64SeqNum = AX_U64(dict.get('seq_num', 0))
    frame.u64UserData = AX_U64(dict.get('user_data', 0))
    frame.u64PrivateData = AX_U64(dict.get('private_data', 0))
    frame.u32FrameFlag = AX_U32(dict.get('frame_flag', 0))
    frame.u32FrameSize = AX_U32(dict.get('frame_size', 0))

def ax_video_frame_info_to_dict(frame_info, dict):
    video_frame = {}
    ax_video_frame_to_dict(frame_info.stVFrame, video_frame)
    dict['video_frame'] = video_frame
    dict['mod_id'] = frame_info.enModId
    dict['is_end_of_stream'] = frame_info.bEndOfStream

def dict_to_ax_video_frame_info(dict, frame_info):
    frame = AX_VIDEO_FRAME_T()
    video_frame = dict.get('video_frame')
    if video_frame:
        dict_to_ax_video_frame(video_frame, frame)
        frame_info.stVFrame = frame
    frame_info.enModId = AX_MOD_ID_E(dict.get('mod_id', AX_ID_USER))
    frame_info.bEndOfStream = AX_BOOL(1 if dict.get('is_end_of_stream', False) else 0)