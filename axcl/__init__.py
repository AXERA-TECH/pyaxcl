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

import axcl.rt
import axcl.sys
import axcl.pool
import axcl.npu
import axcl.ivps
import axcl.ive
import axcl.venc
import axcl.vdec
import axcl.dmadim
import axcl.utils

from axcl.axcl import init
from axcl.axcl import finalize
from axcl.axcl import set_log_level
from axcl.axcl import app_log

from axcl.axcl_base import AXCL_SUCC

# global
from axcl.ax_global_type import DEF_ALL_MOD_GRP_MAX

from axcl.ax_global_type import AX_ID_VENC
from axcl.ax_global_type import AX_ID_VDEC
from axcl.ax_global_type import AX_ID_JENC
from axcl.ax_global_type import AX_ID_JDEC
from axcl.ax_global_type import AX_ID_SYS
from axcl.ax_global_type import AX_ID_IVPS

from axcl.ax_global_type import PT_H264
from axcl.ax_global_type import PT_H265

from axcl.ax_global_type import AX_COMPRESS_MODE_NONE
from axcl.ax_global_type import AX_COMPRESS_MODE_LOSSLESS
from axcl.ax_global_type import AX_COMPRESS_MODE_LOSSY

from axcl.ax_global_type import AX_FORMAT_YUV420_SEMIPLANAR
from axcl.ax_global_type import AX_FORMAT_YUV420_SEMIPLANAR_VU
from axcl.ax_global_type import AX_FORMAT_RGB565
from axcl.ax_global_type import AX_FORMAT_RGB888
from axcl.ax_global_type import AX_FORMAT_BGR888
from axcl.ax_global_type import AX_FORMAT_ARGB8888
from axcl.ax_global_type import AX_FORMAT_RGBA8888

from axcl.ax_global_type import AX_MEMORY_SOURCE_CMM
from axcl.ax_global_type import AX_MEMORY_SOURCE_POOL
from axcl.ax_global_type import AX_MEMORY_SOURCE_OS

# rt
from axcl.rt.axcl_rt_type import AXCL_MEM_MALLOC_HUGE_FIRST
from axcl.rt.axcl_rt_type import AXCL_MEM_MALLOC_HUGE_ONLY
from axcl.rt.axcl_rt_type import AXCL_MEM_MALLOC_NORMAL_ONLY

from axcl.rt.axcl_rt_type import AXCL_MEMCPY_HOST_TO_HOST
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_HOST_TO_DEVICE
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_DEVICE_TO_HOST
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_DEVICE_TO_DEVICE
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_HOST_PHY_TO_DEVICE
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_DEVICE_TO_HOST_PHY

# sys
from axcl.sys.axcl_sys_type import AX_INVALID_POOLID
from axcl.sys.axcl_sys_type import AX_INVALID_BLOCKID
from axcl.sys.axcl_sys_type import AX_MAX_POOLS
from axcl.sys.axcl_sys_type import AX_MAX_COMM_POOLS
from axcl.sys.axcl_sys_type import AX_MAX_BLKS_PER_POOL

from axcl.sys.axcl_sys_type import AX_MAX_POOL_NAME_LEN
from axcl.sys.axcl_sys_type import AX_MAX_PARTITION_NAME_LEN
from axcl.sys.axcl_sys_type import AX_MAX_PARTITION_COUNT

from axcl.sys.axcl_sys_type import AX_MEM_CACHED
from axcl.sys.axcl_sys_type import AX_MEM_NONCACHED

from axcl.sys.axcl_sys_type import POOL_CACHE_MODE_NONCACHE
from axcl.sys.axcl_sys_type import POOL_CACHE_MODE_CACHED

from axcl.sys.axcl_sys_type import POOL_SOURCE_COMMON
from axcl.sys.axcl_sys_type import POOL_SOURCE_PRIVATE
from axcl.sys.axcl_sys_type import POOL_SOURCE_USER

