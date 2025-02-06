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
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.lib.axcl_lib import libaxcl_vdec
from axcl.vdec.axcl_vdec_type import *
from axcl.ax_global_type import *
from axcl.axcl_base import *
from axcl.sys.axcl_sys_type import *
from axcl.utils.axcl_logger import *


def get_buf_size(width: int, height: int, pixel_fmt: int, compress_info: dict, codec_type: int) -> int:
    """
    Calculate buffer size of channel attribute.

    :param int width: Width.
    :param int height: Height.
    :param int pixel_fmt: :class:`AX_IMG_FORMAT_E <axcl.ax_global_type.AX_IMG_FORMAT_E>`.
    :param dict compress_info: :class:`AX_FRAME_COMPRESS_INFO_T <axcl.ax_global_type.AX_FRAME_COMPRESS_INFO_T>`.
    :param int codec_type: :class:`AX_PAYLOAD_TYPE_E <axcl.ax_global_type.AX_PAYLOAD_TYPE_E>`.
    :returns: **ret** (*int*) - Buffer size.
    """

    def ax_comm_align(value, n):
        return (value + n - 1) & ~(n - 1)

    pic_size_in_mbs = 0
    pic_size = 0
    dmv_mem_size = 0
    ref_buff_size = 0
    pix_bits = 8
    height_align = 0
    width_align = 0
    align_size = (1 << 8)
    ax_fbc_tile128x2_size = [0, 32, 64, 96, 128, 160, 192, 224, 256, 288]

    if codec_type in [PT_H264, PT_H265]:
        if pixel_fmt in [
            AX_FORMAT_YUV400, AX_FORMAT_YUV420_PLANAR, AX_FORMAT_YUV420_PLANAR_VU,
            AX_FORMAT_YUV420_SEMIPLANAR, AX_FORMAT_YUV420_SEMIPLANAR_VU,
            AX_FORMAT_YUV422_PLANAR, AX_FORMAT_YUV422_PLANAR_VU,
            AX_FORMAT_YUV422_SEMIPLANAR, AX_FORMAT_YUV422_SEMIPLANAR_VU,
            AX_FORMAT_YUV422_INTERLEAVED_YUVY, AX_FORMAT_YUV422_INTERLEAVED_YUYV,
            AX_FORMAT_YUV422_INTERLEAVED_UYVY, AX_FORMAT_YUV422_INTERLEAVED_VYUY,
            AX_FORMAT_YUV444_PLANAR, AX_FORMAT_YUV444_PLANAR_VU,
            AX_FORMAT_YUV444_SEMIPLANAR, AX_FORMAT_YUV444_SEMIPLANAR_VU,
            AX_FORMAT_YUV444_PACKED
        ]:
            pix_bits = 8
        elif pixel_fmt in [
            AX_FORMAT_YUV400_10BIT, AX_FORMAT_YUV420_PLANAR_10BIT_UV_PACKED_4Y5B,
            AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P101010, AX_FORMAT_YUV444_PACKED_10BIT_P101010
        ]:
            pix_bits = 10
        elif pixel_fmt in [
            AX_FORMAT_YUV420_PLANAR_10BIT_I010, AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P010,
            AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P016, AX_FORMAT_YUV420_SEMIPLANAR_10BIT_I016,
            AX_FORMAT_YUV444_PACKED_10BIT_P010
        ]:
            pix_bits = 16
        else:
            pix_bits = 8

        # luma
        height_align = ax_comm_align(height, 2)
        width_align = ax_comm_align(width, align_size)

        if compress_info is not None and compress_info['compress_mode'] == AX_COMPRESS_MODE_LOSSY:
            ax_tile128x2_size = 128 * 2 * pix_bits // 8
            pic_size = width_align * height_align * ax_fbc_tile128x2_size[compress_info['compress_level']] // ax_tile128x2_size
        else:
            pic_size = height_align * width_align

        # chroma
        if pixel_fmt != AX_FORMAT_YUV400:
            height_align = (height_align >> 1)
            if compress_info is not None and compress_info['compress_mode'] == AX_COMPRESS_MODE_LOSSY:
                ax_tile128x2_size = 128 * 2 * pix_bits // 8
                pic_size += width_align * height_align * ax_fbc_tile128x2_size[compress_info['compress_level']] // ax_tile128x2_size
            else:
                pic_size += width_align * height_align

        # buffer size of dpb pic = pic_size + dir_mv_size + tbl_size
        dmv_mem_size = pic_size_in_mbs * 64
        ref_buff_size = pic_size + dmv_mem_size + 32

    elif codec_type in [PT_JPEG, PT_MJPEG]:
        pic_size = (ax_comm_align(height, 2) * ax_comm_align(width, 64) * 3) >> 1
        ref_buff_size = pic_size

    else:
        ref_buff_size = -1

    return ref_buff_size


