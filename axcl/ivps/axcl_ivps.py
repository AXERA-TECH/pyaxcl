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

from axcl.lib.axcl_lib import libaxcl_ivps
from axcl.ivps.axcl_ivps_type import *
from axcl.utils.axcl_logger import *

def init() -> int:
    """
    init

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_Init(AX_VOID)`
        **python**              `ret = axcl.ivps.init()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_Init.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_Init.argtypes = None
        ret = libaxcl_ivps.AXCL_IVPS_Init()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def deinit() -> int:
    """
    deinit

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_Deinit(AX_VOID)`
        **python**              `ret = axcl.ivps.deinit()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_Deinit.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_Deinit.argtypes = None
        ret = libaxcl_ivps.AXCL_IVPS_Deinit()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def create_grp(ivps_grp: int, grp_attr: int) -> int:
    """
    create ivps group

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CreateGrp(IVPS_GRP IvpsGrp, const AX_IVPS_GRP_ATTR_T *ptGrpAttr)`
        **python**              `ret = axcl.ivps.create_grp(ivps_grp, grp_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group, Value range: [0, :ref:`AX_IVPS_MAX_GRP_NUM <target to ax_ivps_max_grp_num>`)
    :param int grp_attr: group attr
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_grp_attr = AX_IVPS_GRP_ATTR_T()
        c_grp_attr.dict2struct(grp_attr)

        libaxcl_ivps.AXCL_IVPS_CreateGrp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CreateGrp.argtypes = [c_int32, POINTER(AX_IVPS_GRP_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_CreateGrp(c_int32(ivps_grp), byref(c_grp_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def create_grp_ex(grp_attr: dict) -> tuple[int, int]:
    """
    create group ex, must be executed after axcl.ivps.init, and can be executed concurrently with AX_IVPS_CreateGrp.
    It supports multi-process, and the Group ID is different among different processes.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CreateGrpEx(IVPS_GRP *IvpsGrp, const AX_IVPS_GRP_ATTR_T *ptGrpAttr)`
        **python**              `ivps_grp, ret = create_grp_ex(grp_attr)`
        ======================= =====================================================

    :param dict grp_attr: group attr, see :class:`AX_IVPS_GRP_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_GRP_ATTR_T>`
    :returns: tuple[int, int]

        - **ivps_grp** (*int*) - ivps group, Value range: [0, :class:`AX_IVPS_MAX_GRP_NUM <axcl.ivps.axcl_ivps_type.AX_IVPS_MAX_GRP_NUM>`)
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    c_ivps_grp = IVPS_GRP(0)
    try:
        c_grp_attr = AX_IVPS_GRP_ATTR_T()
        c_grp_attr.dict2struct(grp_attr)

        libaxcl_ivps.AXCL_IVPS_CreateGrpEx.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CreateGrpEx.argtypes = [POINTER(c_int32), POINTER(AX_IVPS_GRP_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_CreateGrpEx(byref(c_ivps_grp), byref(c_grp_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_ivps_grp.value, ret

def destroy_grp(ivps_grp: int) -> int:
    """
    destroy group

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DestoryGrp(IVPS_GRP IvpsGrp)`
        **python**              `ret = axcl.ivps.destroy_grp(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_DestoryGrp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DestoryGrp.argtypes = [c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_DestoryGrp(c_int32(ivps_grp))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def set_pipeline_attr(ivps_grp: int, pipeline_attr: dict) -> int:
    """
    set pipeline attr, must be executed after axcl.ivps.create_grp/axcl.ivps.create_grp_ex.
    axcl.ivps.disable_chn and axcl.ivps.enable_chn must be executed for the attributes to take effect.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetPipelineAttr(IVPS_GRP IvpsGrp, AX_IVPS_PIPELINE_ATTR_T *ptPipelineAttr)`
        **python**              `ret = axcl.ivps.set_pipeline_attr(ivps_grp, pipeline_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param dict pipeline_attr: pipeline attr, see :class:`AX_IVPS_PIPELINE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_PIPELINE_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_pipeline_attr = AX_IVPS_PIPELINE_ATTR_T()
        c_pipeline_attr.dict2struct(pipeline_attr)

        libaxcl_ivps.AXCL_IVPS_SetPipelineAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetPipelineAttr.argtypes = [c_int32, POINTER(AX_IVPS_PIPELINE_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetPipelineAttr(c_int32(ivps_grp), byref(c_pipeline_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_pipeline_attr(ivps_grp: int) -> tuple[dict, int]:
    """
    get pipeline attr, must be executed after axcl.ivps.create_grp.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetPipelineAttr(IVPS_GRP IvpsGrp, AX_IVPS_PIPELINE_ATTR_T *ptPipelineAttr)`
        **python**              `dict, ret = get_pipeline_attr(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: tuple[dict, int]

        - **pipeline_attr** (*dict*) - see :class:`AX_IVPS_PIPELINE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_PIPELINE_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    try:
        pipeline_attr = {}
        c_pipeline_attr = AX_IVPS_PIPELINE_ATTR_T()

        libaxcl_ivps.AXCL_IVPS_GetPipelineAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetPipelineAttr.argtypes = [c_int32, POINTER(AX_IVPS_PIPELINE_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_GetPipelineAttr(c_int32(ivps_grp), byref(c_pipeline_attr))

        if ret == AX_SUCCESS:
            pipeline_attr = c_pipeline_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return pipeline_attr, ret

def start_grp(ivps_grp: int) -> int:
    """
    start group, must be executed after axcl.ipvs.create_grp.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_StartGrp(IVPS_GRP IvpsGrp)`
        **python**              `ret = axcl.ivps.start_grp(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_StartGrp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_StartGrp.argtypes = [c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_StartGrp(c_int32(ivps_grp))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def stop_grp(ivps_grp: int) -> int:
    """
    stop group, must be executed after axcl.ivps.start_grp.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_StopGrp(IVPS_GRP IvpsGrp)`
        **python**              `ret = axcl.ivps.stop_grp(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_StopGrp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_StopGrp.argtypes = [c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_StopGrp(c_int32(ivps_grp))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def enable_chn(ivps_grp: int, ivps_chn: int) -> int:
    """
    enable channel, must be executed after axcl.ivps.set_pipeline_attr.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_EnableChn(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn)`
        **python**              `ret = axcl.ivps.enable_chn(ivps_grp, ivps_chn)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn, Value range: [0, :ref:`AX_IVPS_MAX_OUTCHN_NUM <target to ax_ivps_max_outchn_num>`)
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    try:
        libaxcl_ivps.AXCL_IVPS_EnableChn.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_EnableChn.argtypes = [c_int32, c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_EnableChn(c_int32(ivps_grp), c_int32(ivps_chn))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def disable_chn(ivps_grp: int, ivps_chn: int) -> int:
    """
    disable channel, must be executed after axcl.ivps.enable_chn.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DisableChn(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn)`
        **python**              `ret = axcl.ivps.disable_chn(ivps_grp, ivps_chn)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_DisableChn.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DisableChn.argtypes = [c_int32, c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_DisableChn(c_int32(ivps_grp), c_int32(ivps_chn))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def send_frame(ivps_grp: int, frame: dict, millisec: int) -> int:
    """
    User sends data to IVPS

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SendFrame(IVPS_GRP IvpsGrp, const AX_VIDEO_FRAME_T *ptFrame, AX_S32 nMilliSec)`
        **python**              `ret = axcl.ivps.send_frame(ivps_grp, frame, millisec)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param dict frame: frame, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param int millisec: timeout parameter, -1: Blocking interface; 0: Non-blocking interface; >0: Timeout waiting time, unit milliseconds
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_frame = AX_VIDEO_FRAME_T()
        c_frame.dict2struct(frame)
        libaxcl_ivps.AXCL_IVPS_SendFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SendFrame.argtypes = [c_int32, POINTER(AX_VIDEO_FRAME_T), c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_SendFrame(c_int32(ivps_grp), byref(c_frame), c_int32(millisec))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_chn_frame(ivps_grp: int, ivps_chn: int, millisec: int) -> tuple[dict, int]:
    """
    The user gets a processed frame from a channel

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetChnFrame(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, AX_VIDEO_FRAME_T *ptFrame, AX_S32 nMilliSec)`
        **python**              `frame, ret = get_chn_frame(ivps_grp, ivps_chn, millisec)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param int millisec: timeout parameter, -1: Blocking interface; 0: Non-blocking interface; >0: Timeout waiting time, unit milliseconds
    :returns: tuple[dict, int]

        - **frame** (*dict*) - see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    frame = {}
    try:
        c_frame = AX_VIDEO_FRAME_T()
        libaxcl_ivps.AXCL_IVPS_GetChnFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetChnFrame.argtypes = [c_int32, c_int32, POINTER(AX_VIDEO_FRAME_T), c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_GetChnFrame(c_int32(ivps_grp), c_int32(ivps_chn), byref(c_frame), c_int32(millisec))
        if ret == AX_SUCCESS:
            frame = c_frame.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return frame, ret

def release_chn_frame(ivps_grp: int, ivps_chn: int, frame: dict) -> int:
    """
    The user releases a channel frame.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_ReleaseChnFrame(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, AX_VIDEO_FRAME_T *ptFrame)`
        **python**              `ret = axcl.ivps.release_chn_frame(ivps_grp, ivps_chn, frame)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param dict frame: frame, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_frame = AX_VIDEO_FRAME_T()
        c_frame.dict2struct(frame)

        libaxcl_ivps.AXCL_IVPS_ReleaseChnFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_ReleaseChnFrame.argtypes = [c_int32, c_int32, POINTER(AX_VIDEO_FRAME_T)]
        ret = libaxcl_ivps.AXCL_IVPS_ReleaseChnFrame(c_int32(ivps_grp), c_int32(ivps_chn), byref(c_frame))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_grp_frame(ivps_grp: int, millisec: int) -> tuple[dict, int]:
    """
    The user gets a raw frame from the group.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetGrpFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame, AX_S32 nMilliSec)`
        **python**              `frame, ret = get_grp_frame(ivps_grp, millisec)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int millisec: timeout parameter, -1: Blocking interface; 0: Non-blocking interface; >0: Timeout waiting time, unit milliseconds
    :returns: tuple[dict, int]

        - **frame** (*dict*) - see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    frame = {}
    try:
        c_frame = AX_VIDEO_FRAME_T()
        libaxcl_ivps.AXCL_IVPS_GetGrpFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetGrpFrame.argtypes = [c_int32, POINTER(AX_VIDEO_FRAME_T), c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_GetGrpFrame(c_int32(ivps_grp), byref(c_frame), c_int32(millisec))
        if ret == AX_SUCCESS:
            frame = c_frame.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return frame, ret

def release_grp_frame(ivps_grp: int, frame: dict) -> int:
    """
    The user releases a group frame.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_ReleaseGrpFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame)`
        **python**              `ret = axcl.ivps.release_grp_frame(ivps_grp, frame)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param dict frame: frame, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_frame = AX_VIDEO_FRAME_T()
        c_frame.dict2struct(frame)

        libaxcl_ivps.AXCL_IVPS_ReleaseGrpFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_ReleaseGrpFrame.argtypes = [c_int32, POINTER(AX_VIDEO_FRAME_T)]
        ret = libaxcl_ivps.AXCL_IVPS_ReleaseGrpFrame(c_int32(ivps_grp), byref(c_frame))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_debug_fifo_frame(ivps_grp: int) -> tuple[dict, int]:
    """
    The user gets a raw frame from the debug fifo.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetDebugFifoFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame)`
        **python**              `frame, ret = get_debug_fifo_frame(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: tuple[dict, int]

        - **frame** (*dict*) - see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    frame = {}
    try:
        c_frame = AX_VIDEO_FRAME_T()

        libaxcl_ivps.AXCL_IVPS_GetDebugFifoFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetDebugFifoFrame.argtypes = [c_int32, POINTER(AX_VIDEO_FRAME_T)]
        ret = libaxcl_ivps.AXCL_IVPS_GetDebugFifoFrame(c_int32(ivps_grp), byref(c_frame))
        if ret == AX_SUCCESS:
            frame = c_frame.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return frame, ret

def release_debug_fifo_frame(ivps_grp: int, frame: dict) -> int:
    """
    release debug fifo frame

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_ReleaseDebugFifoFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame)`
        **python**              `ret = axcl.ivps.release_debug_fifo_frame(ivps_grp, frame)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param dict frame: frame, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_frame = AX_VIDEO_FRAME_T()
        c_frame.dict2struct(frame)
        libaxcl_ivps.AXCL_IVPS_ReleaseDebugFifoFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_ReleaseDebugFifoFrame.argtypes = [c_int32, POINTER(AX_VIDEO_FRAME_T)]
        ret = libaxcl_ivps.AXCL_IVPS_ReleaseDebugFifoFrame(c_int32(ivps_grp), byref(c_frame))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def set_grp_ldc_attr(ivps_grp: int, ivps_filter: int, ldc_attr: dict) -> int:
    """
    set group ldc attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetGrpLDCAttr(IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter, const AX_IVPS_LDC_ATTR_T *ptLDCAttr)`
        **python**              `ret = axcl.ivps.set_grp_ldc_attr(ivps_grp, ivps_filter, ldc_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_filter: ivps filter
    :param dict ldc_attr: ldc attr, see :class:`AX_IVPS_LDC_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_LDC_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_ldc_attr = AX_IVPS_LDC_ATTR_T()
        c_ldc_attr.dict2struct(ldc_attr)

        libaxcl_ivps.AXCL_IVPS_SetGrpLDCAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetGrpLDCAttr.argtypes = [c_int32, c_int32, POINTER(AX_IVPS_LDC_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetGrpLDCAttr(c_int32(ivps_grp), c_int32(ivps_filter), byref(c_ldc_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_grp_ldc_attr(ivps_grp: int, ivps_filter: int) -> tuple[dict, int]:
    """
    get group ldc attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetGrpLDCAttr(IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter, AX_IVPS_LDC_ATTR_T *ptLDCAttr)`
        **python**              `ldc_attr, ret = get_grp_ldc_attr(ivps_grp, ivps_filter)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_filter: ivps filter
    :returns: tuple[dict, int]

        - **ldc_attr** (*dict*) - see :class:`AX_IVPS_LDC_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_LDC_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    ldc_attr = {}
    try:
        c_ldc_attr = AX_IVPS_LDC_ATTR_T()

        libaxcl_ivps.AXCL_IVPS_GetGrpLDCAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetGrpLDCAttr.argtypes = [c_int32, c_int32, POINTER(AX_IVPS_LDC_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_GetGrpLDCAttr(c_int32(ivps_grp), c_int32(ivps_filter), byref(c_ldc_attr))
        if ret == AX_SUCCESS:
            ldc_attr = c_ldc_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ldc_attr, ret

def set_chn_ldc_attr(ivps_grp: int, ivps_chn: int, ivps_filter: int, ldc_attr: dict) -> int:
    """
    set chn ldc attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetChnLDCAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, const AX_IVPS_LDC_ATTR_T *ptLDCAttr)`
        **python**              `ret = axcl.ivps.set_chn_ldc_attr(ivps_grp, ivps_chn, ivps_filter, ldc_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param int ivps_filter: ivps filter
    :param dict ldc_attr: ldc attr, see :class:`AX_IVPS_LDC_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_LDC_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_ldc_attr = AX_IVPS_LDC_ATTR_T()
        c_ldc_attr.dict2struct(ldc_attr)
        libaxcl_ivps.AXCL_IVPS_SetChnLDCAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetChnLDCAttr.argtypes = [c_int32, c_int32, c_int32, POINTER(AX_IVPS_LDC_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetChnLDCAttr(c_int32(ivps_grp), c_int32(ivps_chn), c_int32(ivps_filter), byref(c_ldc_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_chn_ldc_attr(ivps_grp: int, ivps_chn: int, ivps_filter: int) -> tuple[dict, int]:
    """
    get chn ldc attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetChnLDCAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, AX_IVPS_LDC_ATTR_T *ptLDCAttr)`
        **python**              `ldc_attr, ret = get_chn_ldc_attr(ivps_grp, ivps_chn, ivps_filter)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param int ivps_filter: ivps filter
    :returns: tuple[dict, int]

        - **ldc_attr** (*dict*) - ssee :class:`AX_IVPS_LDC_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_LDC_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    ldc_attr = {}
    try:
        c_ldc_attr = AX_IVPS_LDC_ATTR_T()

        libaxcl_ivps.AXCL_IVPS_GetChnLDCAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetChnLDCAttr.argtypes = [c_int32, c_int32, c_int32, POINTER(AX_IVPS_LDC_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_GetChnLDCAttr(c_int32(ivps_grp), c_int32(ivps_chn), c_int32(ivps_filter), byref(c_ldc_attr))
        if ret == AX_SUCCESS:
            ldc_attr = c_ldc_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ldc_attr, ret

def set_grp_pool_attr(ivps_grp: int, pool_attr: dict) -> int:
    """
    set group pool attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetGrpPoolAttr(IVPS_GRP IvpsGrp, const AX_IVPS_POOL_ATTR_T *ptPoolAttr)`
        **python**              `ret = axcl.ivps.set_grp_pool_attr(ivps_grp, pool_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param dict pool_attr: pool attr, see :class:`AX_IVPS_POOL_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POOL_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_pool_attr = AX_IVPS_POOL_ATTR_T()
        c_pool_attr.dict2struct(pool_attr)

        libaxcl_ivps.AXCL_IVPS_SetGrpPoolAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetGrpPoolAttr.argtypes = [c_int32, POINTER(AX_IVPS_POOL_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetGrpPoolAttr(c_int32(ivps_grp), byref(c_pool_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def set_chn_pool_attr(ivps_grp: int, ivps_chn: int, pool_attr: dict) -> int:
    """
    set chn pool attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetChnPoolAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, const AX_IVPS_POOL_ATTR_T *ptPoolAttr)`
        **python**              `ret = axcl.ivps.set_chn_pool_attr(ivps_grp, ivps_chn, pool_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param dict pool_attr: pool attr, see :class:`AX_IVPS_POOL_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POOL_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_pool_attr = AX_IVPS_POOL_ATTR_T()
        c_pool_attr.dict2struct(pool_attr)

        libaxcl_ivps.AXCL_IVPS_SetChnPoolAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetChnPoolAttr.argtypes = [c_int32, c_int32, POINTER(AX_IVPS_POOL_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetChnPoolAttr(c_int32(ivps_grp), c_int32(ivps_chn), byref(c_pool_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def set_grp_user_frc(ivps_grp: int, framerate_attr: dict) -> int:
    """
    set group user frc

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetGrpUserFRC(IVPS_GRP IvpsGrp, const AX_IVPS_USER_FRAME_RATE_CTRL_T *ptFrameRateAttr)`
        **python**              `ret = axcl.ivps.set_grp_user_frc(ivps_grp, framerate_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param dict framerate_attr: framerate attr, see :class:`AX_IVPS_USER_FRAME_RATE_CTRL_T <axcl.ivps.axcl_ivps_type.AX_IVPS_USER_FRAME_RATE_CTRL_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_framerate_attr = AX_IVPS_USER_FRAME_RATE_CTRL_T()
        c_framerate_attr.dict2struct(framerate_attr)

        libaxcl_ivps.AXCL_IVPS_SetGrpUserFRC.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetGrpUserFRC.argtypes = [c_int32, POINTER(AX_IVPS_USER_FRAME_RATE_CTRL_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetGrpUserFRC(c_int32(ivps_grp), byref(c_framerate_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def set_chn_user_frc(ivps_grp: int, ivps_chn: int, framerate_attr: dict) -> int:
    """
    set chn user frc

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetChnUserFRC(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, const AX_IVPS_USER_FRAME_RATE_CTRL_T *ptFrameRateAttr)`
        **python**              `ret = axcl.ivps.set_chn_user_frc(ivps_grp, ivps_chn, framerate_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param dict framerate_attr: framerate attr, see :class:`AX_IVPS_USER_FRAME_RATE_CTRL_T <axcl.ivps.axcl_ivps_type.AX_IVPS_USER_FRAME_RATE_CTRL_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_framerate_attr = AX_IVPS_USER_FRAME_RATE_CTRL_T()
        c_framerate_attr.dict2struct(framerate_attr)

        libaxcl_ivps.AXCL_IVPS_SetChnUserFRC.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetChnUserFRC.argtypes = [c_int32, c_int32, POINTER(AX_IVPS_USER_FRAME_RATE_CTRL_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetChnUserFRC(c_int32(ivps_grp), c_int32(ivps_chn), byref(c_framerate_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def set_grp_crop(ivps_grp: int, crop_info: dict) -> int:
    """
    set group crop

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetGrpCrop(IVPS_GRP IvpsGrp, const AX_IVPS_CROP_INFO_T *ptCropInfo)`
        **python**              `ret = axcl.ivps.set_grp_crop(ivps_grp, crop_info)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int crop_info: crop info, see :class:`AX_IVPS_CROP_INFO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_CROP_INFO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:

        c_crop_info = AX_IVPS_CROP_INFO_T()
        c_crop_info.dict2struct(crop_info)

        libaxcl_ivps.AXCL_IVPS_SetGrpCrop.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetGrpCrop.argtypes = [c_int32, POINTER(AX_IVPS_CROP_INFO_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetGrpCrop(c_int32(ivps_grp), byref(c_crop_info))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_grp_crop(ivps_grp: int) -> tuple[dict, int]:
    """
    get group crop

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetGrpCrop(IVPS_GRP IvpsGrp, AX_IVPS_CROP_INFO_T *ptCropInfo)`
        **python**              `crop_info, ret = get_grp_crop(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: tuple[dict, int]

        - **crop_info** (*dict*) - see :class:`AX_IVPS_CROP_INFO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_CROP_INFO_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    crop_info = {}
    try:
        c_crop_info = AX_IVPS_CROP_INFO_T()

        libaxcl_ivps.AXCL_IVPS_GetGrpCrop.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetGrpCrop.argtypes = [c_int32, POINTER(AX_IVPS_CROP_INFO_T)]
        ret = libaxcl_ivps.AXCL_IVPS_GetGrpCrop(c_int32(ivps_grp), byref(c_crop_info))
        if ret == AX_SUCCESS:
            crop_info = c_crop_info.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return crop_info, ret

def set_chn_attr(ivps_grp: int, ivps_chn: int, ivps_filter: int, chn_attr: dict) -> int:
    """
    set chn attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetChnAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, const AX_IVPS_CHN_ATTR_T *ptChnAttr)`
        **python**              `ret = axcl.ivps.set_chn_attr(ivps_grp, ivps_chn, ivps_filter, chn_attr)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param int ivps_filter: ivps filter
    :param dict chn_attr: chn attr, see :class:`AX_IVPS_CHN_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_CHN_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_chn_attr = AX_IVPS_CHN_ATTR_T()
        c_chn_attr.dict2struct(chn_attr)
        libaxcl_ivps.AXCL_IVPS_SetChnAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetChnAttr.argtypes = [c_int32, c_int32, c_int32, POINTER(AX_IVPS_CHN_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_SetChnAttr(c_int32(ivps_grp), c_int32(ivps_chn), c_int32(ivps_filter), byref(c_chn_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_chn_attr(ivps_grp: int, ivps_chn: int, ivps_filter: int) -> tuple[dict, int]:
    """
    get chn attr

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetChnAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, AX_IVPS_CHN_ATTR_T *ptChnAttr)`
        **python**              `chn_attr, ret = get_chn_attr(ivps_grp, ivps_chn, ivps_filter)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int ivps_chn: ivps chn
    :param int ivps_filter: ivps filter
    :returns: tuple[dict, int]

        - **chn_attr** (*dict*) - see :class:`AX_IVPS_CHN_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_CHN_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    chn_attr = {}
    try:
        c_chn_attr = AX_IVPS_CHN_ATTR_T()

        libaxcl_ivps.AXCL_IVPS_GetChnAttr.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetChnAttr.argtypes = [c_int32, c_int32, c_int32, POINTER(AX_IVPS_CHN_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_GetChnAttr(c_int32(ivps_grp), c_int32(ivps_chn), c_int32(ivps_filter), byref(c_chn_attr))
        if ret == AX_SUCCESS:
            chn_attr = c_chn_attr.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return chn_attr, ret

def enable_backup_frame(ivps_grp: int, fifo_depth: int) -> int:
    """
    enable backup frame

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_EnableBackupFrame(IVPS_GRP IvpsGrp, AX_U8 nFifoDepth)`
        **python**              `ret = axcl.ivps.enable_backup_frame(ivps_grp, fifo_depth)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :param int fifo_depth: fifo depth
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_EnableBackupFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_EnableBackupFrame.argtypes = [c_int32, c_uint8]
        ret = libaxcl_ivps.AXCL_IVPS_EnableBackupFrame(c_int32(ivps_grp), c_uint8(fifo_depth))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def disable_backup_frame(ivps_grp: int) -> int:
    """
    disable backup frame

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DisableBackupFrame(IVPS_GRP IvpsGrp)`
        **python**              `ret = axcl.ivps.disable_backup_frame(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_DisableBackupFrame.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DisableBackupFrame.argtypes = [c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_DisableBackupFrame(c_int32(ivps_grp))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def reset_grp(ivps_grp: int) -> int:
    """
    reset group

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_ResetGrp(IVPS_GRP IvpsGrp)`
        **python**              `ret = axcl.ivps.reset_grp(ivps_grp)`
        ======================= =====================================================

    :param int ivps_grp: ivps group
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_ResetGrp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_ResetGrp.argtypes = [c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_ResetGrp(c_int32(ivps_grp))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_engine_duty_cycle() -> tuple[dict, int]:
    """
    get engine duty cycle

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetEngineDutyCycle(AX_IVPS_DUTY_CYCLE_ATTR_T *ptDutyCycle)`
        **python**              `duty_cycle, ret = get_engine_duty_cycle()`
        ======================= =====================================================

    :returns: tuple[dict, int]

        - **duty_cycle** (*dict*) - see :class:`AX_IVPS_DUTY_CYCLE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_DUTY_CYCLE_ATTR_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    duty_cycle = {}
    try:
        c_duty_cycle = AX_IVPS_DUTY_CYCLE_ATTR_T()

        libaxcl_ivps.AXCL_IVPS_GetEngineDutyCycle.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetEngineDutyCycle.argtypes = [POINTER(AX_IVPS_DUTY_CYCLE_ATTR_T)]
        ret = libaxcl_ivps.AXCL_IVPS_GetEngineDutyCycle(byref(c_duty_cycle))
        if ret == AX_SUCCESS:
            duty_cycle = c_duty_cycle.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return duty_cycle, ret

def rgn_create() -> int:
    """
    rgn create

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `IVPS_RGN_HANDLE AXCL_IVPS_RGN_Create(AX_VOID)`
        **python**              `ret = axcl.ivps.rgn_create()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    handle = -1
    try:
        libaxcl_ivps.AXCL_IVPS_RGN_Create.restype = IVPS_RGN_HANDLE
        libaxcl_ivps.AXCL_IVPS_RGN_Create.argtypes = []
        handle = libaxcl_ivps.AXCL_IVPS_RGN_Create()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
        return handle

def rgn_destroy(region: int) -> int:
    """
    rgn destroy

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_RGN_Destroy(IVPS_RGN_HANDLE hRegion)`
        **python**              `ret = axcl.ivps.rgn_destroy(region)`
        ======================= =====================================================

    :param int region: region
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_RGN_Destroy.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_RGN_Destroy.argtypes = [IVPS_RGN_HANDLE]
        ret = libaxcl_ivps.AXCL_IVPS_RGN_Destroy(region)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def rgn_attach_to_filter(region: int, ivps_grp: int, ivps_filter: dict) -> int:
    """
    rgn attach to filter

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_RGN_AttachToFilter(IVPS_RGN_HANDLE hRegion, IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter)`
        **python**              `ret = axcl.ivps.rgn_attach_to_filter(region, ivps_grp, ivps_filter)`
        ======================= =====================================================

    :param int region: region
    :param int ivps_grp: ivps group
    :param dict ivps_filter: ivps filter
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_RGN_AttachToFilter.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_RGN_AttachToFilter.argtypes = [IVPS_RGN_HANDLE, c_int32, c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_RGN_AttachToFilter(region, c_int32(ivps_grp), c_int32(ivps_filter))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def rgn_detach_from_filter(region: int, ivps_grp: int, ivps_filter: dict) -> int:
    """
    rgn detach from filter

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_RGN_DetachFromFilter(IVPS_RGN_HANDLE hRegion, IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter)`
        **python**              `ret = axcl.ivps.rgn_detach_from_filter(region, ivps_grp, ivps_filter)`
        ======================= =====================================================

    :param int region: region
    :param int ivps_grp: ivps group
    :param dict ivps_filter: ivps filter
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_RGN_DetachFromFilter.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_RGN_DetachFromFilter.argtypes = [IVPS_RGN_HANDLE, c_int32, c_int32]
        ret = libaxcl_ivps.AXCL_IVPS_RGN_DetachFromFilter(region, c_int32(ivps_grp), c_int32(ivps_filter))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def rgn_update(region: int, rgn_chn_attr: dict, disp_list: list[dict]) -> int:
    """
    rgn update

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_RGN_Update(IVPS_RGN_HANDLE hRegion, const AX_IVPS_RGN_DISP_GROUP_T *ptDisp)`
        **python**              `ret = axcl.ivps.rgn_update(region, rgn_chn_attr, disp_list)`
        ======================= =====================================================

    :param int region: region
    :param dict rgn_chn_attr: rgn chn attr, see :class:`AX_IVPS_RGN_CHN_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_CHN_ATTR_T>`
    :param list[dict] disp_list: array of display attributes, see :class:`AX_IVPS_RGN_DISP_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_DISP_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_disp = AX_IVPS_RGN_DISP_GROUP_T()
        c_disp.nNum = len(disp_list)

        c_disp.tChnAttr.dict2struct(rgn_chn_attr)

        for i in range(c_disp.nNum):
            c_disp.arrDisp[i].dict2struct(disp_list[i], c_disp.arrDisp[i])

        libaxcl_ivps.AXCL_IVPS_RGN_Update.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_RGN_Update.argtypes = [IVPS_RGN_HANDLE, POINTER(AX_IVPS_RGN_DISP_GROUP_T)]
        ret = libaxcl_ivps.AXCL_IVPS_RGN_Update(region, byref(c_disp))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def cmm_copy_tdp(src_phy_addr: int, dst_phy_addr: int, mem_size: int) -> int:
    """
    cmm copy tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CmmCopyTdp(AX_U64 nSrcPhyAddr, AX_U64 nDstPhyAddr, AX_U64 nMemSize)`
        **python**              `ret = axcl.ivps.cmm_copy_tdp(src_phy_addr, dst_phy_addr, mem_size)`
        ======================= =====================================================

    :param int src_phy_addr: src phy addr
    :param int dst_phy_addr: dst phy addr
    :param int mem_size: mem size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_CmmCopyTdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CmmCopyTdp.argtypes = [c_uint64, c_uint64, c_uint64]
        ret = libaxcl_ivps.AXCL_IVPS_CmmCopyTdp(c_uint64(src_phy_addr), c_uint64(dst_phy_addr), c_uint64(mem_size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def flip_and_rotation_tdp(src: dict, flip_mode: int, rotation: int, dst: dict) -> int:
    """
    flip and rotation tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_FlipAndRotationTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_CHN_FLIP_MODE_E eFlipMode, AX_IVPS_ROTATION_E eRotation, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.flip_and_rotation_tdp(src, flip_mode, rotation, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param int flip_mode: :class:`AX_IVPS_CHN_FLIP_MODE_E <axcl.ivps.axcl_ivps_type.AX_IVPS_CHN_FLIP_MODE_E>`
    :param int rotation: :class:`AX_IVPS_ROTATION_E <axcl.ivps.axcl_ivps_type.AX_IVPS_ROTATION_E>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)
        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        libaxcl_ivps.AXCL_IVPS_FlipAndRotationTdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_FlipAndRotationTdp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            c_int32,
            c_int32,
            POINTER(AX_VIDEO_FRAME_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_FlipAndRotationTdp(byref(c_src), c_int32(flip_mode), c_int32(rotation), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def csc_tdp(src: dict, dst: dict) -> int:
    """
    csc tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CscTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.csc_tdp(src, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)
        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        libaxcl_ivps.AXCL_IVPS_CscTdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CscTdp.argtypes = [POINTER(AX_VIDEO_FRAME_T), POINTER(AX_VIDEO_FRAME_T)]
        ret = libaxcl_ivps.AXCL_IVPS_CscTdp(byref(c_src), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_tdp(src: dict, dst: dict, aspect_ratio: dict) -> int:
    """
    crop resize tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio)`
        **python**              `ret = axcl.ivps.crop_resize_tdp(src, dst, aspect_ratio)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)
        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        libaxcl_ivps.AXCL_IVPS_CropResizeTdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeTdp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_ASPECT_RATIO_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_CropResizeTdp(byref(c_src), byref(c_dst), byref(c_aspect_ratio))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_v2_tdp(src: dict, box_list: list[dict], dst_list: list[dict], aspect_ratio: dict) -> int:
    """
    crop resize v2 tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeV2Tdp(const AX_VIDEO_FRAME_T *ptSrc, const AX_IVPS_RECT_T tBox[], AX_U32 nCropNum, AX_VIDEO_FRAME_T *ptDst[], const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio)`
        **python**              `ret = axcl.ivps.crop_resize_v2_tdp(src, box_list, dst_list, aspect_ratio)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] box_list: box list, see :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`
    :param list[dict] dst_list: dst list, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        crop_num = len(box_list)

        c_box_list = (AX_IVPS_RECT_T * crop_num)()
        for idx, box in enumerate(box_list):
            c_box_list[idx].dict2struct(box)

        dst_num = len(dst_list)
        LP_AX_VIDEO_FRAME_T = POINTER(AX_VIDEO_FRAME_T)
        c_dst_array = (AX_VIDEO_FRAME_T * dst_num)()
        c_dstptr_array = (LP_AX_VIDEO_FRAME_T * dst_num)()
        for idx in range(dst_num):
            c_dst_array[idx].dict2struct(dst_list[idx])
            c_dstptr_array[idx] = cast(addressof(c_dst_array[idx]), LP_AX_VIDEO_FRAME_T)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        libaxcl_ivps.AXCL_IVPS_CropResizeV2Tdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeV2Tdp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_RECT_T),
            c_uint32,
            POINTER(POINTER(AX_VIDEO_FRAME_T)),
            POINTER(AX_IVPS_ASPECT_RATIO_T)
        ]

        ret = libaxcl_ivps.AXCL_IVPS_CropResizeV2Tdp(byref(c_src), c_box_list, c_uint32(crop_num), c_dstptr_array, byref(c_aspect_ratio))
        if ret == AX_SUCCESS:
            for idx in range(dst_num):
                dst_list[idx].update(c_dst_array[idx].struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def alpha_blending_tdp(src: dict, overlay: dict, offset: dict, alpha: int, dst: dict) -> int:
    """
    alpha blending tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_AlphaBlendingTdp(const AX_VIDEO_FRAME_T *ptSrc, const AX_VIDEO_FRAME_T *ptOverlay, const AX_IVPS_POINT_T tOffset, AX_U8 nAlpha, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.alpha_blending_tdp(src, overlay, offset, alpha, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict overlay: overlay, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict offset: offset, see :class:`AX_IVPS_POINT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_T>`
    :param int alpha: alpha
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_overlay = AX_VIDEO_FRAME_T()
        c_overlay.dict2struct(overlay)

        c_offset = AX_IVPS_POINT_T()
        c_offset.dict2struct(offset)

        libaxcl_ivps.AXCL_IVPS_AlphaBlendingTdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_AlphaBlendingTdp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            AX_IVPS_POINT_T,
            c_uint8,
            POINTER(AX_VIDEO_FRAME_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_AlphaBlendingTdp(byref(c_src), byref(c_overlay), c_offset, c_uint8(alpha), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def alpha_blending_v3_tdp(src: dict, overlay: dict, dst: dict) -> int:
    """
    alpha blending v3 tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_AlphaBlendingV3Tdp(const AX_VIDEO_FRAME_T *ptSrc, const AX_OVERLAY_T *ptOverlay, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.alpha_blending_v3_tdp(src, overlay, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict overlay: overlay, see :class:`AX_OVERLAY_T <axcl.ax_global_type.AX_OVERLAY_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_overlay = AX_OVERLAY_T()
        c_overlay.dict2struct(overlay)

        libaxcl_ivps.AXCL_IVPS_AlphaBlendingV3Tdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_AlphaBlendingV3Tdp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_OVERLAY_T),
            POINTER(AX_VIDEO_FRAME_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_AlphaBlendingV3Tdp(byref(c_src), byref(c_overlay), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def draw_osd_tdp(src: dict, bmp_list: list[dict]) -> int:
    """
    draw osd tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawOsdTdp(const AX_VIDEO_FRAME_T *ptFrame, const AX_OSD_BMP_ATTR_T arrBmp[], AX_U32 nNum)`
        **python**              `ret = axcl.ivps.draw_osd_tdp(src, bmp_list)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] bmp_list: bmp list, see :class:`AX_OSD_BMP_ATTR_T <axcl.ax_global_type.AX_OSD_BMP_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        num = len(bmp_list)

        c_bmp_list = (AX_OSD_BMP_ATTR_T * num)()
        for idx, bmp in enumerate(bmp_list):
            c_bmp_list[idx].dict2struct(bmp)

        libaxcl_ivps.AXCL_IVPS_DrawOsdTdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawOsdTdp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_OSD_BMP_ATTR_T),
            c_uint32
        ]
        ret = libaxcl_ivps.AXCL_IVPS_DrawOsdTdp(byref(c_src), c_bmp_list, c_uint32(num))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def draw_mosaic_tdp(src: dict, mosaic_list: list[dict]) -> int:
    """
    draw mosaic tdp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawMosaicTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_RGN_MOSAIC_T tMosaic[], AX_U32 nNum)`
        **python**              `ret = axcl.ivps.draw_mosaic_tdp(src, mosaic_list)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] mosaic_list: mosaic list, see :class:`AX_IVPS_RGN_MOSAIC_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_MOSAIC_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        num = len(mosaic_list)

        c_mosaic_list = (AX_IVPS_RGN_MOSAIC_T * num)()
        for idx, mosaic in enumerate(mosaic_list):
            c_mosaic_list[idx].dict2struct(mosaic)

        libaxcl_ivps.AXCL_IVPS_DrawMosaicTdp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawMosaicTdp.argtypes = [POINTER(AX_VIDEO_FRAME_T), POINTER(AX_IVPS_RGN_MOSAIC_T), c_uint32]
        ret = libaxcl_ivps.AXCL_IVPS_DrawMosaicTdp(byref(c_src), c_mosaic_list, c_uint32(num))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def cmm_copy_vpp(src_phy_addr: int, dst_phy_addr: int, mem_size: int) -> int:
    """
    cmm copy vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CmmCopyVpp(AX_U64 nSrcPhyAddr, AX_U64 nDstPhyAddr, AX_U64 nMemSize)`
        **python**              `ret = axcl.ivps.cmm_copy_vpp(src_phy_addr, dst_phy_addr, mem_size)`
        ======================= =====================================================

    :param int src_phy_addr: src phy addr
    :param int dst_phy_addr: dst phy addr
    :param int mem_size: mem size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_CmmCopyVpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CmmCopyVpp.argtypes = [c_uint64, c_uint64, c_uint64]
        ret = libaxcl_ivps.AXCL_IVPS_CmmCopyVpp(c_uint64(src_phy_addr), c_uint64(dst_phy_addr), c_uint64(mem_size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_vpp(src: dict, dst: dict, aspect_ratio: dict) -> int:
    """
    crop resize vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeVpp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio)`
        **python**              `ret = axcl.ivps.crop_resize_vpp(src, dst, aspect_ratio)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        libaxcl_ivps.AXCL_IVPS_CropResizeVpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeVpp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_ASPECT_RATIO_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_CropResizeVpp(byref(c_src), byref(c_dst), byref(c_aspect_ratio))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_v2_vpp(src: dict, box_list: list[dict], dst_list: list[dict], aspect_ratio: dict) -> int:
    """
    crop resize v2 vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeV2Vpp(const AX_VIDEO_FRAME_T *ptSrc, const AX_IVPS_RECT_T tBox[], AX_U32 nCropNum, AX_VIDEO_FRAME_T *ptDst[], const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio)`
        **python**              `ret = axcl.ivps.crop_resize_v2_vpp(src, box_list, dst_list, aspect_ratio)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] box_list: box list, see :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`
    :param list[dict] dst_list: dst list, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        crop_num = len(box_list)

        c_box_list = (AX_IVPS_RECT_T * crop_num)()
        for idx, box in enumerate(box_list):
            c_box_list[idx].dict2struct(box)

        dst_num = len(dst_list)
        LP_AX_VIDEO_FRAME_T = POINTER(AX_VIDEO_FRAME_T)
        c_dst_array = (AX_VIDEO_FRAME_T * dst_num)()
        c_dstptr_array = (LP_AX_VIDEO_FRAME_T * dst_num)()
        for idx in range(dst_num):
            c_dst_array[idx].dict2struct(dst_list[idx])
            c_dstptr_array[idx] = cast(addressof(c_dst_array[idx]), LP_AX_VIDEO_FRAME_T)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        libaxcl_ivps.AXCL_IVPS_CropResizeV2Vpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeV2Vpp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_RECT_T),
            c_uint32,
            POINTER(POINTER(AX_VIDEO_FRAME_T)),
            POINTER(AX_IVPS_ASPECT_RATIO_T)
        ]

        ret = libaxcl_ivps.AXCL_IVPS_CropResizeV2Vpp(byref(c_src), c_box_list, crop_num, c_dstptr_array, byref(c_aspect_ratio))
        if ret == AX_SUCCESS:
            for idx in range(crop_num):
                dst_list[idx].update(c_dst_array[idx].struct2dict())

    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_v3_vpp(src: dict, dst_list: list[dict], aspect_ratio: dict) -> int:
    """
    crop resize v3 vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeV3Vpp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst[], AX_U32 nNum, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio)`
        **python**              `ret = axcl.ivps.crop_resize_v3_vpp(src, dst_list, aspect_ratio)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] dst_list: dst list, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:

        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        num = len(dst_list)

        LP_AX_VIDEO_FRAME_T = POINTER(AX_VIDEO_FRAME_T)
        c_dst_array = (AX_VIDEO_FRAME_T * num)()
        c_dstptr_array = (LP_AX_VIDEO_FRAME_T * num)()
        for idx in range(num):
            c_dst_array[idx].dict2struct(dst_list[idx])
            c_dstptr_array[idx] = cast(addressof(c_dst_array[idx]), LP_AX_VIDEO_FRAME_T)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        libaxcl_ivps.AXCL_IVPS_CropResizeV3Vpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeV3Vpp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(POINTER(AX_VIDEO_FRAME_T)),
            c_uint32,
            POINTER(AX_IVPS_ASPECT_RATIO_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_CropResizeV3Vpp(byref(c_src), c_dstptr_array, c_uint32(num), byref(c_aspect_ratio))
        if ret == AX_SUCCESS:
            for idx in range(num):
                dst_list[idx].update(c_dst_array[idx].struct2dict())

    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def csc_vpp(src: dict, dst: dict) -> int:
    """
    csc vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CscVpp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.csc_vpp(src, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        libaxcl_ivps.AXCL_IVPS_CscVpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CscVpp.argtypes = [POINTER(AX_VIDEO_FRAME_T), POINTER(AX_VIDEO_FRAME_T)]
        ret = libaxcl_ivps.AXCL_IVPS_CscVpp(byref(c_src), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def draw_mosaic_vpp(src: dict, mosaic_list: list[dict]) -> int:
    """
    draw mosaic vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawMosaicVpp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_RGN_MOSAIC_T tMosaic[], AX_U32 nNum)`
        **python**              `ret = axcl.ivps.draw_mosaic_vpp(src, mosaic_list)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] mosaic_list: mosaic list, see :class:`AX_IVPS_RGN_MOSAIC_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_MOSAIC_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        num = len(mosaic_list)

        c_mosaic_list = (AX_IVPS_RGN_MOSAIC_T * num)()
        for idx, mosaic in enumerate(mosaic_list):
            c_mosaic_list[idx].dict2struct(mosaic)

        libaxcl_ivps.AXCL_IVPS_DrawMosaicVpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawMosaicVpp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_RGN_MOSAIC_T),
            c_uint32
        ]
        ret = libaxcl_ivps.AXCL_IVPS_DrawMosaicVpp(byref(c_src), c_mosaic_list, c_uint32(num))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def set_scale_coef_level_vpp(scale_range: dict, coef_level: dict) -> int:
    """
    set scale coef level vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetScaleCoefLevelVpp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, const AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel)`
        **python**              `ret = axcl.ivps.set_scale_coef_level_vpp(scale_range, coef_level)`
        ======================= =====================================================

    :param dict scale_range: scale range, see :class:`AX_IVPS_SCALE_RANGE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_RANGE_T>`
    :param dict coef_level: coef level, see :class:`AX_IVPS_SCALE_COEF_LEVEL_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_COEF_LEVEL_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_scale_range = AX_IVPS_SCALE_RANGE_T()
        c_scale_range.dict2struct(scale_range)

        c_coef_level = AX_IVPS_SCALE_COEF_LEVEL_T()
        c_coef_level.dict2struct(coef_level)

        libaxcl_ivps.AXCL_IVPS_SetScaleCoefLevelVpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetScaleCoefLevelVpp.argtypes = [
            POINTER(AX_IVPS_SCALE_RANGE_T),
            POINTER(AX_IVPS_SCALE_COEF_LEVEL_T)
        ]

        ret = libaxcl_ivps.AXCL_IVPS_SetScaleCoefLevelVpp(byref(c_scale_range), byref(c_coef_level))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_scale_coef_level_vpp(scale_range: dict) -> tuple[dict, int]:
    """
    get scale coef level vpp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetScaleCoefLevelVpp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel)`
        **python**              `coef_level, ret = get_scale_coef_level_vpp(scale_range)`
        ======================= =====================================================

    :param dict scale_range: scale range, see :class:`AX_IVPS_SCALE_RANGE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_RANGE_T>`
    :returns: tuple[dict, int]

        - **coef_level** (*dict*) - see :class:`AX_IVPS_SCALE_COEF_LEVEL_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_COEF_LEVEL_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    coef_level = {}
    try:
        c_scale_range = AX_IVPS_SCALE_RANGE_T()
        c_scale_range.dict2struct(scale_range)

        c_coef_level = AX_IVPS_SCALE_COEF_LEVEL_T()

        libaxcl_ivps.AXCL_IVPS_GetScaleCoefLevelVpp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetScaleCoefLevelVpp.argtypes = [
            POINTER(AX_IVPS_SCALE_RANGE_T),
            POINTER(AX_IVPS_SCALE_COEF_LEVEL_T)
        ]

        ret = libaxcl_ivps.AXCL_IVPS_GetScaleCoefLevelVpp(byref(c_scale_range), byref(c_coef_level))
        if ret == AX_SUCCESS:
            coef_level = c_coef_level.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return coef_level, ret

def cmm_copy_vgp(src_phy_addr: int, dst_phy_addr: int, mem_size: int) -> int:
    """
    cmm copy vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CmmCopyVgp(AX_U64 nSrcPhyAddr, AX_U64 nDstPhyAddr, AX_U64 nMemSize)`
        **python**              `ret = axcl.ivps.cmm_copy_vgp(src_phy_addr, dst_phy_addr, mem_size)`
        ======================= =====================================================

    :param int src_phy_addr: src phy addr
    :param int dst_phy_addr: dst phy addr
    :param int mem_size: mem size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_CmmCopyVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CmmCopyVgp.argtypes = [c_uint64, c_uint64, c_uint64]
        ret = libaxcl_ivps.AXCL_IVPS_CmmCopyVgp(c_uint64(src_phy_addr), c_uint64(dst_phy_addr), c_uint64(mem_size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def csc_vgp(src: dict, dst: dict) -> int:
    """
    csc vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CscVgp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.csc_vgp(src, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure


    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        libaxcl_ivps.AXCL_IVPS_CscVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CscVgp.argtypes = [POINTER(AX_VIDEO_FRAME_T), POINTER(AX_VIDEO_FRAME_T)]
        ret = libaxcl_ivps.AXCL_IVPS_CscVgp(byref(c_src), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_vgp(src: dict, dst: dict, aspect_ratio: dict) -> int:
    """
    crop resize vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeVgp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio)`
        **python**              `ret = axcl.ivps.crop_resize_vgp(src, dst, aspect_ratio)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        libaxcl_ivps.AXCL_IVPS_CropResizeVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeVgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_ASPECT_RATIO_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_CropResizeVgp(byref(c_src), byref(c_dst), byref(c_aspect_ratio))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_v2_vgp(src: dict, box_list: list[dict], dst_list: list[dict], aspect_ratio: dict) -> int:
    """
    crop resize v2 vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeV2Vgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_IVPS_RECT_T tBox[], AX_U32 nCropNum, AX_VIDEO_FRAME_T *ptDst[], const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio)`
        **python**              `ret = axcl.ivps.crop_resize_v2_vgp(src, box_list, dst_list, aspect_ratio)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] box_list: box list, see :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`
    :param list[dict] dst_list: dst list, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:

        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        crop_num = len(box_list)

        c_box_list = (AX_IVPS_RECT_T * crop_num)()
        for idx, box in enumerate(box_list):
            c_box_list[idx].dict2struct(box)

        LP_AX_VIDEO_FRAME_T = POINTER(AX_VIDEO_FRAME_T)
        c_dst_array = (AX_VIDEO_FRAME_T * crop_num)()
        c_dstptr_array = (LP_AX_VIDEO_FRAME_T * crop_num)()
        for idx in range(crop_num):
            c_dst_array[idx].dict2struct(dst_list[idx])
            c_dstptr_array[idx] = cast(addressof(c_dst_array[idx]), LP_AX_VIDEO_FRAME_T)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        libaxcl_ivps.AXCL_IVPS_CropResizeV2Vgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeV2Vgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_RECT_T),
            c_uint32,
            POINTER(POINTER(AX_VIDEO_FRAME_T)),
            POINTER(AX_IVPS_ASPECT_RATIO_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_CropResizeV2Vgp(byref(c_src), c_box_list, c_uint32(crop_num), c_dstptr_array, byref(c_aspect_ratio))
        if ret == AX_SUCCESS:
            for idx in range(crop_num):
                dst_list[idx].update(c_dst_array[idx].struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def crop_resize_v4_vgp(src: dict, dst: dict, aspect_ratio: dict, scale_step: dict) -> int:
    """
    crop resize v4 vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_CropResizeV4Vgp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio, const AX_IVPS_SCALE_STEP_T *ptScaleStep)`
        **python**              `ret = axcl.ivps.crop_resize_v4_vgp(src, dst, aspect_ratio, scale_step)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict aspect_ratio: aspect ratio, see :class:`AX_IVPS_ASPECT_RATIO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ASPECT_RATIO_T>`
    :param dict scale_step: scale step, see :class:`AX_IVPS_SCALE_STEP_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_STEP_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_aspect_ratio = AX_IVPS_ASPECT_RATIO_T()
        c_aspect_ratio.dict2struct(aspect_ratio)

        c_scale_step = AX_IVPS_SCALE_STEP_T()
        c_scale_step.dict2struct(scale_step)

        libaxcl_ivps.AXCL_IVPS_CropResizeV4Vgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_CropResizeV4Vgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_ASPECT_RATIO_T),
            POINTER(AX_IVPS_SCALE_STEP_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_CropResizeV4Vgp(byref(c_src), byref(c_dst), byref(c_aspect_ratio), byref(c_scale_step))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def alpha_blending_vgp(src: dict, overlay: dict, offset: dict, alpha: int, dst: dict) -> int:
    """
    alpha blending vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_AlphaBlendingVgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_VIDEO_FRAME_T *ptOverlay, const AX_IVPS_POINT_T tOffset, AX_U8 nAlpha, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.alpha_blending_vgp(src, overlay, offset, alpha, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict overlay: overlay, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict offset: offset, see :class:`AX_IVPS_POINT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_T>`
    :param int alpha: alpha
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_overlay = AX_VIDEO_FRAME_T()
        c_overlay.dict2struct(overlay)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_offset = AX_IVPS_POINT_T()
        c_offset.dict2struct(offset)

        libaxcl_ivps.AXCL_IVPS_AlphaBlendingVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_AlphaBlendingVgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            AX_IVPS_POINT_T,
            c_uint8,
            POINTER(AX_VIDEO_FRAME_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_AlphaBlendingVgp(byref(c_src), byref(c_overlay), c_offset, c_uint8(alpha), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def alpha_blending_v2_vgp(src: dict, overlay: dict, offset: dict, alpha_lut: dict, dst: dict) -> int:
    """
    alpha blending v2 vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_AlphaBlendingV2Vgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_VIDEO_FRAME_T *ptOverlay, const AX_IVPS_POINT_T tOffset, const AX_IVPS_ALPHA_LUT_T *ptSpAlpha, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.alpha_blending_v2_vgp(src, overlay, offset, alpha_lut, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict overlay: overlay, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict offset: offset, see :class:`AX_IVPS_POINT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_T>`
    :param dict alpha_lut: alpha lut, see :class:`AX_IVPS_ALPHA_LUT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_ALPHA_LUT_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_overlay = AX_VIDEO_FRAME_T()
        c_overlay.dict2struct(overlay)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_offset = AX_IVPS_POINT_T()
        c_offset.dict2struct(offset)

        c_alpha_lut = AX_IVPS_ALPHA_LUT_T()
        c_alpha_lut.dict2struct(alpha_lut)

        libaxcl_ivps.AXCL_IVPS_AlphaBlendingV2Vgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_AlphaBlendingV2Vgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            AX_IVPS_POINT_T,
            POINTER(AX_IVPS_ALPHA_LUT_T),
            POINTER(AX_VIDEO_FRAME_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_AlphaBlendingV2Vgp(byref(c_src), byref(c_overlay), c_offset, byref(c_alpha_lut), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def alpha_blending_v3_vgp(src: dict, overlay: dict, dst: dict) -> int:
    """
    alpha blending v3 vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_AlphaBlendingV3Vgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_OVERLAY_T *ptOverlay, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.alpha_blending_v3_vgp(src, overlay, dst)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict overlay: overlay, see :class:`AX_OVERLAY_T <axcl.ax_global_type.AX_OVERLAY_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_overlay = AX_OVERLAY_T()
        c_overlay.dict2struct(overlay)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        libaxcl_ivps.AXCL_IVPS_AlphaBlendingV3Vgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_AlphaBlendingV3Vgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_OVERLAY_T),
            POINTER(AX_VIDEO_FRAME_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_AlphaBlendingV3Vgp(byref(c_src), byref(c_overlay), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def draw_osd_vgp(src: dict, bmp_list: list[dict]) -> int:
    """
    draw osd vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawOsdVgp(const AX_VIDEO_FRAME_T *ptFrame, const AX_OSD_BMP_ATTR_T arrBmp[], AX_U32 nNum)`
        **python**              `ret = axcl.ivps.draw_osd_vgp(src, bmp_list)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] bmp_list: bmp list, see :class:`AX_OSD_BMP_ATTR_T <axcl.ax_global_type.AX_OSD_BMP_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:

        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        num = len(bmp_list)

        c_bmp_list = (AX_OSD_BMP_ATTR_T * num)()
        for idx, bmp in enumerate(bmp_list):
            c_bmp_list[idx].dict2struct(bmp)

        libaxcl_ivps.AXCL_IVPS_DrawOsdVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawOsdVgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_OSD_BMP_ATTR_T),
            c_uint32
        ]
        ret = libaxcl_ivps.AXCL_IVPS_DrawOsdVgp(byref(c_src), c_bmp_list, c_uint32(num))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def draw_mosaic_vgp(src: dict, mosaic_list: list[dict]) -> int:
    """
    draw mosaic vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawMosaicVgp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_RGN_MOSAIC_T tMosaic[], AX_U32 nNum)`
        **python**              `ret = axcl.ivps.draw_mosaic_vgp(src, mosaic_list)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param list[dict] mosaic_list: mosaic list, see :class:`AX_IVPS_RGN_MOSAIC_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_MOSAIC_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:

        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        num = len(mosaic_list)

        c_mosaic_list = (AX_IVPS_RGN_MOSAIC_T * num)()
        for idx, mosaic in enumerate(mosaic_list):
            c_mosaic_list[idx].dict2struct(mosaic)

        libaxcl_ivps.AXCL_IVPS_DrawMosaicVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawMosaicVgp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_RGN_MOSAIC_T),
            c_uint32
        ]
        ret = libaxcl_ivps.AXCL_IVPS_DrawMosaicVgp(byref(c_src), c_mosaic_list, c_uint32(num))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def set_scale_coef_level_vgp(scale_range: dict, coef_level: dict) -> int:
    """
    set scale coef level vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_SetScaleCoefLevelVgp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, const AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel)`
        **python**              `ret = axcl.ivps.set_scale_coef_level_vgp(scale_range, coef_level)`
        ======================= =====================================================

    :param dict scale_range: scale range, see :class:`AX_IVPS_SCALE_RANGE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_RANGE_T>`
    :param dict coef_level: coef level, see :class:`AX_IVPS_SCALE_COEF_LEVEL_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_COEF_LEVEL_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure



    """
    ret = -1
    try:
        c_scale_range = AX_IVPS_SCALE_RANGE_T()
        c_scale_range.dict2struct(scale_range)

        c_coef_level = AX_IVPS_SCALE_COEF_LEVEL_T()
        c_coef_level.dict2struct(coef_level)

        libaxcl_ivps.AXCL_IVPS_SetScaleCoefLevelVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_SetScaleCoefLevelVgp.argtypes = [
            POINTER(AX_IVPS_SCALE_RANGE_T),
            POINTER(AX_IVPS_SCALE_COEF_LEVEL_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_SetScaleCoefLevelVgp(byref(c_scale_range), byref(c_coef_level))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def get_scale_coef_level_vgp(scale_range: dict) -> tuple[dict, int]:
    """
    get scale coef level vgp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GetScaleCoefLevelVgp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel)`
        **python**              `coef_level, ret = get_scale_coef_level_vgp(scale_range)`
        ======================= =====================================================

    :param dict scale_range: scale range, see :class:`AX_IVPS_SCALE_RANGE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_RANGE_T>`
    :returns: tuple[dict, int]

        - **coef_level** (*dict*) -  see :class:`AX_IVPS_SCALE_COEF_LEVEL_T <axcl.ivps.axcl_ivps_type.AX_IVPS_SCALE_COEF_LEVEL_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    coef_level = {}
    try:
        c_scale_range = AX_IVPS_SCALE_RANGE_T()
        c_scale_range.dict2struct(scale_range)

        c_coef_level = AX_IVPS_SCALE_COEF_LEVEL_T()

        libaxcl_ivps.AXCL_IVPS_GetScaleCoefLevelVgp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GetScaleCoefLevelVgp.argtypes = [
            POINTER(AX_IVPS_SCALE_RANGE_T),
            POINTER(AX_IVPS_SCALE_COEF_LEVEL_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_GetScaleCoefLevelVgp(byref(c_scale_range), byref(c_coef_level))
        if ret == AX_SUCCESS:
            coef_level = c_coef_level.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return coef_level, ret


def draw_line(canvas: dict, gdi_attr: dict, point_list: list[dict]) -> int:
    """
    draw line

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawLine(const AX_IVPS_RGN_CANVAS_INFO_T *ptCanvas, AX_IVPS_GDI_ATTR_T tAttr, const AX_IVPS_POINT_T tPoint[], AX_U32 nPointNum)`
        **python**              `ret = axcl.ivps.draw_line(canvas, gdi_attr, point_list)`
        ======================= =====================================================

    :param dict canvas: canvas, see :class:`AX_IVPS_RGN_CANVAS_INFO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_CANVAS_INFO_T>`
    :param dict gdi_attr: gdi attr, see :class:`AX_IVPS_GDI_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_GDI_ATTR_T>`
    :param list[dict] point_list: point list, see :class:`AX_IVPS_POINT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_canvas = AX_IVPS_RGN_CANVAS_INFO_T()
        c_canvas.dict2struct(canvas)

        c_gdi_attr = AX_IVPS_GDI_ATTR_T()
        c_gdi_attr.dict2struct(gdi_attr)

        point_num = len(point_list)

        c_pt_list = (AX_IVPS_POINT_T * point_num)()
        for idx, pt in enumerate(point_list):
            c_pt_list[idx].dict2struct(pt)

        libaxcl_ivps.AXCL_IVPS_DrawLine.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawLine.argtypes = [
            POINTER(AX_IVPS_RGN_CANVAS_INFO_T),
            AX_IVPS_GDI_ATTR_T,
            POINTER(AX_IVPS_POINT_T),
            c_uint32
        ]
        ret = libaxcl_ivps.AXCL_IVPS_DrawLine(byref(c_canvas), c_gdi_attr, c_pt_list, c_uint32(point_num))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def draw_polygon(canvas: dict, gdi_attr: dict, point_list: list[dict]) -> int:
    """
    draw polygon

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawPolygon(const AX_IVPS_RGN_CANVAS_INFO_T *ptCanvas, AX_IVPS_GDI_ATTR_T tAttr, const AX_IVPS_POINT_T tPoint[], AX_U32 nPointNum)`
        **python**              `ret = axcl.ivps.draw_polygon(canvas, gdi_attr, point_list)`
        ======================= =====================================================

    :param dict canvas: canvas, see :class:`AX_IVPS_RGN_CANVAS_INFO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_CANVAS_INFO_T>`
    :param dict gdi_attr: gdi attr, see :class:`AX_IVPS_GDI_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_GDI_ATTR_T>`
    :param list[dict] point_list: point list, see :class:`AX_IVPS_POINT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_canvas = AX_IVPS_RGN_CANVAS_INFO_T()
        c_canvas.dict2struct(canvas)

        c_gdi_attr = AX_IVPS_GDI_ATTR_T()
        c_gdi_attr.dict2struct(gdi_attr)

        point_num = len(point_list)

        c_pt_list = (AX_IVPS_POINT_T * point_num)()
        for idx, pt in enumerate(point_list):
            c_pt_list[idx].dict2struct(pt)

        libaxcl_ivps.AXCL_IVPS_DrawPolygon.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawPolygon.argtypes = [
            POINTER(AX_IVPS_RGN_CANVAS_INFO_T),
            AX_IVPS_GDI_ATTR_T,
            POINTER(AX_IVPS_POINT_T),
            c_uint32
        ]
        ret = libaxcl_ivps.AXCL_IVPS_DrawPolygon(byref(c_canvas), c_gdi_attr, c_pt_list, c_uint32(point_num))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def draw_rect(canvas: dict, gdi_attr: dict, rect: dict) -> int:
    """
    draw rect

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_DrawRect(const AX_IVPS_RGN_CANVAS_INFO_T *ptCanvas, AX_IVPS_GDI_ATTR_T tAttr, AX_IVPS_RECT_T tRect)`
        **python**              `ret = axcl.ivps.draw_rect(canvas, gdi_attr, rect)`
        ======================= =====================================================

    :param dict canvas: canvas, see :class:`AX_IVPS_RGN_CANVAS_INFO_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RGN_CANVAS_INFO_T>`
    :param dict gdi_attr: gdi attr, see :class:`AX_IVPS_GDI_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_GDI_ATTR_T>`
    :param dict rect: rect, see :class:`AX_IVPS_RECT_T <axcl.ivps.axcl_ivps_type.AX_IVPS_RECT_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_canvas = AX_IVPS_RGN_CANVAS_INFO_T()
        c_canvas.dict2struct(canvas)

        c_gdi_attr = AX_IVPS_GDI_ATTR_T()
        c_gdi_attr.dict2struct(gdi_attr)

        c_rect = AX_IVPS_RECT_T()
        c_rect.dict2struct(rect)

        libaxcl_ivps.AXCL_IVPS_DrawRect.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_DrawRect.argtypes = [
            POINTER(AX_IVPS_RGN_CANVAS_INFO_T),
            AX_IVPS_GDI_ATTR_T,
            AX_IVPS_RECT_T
        ]
        ret = libaxcl_ivps.AXCL_IVPS_DrawRect(byref(c_canvas), c_gdi_attr, c_rect)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def dewarp(src: dict, dst: dict, dewarp_attr: dict) -> int:
    """
    dewarp

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_Dewarp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_DEWARP_ATTR_T *ptAttr)`
        **python**              `ret = axcl.ivps.dewarp(src, dst, dewarp_attr)`
        ======================= =====================================================

    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dewarp_attr: dewarp attr, see :class:`AX_IVPS_DEWARP_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_DEWARP_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        c_dewarp_attr = AX_IVPS_DEWARP_ATTR_T()
        c_dewarp_attr.dict2struct(dewarp_attr)

        libaxcl_ivps.AXCL_IVPS_Dewarp.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_Dewarp.argtypes = [
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_IVPS_DEWARP_ATTR_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_Dewarp(byref(c_src), byref(c_dst), byref(c_dewarp_attr))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def pyra_lite_gen(src_pyra: dict, dst_pyra: dict, mask: bool) -> int:
    """
    pyra lite gen

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_PyraLite_Gen(const AX_PYRA_FRAME_T *tSrcFrame, AX_PYRA_FRAME_T *tDstFrame, AX_BOOL bMaskFlag)`
        **python**              `ret = axcl.ivps.pyra_lite_gen(src_pyra, dst_pyra, mask)`
        ======================= =====================================================

    :param dict src_pyra: src pyra, see :class:`AX_PYRA_FRAME_T <axcl.ax_global_type.AX_PYRA_FRAME_T>`
    :param dict dst_pyra: dst pyra, see :class:`AX_PYRA_FRAME_T <axcl.ax_global_type.AX_PYRA_FRAME_T>`
    :param bool mask:
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_PYRA_FRAME_T()
        c_src.dict2struct(src_pyra)

        c_dst = AX_PYRA_FRAME_T()
        c_dst.dict2struct(dst_pyra)

        libaxcl_ivps.AXCL_PyraLite_Gen.restype = c_int32
        libaxcl_ivps.AXCL_PyraLite_Gen.argtypes = [
            POINTER(AX_PYRA_FRAME_T),
            POINTER(AX_PYRA_FRAME_T),
            AX_BOOL
        ]
        ret = libaxcl_ivps.AXCL_PyraLite_Gen(byref(c_src), byref(c_dst), AX_BOOL(mask))
        if ret == AX_SUCCESS:
            dst_pyra.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def pyra_lite_rcn(src_pyra: dict, dst_pyra: dict, bottom: bool) -> int:
    """
    pyra lite rcn

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_PyraLite_Rcn(const AX_PYRA_FRAME_T *tSrcFrame, AX_PYRA_FRAME_T *tDstFrame, AX_BOOL bBottom)`
        **python**              `ret = axcl.ivps.pyra_lite_rcn(src_pyra, dst_pyra, bottom)`
        ======================= =====================================================

    :param dict src_pyra: src pyra, see :class:`AX_PYRA_FRAME_T <axcl.ax_global_type.AX_PYRA_FRAME_T>`
    :param dict dst_pyra: dst pyra, see :class:`AX_PYRA_FRAME_T <axcl.ax_global_type.AX_PYRA_FRAME_T>`
    :param bool bottom:
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_PYRA_FRAME_T()
        c_src.dict2struct(src_pyra)

        c_dst = AX_PYRA_FRAME_T()
        c_dst.dict2struct(dst_pyra)

        libaxcl_ivps.AXCL_PyraLite_Rcn.restype = c_int32
        libaxcl_ivps.AXCL_PyraLite_Rcn.argtypes = [
            POINTER(AX_PYRA_FRAME_T),
            POINTER(AX_PYRA_FRAME_T),
            AX_BOOL
        ]
        ret = libaxcl_ivps.AXCL_PyraLite_Rcn(byref(c_src), byref(c_dst), AX_BOOL(bottom))
        if ret == AX_SUCCESS:
            dst_pyra.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def gdc_work_create() -> tuple[int, int]:
    """
    gdc work create

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GdcWorkCreate(GDC_HANDLE *pGdcHandle)`
        **python**              `gdc_handle, ret = gdc_work_create()`
        ======================= =====================================================

    :returns: tuple[int, int]

        - **gdc_handle** (*dict*) - gdc handle
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    c_gdc_handle = GDC_HANDLE(0)
    try:
        libaxcl_ivps.AXCL_IVPS_GdcWorkCreate.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GdcWorkCreate.argtypes = [POINTER(GDC_HANDLE)]
        ret = libaxcl_ivps.AXCL_IVPS_GdcWorkCreate(byref(c_gdc_handle))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_gdc_handle.value, ret

def gdc_work_attr_set(gdc_handle: int, gdc_attr: dict) -> int:
    """
    gdc work attr set

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GdcWorkAttrSet(GDC_HANDLE nGdcHandle, const AX_IVPS_GDC_ATTR_T *ptGdcAttr)`
        **python**              `ret = axcl.ivps.gdc_work_attr_set(gdc_handle, gdc_attr)`
        ======================= =====================================================

    :param int gdc_handle: gdc handle
    :param dict gdc_attr: gdc attr, see :class:`AX_IVPS_GDC_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_GDC_ATTR_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_gdc_attr = AX_IVPS_GDC_ATTR_T()
        c_gdc_attr.dict2struct(gdc_attr)

        libaxcl_ivps.AXCL_IVPS_GdcWorkAttrSet.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GdcWorkAttrSet.argtypes = [
            GDC_HANDLE,
            POINTER(AX_IVPS_GDC_ATTR_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_GdcWorkAttrSet(gdc_handle, byref(c_gdc_attr))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def gdc_work_run(gdc_handle: int, src: dict, dst: dict) -> int:
    """
    gdc work run

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GdcWorkRun(GDC_HANDLE nGdcHandle, const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst)`
        **python**              `ret = axcl.ivps.gdc_work_run(gdc_handle, src, dst)`
        ======================= =====================================================

    :param int gdc_handle: gdc handle
    :param dict src: src, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :param dict dst: dst, see :class:`AX_VIDEO_FRAME_T <axcl.ax_global_type.AX_VIDEO_FRAME_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        c_src = AX_VIDEO_FRAME_T()
        c_src.dict2struct(src)

        c_dst = AX_VIDEO_FRAME_T()
        c_dst.dict2struct(dst)

        libaxcl_ivps.AXCL_IVPS_GdcWorkRun.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GdcWorkRun.argtypes = [
            GDC_HANDLE,
            POINTER(AX_VIDEO_FRAME_T),
            POINTER(AX_VIDEO_FRAME_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_GdcWorkRun(gdc_handle, byref(c_src), byref(c_dst))
        if ret == AX_SUCCESS:
            dst.update(c_dst.struct2dict())
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def gdc_work_destroy(gdc_handle: int) -> int:
    """
    gdc work destroy

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_GdcWorkDestroy(GDC_HANDLE nGdcHandle)`
        **python**              `ret = axcl.ivps.gdc_work_destroy(gdc_handle)`
        ======================= =====================================================

    :param int gdc_handle: gdc handle
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure

    """
    ret = -1
    try:
        libaxcl_ivps.AXCL_IVPS_GdcWorkDestroy.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_GdcWorkDestroy.argtypes = [GDC_HANDLE]
        ret = libaxcl_ivps.AXCL_IVPS_GdcWorkDestroy(gdc_handle)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret

def fisheye_point_query_dst2src(dst_point: dict, input_w: int, input_h: int, rgn_idx: int, fisheye_attr: dict) -> tuple[dict, int]:
    """
    fisheye point query dst2src

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_FisheyePointQueryDst2Src(AX_IVPS_POINT_NICE_T *ptSrcPoint, const AX_IVPS_POINT_NICE_T *ptDstPoint, AX_U16 nInputW, AX_U16 nInputH, AX_U8 nRgnIdx, const AX_IVPS_FISHEYE_ATTR_T *ptFisheyeAttr)`
        **python**              `src_point, ret = fisheye_point_query_dst2src(dst_point, input_w, input_h, rgn_idx, fisheye_attr)`
        ======================= =====================================================

    :param dict dst_point: dst point, see :class:`AX_IVPS_POINT_NICE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_NICE_T>`
    :param int input_w: input w
    :param int input_h: input h
    :param int rgn_idx: rgn idx
    :param dict fisheye_attr: fisheye attr, see :class:`AX_IVPS_FISHEYE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_FISHEYE_ATTR_T>`
    :returns: tuple[dict, int]

        - **src_point** (*dict*) -  see :class:`AX_IVPS_POINT_NICE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_NICE_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    src_point = {}
    try:
        c_src_point = AX_IVPS_POINT_NICE_T()

        c_dst_point = AX_IVPS_POINT_NICE_T()
        c_dst_point.dict2struct(dst_point)

        c_fisheye_attr = AX_IVPS_FISHEYE_ATTR_T()
        c_fisheye_attr.dict2struct(fisheye_attr)

        libaxcl_ivps.AXCL_IVPS_FisheyePointQueryDst2Src.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_FisheyePointQueryDst2Src.argtypes = [
            POINTER(AX_IVPS_POINT_NICE_T),
            POINTER(AX_IVPS_POINT_NICE_T),
            c_uint16,
            c_uint16,
            c_uint8,
            POINTER(AX_IVPS_FISHEYE_ATTR_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_FisheyePointQueryDst2Src(
            byref(c_src_point), byref(c_dst_point), c_uint16(input_w), c_uint16(input_h), c_uint8(rgn_idx), byref(c_fisheye_attr)
        )
        if ret == AX_SUCCESS:
            src_point = c_dst_point.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return src_point, ret

def fisheye_point_query_src2dst(src_point: dict, input_w: int, input_h: int, rgn_idx: int, fisheye_attr: dict) -> tuple[dict, int]:
    """
    fisheye point query src2dst

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVPS_FisheyePointQuerySrc2Dst(AX_IVPS_POINT_NICE_T *ptDstPoint, const AX_IVPS_POINT_NICE_T *ptSrcPoint, AX_U16 nInputW, AX_U16 nInputH, AX_U8 nRgnIdx, const AX_IVPS_FISHEYE_ATTR_T *ptFisheyeAttr)`
        **python**              `dst_point, ret = fisheye_point_query_src2dst(src_point, input_w, input_h, rgn_idx, fisheye_attr)`
        ======================= =====================================================

    :param dict src_point: src point, see :class:`AX_IVPS_POINT_NICE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_NICE_T>`
    :param int input_w: input w
    :param int input_h: input h
    :param int rgn_idx: rgn idx
    :param dict fisheye_attr: fisheye attr, see :class:`AX_IVPS_FISHEYE_ATTR_T <axcl.ivps.axcl_ivps_type.AX_IVPS_FISHEYE_ATTR_T>`
    :returns: tuple[dict, int]

        - **dst_point** (*dict*) -  see :class:`AX_IVPS_POINT_NICE_T <axcl.ivps.axcl_ivps_type.AX_IVPS_POINT_NICE_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    """
    ret = -1
    try:
        c_src_point = AX_IVPS_POINT_NICE_T()
        c_src_point.dict2struct(src_point)

        c_dst_point = AX_IVPS_POINT_NICE_T()

        c_fisheye_attr = AX_IVPS_FISHEYE_ATTR_T()
        c_fisheye_attr.dict2struct(fisheye_attr)

        libaxcl_ivps.AXCL_IVPS_FisheyePointQuerySrc2Dst.restype = c_int32
        libaxcl_ivps.AXCL_IVPS_FisheyePointQuerySrc2Dst.argtypes = [
            POINTER(AX_IVPS_POINT_NICE_T),
            POINTER(AX_IVPS_POINT_NICE_T),
            c_uint16,
            c_uint16,
            c_uint8,
            POINTER(AX_IVPS_FISHEYE_ATTR_T)
        ]
        ret = libaxcl_ivps.AXCL_IVPS_FisheyePointQuerySrc2Dst(
            byref(c_dst_point), byref(c_src_point), c_uint16(input_w), c_uint16(input_h), c_uint8(rgn_idx), byref(c_fisheye_attr)
        )
        if ret == AX_SUCCESS:
            dst_point = c_dst_point.struct2dict()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return dst_point, ret