# ivps
from axcl.ivps.axcl_ivps_type import AX_IVPS_MIN_IMAGE_WIDTH
from axcl.ivps.axcl_ivps_type import AX_IVPS_MAX_IMAGE_WIDTH
from axcl.ivps.axcl_ivps_type import AX_IVPS_MIN_IMAGE_HEIGHT
from axcl.ivps.axcl_ivps_type import AX_IVPS_MAX_IMAGE_HEIGHT
from axcl.ivps.axcl_ivps_type import AX_IVPS_MAX_GRP_NUM
from axcl.ivps.axcl_ivps_type import AX_IVPS_MAX_OUTCHN_NUM
from axcl.ivps.axcl_ivps_type import AX_IVPS_MAX_FILTER_NUM_PER_OUTCHN

from axcl.ivps.axcl_ivps_type import AX_IVPS_ENGINE_SUBSIDIARY
from axcl.ivps.axcl_ivps_type import AX_IVPS_ENGINE_TDP
from axcl.ivps.axcl_ivps_type import AX_IVPS_ENGINE_GDC
from axcl.ivps.axcl_ivps_type import AX_IVPS_ENGINE_VPP
from axcl.ivps.axcl_ivps_type import AX_IVPS_ENGINE_VGP

from axcl.ivps.axcl_ivps_type import AX_IVPS_PIPELINE_DEFAULT

from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_HORIZONTAL_CENTER
from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_HORIZONTAL_LEFT
from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_HORIZONTAL_RIGHT
from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_VERTICAL_CENTER
from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_VERTICAL_TOP
from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_VERTICAL_BOTTOM

from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_STRETCH
from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_AUTO
from axcl.ivps.axcl_ivps_type import AX_IVPS_ASPECT_RATIO_MANUAL

from axcl.ivps.axcl_ivps_type import AX_IVPS_SCALE_NORMAL
from axcl.ivps.axcl_ivps_type import AX_IVPS_SCALE_UP
from axcl.ivps.axcl_ivps_type import AX_IVPS_SCALE_DOWN

# vdec
from axcl.vdec.axcl_vdec_type import AX_VDEC_MAX_GRP_NUM
from axcl.vdec.axcl_vdec_type import AX_VDEC_MAX_CHN_NUM
from axcl.vdec.axcl_vdec_type import AX_JDEC_MAX_CHN_NUM
from axcl.vdec.axcl_vdec_type import AX_DEC_MAX_CHN_NUM

from axcl.vdec.axcl_vdec_type import AX_VDEC_MAX_WIDTH
from axcl.vdec.axcl_vdec_type import AX_VDEC_MAX_HEIGHT
from axcl.vdec.axcl_vdec_type import AX_VDEC_MIN_WIDTH
from axcl.vdec.axcl_vdec_type import AX_VDEC_MIN_HEIGHT
from axcl.vdec.axcl_vdec_type import AX_VDEC_OUTPUT_MIN_WIDTH
from axcl.vdec.axcl_vdec_type import AX_VDEC_OUTPUT_MIN_HEIGHT

from axcl.vdec.axcl_vdec_type import AX_ENABLE_BOTH_VDEC_JDEC
from axcl.vdec.axcl_vdec_type import AX_ENABLE_ONLY_VDEC
from axcl.vdec.axcl_vdec_type import AX_ENABLE_ONLY_JDEC

from axcl.vdec.axcl_vdec_type import AX_VDEC_INPUT_MODE_FRAME

from axcl.vdec.axcl_vdec_type import AX_VDEC_OUTPUT_ORDER_DISP
from axcl.vdec.axcl_vdec_type import AX_VDEC_OUTPUT_ORDER_DEC

from axcl.vdec.axcl_vdec_type import AX_VDEC_OUTPUT_ORIGINAL
from axcl.vdec.axcl_vdec_type import AX_VDEC_OUTPUT_CROP
from axcl.vdec.axcl_vdec_type import AX_VDEC_OUTPUT_SCALE
from axcl.vdec.axcl_vdec_type import AX_VDEC_DISPLAY_MODE_PREVIEW
from axcl.vdec.axcl_vdec_type import AX_VDEC_DISPLAY_MODE_PLAYBACK

from axcl.vdec.axcl_vdec_type import VIDEO_DEC_MODE_IPB
from axcl.vdec.axcl_vdec_type import VIDEO_DEC_MODE_IP
from axcl.vdec.axcl_vdec_type import VIDEO_DEC_MODE_I
from axcl.vdec.axcl_vdec_type import VIDEO_DEC_MODE_GDR