def init(mod_attr: dict) -> int:
    """
    Initialize decoder module.
    This api should be called at first before any APIs of decoder.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_Init(const AX_VDEC_MOD_ATTR_T *pstModAttr);`
        **python**              `ret = axcl.vdec.init(mod_attr)`
        ======================= =====================================================

    :param dict mod_attr: :class:`AX_VDEC_MOD_ATTR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_MOD_ATTR_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        mod_attr = {
            "max_group_count": 32,
            "dec_module": axcl.AX_ENABLE_BOTH_VDEC_JDEC,
            "vdec_mc": 0,
            "vdec_virt_chn": 0
        }

        ret = axcl.vdec.init(mod_attr)
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_Init.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_Init.argtypes = [POINTER(AX_VDEC_MOD_ATTR_T)]
        c_mode_attr = AX_VDEC_MOD_ATTR_T()
        c_mode_attr.dict2struct(mod_attr)
        ret = libaxcl_vdec.AXCL_VDEC_Init(byref(c_mode_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def deinit() -> int:
    """
    De-initialize decoder module.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_Deinit(AX_VOID);`
        **python**              `ret = axcl.vdec.deinit()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_Deinit.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_Deinit.argtypes = None
        ret = libaxcl_vdec.AXCL_VDEC_Deinit()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def extract_stream_header_info(stream_buf: dict, video_type: int) -> tuple[dict, int]:
    """
    Extract video information of input stream.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_ExtractStreamHeaderInfo(const AX_VDEC_STREAM_T *pstStreamBuf, AX_PAYLOAD_TYPE_E enVideoType, AX_VDEC_BITSTREAM_INFO_T *pstBitStreamInfo);`
        **python**              `bit_stream_info, ret = axcl.vdec.extract_stream_header_info(stream_buf, video_type)`
        ======================= =====================================================

    :param dict stream_buf: :class:`AX_VDEC_STREAM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_STREAM_T>` to extract video information.
    :param int video_type: :class:`AX_PAYLOAD_TYPE_E <axcl.ax_global_type.AX_PAYLOAD_TYPE_E>`.
    :returns: tuple[dict, int]

        - **bitstream_info** (*dict*) - :class:`AX_VDEC_BITSTREAM_INFO_T <axcl.vdec.axcl_vdec_type.AX_VDEC_BITSTREAM_INFO_T>`.
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    bit_stream_info = {}
    try:
        libaxcl_vdec.AXCL_VDEC_ExtractStreamHeaderInfo.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_ExtractStreamHeaderInfo.argtypes = [POINTER(AX_VDEC_STREAM_T), AX_PAYLOAD_TYPE_E, POINTER(AX_VDEC_BITSTREAM_INFO_T)]
        c_bit_stream_info = AX_VDEC_BITSTREAM_INFO_T()
        c_stream_buf = AX_VDEC_STREAM_T()
        c_stream_buf.dict2struct(stream_buf)
        c_video_type = AX_PAYLOAD_TYPE_E(video_type)
        ret = libaxcl_vdec.AXCL_VDEC_ExtractStreamHeaderInfo(byref(c_stream_buf), c_video_type, byref(c_bit_stream_info))
        if ret == AXCL_SUCC:
            bit_stream_info = c_bit_stream_info.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return bit_stream_info, ret


def create_grp(grp: int, grp_attr: dict) -> int:
    """
    Create a specified group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_CreateGrp(AX_VDEC_GRP VdGrp, const AX_VDEC_GRP_ATTR_T *pstGrpAttr);`
        **python**              `ret = axcl.vdec.create_grp(grp, grp_attr)`
        ======================= =====================================================

    :param int grp: Group id to create.
    :param dict grp_attr: :class:`AX_VDEC_GRP_ATTR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_ATTR_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_CreateGrp.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_CreateGrp.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_GRP_ATTR_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_grp_attr = AX_VDEC_GRP_ATTR_T()
        c_grp_attr.dict2struct(grp_attr)
        ret = libaxcl_vdec.AXCL_VDEC_CreateGrp(c_grp, byref(c_grp_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def create_grp_ex(grp_attr: dict) -> tuple[int, int]:
    """
    Create a new group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_CreateGrpEx(AX_VDEC_GRP *VdGrp, const AX_VDEC_GRP_ATTR_T *pstGrpAttr);`
        **python**              `grp, ret = axcl.vdec.create_grp_ex(grp_attr)`
        ======================= =====================================================

    :param dict grp_attr: :class:`AX_VDEC_GRP_ATTR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_ATTR_T>`.
    :returns: tuple[int, int]

        - **group id** (*int*) - The group id created.
        - **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        grp_attr = {
            "codec_type": axcl.PT_H264,
            "input_mode": axcl.AX_VDEC_INPUT_MODE_STREAM,
            "max_pic_width": width,
            "max_pic_height": height,
            "stream_buf_size": width * height * 2,
            "sdk_auto_frame_pool": 1,
            "skip_sdk_stream_pool": 0
        }

        grp_id, ret = axcl.vdec.create_grp_ex(grp_attr)
    """
    ret = -1
    c_grp = AX_VDEC_GRP(-1)
    try:
        libaxcl_vdec.AXCL_VDEC_CreateGrpEx.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_CreateGrpEx.argtypes = [POINTER(AX_VDEC_GRP), POINTER(AX_VDEC_GRP_ATTR_T)]
        c_grp_attr = AX_VDEC_GRP_ATTR_T()
        c_grp_attr.dict2struct(grp_attr)
        ret = libaxcl_vdec.AXCL_VDEC_CreateGrpEx(byref(c_grp), byref(c_grp_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_grp.value, ret


def destroy_grp(grp: int) -> int:
    """
    Destroy a specified group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_DestroyGrp(AX_VDEC_GRP VdGrp);`
        **python**              `ret = axcl.vdec.destroy_grp()`
        ======================= =====================================================

    :param int grp: Group id to destroy.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_DestroyGrp.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_DestroyGrp.argtypes = [AX_VDEC_GRP]
        ret = libaxcl_vdec.AXCL_VDEC_DestroyGrp(AX_VDEC_GRP(grp))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_grp_attr(grp: int) -> tuple[dict, int]:
    """
    Get the specified group attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_GetGrpAttr(AX_VDEC_GRP VdGrp, AX_VDEC_GRP_ATTR_T *pstGrpAttr);`
        **python**              `grp_attr, ret = axcl.vdec.get_grp_attr()`
        ======================= =====================================================

    :param int grp: Group id to get.
    :returns: tuple[dict, int]

        - **grp_attr** (*dict*) - :class:`AX_VDEC_GRP_ATTR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    grp_attr = {}
    try:
        libaxcl_vdec.AXCL_VDEC_GetGrpAttr.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_GetGrpAttr.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_GRP_ATTR_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_grp_attr = AX_VDEC_GRP_ATTR_T()
        ret = libaxcl_vdec.AXCL_VDEC_GetGrpAttr(c_grp, byref(c_grp_attr))
        if ret == AXCL_SUCC:
            grp_attr = c_grp_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return grp_attr, ret


def set_grp_attr(grp: int, grp_attr: dict) -> int:
    """
    Set a specified group attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_SetGrpAttr(AX_VDEC_GRP VdGrp, const AX_VDEC_GRP_ATTR_T *pstGrpAttr);`
        **python**              `ret = axcl.vdec.set_grp_attr(grp, grp_attr)`
        ======================= =====================================================

    :param int grp: Group id.
    :param dict grp_attr: :class:`AX_VDEC_GRP_ATTR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_ATTR_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_SetGrpAttr.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_SetGrpAttr.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_GRP_ATTR_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_grp_attr = AX_VDEC_GRP_ATTR_T()
        c_grp_attr.dict2struct(grp_attr)
        ret = libaxcl_vdec.AXCL_VDEC_SetGrpAttr(c_grp, byref(c_grp_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def start_recv_stream(grp: int, recv_param: dict) -> int:
    """
    Start to receive streams.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_StartRecvStream(AX_VDEC_GRP VdGrp, const AX_VDEC_RECV_PIC_PARAM_T *pstRecvParam);`
        **python**              `ret = axcl.vdec.start_recv_stream(grp, recv_param)`
        ======================= =====================================================

    :param int grp: Group id.
    :param dict recv_param: :class:`AX_VDEC_RECV_PIC_PARAM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_RECV_PIC_PARAM_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        recv_param = {
            "recv_pic_num": -1
        }

        ret = axcl.vdec.start_recv_stream(grp_id, recv_param)
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_StartRecvStream.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_StartRecvStream.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_RECV_PIC_PARAM_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_recv_param = AX_VDEC_RECV_PIC_PARAM_T()
        c_recv_param.dict2struct(recv_param)
        ret = libaxcl_vdec.AXCL_VDEC_StartRecvStream(c_grp, byref(c_recv_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def stop_recv_stream(grp: int) -> int:
    """
    Stop to receive streams.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_StopRecvStream(AX_VDEC_GRP VdGrp);`
        **python**              `ret = axcl.vdec.stop_recv_stream(grp)`
        ======================= =====================================================

    :param int grp: Group id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_StopRecvStream.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_StopRecvStream.argtypes = [AX_VDEC_GRP]
        c_grp = AX_VDEC_GRP(grp)
        ret = libaxcl_vdec.AXCL_VDEC_StopRecvStream(c_grp)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def query_status(grp: int) -> tuple[dict, int]:
    """
    Query the decoded status of the specified group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_QueryStatus(AX_VDEC_GRP VdGrp, AX_VDEC_GRP_STATUS_T *pstGrpStatus);`
        **python**              `grp_status, ret = axcl.vdec.query_status(grp)`
        ======================= =====================================================

    :param int grp: Group id to get.
    :returns: tuple[dict, int]

        - **grp_status** (*dict*) - :class:`AX_VDEC_GRP_STATUS_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_STATUS_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        grp_status, ret = axcl.vdec.query_status(grp_id)
        if 0 == ret:
            print(f"left_pics[0] = {grp_status['left_pics'][0]}, left_pics[1] = {grp_status['left_pics'][1]}, left_pics[2] = {grp_status['left_pics'][2]}")
            print(f"recv_stream_frames = {grp_status['recv_stream_frames']}")
            print(f"decode_stream_frames = {grp_status['decode_stream_frames']}")
    """
    ret = -1
    grp_status = {}
    try:
        libaxcl_vdec.AXCL_VDEC_QueryStatus.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_QueryStatus.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_GRP_STATUS_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_grp_status = AX_VDEC_GRP_STATUS_T()
        ret = libaxcl_vdec.AXCL_VDEC_QueryStatus(c_grp, byref(c_grp_status))
        if ret == AXCL_SUCC:
            grp_status = c_grp_status.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return grp_status, ret


def reset_grp(grp: int) -> int:
    """
    Reset the specified group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_ResetGrp(AX_VDEC_GRP VdGrp);`
        **python**              `ret = axcl.vdec.reset_grp(grp)`
        ======================= =====================================================

    :param int grp: Group id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_ResetGrp.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_ResetGrp.argtypes = [AX_VDEC_GRP]
        c_grp = AX_VDEC_GRP(grp)
        ret = libaxcl_vdec.AXCL_VDEC_ResetGrp(c_grp)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_grp_param(grp: int, grp_param: dict) -> int:
    """
    set the specified group parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_SetGrpParam(AX_VDEC_GRP VdGrp, const AX_VDEC_GRP_PARAM_T *pstGrpParam);`
        **python**              `ret = axcl.vdec.set_grp_param(grp, grp_param)`
        ======================= =====================================================

    :param int grp: Group id.
    :param dict grp_param: :class:`AX_VDEC_GRP_PARAM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_PARAM_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        grp_param = {
            "vdec_video_param": {
                "output_order": axcl.AX_VDEC_OUTPUT_ORDER_DEC,
                "vdec_mode": axcl.VIDEO_DEC_MODE_IPB
            }
        }

        ret = axcl.vdec.set_grp_param(grp_id, grp_param)
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_SetGrpParam.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_SetGrpParam.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_GRP_PARAM_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_grp_param = AX_VDEC_GRP_PARAM_T()
        c_grp_param.dict2struct(grp_param)
        ret = libaxcl_vdec.AXCL_VDEC_SetGrpParam(c_grp, byref(c_grp_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_grp_param(grp: int) -> tuple[dict, int]:
    """
    Get the specified group parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_GetGrpParam(AX_VDEC_GRP VdGrp, AX_VDEC_GRP_PARAM_T *pstGrpParam);`
        **python**              `grp_param, ret = axcl.vdec.get_grp_param(grp)`
        ======================= =====================================================

    :param int grp: Group id to get.
    :returns: tuple[dict, int]

        - **grp_param** (*dict*) - :class:`AX_VDEC_GRP_PARAM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_PARAM_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    grp_param = {}
    try:
        libaxcl_vdec.AXCL_VDEC_GetGrpParam.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_GetGrpParam.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_GRP_PARAM_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_grp_param = AX_VDEC_GRP_PARAM_T()
        ret = libaxcl_vdec.AXCL_VDEC_GetGrpParam(c_grp, byref(c_grp_param))
        if ret == AXCL_SUCC:
            grp_param = c_grp_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return grp_param, ret


def select_grp(ms: int) -> tuple[dict, int]:
    """
    Select to traverse all groups to query check if decoding is complete.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_SelectGrp(AX_VDEC_GRP_SET_INFO_T *pstGrpSet, AX_S32 s32MilliSec);`
        **python**              `grp_set, ret = axcl.vdec.select_grp(ms)`
        ======================= =====================================================

    :param int ms: Timeout in milliseconds to query.
    :returns: tuple[dict, int]

        - **grp_set** (*dict*) - :class:`AX_VDEC_GRP_SET_INFO_T <axcl.vdec.axcl_vdec_type.AX_VDEC_GRP_SET_INFO_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        grp_set, ret = axcl.vdec.select_grp(1000)
        if 0 == ret:
            for i in range(grp_set['grp_count']):
                chn_set = grp_set['chn_set'][i]
                for j in range(chn_set['chn_count']):
                    grp_id = chn_set['grp']
                    chn_id = chn_set['chn'][j]
                    frame_info, ret = axcl.vdec.get_chn_frame(grp_id, chn_id, 1000)
    """
    ret = -1
    grp_set = {}
    try:
        libaxcl_vdec.AXCL_VDEC_SelectGrp.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_SelectGrp.argtypes = [POINTER(AX_VDEC_GRP_SET_INFO_T), AX_S32]
        c_ms = AX_S32(ms)
        c_grp_set = AX_VDEC_GRP_SET_INFO_T()
        ret = libaxcl_vdec.AXCL_VDEC_SelectGrp(byref(c_grp_set), c_ms)
        if ret == AXCL_SUCC:
            grp_set = c_grp_set.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return grp_set, ret


def send_stream(grp: int, stream: dict, ms: int) -> int:
    """
    Send a stream buffer to decoder.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_SendStream(AX_VDEC_GRP VdGrp, const AX_VDEC_STREAM_T *pstStream, AX_S32 s32MilliSec);`
        **python**              `ret = axcl.vdec.send_stream(grp, stream, ms)`
        ======================= =====================================================

    :param int grp: Group id.
    :param dict stream: :class:`AX_VDEC_STREAM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_STREAM_T>` to send.
    :param int ms: Timeout in milliseconds to send.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        from axcl.utils.axcl_utils import bytes_to_ptr

        stream = {
            'addr': bytes_to_ptr(data),
            'stream_pack_len': 0 if data is None else len(data),
            'end_of_frame': 1,
            'end_of_stream': 1 if data is None or len(data) == 0 else 0,
            'pts': pts,
            'user_data': user_data
        }

        ret = axcl.vdec.send_stream(grp, stream, 1000)
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_SendStream.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_SendStream.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_STREAM_T), AX_S32]
        c_grp = AX_VDEC_GRP(grp)
        c_stream = AX_VDEC_STREAM_T()
        c_stream.dict2struct(stream)
        c_ms = AX_S32(ms)
        ret = libaxcl_vdec.AXCL_VDEC_SendStream(c_grp, byref(c_stream), c_ms)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_chn_frame(grp: int, chn: int, ms: int) -> tuple[dict, int]:
    """
    Get a decoded frame from decoder.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_GetChnFrame(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, AX_VIDEO_FRAME_INFO_T *pstFrameInfo, AX_S32 s32MilliSec);`
        **python**              `frame_info, ret = axcl.vdec.get_chn_frame(grp, chn, ms)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int chn: Channel id.
    :param int ms: Timeout in milliseconds to get decoded frame.
    :returns: tuple[dict, int]

        - **frame_info** (*dict*) - :class:`AX_VIDEO_FRAME_INFO_T <axcl.ax_global_type.AX_VIDEO_FRAME_INFO_T>`.
        - **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        frame_info, ret = axcl.vdec.get_chn_frame(grp, chn, 1000)
        if 0 == ret:
            video_frame = frame_info['video_frame']
            print(
                f"seq_num {video_frame['seq_num']}: {video_frame['width']} x {video_frame['height']} stride {video_frame['pic_stride'][0]}, "
                f"size {video_frame['frame_size']}, phy_addr 0x{video_frame['phy_addr'][0]:x}, blk 0x{video_frame['blk_id'][0]:x}"
            )

            ret = axcl.vdec.release_chn_frame(grp, chn, frame_info)
    """
    ret = -1
    frame_info = {}
    try:
        libaxcl_vdec.AXCL_VDEC_GetChnFrame.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_GetChnFrame.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN, POINTER(AX_VIDEO_FRAME_INFO_T), AX_S32]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        c_frame_info = AX_VIDEO_FRAME_INFO_T()
        c_ms = AX_S32(ms)
        ret = libaxcl_vdec.AXCL_VDEC_GetChnFrame(c_grp, c_chn, byref(c_frame_info), c_ms)
        if ret == AXCL_SUCC:
            frame_info = c_frame_info.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return frame_info, ret


def release_chn_frame(grp: int, chn: int, frame_info: dict) -> int:
    """
    Release the decoded frame.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_ReleaseChnFrame(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, const AX_VIDEO_FRAME_INFO_T *pstFrameInfo);`
        **python**              `ret = axcl.vdec.release_chn_frame(grp, chn, frame_info)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int chn: Channel id.
    :param dict frame_info: :class:`AX_VIDEO_FRAME_INFO_T <axcl.ax_global_type.AX_VIDEO_FRAME_INFO_T>` received from :func:`get_chn_frame`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        frame_info, ret = axcl.vdec.get_chn_frame(grp, chn, 1000)
        if 0 == ret:
            ret = axcl.vdec.release_chn_frame(grp, chn, frame_info)
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_ReleaseChnFrame.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_ReleaseChnFrame.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN, POINTER(AX_VIDEO_FRAME_INFO_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        c_frame_info = AX_VIDEO_FRAME_INFO_T()
        c_frame_info.dict2struct(frame_info)
        ret = libaxcl_vdec.AXCL_VDEC_ReleaseChnFrame(c_grp, c_chn, byref(c_frame_info))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_user_data(grp: int) -> tuple[dict, int]:
    """
    Get user data.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_GetUserData(AX_VDEC_GRP VdGrp, AX_VDEC_USERDATA_T *pstUserData);`
        **python**              `user_data, ret = axcl.vdec.get_user_data(grp)`
        ======================= =====================================================

    :param int grp: Group id.
    :returns: tuple[dict, int]

        - **user_data** (*dict*) - :class:`AX_VDEC_USERDATA_T <axcl.vdec.axcl_vdec_type.AX_VDEC_USERDATA_T>`.
        - **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        user_data, ret = axcl.vdec.get_user_data(grp)
        if 0 == ret:
            ret = axcl.vdec.release_user_data(grp, user_data)
    """
    ret = -1
    user_data = {}
    try:
        libaxcl_vdec.AXCL_VDEC_GetUserData.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_GetUserData.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_USERDATA_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_user_data = AX_VDEC_USERDATA_T()
        ret = libaxcl_vdec.AXCL_VDEC_GetUserData(c_grp, byref(c_user_data))
        if ret == AXCL_SUCC:
            user_data = c_user_data.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return user_data, ret


def release_user_data(grp: int, user_data: dict) -> int:
    """
    Release user data.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_ReleaseUserData(AX_VDEC_GRP VdGrp, const AX_VDEC_USERDATA_T *pstUserData);`
        **python**              `ret = axcl.vdec.release_user_data(grp, user_data)`
        ======================= =====================================================

    :param int grp: Group id.
    :param dict user_data: :class:`AX_VDEC_USERDATA_T <axcl.vdec.axcl_vdec_type.AX_VDEC_USERDATA_T>` received from :func:`get_user_data`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_ReleaseUserData.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_ReleaseUserData.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_USERDATA_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_user_data = AX_VDEC_USERDATA_T()
        c_user_data.dict2struct(user_data)
        ret = libaxcl_vdec.AXCL_VDEC_ReleaseUserData(c_grp, byref(c_user_data))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_user_pic(grp: int, user_pic: dict) -> int:
    """
    Configure user picture. Invoke :func:`enable_user_pic` to enable insertion.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_SetUserPic(AX_VDEC_GRP VdGrp, const AX_VDEC_USRPIC_T *pstUsrPic);`
        **python**              `ret = axcl.vdec.set_user_pic(grp, user_pic)`
        ======================= =====================================================

    :param int grp: Group id.
    :param dict user_pic: :class:`AX_VDEC_USRPIC_T <axcl.vdec.axcl_vdec_type.AX_VDEC_USRPIC_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_SetUserPic.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_SetUserPic.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_USRPIC_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_user_pic = AX_VDEC_USRPIC_T()
        c_user_pic.dict2struct(user_pic)
        ret = libaxcl_vdec.AXCL_VDEC_SetUserPic(c_grp, byref(c_user_pic))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def enable_user_pic(grp: int) -> int:
    """
    Enable to insert user picture.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_EnableUserPic(AX_VDEC_GRP VdGrp);`
        **python**              `ret = axcl.vdec.enable_user_pic(grp)`
        ======================= =====================================================

    :param int grp: Group id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_EnableUserPic.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_EnableUserPic.argtypes = [AX_VDEC_GRP]
        c_grp = AX_VDEC_GRP(grp)
        ret = libaxcl_vdec.AXCL_VDEC_EnableUserPic(c_grp)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def disable_user_pic(grp: int) -> int:
    """
    Disable to insert user picture.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_DisableUserPic(AX_VDEC_GRP VdGrp);`
        **python**              `ret = axcl.vdec.disable_user_pic(grp)`
        ======================= =====================================================

    :param int grp: Group id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_DisableUserPic.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_DisableUserPic.argtypes = [AX_VDEC_GRP]
        c_grp = AX_VDEC_GRP(grp)
        ret = libaxcl_vdec.AXCL_VDEC_DisableUserPic(c_grp)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_display_mode(grp: int, display_mode: int) -> int:
    """
    Set display mode.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_SetDisplayMode(AX_VDEC_GRP VdGrp, AX_VDEC_DISPLAY_MODE_E enDisplayMode);`
        **python**              `ret = axcl.vdec.set_display_mode(grp, display_mode)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int display_mode: :class:`AX_VDEC_DISPLAY_MODE_E <axcl.vdec.axcl_vdec_type.AX_VDEC_DISPLAY_MODE_E>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    .. note::

        - If play local file, recommends `axcl.AX_VDEC_DISPLAY_MODE_PLAYBACK`
        - If play RTSP stream, recommends `axcl.AX_VDEC_DISPLAY_MODE_PREVIEW`
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_SetDisplayMode.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_SetDisplayMode.argtypes = [AX_VDEC_GRP, AX_VDEC_DISPLAY_MODE_E]
        c_grp = AX_VDEC_GRP(grp)
        c_display_mode = AX_VDEC_DISPLAY_MODE_E(display_mode)
        ret = libaxcl_vdec.AXCL_VDEC_SetDisplayMode(c_grp, c_display_mode)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_display_mode(grp: int) -> tuple[int, int]:
    """
    Get display mode.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_GetDisplayMode(AX_VDEC_GRP VdGrp, AX_VDEC_DISPLAY_MODE_E *penDisplayMode);`
        **python**              `display_mode, ret = axcl.vdec.get_display_mode(grp)`
        ======================= =====================================================

    :param int grp: Group id.
    :returns: tuple[int, int]

        - **display_mode** (*int*) - :class:`AX_VDEC_DISPLAY_MODE_E <axcl.vdec.axcl_vdec_type.AX_VDEC_DISPLAY_MODE_E>`.
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    display_mode = AX_VDEC_DISPLAY_MODE_PREVIEW
    try:
        libaxcl_vdec.AXCL_VDEC_GetDisplayMode.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_GetDisplayMode.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_DISPLAY_MODE_E)]
        c_grp = AX_VDEC_GRP(grp)
        c_display_mode = AX_VDEC_DISPLAY_MODE_E(AX_VDEC_DISPLAY_MODE_PREVIEW)
        ret = libaxcl_vdec.AXCL_VDEC_GetDisplayMode(c_grp, byref(c_display_mode))
        if ret == AXCL_SUCC:
            display_mode = c_display_mode.value
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return display_mode, ret


def attach_pool(grp: int, chn: int, pool: int) -> int:
    """
    Attach a user pool.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_AttachPool(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, AX_POOL PoolId);`
        **python**              `ret = axcl.vdec.attach_pool(grp, chn, pool)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int chn: Channel id.
    :param int pool: Pool id created by :func:`create_pool <axcl.pool.axcl_pool.create_pool>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_AttachPool.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_AttachPool.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN, AX_POOL]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        c_pool_id = AX_POOL(pool)
        ret = libaxcl_vdec.AXCL_VDEC_AttachPool(c_grp, c_chn, c_pool_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def detach_pool(grp: int, chn: int) -> int:
    """
    Detach user pool.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_DetachPool(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn);`
        **python**              `ret = axcl.vdec.detach_pool(grp, chn)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int chn: Channel id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_DetachPool.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_DetachPool.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        ret = libaxcl_vdec.AXCL_VDEC_DetachPool(c_grp, c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def enable_chn(grp: int, chn: int) -> int:
    """
    Enable channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_EnableChn(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn);`
        **python**              `ret = axcl.vdec.enable_chn(grp, chn)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int chn: Channel id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_EnableChn.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_EnableChn.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        ret = libaxcl_vdec.AXCL_VDEC_EnableChn(c_grp, c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def disable_chn(grp: int, chn: int) -> int:
    """
    Disable channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_DisableChn(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn);`
        **python**              `ret = axcl.vdec.disable_chn(grp, chn)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int chn: Channel id.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_DisableChn.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_DisableChn.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        ret = libaxcl_vdec.AXCL_VDEC_DisableChn(c_grp, c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_chn_attr(grp: int, chn: int, chn_attr: dict) -> int:
    """
    Set channel attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_SetChnAttr(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, const AX_VDEC_CHN_ATTR_T *pstVdChnAttr);`
        **python**              `ret = axcl.vdec.set_chn_attr(grp, chn, chn_attr)`
        ======================= =====================================================

    :param int grp: Group id.
    :param int chn: Channel id.
    :param dict chn_attr: :class:`AX_VDEC_CHN_ATTR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_CHN_ATTR_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        def align_up(x, align):
            return (x + (align - 1)) & ~(align - 1)

        compress_info = {
                'compress_mode': axcl.AX_COMPRESS_MODE_NONE,
                'compress_level': 4
        }

        img_format = axcl.AX_FORMAT_YUV420_SEMIPLANAR

        chn_attr = {
            'pic_width': width,
            'pic_height': height,
            'frame_stride': align_up(width, 256),
            'frame_padding': 0,
            'crop_x': 0,
            'crop_y': 0,
            'scale_ratio_x': 0,
            'scale_ratio_y': 0,
            'output_fifo_depth': 4,
            'frame_buf_cnt': 8,
            'frame_buf_size': axcl.vdec.get_buf_size(width, height, img_format, compress_info, axcl.PT_H264),
            'output_mode': axcl.AX_VDEC_OUTPUT_ORIGINAL if chn == 0 else axcl.AX_VDEC_OUTPUT_SCALE,
            'img_format': img_format,
            'compress_info': compress_info
        }

        ret = axcl.vdec.set_chn_attr(grp, chn, chn_attr)

    .. note::

        - `frame_stride` should be aligned to 256.
        - Calculate `frame_buf_size` by :func:`get_buf_size`.
        - `output_fifo_depth` must be greater than 0.

        .. list-table::
           :header-rows: 1

           * - chn
             - crop
             - scaling down
             - scaling up
             - Max. Output
           * - 0
             - O
             - X
             - X
             - [8192x8192]
           * - 1
             - O
             - O
             - X
             - [4096x4096]
           * - 2
             - O
             - O
             - X
             - [1920x1080]
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_SetChnAttr.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_SetChnAttr.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN, POINTER(AX_VDEC_CHN_ATTR_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        c_chn_attr = AX_VDEC_CHN_ATTR_T()
        c_chn_attr.dict2struct(chn_attr)
        ret = libaxcl_vdec.AXCL_VDEC_SetChnAttr(c_grp, c_chn, byref(c_chn_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_chn_attr(grp: int, chn: int) -> tuple[dict, int]:
    """
    Get channel attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_GetChnAttr(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, AX_VDEC_CHN_ATTR_T *pstVdChnAttr);`
        **python**              `chn_attr, ret = axcl.vdec.get_chn_attr(grp, chn)`
        ======================= =====================================================

    :param int chn: Channel id.
    :returns: tuple[dict, int]

        - **chn_attr** (*dict*) - :class:`AX_VDEC_CHN_ATTR_T <axcl.vdec.axcl_vdec_type.AX_VDEC_CHN_ATTR_T>`.
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    chn_attr = {}
    try:
        libaxcl_vdec.AXCL_VDEC_GetChnAttr.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_GetChnAttr.argtypes = [AX_VDEC_GRP, AX_VDEC_CHN, POINTER(AX_VDEC_CHN_ATTR_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_chn = AX_VDEC_CHN(chn)
        c_chn_attr = AX_VDEC_CHN_ATTR_T()
        ret = libaxcl_vdec.AXCL_VDEC_GetChnAttr(c_grp, c_chn, byref(c_chn_attr))
        if ret == AXCL_SUCC:
            chn_attr = c_chn_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return chn_attr, ret


def jpeg_decode_one_frame(param: dict) -> int:
    """
    Decode one jpg to YUV frame.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_JpegDecodeOneFrame(AX_VDEC_DEC_ONE_FRM_T *pstParam);`
        **python**              `ret = axcl.vdec.jpeg_decode_one_frame(param)`
        ======================= =====================================================

    :param dict param: :class:`AX_VDEC_DEC_ONE_FRM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_DEC_ONE_FRM_T>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_vdec.AXCL_VDEC_JpegDecodeOneFrame.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_JpegDecodeOneFrame.argtypes = [POINTER(AX_VDEC_DEC_ONE_FRM_T)]
        c_param = AX_VDEC_DEC_ONE_FRM_T()
        c_param.dict2struct(param)
        ret = libaxcl_vdec.AXCL_VDEC_JpegDecodeOneFrame(byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_vui_param(grp: int) -> tuple[dict, int]:
    """
    Get VUI parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VDEC_GetVuiParam(AX_VDEC_GRP VdGrp, AX_VDEC_VUI_PARAM_T *pstVuiParam);`
        **python**              `vui_param, ret = axcl.vdec.get_vui_param(grp)`
        ======================= =====================================================

    :param int grp: Group id.
    :returns: tuple[dict, int]

        - **vui_param** (*dict*) - :class:`AX_VDEC_VUI_PARAM_T <axcl.vdec.axcl_vdec_type.AX_VDEC_VUI_PARAM_T>`.
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    vui_param = {}
    try:
        libaxcl_vdec.AXCL_VDEC_GetVuiParam.restype = AX_S32
        libaxcl_vdec.AXCL_VDEC_GetVuiParam.argtypes = [AX_VDEC_GRP, POINTER(AX_VDEC_VUI_PARAM_T)]
        c_grp = AX_VDEC_GRP(grp)
        c_vui_param = AX_VDEC_VUI_PARAM_T()
        ret = libaxcl_vdec.AXCL_VDEC_GetVuiParam(c_grp, byref(c_vui_param))
        if ret == AXCL_SUCC:
            vui_param = c_vui_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return vui_param, ret
