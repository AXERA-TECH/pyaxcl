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

from axcl.lib.axcl_lib import libaxcl_venc
from axcl.venc.axcl_venc_comm import *
from axcl.ax_global_type import *
from axcl.utils.axcl_logger import *


def init(mod_attr: dict) -> int:
    """
    Initialize encoder module.
    This api should be called at first before any APIs of encoder.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_Init(const AX_VENC_MOD_ATTR_T *pstModAttr);`
        **python**              `ret = axcl.venc.init(mod_attr)`
        ======================= =====================================================

    :param dict mod_attr: :class:`AX_VENC_MOD_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_MOD_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        mod_attr = {
            "venc_type" : axcl.AX_VENC_MULTI_ENCODER,
            "mod_thd_attr": {
                "explicit_sched": False,
                "sched_policy": axcl.AX_VENC_SCHED_OTHER,
                "sched_priority": 0,
                "total_thread_num": 2
            }
        }
        ret = axcl.venc.init(mode_attr)
    """
    ret = -1
    c_mode_attr = AX_VENC_MOD_ATTR_T()
    try:
        if mod_attr:
            c_mode_attr.dict2struct(mod_attr)

        libaxcl_venc.AXCL_VENC_Init.restype = AX_S32
        libaxcl_venc.AXCL_VENC_Init.argtypes = [POINTER(AX_VENC_MOD_ATTR_T)]
        ret = libaxcl_venc.AXCL_VENC_Init(byref(c_mode_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def deinit() -> int:
    """
    De-initialize encoder module.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_Deinit();`
        **python**              `ret = axcl.venc.deinit()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_Deinit.restype = AX_S32
        libaxcl_venc.AXCL_VENC_Deinit.argtypes = None
        ret = libaxcl_venc.AXCL_VENC_Deinit()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_default_codec_attribute(attr: dict):
    if attr["type"] == PT_H264:
        if "attr_h264e" not in attr:
            attr["attr_h264e"] = {"rcn_ref_share_buf": 0}
    elif attr["type"] == PT_H265:
        if "attr_h265e" not in attr:
            attr["attr_h265e"] = {"rcn_ref_share_buf": 0}
    elif attr["type"] == PT_MJPEG:
        if "attr_mjpege" not in attr:
            attr["attr_mjpege"] = {}
    elif attr["type"] == PT_JPEG:
        if "attr_jpege" not in attr:
            attr["attr_jpege"] = {}


def check_rc_attr_dict(rc: dict):
    rc_mode_keys = {
        AX_VENC_RC_MODE_H264CBR: 'h264_cbr_rc_attr',
        AX_VENC_RC_MODE_H264VBR: 'h264_vbr_rc_attr',
        AX_VENC_RC_MODE_H264AVBR: 'h264_avbr_rc_attr',
        AX_VENC_RC_MODE_H264QVBR: 'h264_qvbr_rc_attr',
        AX_VENC_RC_MODE_H264CVBR: 'h264_cvbr_rc_attr',
        AX_VENC_RC_MODE_H264FIXQP: 'h264_fix_qp_rc_attr',
        AX_VENC_RC_MODE_H264QPMAP: 'h264_qp_map_rc_attr',
        AX_VENC_RC_MODE_MJPEGCBR: 'mjpeg_cbr_rc_attr',
        AX_VENC_RC_MODE_MJPEGVBR: 'mjpeg_vbr_rc_attr',
        AX_VENC_RC_MODE_MJPEGFIXQP: 'mjpeg_fix_qp_rc_attr',
        AX_VENC_RC_MODE_H265CBR: 'h265_cbr_rc_attr',
        AX_VENC_RC_MODE_H265VBR: 'h265_vbr_rc_attr',
        AX_VENC_RC_MODE_H265AVBR: 'h265_avbr_rc_attr',
        AX_VENC_RC_MODE_H265QVBR: 'h265_qvbr_rc_attr',
        AX_VENC_RC_MODE_H265CVBR: 'h265_cvbr_rc_attr',
        AX_VENC_RC_MODE_H265FIXQP: 'h265_fix_qp_rc_attr',
        AX_VENC_RC_MODE_H265QPMAP: 'h265_qp_map_rc_attr'
    }

    for mode, key in rc_mode_keys.items():
        if rc["rc_mode"] == mode:
            if key not in rc:
                raise KeyError(f"missing {key} in dict['rc_attr'] when dict['rc_attr']['rc_mode'] == {mode}")


def set_default_gop_attribute(attr: dict):
    if attr["gop_mode"] == AX_VENC_GOPMODE_NORMALP:
        if "normal_p" not in attr:
            attr["normal_p"] = {"pic_config": {"qp_offset": 0, "qp_factor": 0}}

    elif attr["gop_mode"] == AX_VENC_GOPMODE_ONELTR:
        if "one_ltr" not in attr:
            attr["one_ltr"] = {"pic_config": {"qp_offset": 0, "qp_factor": 0},
                               "pic_special_config": {"qp_offset": 0, "qp_factor": 0, "interval": 0}}
    elif attr["gop_mode"] == AX_VENC_GOPMODE_SVC_T:
        if "svc_t" not in attr:
            attr["svc_t"] = {"svc_t_cfg": 0, "gop_size": 0}


def create_chn(chn: int, attr: dict) -> int:
    """
    Create the specified channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_CreateChn(VENC_CHN VeChn, const AX_VENC_CHN_ATTR_T *pstAttr);`
        **python**              `ret = axcl.venc.create_chn(chn, attr)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict attr: :class:`AX_VENC_CHN_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_CHN_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    .. seealso::

        :func:`create_chn_ex <axcl.venc.axcl_venc.create_chn_ex>`
    """

    ret = -1
    c_attr = AX_VENC_CHN_ATTR_T()
    try:
        libaxcl_venc.AXCL_VENC_CreateChn.restype = AX_S32
        libaxcl_venc.AXCL_VENC_CreateChn.argtypes = [VENC_CHN, POINTER(AX_VENC_CHN_ATTR_T)]

        c_chn = VENC_CHN(chn)

        check_rc_attr_dict(attr["rc_attr"])
        set_default_codec_attribute(attr["venc_attr"])
        set_default_gop_attribute(attr["gop_attr"])
        c_attr.dict2struct(attr)

        ret = libaxcl_venc.AXCL_VENC_CreateChn(c_chn, byref(c_attr))

    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def create_chn_ex(attr: int) -> tuple[int, int]:
    """
    Create a new channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_CreateChnEx(VENC_CHN *pVeChn, const AX_VENC_CHN_ATTR_T *pstAttr);`
        **python**              `chn, ret = axcl.venc.create_chn_ex(attr)`
        ======================= =====================================================

    :param dict attr: :class:`AX_VENC_CHN_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_CHN_ATTR_T>`
    :returns: tuple[int, int]

        - **chn** (*int*) - Channel id
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    **Example**

    .. code-block:: python

        codec = 'h264'
        attr = {
            'venc_attr': {
                'link_mode': axcl.AX_VENC_UNLINK_MODE,
                'type': axcl.PT_H264 if codec == 'h264' else axcl.PT_H265,
                'pic_width_src': width,
                'pic_height_src': height,
                'profile': axcl.AX_VENC_H264_MAIN_PROFILE if codec == 'h264' else axcl.AX_VENC_HEVC_MAIN_PROFILE,
                'level': axcl.AX_VENC_H264_LEVEL_5_1 if codec == 'h264' else axcl.AX_VENC_HEVC_LEVEL_5_1,
                'tier': axcl.AX_VENC_HEVC_MAIN_TIER,
                'in_fifo_depth': 4,
                'out_fifo_depth': 4,
                'flag': 0,
                'attr_h264e': {
                    'rcn_ref_share_buf': 0
                },
                'attr_h265e': {
                    'rcn_ref_share_buf': 0
                }
            },
            'rc_attr': {
                'rc_mode': axcl.AX_VENC_RC_MODE_H264CBR if codec == 'h264' else axcl.AX_VENC_RC_MODE_H265CBR,
                'first_frame_start_qp': -1,
                'frame_rate': {
                    'src_frame_rate': fps,
                    'dst_frame_rate': fps
                },
                'h264_cbr_rc_attr': {
                    'gop': fps * 2,
                    'stat_time': 0,
                    'bitrate': 4096,
                    'max_qp': 51,
                    'min_qp': 10,
                    'max_iqp': 51,
                    'min_iqp': 10,
                    'max_iprop': 40,
                    'min_iprop': 10,
                    'intra_qp_delta': -2,
                    'idr_qp_delta_range': 0
                },
                'h265_cbr_rc_attr': {
                    'gop': fps * 2,
                    'stat_time': 0,
                    'bitrate': 4096,
                    'max_qp': 51,
                    'min_qp': 10,
                    'max_iqp': 51,
                    'min_iqp': 10,
                    'max_iprop': 40,
                    'min_iprop': 10,
                    'intra_qp_delta': -2,
                    'idr_qp_delta_range': 0
                }
            },
            'gop_attr': {
                'gop_mode': axcl.AX_VENC_GOPMODE_NORMALP
            }
        }
        chn, ret = axcl.venc.create_chn_ex(attr)
    """
    ret = -1
    c_attr = AX_VENC_CHN_ATTR_T()
    c_chn = VENC_CHN(-1)
    try:
        libaxcl_venc.AXCL_VENC_CreateChnEx.restype = AX_S32
        libaxcl_venc.AXCL_VENC_CreateChnEx.argtypes = [POINTER(VENC_CHN), POINTER(AX_VENC_CHN_ATTR_T)]

        check_rc_attr_dict(attr["rc_attr"])
        set_default_codec_attribute(attr["venc_attr"])
        set_default_gop_attribute(attr["gop_attr"])
        c_attr.dict2struct(attr)

        ret = libaxcl_venc.AXCL_VENC_CreateChnEx(byref(c_chn), byref(c_attr))

    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_chn.value, ret


def destroy_chn(chn: int) -> int:
    """
    Destroy channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_DestroyChn(VENC_CHN VeChn);`
        **python**              `ret = axcl.venc.destroy_chn(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_DestroyChn.restype = AX_S32
        libaxcl_venc.AXCL_VENC_DestroyChn.argtypes = [VENC_CHN]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_DestroyChn(c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def send_frame(chn: int, frame: dict, millisec: int) -> int:
    """
    Send a frame to encoder to encode.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SendFrame(VENC_CHN VeChn, const AX_VIDEO_FRAME_INFO_T *pstFrame, AX_S32 s32MilliSec);`
        **python**              `ret = axcl.venc.send_frame(chn, frame, millisec)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict frame: :class:`AX_VIDEO_FRAME_INFO_T <axcl.ax_global_type.AX_VIDEO_FRAME_INFO_T>`
    :param int millisec: Timeout in milliseconds
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        frame = {
            'video_frame': {
                'width': width, 'height': height, 'img_format': axcl.AX_FORMAT_YUV420_SEMIPLANAR,
                'compress_info': {'compress_mode': axcl.AX_COMPRESS_MODE_NONE, 'compress_level': 0},
                'pic_stride': [width, width, 0], 'phy_addr': [phy_addr, 0, 0], 'vir_addr': [0, 0, 0],
                'blk_id': [blk_id, 0, 0], 'seq_num': seq_num, 'frame_size': size
            },
            'mod_id': axcl.AX_ID_VENC,
            'is_end_of_stream': False
        }

        ret = axcl.venc.send_frame(chn, frame, -1)
    """
    ret = -1
    c_frame = AX_VIDEO_FRAME_INFO_T()
    try:
        libaxcl_venc.AXCL_VENC_SendFrame.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SendFrame.argtypes = [VENC_CHN, POINTER(AX_VIDEO_FRAME_INFO_T), AX_S32]
        c_chn = VENC_CHN(chn)
        c_millisec = AX_S32(millisec)
        c_frame.dict2struct(frame)
        ret = libaxcl_venc.AXCL_VENC_SendFrame(c_chn, byref(c_frame), c_millisec)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def send_frame_ex(chn: int, frame: dict, millisec: int) -> int:
    """
    Send a frame to encoder to encode.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SendFrameEx(VENC_CHN VeChn, const AX_USER_FRAME_INFO_T *pstFrame, AX_S32 s32MilliSec);`
        **python**              `ret = axcl.venc.send_frame_ex(chn, frame, millisec)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict frame: :class:`AX_USER_FRAME_INFO_T <axcl.venc.axcl_venc_comm.AX_USER_FRAME_INFO_T>`
    :param int millisec: Timeout in milliseconds
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_frame = AX_USER_FRAME_INFO_T()
    try:
        libaxcl_venc.AXCL_VENC_SendFrameEx.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SendFrameEx.argtypes = [VENC_CHN, POINTER(AX_USER_FRAME_INFO_T), AX_S32]
        c_chn = VENC_CHN(chn)
        c_millisec = AX_S32(millisec)
        c_frame.dict2struct(frame)
        ret = libaxcl_venc.AXCL_VENC_SendFrameEx(c_chn, byref(c_frame), c_millisec)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def select_grp(grp_id: int, millisec: int) -> tuple[dict, int]:
    """
    Select to traverse the specified group to query check if encoding is complete.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SelectGrp(VENC_GRP grpId, AX_CHN_STREAM_STATUS_T *pstChnStrmState, AX_S32 s32MilliSec);`
        **python**              `strm_state, ret = axcl.venc.select_grp(grp_id, millisec)`
        ======================= =====================================================

    :param int grp_id: Group id to select.
    :param int millisec: Timeout in milliseconds
    :returns: tuple(dict, int)

        - **strm_state** (*dict*) - :class:`AX_CHN_STREAM_STATUS_T <axcl.venc.axcl_venc_comm.AX_CHN_STREAM_STATUS_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_strm_state = AX_CHN_STREAM_STATUS_T()
    strm_state = {}
    try:
        libaxcl_venc.AXCL_VENC_SelectGrp.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SelectGrp.argtypes = [VENC_CHN, POINTER(AX_CHN_STREAM_STATUS_T), AX_S32]
        c_grp_id = VENC_GRP(grp_id)
        c_millisec = AX_S32(millisec)
        ret = libaxcl_venc.AXCL_VENC_SelectGrp(c_grp_id, byref(c_strm_state), c_millisec)
        if ret == AX_SUCCESS:
            strm_state = c_strm_state.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return strm_state, ret


def select_clear_grp(grp_id: int) -> int:
    """
    Clear the specified group parameter.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SelectClearGrp(VENC_GRP grpId);`
        **python**              `ret = axcl.venc.select_clear_grp(grp_id)`
        ======================= =====================================================

    :param int grp_id: Group id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_SelectClearGrp.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SelectClearGrp.argtypes = [VENC_GRP]
        c_grp_id = VENC_GRP(grp_id)
        ret = libaxcl_venc.AXCL_VENC_SelectClearGrp(c_grp_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def select_grp_add_chn(grp_id: int, chn: int) -> int:
    """
    Add the specified channel to selected group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SelectGrpAddChn(VENC_GRP grpId, VENC_CHN VeChn);`
        **python**              `ret = axcl.venc.select_grp_add_chn(grp_id, chn)`
        ======================= =====================================================

    :param int grp_id: Group id
    :param int chn: Channel id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_SelectGrpAddChn.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SelectGrpAddChn.argtypes = [VENC_GRP, VENC_CHN]
        c_grp_id = VENC_GRP(grp_id)
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_SelectGrpAddChn(c_grp_id, c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def select_grp_delete_chn(grp_id: int, chn: int) -> int:
    """
    Delete the specified channel from selected group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SelectGrpDeleteChn(VENC_GRP grpId, VENC_CHN VeChn);`
        **python**              `ret = axcl.venc.select_grp_delete_chn(grp_id, chn)`
        ======================= =====================================================

    :param int grp_id: Group id
    :param int chn: Channel id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_SelectGrpDeleteChn.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SelectGrpDeleteChn.argtypes = [VENC_GRP, VENC_CHN]
        c_grp_id = VENC_GRP(grp_id)
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_SelectGrpDeleteChn(c_grp_id, c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def select_grp_query(grp_id: int) -> tuple[dict, int]:
    """
    Query the specified selected group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SelectGrpQuery(VENC_GRP grpId, AX_VENC_SELECT_GRP_PARAM_T *pstGrpInfo);`
        **python**              `param, ret = axcl.venc.select_grp_query(grp_id)`
        ======================= =====================================================

    :param int grp_id: Group id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_SELECT_GRP_PARAM_T <axcl.venc.axcl_venc_type.AX_VENC_SELECT_GRP_PARAM_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_SELECT_GRP_PARAM_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_SelectGrpQuery.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SelectGrpQuery.argtypes = [VENC_GRP, POINTER(AX_VENC_SELECT_GRP_PARAM_T)]
        c_grp_id = VENC_GRP(grp_id)
        ret = libaxcl_venc.AXCL_VENC_SelectGrpQuery(c_grp_id, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def get_stream(chn: int, millisec: int) -> tuple[dict, int]:
    """
    Get encoded stream of specified channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetStream(VENC_CHN VeChn, AX_VENC_STREAM_T *pstStream, AX_S32 s32MilliSec);`
        **python**              `stream, ret = axcl.venc.get_stream(chn, millisec)`
        ======================= =====================================================

    :param int chn: Channel id
    :param int millisec: Timeout in milliseconds
    :returns: tuple[dict, int]

        - **stream** (*dict*) - :class:`AX_VENC_STREAM_T <axcl.venc.axcl_venc_type.AX_VENC_STREAM_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    **Example**

    .. code-block:: python

        import ctypes

        stream, ret = axcl.venc.get_stream(chn, -1)
        if ret == 0:
            pack = stream['pack']
            size = pack['len']

            # copy stream data from device to host
            buffer = ctypes.create_string_buffer(size)
            axcl.rt.memcpy(ctypes.addressof(buffer), pack['phy_addr'], size, axcl.AXCL_MEMCPY_DEVICE_TO_HOST)

            # release stream
            axcl.venc.release_stream(chn, stream)

    """
    ret = -1
    c_stream = AX_VENC_STREAM_T()
    stream = {}
    try:
        libaxcl_venc.AXCL_VENC_GetStream.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetStream.argtypes = [VENC_CHN, POINTER(AX_VENC_STREAM_T), AX_S32]
        c_chn = VENC_CHN(chn)
        c_millisec = AX_S32(millisec)
        ret = libaxcl_venc.AXCL_VENC_GetStream(c_chn, byref(c_stream), c_millisec)
        if ret == AX_SUCCESS:
            ax_venc_stream_to_dict(c_stream, stream)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return stream, ret


def release_stream(chn: int, stream: dict) -> int:
    """
    Release encoded stream which got from :func:`get_stream <axcl.venc.axcl_venc.get_stream>`.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_ReleaseStream(VENC_CHN VeChn, const AX_VENC_STREAM_T *pstStream);`
        **python**              `ret = axcl.venc.release_stream(chn, stream)`
        ======================= =====================================================

    :param int chn: chn, Channel id
    :param dict stream: :class:`AX_VENC_STREAM_T <axcl.venc.axcl_venc_type.AX_VENC_STREAM_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_stream = AX_VENC_STREAM_T()
    try:
        libaxcl_venc.AXCL_VENC_ReleaseStream.restype = AX_S32
        libaxcl_venc.AXCL_VENC_ReleaseStream.argtypes = [VENC_CHN, POINTER(AX_VENC_STREAM_T)]
        c_chn = VENC_CHN(chn)
        dict_to_ax_venc_stream(stream, c_stream)
        ret = libaxcl_venc.AXCL_VENC_ReleaseStream(c_chn, byref(c_stream))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_stream_buf_info(chn: int) -> tuple[dict, int]:
    """
    get stream buf info

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetStreamBufInfo(VENC_CHN VeChn, AX_VENC_STREAM_BUF_INFO_T *pstStreamBufInfo);`
        **python**              `stream_buf_info, ret = axcl.venc.get_stream_buf_info(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **stream_buf_info** (*dict*) - :class:`AX_VENC_STREAM_BUF_INFO_T <axcl.venc.axcl_venc_type.AX_VENC_STREAM_BUF_INFO_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_stream_buf_info = AX_VENC_STREAM_BUF_INFO_T()
    stream_buf_info = {}
    try:
        libaxcl_venc.AXCL_VENC_GetStreamBufInfo.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetStreamBufInfo.argtypes = [VENC_CHN, POINTER(AX_VENC_STREAM_BUF_INFO_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetStreamBufInfo(c_chn, byref(c_stream_buf_info))
        if ret == AX_SUCCESS:
            stream_buf_info = c_stream_buf_info.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return stream_buf_info, ret


def start_recv_frame(chn: int, recv_param: dict) -> int:
    """
    start to encode.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_StartRecvFrame(VENC_CHN VeChn, const AX_VENC_RECV_PIC_PARAM_T *pstRecvParam);`
        **python**              `ret = axcl.venc.start_recv_frame(chn, recv_param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict recv_param: :class:`AX_VENC_RECV_PIC_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_RECV_PIC_PARAM_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    **Example**

    .. code-block:: python

        recv_param = {'recv_pic_num': -1}
        ret = axcl.venc.start_recv_frame(chn, recv_param)
    """
    ret = -1
    c_recv_param = AX_VENC_RECV_PIC_PARAM_T()
    try:
        libaxcl_venc.AXCL_VENC_StartRecvFrame.restype = AX_S32
        libaxcl_venc.AXCL_VENC_StartRecvFrame.argtypes = [VENC_CHN, POINTER(AX_VENC_RECV_PIC_PARAM_T)]
        c_chn = VENC_CHN(chn)
        c_recv_param.dict2struct(recv_param)
        ret = libaxcl_venc.AXCL_VENC_StartRecvFrame(c_chn, byref(c_recv_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def stop_recv_frame(chn: int) -> int:
    """
    stop encoding.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_StopRecvFrame(VENC_CHN VeChn);`
        **python**              `ret = axcl.venc.stop_recv_frame(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_StopRecvFrame.restype = AX_S32
        libaxcl_venc.AXCL_VENC_StopRecvFrame.argtypes = [VENC_CHN]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_StopRecvFrame(c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def reset_chn(chn: int) -> int:
    """
    Reset the specified channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_ResetChn(VENC_CHN VeChn);`
        **python**              `ret = axcl.venc.reset_chn(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_ResetChn.restype = AX_S32
        libaxcl_venc.AXCL_VENC_ResetChn.argtypes = [VENC_CHN]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_ResetChn(c_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_roi_attr(chn: int, roi_attr: dict) -> int:
    """
    Set ROI attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetRoiAttr(VENC_CHN VeChn, const AX_VENC_ROI_ATTR_T *pstRoiAttr);`
        **python**              `ret = axcl.venc.set_roi_attr(chn, roi_attr)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict roi_attr: :class:`AX_VENC_ROI_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_ROI_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_roi_attr = AX_VENC_ROI_ATTR_T()
    try:
        libaxcl_venc.AXCL_VENC_SetRoiAttr.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetRoiAttr.argtypes = [VENC_CHN, POINTER(AX_VENC_ROI_ATTR_T)]
        c_chn = VENC_CHN(chn)
        c_roi_attr.dict2struct(roi_attr)
        ret = libaxcl_venc.AXCL_VENC_SetRoiAttr(c_chn, byref(c_roi_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_roi_attr(chn: int, index: int) -> tuple[dict, int]:
    """
    Get the ROI attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetRoiAttr(VENC_CHN VeChn, AX_U32 u32Index, AX_VENC_ROI_ATTR_T *pstRoiAttr);`
        **python**              `roi_attr, ret = axcl.venc.get_roi_attr(chn, index)`
        ======================= =====================================================

    :param int chn: Channel id
    :param int index: Index of ROI, range [0, 7]
    :returns: tuple[dict, int]

        - **roi_attr** (*dict*) - :class:`AX_VENC_ROI_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_ROI_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_roi_attr = AX_VENC_ROI_ATTR_T()
    roi_attr = {}
    try:
        libaxcl_venc.AXCL_VENC_GetRoiAttr.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetRoiAttr.argtypes = [VENC_CHN, AX_U32, POINTER(AX_VENC_ROI_ATTR_T)]
        c_chn = VENC_CHN(chn)
        c_index = AX_U32(index)
        ret = libaxcl_venc.AXCL_VENC_GetRoiAttr(c_chn, c_index, byref(c_roi_attr))
        if ret == AX_SUCCESS:
            roi_attr = c_roi_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return roi_attr, ret


def set_rc_param(chn: int, param: dict) -> int:
    """
    Set RC(bitrate control) parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetRcParam(VENC_CHN VeChn, const AX_VENC_RC_PARAM_T *pstRcParam);`
        **python**              `ret = axcl.venc.set_rc_param(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_RC_PARAM_T <axcl.venc.axcl_venc_rc.AX_VENC_RC_PARAM_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_RC_PARAM_T()
    try:
        libaxcl_venc.AXCL_VENC_SetRcParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetRcParam.argtypes = [VENC_CHN, POINTER(AX_VENC_RC_PARAM_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetRcParam(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_rc_param(chn: int) -> tuple[dict, int]:
    """
    Get the RC parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetRcParam(VENC_CHN VeChn, AX_VENC_RC_PARAM_T *pstRcParam);`
        **python**              `param, ret = axcl.venc.get_rc_param(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_RC_PARAM_T <axcl.venc.axcl_venc_rc.AX_VENC_RC_PARAM_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_RC_PARAM_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetRcParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetRcParam.argtypes = [VENC_CHN, POINTER(AX_VENC_RC_PARAM_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetRcParam(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def set_mod_param(venc_type: int, param: dict) -> int:
    """
    Set module parameters such as HW clock frequency.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetModParam(AX_VENC_ENCODER_TYPE_E enVencType, const AX_VENC_MOD_PARAM_T *pstModParam);`
        **python**              `ret = axcl.venc.set_mod_param(venc_type, param)`
        ======================= =====================================================

    :param int venc_type: :class:`AX_VENC_ENCODER_TYPE_E <axcl.venc.axcl_venc_comm.AX_VENC_ENCODER_TYPE_E>`
    :param dict param: :class:`AX_VENC_MOD_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_MOD_PARAM_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_MOD_PARAM_T()
    try:
        libaxcl_venc.AXCL_VENC_SetModParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetModParam.argtypes = [AX_VENC_ENCODER_TYPE_E, POINTER(AX_VENC_MOD_PARAM_T)]
        c_venc_type = AX_VENC_ENCODER_TYPE_E(venc_type)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetModParam(c_venc_type, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_mod_param(venc_type: int) -> tuple[dict, int]:
    """
    Get module parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetModParam(AX_VENC_ENCODER_TYPE_E enVencType, AX_VENC_MOD_PARAM_T *pstModParam);`
        **python**              `param, ret = axcl.venc.get_mod_param(venc_type)`
        ======================= =====================================================

    :param int venc_type: :class:`AX_VENC_ENCODER_TYPE_E <axcl.venc.axcl_venc_comm.AX_VENC_ENCODER_TYPE_E>`
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_MOD_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_MOD_PARAM_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_MOD_PARAM_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetModParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetModParam.argtypes = [AX_VENC_ENCODER_TYPE_E, POINTER(AX_VENC_MOD_PARAM_T)]
        c_venc_type = AX_VENC_ENCODER_TYPE_E(venc_type)
        ret = libaxcl_venc.AXCL_VENC_GetModParam(c_venc_type, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def set_vui_param(chn: int, param: dict) -> int:
    """
    Set VUI parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetVuiParam(VENC_CHN VeChn, const AX_VENC_VUI_PARAM_T *pstVuiParam);`
        **python**              `ret = axcl.venc.set_vui_param(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_VUI_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_VUI_PARAM_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_VUI_PARAM_T()
    try:
        libaxcl_venc.AXCL_VENC_SetVuiParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetVuiParam.argtypes = [VENC_CHN, POINTER(AX_VENC_VUI_PARAM_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetVuiParam(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_vui_param(chn: int) -> tuple[dict, int]:
    """
    Get VUI parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetVuiParam(VENC_CHN VeChn, AX_VENC_VUI_PARAM_T *pstVuiParam);`
        **python**              `param, ret = axcl.venc.get_vui_param(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_VUI_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_VUI_PARAM_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_VUI_PARAM_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetVuiParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetVuiParam.argtypes = [VENC_CHN, POINTER(AX_VENC_VUI_PARAM_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetVuiParam(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def set_chn_attr(chn: int, attr: dict) -> int:
    """
    set channel attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetChnAttr(VENC_CHN VeChn, const AX_VENC_CHN_ATTR_T *pstChnAttr);`
        **python**              `ret = axcl.venc.set_chn_attr(chn, attr)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict attr: :class:`AX_VENC_CHN_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_CHN_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    .. seealso::

        :func:`create_chn_ex <axcl.venc.axcl_venc.create_chn_ex>`

    """
    ret = -1
    c_attr = AX_VENC_CHN_ATTR_T()
    try:
        libaxcl_venc.AXCL_VENC_SetChnAttr.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetChnAttr.argtypes = [VENC_CHN, POINTER(AX_VENC_CHN_ATTR_T)]
        c_chn = VENC_CHN(chn)
        check_rc_attr_dict(attr["rc_attr"])
        set_default_codec_attribute(attr["venc_attr"])
        set_default_gop_attribute(attr["gop_attr"])
        c_attr.dict2struct(attr)
        ret = libaxcl_venc.AXCL_VENC_SetChnAttr(c_chn, byref(c_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_chn_attr(chn: int) -> tuple[dict, int]:
    """
    Get channel attribute.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetChnAttr(VENC_CHN VeChn, AX_VENC_CHN_ATTR_T *pstChnAttr);`
        **python**              `attr, ret = axcl.venc.get_chn_attr(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **attr** (*dict*) - :class:`AX_VENC_CHN_ATTR_T <axcl.venc.axcl_venc_comm.AX_VENC_CHN_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_attr = AX_VENC_CHN_ATTR_T()
    attr = {}
    try:
        libaxcl_venc.AXCL_VENC_GetChnAttr.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetChnAttr.argtypes = [VENC_CHN, POINTER(AX_VENC_CHN_ATTR_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetChnAttr(c_chn, byref(c_attr))
        if ret == AX_SUCCESS:
            attr = c_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return attr, ret


def set_rate_jam_strategy(chn: int, param: dict) -> int:
    """
    Set the strategy when bitrate exceeds limitation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetRateJamStrategy(VENC_CHN VeChn, const AX_VENC_RATE_JAM_CFG_T *pstRateJamParam);`
        **python**              `ret = axcl.venc.set_rate_jam_strategy(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_RATE_JAM_CFG_T <axcl.venc.axcl_venc_rc.AX_VENC_RATE_JAM_CFG_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_RATE_JAM_CFG_T()
    try:
        libaxcl_venc.AXCL_VENC_SetRateJamStrategy.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetRateJamStrategy.argtypes = [VENC_CHN, POINTER(AX_VENC_RATE_JAM_CFG_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetRateJamStrategy(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_rate_jam_strategy(chn: int) -> tuple[dict, int]:
    """
    Get the strategy when bitrate exceeds limitation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetRateJamStrategy(VENC_CHN VeChn, AX_VENC_RATE_JAM_CFG_T *pstRateJamParam);`
        **python**              `param, ret = axcl.venc.get_rate_jam_strategy(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_RATE_JAM_CFG_T <axcl.venc.axcl_venc_rc.AX_VENC_RATE_JAM_CFG_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_RATE_JAM_CFG_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetRateJamStrategy.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetRateJamStrategy.argtypes = [VENC_CHN, POINTER(AX_VENC_RATE_JAM_CFG_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetRateJamStrategy(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def set_supper_frame_strategy(chn: int, param: dict) -> int:
    """
    Set the strategy of super frame.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetSuperFrameStrategy(VENC_CHN VeChn, const AX_VENC_SUPERFRAME_CFG_T *pstSuperFrameCfg);`
        **python**              `ret = axcl.venc.set_supper_frame_strategy(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_SUPERFRAME_CFG_T <axcl.venc.axcl_venc_rc.AX_VENC_SUPERFRAME_CFG_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_SUPERFRAME_CFG_T()
    try:
        libaxcl_venc.AXCL_VENC_SetSuperFrameStrategy.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetSuperFrameStrategy.argtypes = [VENC_CHN, POINTER(AX_VENC_SUPERFRAME_CFG_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetSuperFrameStrategy(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_supper_frame_strategy(chn: int) -> tuple[dict, int]:
    """
    Get the strategy of super frame.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetSuperFrameStrategy(VENC_CHN VeChn, AX_VENC_SUPERFRAME_CFG_T *pstSuperFrameCfg);`
        **python**              `param, ret = axcl.venc.get_supper_frame_strategy(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_SUPERFRAME_CFG_T <axcl.venc.axcl_venc_rc.AX_VENC_SUPERFRAME_CFG_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_SUPERFRAME_CFG_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetSuperFrameStrategy.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetSuperFrameStrategy.argtypes = [VENC_CHN, POINTER(AX_VENC_SUPERFRAME_CFG_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetSuperFrameStrategy(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def set_intra_refresh(chn: int, param: dict) -> int:
    """
    Set GDR parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetIntraRefresh(VENC_CHN VeChn, const AX_VENC_INTRA_REFRESH_T *pstIntraRefresh);`
        **python**              `ret = axcl.venc.set_intra_refresh(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_INTRA_REFRESH_T <axcl.venc.axcl_venc_comm.AX_VENC_INTRA_REFRESH_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_INTRA_REFRESH_T()
    try:
        libaxcl_venc.AXCL_VENC_SetIntraRefresh.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetIntraRefresh.argtypes = [VENC_CHN, POINTER(AX_VENC_INTRA_REFRESH_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetIntraRefresh(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_intra_refresh(chn: int) -> tuple[dict, int]:
    """
    Get GDR parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetIntraRefresh(VENC_CHN VeChn, AX_VENC_INTRA_REFRESH_T *pstIntraRefresh);`
        **python**              `param, ret = axcl.venc.get_intra_refresh(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_INTRA_REFRESH_T <axcl.venc.axcl_venc_comm.AX_VENC_INTRA_REFRESH_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_INTRA_REFRESH_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetIntraRefresh.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetIntraRefresh.argtypes = [VENC_CHN, POINTER(AX_VENC_INTRA_REFRESH_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetIntraRefresh(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def set_usr_data(chn: int, param: dict) -> int:
    """
    Set user data.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetUsrData(VENC_CHN VeChn, const AX_VENC_USR_DATA_T *pstUsrData);`
        **python**              `ret = axcl.venc.set_usr_data(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_USR_DATA_T <axcl.venc.axcl_venc_comm.AX_VENC_USR_DATA_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_USR_DATA_T()
    try:
        libaxcl_venc.AXCL_VENC_SetUsrData.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetUsrData.argtypes = [VENC_CHN, POINTER(AX_VENC_USR_DATA_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetUsrData(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_usr_data(chn: int, usr_data: dict) -> tuple[dict, int]:
    """
    Get user data.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetUsrData(VENC_CHN VeChn, AX_VENC_USR_DATA_T *pstUsrData);`
        **python**              `output, ret = axcl.venc.get_usr_data(chn, usr_data)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict usr_data: :class:`AX_VENC_USR_DATA_T <axcl.venc.axcl_venc_comm.AX_VENC_USR_DATA_T>`
    :returns: tuple[dict, int]

        - **output** (*dict*) - :class:`AX_VENC_USR_DATA_T <axcl.venc.axcl_venc_comm.AX_VENC_USR_DATA_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_USR_DATA_T()
    output = {}
    try:
        libaxcl_venc.AXCL_VENC_GetUsrData.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetUsrData.argtypes = [VENC_CHN, POINTER(AX_VENC_USR_DATA_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(usr_data)
        ret = libaxcl_venc.AXCL_VENC_GetUsrData(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            output = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return output, ret


def set_slice_split(chn: int, param: dict) -> int:
    """
    Set slice splitting parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetSliceSplit(VENC_CHN VeChn, const AX_VENC_SLICE_SPLIT_T *pstSliceSplit);`
        **python**              `ret = axcl.venc.set_slice_split(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_SLICE_SPLIT_T <axcl.venc.axcl_venc_comm.AX_VENC_SLICE_SPLIT_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_SLICE_SPLIT_T()
    try:
        libaxcl_venc.AXCL_VENC_SetSliceSplit.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetSliceSplit.argtypes = [VENC_CHN, POINTER(AX_VENC_SLICE_SPLIT_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetSliceSplit(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_slice_split(chn: int) -> tuple[dict, int]:
    """
    Get slice splitting parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetSliceSplit(VENC_CHN VeChn, AX_VENC_SLICE_SPLIT_T *pstUsrData);`
        **python**              `param, ret = axcl.venc.get_slice_split(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_SLICE_SPLIT_T <axcl.venc.axcl_venc_comm.AX_VENC_SLICE_SPLIT_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_param = AX_VENC_SLICE_SPLIT_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetSliceSplit.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetSliceSplit.argtypes = [VENC_CHN, POINTER(AX_VENC_SLICE_SPLIT_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetSliceSplit(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def request_idr(chn: int, instant: int) -> int:
    """
    Request to encode an IDR frame.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_RequestIDR(VENC_CHN VeChn, AX_BOOL bInstant);`
        **python**              `ret = axcl.venc.request_idr(chn, instant)`
        ======================= =====================================================

    :param int chn: Channel id
    :param bool instant: True means request to encode IDR frame immediately.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_venc.AXCL_VENC_RequestIDR.restype = AX_S32
        libaxcl_venc.AXCL_VENC_RequestIDR.argtypes = [VENC_CHN, AX_BOOL]
        c_chn = VENC_CHN(chn)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_venc.AXCL_VENC_RequestIDR(c_chn, c_instant)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def query_status(chn: int) -> tuple[dict, int]:
    """
    Query the encoding status of specified channel.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_QueryStatus(VENC_CHN VeChn, AX_VENC_CHN_STATUS_T *pstStatus);`
        **python**              `status, ret = axcl.venc.query_status(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **status** (*dict*) - :class:`AX_VENC_CHN_STATUS_T <axcl.venc.axcl_venc_comm.AX_VENC_CHN_STATUS_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_status = AX_VENC_CHN_STATUS_T()
    status = {}
    try:
        libaxcl_venc.AXCL_VENC_QueryStatus.restype = AX_S32
        libaxcl_venc.AXCL_VENC_QueryStatus.argtypes = [VENC_CHN, POINTER(AX_VENC_CHN_STATUS_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_QueryStatus(c_chn, byref(c_status))
        if ret == AX_SUCCESS:
            status = c_status.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return status, ret


def set_jpeg_param(chn: int, param: dict) -> int:
    """
    Set jpeg encoding parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_SetJpegParam(VENC_CHN VeChn, const AX_VENC_JPEG_PARAM_T *pstJpegParam);`
        **python**              `ret = axcl.venc.set_jpeg_param(chn, param)`
        ======================= =====================================================

    :param int chn: Channel id
    :param dict param: :class:`AX_VENC_JPEG_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_JPEG_PARAM_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_JPEG_PARAM_T()
    try:
        libaxcl_venc.AXCL_VENC_SetJpegParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_SetJpegParam.argtypes = [VENC_CHN, POINTER(AX_VENC_JPEG_PARAM_T)]
        c_chn = VENC_CHN(chn)
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_SetJpegParam(c_chn, byref(c_param))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_jpeg_param(chn: int) -> tuple[dict, int]:
    """
    Get jpeg encoding parameters.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_GetJpegParam(VENC_CHN VeChn, AX_VENC_JPEG_PARAM_T *pstJpegParam);`
        **python**              `param, ret = axcl.venc.get_jpeg_param(chn)`
        ======================= =====================================================

    :param int chn: Channel id
    :returns: tuple[dict, int]

        - **param** (*dict*) - :class:`AX_VENC_JPEG_PARAM_T <axcl.venc.axcl_venc_comm.AX_VENC_JPEG_PARAM_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_VENC_JPEG_PARAM_T()
    param = {}
    try:
        libaxcl_venc.AXCL_VENC_GetJpegParam.restype = AX_S32
        libaxcl_venc.AXCL_VENC_GetJpegParam.argtypes = [VENC_CHN, POINTER(AX_VENC_JPEG_PARAM_T)]
        c_chn = VENC_CHN(chn)
        ret = libaxcl_venc.AXCL_VENC_GetJpegParam(c_chn, byref(c_param))
        if ret == AX_SUCCESS:
            param = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return param, ret


def jpeg_encode_one_frame(param: dict) -> tuple[dict, int]:
    """
    Encode one frame to jpeg picture.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_VENC_JpegEncodeOneFrame(AX_JPEG_ENCODE_ONCE_PARAMS_T *pstJpegParam);`
        **python**              `output, ret = axcl.venc.jpeg_encode_one_frame(param)`
        ======================= =====================================================

    :param dict param: :class:`AX_JPEG_ENCODE_ONCE_PARAMS_T <axcl.venc.axcl_venc_comm.AX_JPEG_ENCODE_ONCE_PARAMS_T>`
    :returns: tuple[dict, int]

        - **output** (*dict*) - :class:`AX_JPEG_ENCODE_ONCE_PARAMS_T <axcl.venc.axcl_venc_comm.AX_JPEG_ENCODE_ONCE_PARAMS_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_param = AX_JPEG_ENCODE_ONCE_PARAMS_T()
    output = {}
    try:
        libaxcl_venc.AXCL_VENC_JpegEncodeOneFrame.restype = AX_S32
        libaxcl_venc.AXCL_VENC_JpegEncodeOneFrame.argtypes = [POINTER(AX_JPEG_ENCODE_ONCE_PARAMS_T)]
        c_param.dict2struct(param)
        ret = libaxcl_venc.AXCL_VENC_JpegEncodeOneFrame(byref(c_param))
        if ret == AX_SUCCESS:
            output = c_param.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return output, ret