from axcl.vdec.axcl_vdec_type import AX_ERR_VDEC_BUSY

# venc
from axcl.venc.axcl_venc_comm import MAX_VENC_CHN_NUM

from axcl.venc.axcl_venc_comm import MIN_VENC_PIC_WIDTH
from axcl.venc.axcl_venc_comm import MAX_VENC_PIC_WIDTH
from axcl.venc.axcl_venc_comm import MIN_VENC_PIC_HEIGHT
from axcl.venc.axcl_venc_comm import MAX_VENC_PIC_HEIGHT
from axcl.venc.axcl_venc_comm import MIN_JENC_PIC_WIDTH
from axcl.venc.axcl_venc_comm import MAX_JENC_PIC_WIDTH
from axcl.venc.axcl_venc_comm import MIN_JENC_PIC_HEIGHT
from axcl.venc.axcl_venc_comm import MAX_JENC_PIC_HEIGHT

from axcl.venc.axcl_venc_comm import AX_VENC_LINK_MODE
from axcl.venc.axcl_venc_comm import AX_VENC_UNLINK_MODE

from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_MAIN_PROFILE
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_MAIN_STILL_PICTURE_PROFILE
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_MAIN_10_PROFILE
from axcl.venc.axcl_venc_comm import AX_VENC_H264_BASE_PROFILE
from axcl.venc.axcl_venc_comm import AX_VENC_H264_MAIN_PROFILE
from axcl.venc.axcl_venc_comm import AX_VENC_H264_HIGH_PROFILE
from axcl.venc.axcl_venc_comm import AX_VENC_H264_HIGH_10_PROFILE

from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_1
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_2
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_2_1
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_3
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_3_1
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_4
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_4_1
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_5
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_5_1
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_5_2
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_6
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_6_1
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_LEVEL_6_2

from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_1
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_1_b
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_1_1
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_1_2
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_1_3
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_2
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_2_1
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_2_2
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_3
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_3_1
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_3_2
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_4
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_4_1
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_4_2
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_5
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_5_1
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_5_2
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_6
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_6_1
from axcl.venc.axcl_venc_comm import AX_VENC_H264_LEVEL_6_2

from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_MAIN_TIER
from axcl.venc.axcl_venc_comm import AX_VENC_HEVC_HIGH_TIER

from axcl.venc.axcl_venc_comm import AX_VENC_STREAM_BIT_8
from axcl.venc.axcl_venc_comm import AX_VENC_STREAM_BIT_10

from axcl.venc.axcl_venc_comm import AX_VENC_VIDEO_ENCODER
from axcl.venc.axcl_venc_comm import AX_VENC_JPEG_ENCODER
from axcl.venc.axcl_venc_comm import AX_VENC_MULTI_ENCODER

from axcl.venc.axcl_venc_comm import AX_VENC_SCHED_OTHER
from axcl.venc.axcl_venc_comm import AX_VENC_SCHED_FIFO
from axcl.venc.axcl_venc_comm import AX_VENC_SCHED_RR

from axcl.venc.axcl_venc_comm import AX_VENC_GOPMODE_NORMALP
from axcl.venc.axcl_venc_comm import AX_VENC_GOPMODE_ONELTR
from axcl.venc.axcl_venc_comm import AX_VENC_GOPMODE_SVC_T

from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H264CBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H264VBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H264AVBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H264QVBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H264CVBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H264FIXQP
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H264QPMAP

from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_MJPEGCBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_MJPEGVBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_MJPEGFIXQP

from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H265CBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H265VBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H265AVBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H265QVBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H265CVBR
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H265FIXQP
from axcl.venc.axcl_venc_comm import AX_VENC_RC_MODE_H265QPMAP

from axcl.venc.axcl_venc_comm import AX_VENC_RC_CTBRC_DISABLE
from axcl.venc.axcl_venc_comm import AX_VENC_RC_CTBRC_QUALITY
from axcl.venc.axcl_venc_comm import AX_VENC_RC_CTBRC_RATE
from axcl.venc.axcl_venc_comm import AX_VENC_RC_CTBRC_QUALITY_RATE

from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_QP_DISABLE
from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_QP_DELTA
from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_QP_ABS

from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_BLOCK_DISABLE
from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_BLOCK_SKIP
from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_BLOCK_IPCM

from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_BLOCK_UNIT_NONE
from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_BLOCK_UNIT_64x64
from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_BLOCK_UNIT_32x32
from axcl.venc.axcl_venc_comm import AX_VENC_QPMAP_BLOCK_UNIT_16x16

from axcl.venc.axcl_venc_comm import AX_ERR_VENC_FLOW_END

# dmadim
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_ENDIAN_DEF
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_ENDIAN_32
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_ENDIAN_16
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_1D
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_2D
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_3D
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_4D
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_MEMORY_INIT
from axcl.dmadim.axcl_dmadim_type import AX_DMADIM_CHECKSUM

# ive
from axcl.ive.axcl_ive_type import AX_IVE_DMA_MODE_DIRECT_COPY
from axcl.ive.axcl_ive_type import AX_IVE_DMA_MODE_INTERVAL_COPY
from axcl.ive.axcl_ive_type import AX_IVE_DMA_MODE_SET_3BYTE
from axcl.ive.axcl_ive_type import AX_IVE_DMA_MODE_SET_8BYTE

from axcl.ive.axcl_ive_type import AX_IVE_SUB_MODE_ABS
from axcl.ive.axcl_ive_type import AX_IVE_SUB_MODE_SHIFT

from axcl.ive.axcl_ive_type import AX_IVE_CCL_MODE_4C
from axcl.ive.axcl_ive_type import AX_IVE_CCL_MODE_8C

from axcl.ive.axcl_ive_type import AX_IVE_INTEG_OUT_CTRL_COMBINE
from axcl.ive.axcl_ive_type import AX_IVE_INTEG_OUT_CTRL_SUM
from axcl.ive.axcl_ive_type import AX_IVE_INTEG_OUT_CTRL_SQSUM

from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_BINARY
from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_TRUNC
from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_TO_MINVAL
from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_MIN_MID_MAX
from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_ORI_MID_MAX
from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_MIN_MID_ORI
from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_MIN_ORI_MAX
from axcl.ive.axcl_ive_type import AX_IVE_THRESH_MODE_ORI_MID_ORI

from axcl.ive.axcl_ive_type import AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_S8
from axcl.ive.axcl_ive_type import AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_U8_ABS
from axcl.ive.axcl_ive_type import AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_U8_BIAS
from axcl.ive.axcl_ive_type import AX_IVE_16BIT_TO_8BIT_MODE_U16_TO_U8

from axcl.ive.axcl_ive_type import AX_IVE_ASPECT_RATIO_FORCE_RESIZE
from axcl.ive.axcl_ive_type import AX_IVE_ASPECT_RATIO_HORIZONTAL_LEFT
from axcl.ive.axcl_ive_type import AX_IVE_ASPECT_RATIO_HORIZONTAL_CENTER
from axcl.ive.axcl_ive_type import AX_IVE_ASPECT_RATIO_HORIZONTAL_RIGHT
from axcl.ive.axcl_ive_type import AX_IVE_ASPECT_RATIO_VERTICAL_TOP
from axcl.ive.axcl_ive_type import AX_IVE_ASPECT_RATIO_VERTICAL_CENTER
from axcl.ive.axcl_ive_type import AX_IVE_ASPECT_RATIO_VERTICAL_BOTTOM

from axcl.ive.axcl_ive_type import AX_IVE_MAU_ID_0

from axcl.ive.axcl_ive_type import AX_IVE_MAU_ORDER_ASCEND
from axcl.ive.axcl_ive_type import AX_IVE_MAU_ORDER_DESCEND

from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_UNKNOWN
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_UINT8
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_UINT16
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_FLOAT32
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_SINT16
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_SINT8
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_SINT32
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_UINT32
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_FLOAT64
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_FLOAT16
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_UINT64
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_SINT64
from axcl.ive.axcl_ive_type import AX_IVE_MAU_DT_BFLOAT16
