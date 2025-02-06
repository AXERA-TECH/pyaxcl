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

from axcl.lib.axcl_lib import libaxcl_ive
from axcl.ive.axcl_ive_type import *
from axcl.ive.axcl_ive_dict import *
from axcl.ax_global_type import *
from axcl.utils.axcl_logger import *


def init() -> int:
    """
    IVE module initialize

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Init(AX_VOID);`
        **python**              `ret = axcl.ive.init()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_ive.AXCL_IVE_Init.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Init.argtypes = None
        ret = libaxcl_ive.AXCL_IVE_Init()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def exit() -> int:
    """
    IVE module exit

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID AX_IVE_Exit(AX_VOID);`
        **python**              `ret = axcl.ive.exit()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = 0
    try:
        libaxcl_ive.AXCL_IVE_Exit.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Exit.argtypes = None
        libaxcl_ive.AXCL_IVE_Exit()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def query(handle: int, block: bool) -> tuple[int, int]:
    """
    This API is used to query the status of a called function by using the returned IveHandle of the function.
    In block mode, the system waits until the function that is being queried is called.
    In non-block mode, the current status is queried and no action is taken.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Query(AX_IVE_HANDLE IveHandle, AX_BOOL *pbFinish, AX_BOOL bBlock);`
        **python**              `is_finish, ret = axcl.ive.query(handle, block)`
        ======================= =====================================================

    :param int handle: IveHandle of a called function. It is entered by users.
    :param bool block: Flag indicating the block mode or non-block mode.
    :returns: tuple[int, int]

        - **is_finish** (*bool*) - Returned status.
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_finish = AX_BOOL(0)
    try:
        libaxcl_ive.AXCL_IVE_Query.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Query.argtypes = [
            AX_IVE_HANDLE,
            POINTER(AX_BOOL),
            AX_BOOL
        ]
        c_handle = handle
        c_block = AX_BOOL(1 if block else 0)
        ret = libaxcl_ive.AXCL_IVE_Query(c_handle, byref(c_finish), c_block)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return True if c_finish else False, ret


def dma(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Direct memory access (DMA):
        - Direct memory copy;
        - Copy with interval bytes;
        - Memset using 3 bytes;
        - Memset using 8 bytes.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_DMA(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_DATA_T *pstSrc, AX_IVE_DST_DATA_T *pstDst, AX_IVE_DMA_CTRL_T *pstDmaCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = dma(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source data.The input data is treated as U8C1 data. :class:`AX_IVE_SRC_DATA_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_DATA_T>` to extract ive src data information.
    :param dict dst[IN/OUT]: Output result data. :class:`AX_IVE_DST_DATA_T <axcl.ive.axcl_ive_type.AX_IVE_DST_DATA_T>` to extract ive dst data information.
    :param dict ctrl: Control parameter of dma. :class:`AX_IVE_DMA_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_DMA_CTRL_T>` to extract ive dma control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x1 pixels to 1920x1080 pixels.
        - The stride must be 16-byte-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_DATA_T()
    c_dst = AX_IVE_DST_DATA_T()
    c_ctrl = AX_IVE_DMA_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_DMA.restype = AX_S32
        libaxcl_ive.AXCL_IVE_DMA.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_DATA_T),
            POINTER(AX_IVE_DST_DATA_T),
            POINTER(AX_IVE_DMA_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_data(src, c_src)
        dict_to_ax_ive_data(dst, c_dst)
        dict_to_ax_ive_dma_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_DMA(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_data_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def add(src1: dict, src2: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Two gray images' Add operation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Add(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_ADD_CTRL_T *pstAddCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = add(src1, src2, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src1: Augend of the input source. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Addend of the input source. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result of src1 plus src2. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of add. :class:`AX_IVE_ADD_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_ADD_CTRL_T>` to extract ive add control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
        - The types, widths, heights of two input sources must be the same.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_ADD_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Add.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Add.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_ADD_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_add_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Add(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def sub(src1: dict, src2: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Two gray images' Sub operation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Sub(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_SUB_CTRL_T *pstSubCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = sub(src1, src2, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src1: Minuend of the input source. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Subtrahend of the input source. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result of src1 minus src2. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of sub. :class:`AX_IVE_SUB_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_SUB_CTRL_T>` to extract ive sub control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
        - The types, widths, heights of two input sources must be the same.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_SUB_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Sub.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Sub.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_SUB_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_sub_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Sub(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def ive_and(src1: dict, src2: dict, dst: dict, instant: bool) -> tuple[int, int]:
    """
    Binary images' And operation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_And(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant);`
        **python**              `handle, ret = ive_and(src1, src2, dst, instant)`
        ======================= =====================================================

    :param dict src1: The input source1. Only U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: The input source2. Only U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result of " src1 & src2 ". :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
        - The types, widths, heights of two input sources must be the same.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    try:
        libaxcl_ive.AXCL_IVE_And.restype = AX_S32
        libaxcl_ive.AXCL_IVE_And.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst, c_dst)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_And(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def ive_or(src1: dict, src2: dict, dst: dict, instant: bool) -> tuple[int, int]:
    """
    Two binary images' Or operation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Or(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant);`
        **python**              `handle, ret = ive_or(src1, src2, dst, instant)`
        ======================= =====================================================

    :param dict src1: Input source1. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Input source2. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result src1 or src2. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
        - The types, widths, heights of two input sources must be the same.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    try:
        libaxcl_ive.AXCL_IVE_Or.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Or.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst, c_dst)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Or(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def xor(src1: dict, src2: dict, dst: dict, instant: bool) -> tuple[int, int]:
    """
    Two binary images' Xor operation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Xor(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant);`
        **python**              `handle, ret = xor(src1, src2, dst, instant)`
        ======================= =====================================================

    :param dict src1: The input source1. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: The input source2. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result src1 xor src2. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
        - The types, widths, heights of two input sources must be the same.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    try:
        libaxcl_ive.AXCL_IVE_Xor.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Xor.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst, c_dst)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Xor(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def mse(src1: dict, src2: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Two gray images' Mse operation.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Mse(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_MSE_CTRL_T *pstMseCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = mse(src1, src2, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src1: Minuend of the input source. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Subtrahend of the input source. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result of src1 mse src2. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of mse. :class:`AX_IVE_MSE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_MSE_CTRL_T>` to extract ive mse control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
        - The types, widths, heights of two input sources must be the same.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_MSE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Mse.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Mse.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_MSE_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_mse_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Mse(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def canny_hys_edge(src1: dict, src2: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    The first part of canny Edge detection. Including step: gradient calculation, magnitude and angle calculation, hysteresis threshold, NMS(Non-Maximum Suppression).

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CannyHysEdge(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_HYS_EDGE_CTRL_T *pstCannyHysEdgeCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = canny_hys_edge(src1, src2, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src1: Input source1. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Input source2. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of hys edge. :class:`AX_IVE_HYS_EDGE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_HYS_EDGE_CTRL_T>` to extract ive hys edge control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1024 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_HYS_EDGE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CannyHysEdge.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CannyHysEdge.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_HYS_EDGE_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_hys_edge_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CannyHysEdge(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def canny_edge(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    The second part of canny Edge detection: trace strong edge by weak edge.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CannyEdge(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_CANNY_EDGE_CTRL_T *pstCannyEdgeCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = canny_hys_edge(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source. Only the U8C1 format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of canny edge. :class:`AX_IVE_CANNY_EDGE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_CANNY_EDGE_CTRL_T>` to extract ive canny edge control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1024 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_CANNY_EDGE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CannyEdge.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CannyEdge.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_CANNY_EDGE_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_canny_edge_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CannyEdge(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def ccl(src: dict, dst: dict, blob: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Connected Component Labeling. Only 8-Connected method is supported.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CCL(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_DST_MEM_INFO_T *pstBlob, AX_IVE_CCL_CTRL_T *pstCclCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = ccl(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source. Only the U8C1 format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result of label. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict blob[IN/OUT]: Output result of detected region. :class:`AX_IVE_DST_MEM_INFO_T <axcl.ive.axcl_ive_type.AX_IVE_DST_MEM_INFO_T>` to extract ive memory information.
    :param dict ctrl: Control parameter of ccl. :class:`AX_IVE_CCL_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_CCL_CTRL_T>` to extract ive ccl control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1280x720 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_blob = AX_IVE_DST_MEM_INFO_T()
    c_ctrl = AX_IVE_CCL_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CCL.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CCL.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_DST_MEM_INFO_T),
            POINTER(AX_IVE_CCL_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_mem_info(blob, c_blob)
        dict_to_ax_ive_ccl_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CCL(byref(c_handle), byref(c_src), byref(c_dst), byref(c_blob), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
        ax_ive_mem_info_to_dict(c_blob, blob)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def erode(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    5x5 template erode. Only the U8C1 binary image input is supported.Or else the result is not correct.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Erode(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_ERODE_CTRL_T *pstErodeCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = erode(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input binary image, which consists of 0 or 255. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of erode. :class:`AX_IVE_ERODE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_ERODE_CTRL_T>` to extract ive erode control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1024 pixels.
        - The stride must be 16-pixel-aligned.
        - The input value, output value, and mask value must be 0 or 255.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_ERODE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Erode.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Erode.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_ERODE_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_erode_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Erode(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def dilate(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    5x5 template dilate. Only the U8C1 binary image input is supported.Or else the result is not expected.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Dilate(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_DILATE_CTRL_T *pstDilateCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = dilate(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input binary image, which consists of 0 or 255. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of dilate. :class:`AX_IVE_ERODE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_ERODE_CTRL_T>` to extract ive dilate control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1024 pixels.
        - The stride must be 16-pixel-aligned.
        - The input value, output value, and mask value must be 0 or 255.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_DILATE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Dilate.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Dilate.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_DILATE_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_dilate_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Dilate(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def filter(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    5x5 template filter.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Filter(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_FILTER_CTRL_T *pstFltCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = filter(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source data. The U8C1, SP420 and SP422 input formats are supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result, with same type of src. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of filter. :class:`AX_IVE_FILTER_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_FILTER_CTRL_T>` to extract ive filter control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1024 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_FILTER_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Filter.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Filter.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_FILTER_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_filter_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Filter(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def hist(src: dict, dst: dict, instant: bool) -> tuple[int, int]:
    """
    Calculate the input gray image's histogram.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Hist(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_MEM_INFO_T *pstDst, AX_BOOL bInstant);`
        **python**              `handle, ret = hist(src, dst, instant)`
        ======================= =====================================================

    :param dict src: Input source data. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_MEM_INFO_T()
    try:
        libaxcl_ive.AXCL_IVE_Hist.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Hist.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_MEM_INFO_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_mem_info(dst, c_dst)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Hist(byref(c_handle), byref(c_src), byref(c_dst), c_instant)
        ax_ive_mem_info_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def equalize_hist(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Enhance the input image's contrast through histogram equalization.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_EqualizeHist(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_MEM_INFO_T *pstDst, AX_IVE_EQUALIZE_HIST_CTRL_T *pstEqualizeHistCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = equalize_hist(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source. Only U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of histogram equalization. :class:`AX_IVE_EQUALIZEHIST_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_EQUALIZEHIST_CTRL_T>` to extract ive histogram equalization control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_MEM_INFO_T()
    c_ctrl = AX_IVE_EQUALIZE_HIST_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_EqualizeHist.restype = AX_S32
        libaxcl_ive.AXCL_IVE_EqualizeHist.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_MEM_INFO_T),
            POINTER(AX_IVE_EQUALIZE_HIST_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_mem_info(dst, c_dst)
        dict_to_ax_ive_equalize_hist_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_EqualizeHist(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_mem_info_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def integ(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Calculate the input gray image's integral image.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Integ(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_INTEG_CTRL_T *pstIntegCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = integ(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source data. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result.Can be U32C1 or U64C1, relied on the control parameter. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of integ. :class:`AX_IVE_INTEG_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_INTEG_CTRL_T>` to extract ive integ control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x16 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
        - The pixel can be 32bit or 64 bit relied on the control parameter.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_INTEG_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Integ.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Integ.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_INTEG_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_integ_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Integ(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def mag_and_ang(src1: dict, src2: dict, dst_mag: dict, dst_ang: dict, instant: bool) -> tuple[int, int]:
    """
    MagAndAng is used to extract the edge information.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_MagAndAng(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pstDstMag, AX_IVE_DST_IMAGE_T *pstDstAng, AX_BOOL bInstant);`
        **python**              `handle, ret = mag_and_ang(src1, src2, dst_mag, dst_ang, instant)`
        ======================= =====================================================

    :param dict src1: Input source data. Input source1 data. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Input source data. Input source2 data. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst_mag[IN/OUT]: Output magnitude. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict dst_ang[IN/OUT]: Output angle. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
        - If the output mode is set to magnitude only, this item can be set to null.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1024 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst_mag = AX_IVE_DST_IMAGE_T()
    c_dst_ang = AX_IVE_DST_IMAGE_T()
    try:
        libaxcl_ive.AXCL_IVE_MagAndAng.restype = AX_S32
        libaxcl_ive.AXCL_IVE_MagAndAng.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_image(dst_mag, c_dst_mag)
        dict_to_ax_ive_image(dst_ang, c_dst_ang)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_MagAndAng(byref(c_handle), byref(c_src1), byref(c_src2), byref(c_dst_mag), byref(c_dst_ang), c_instant)
        ax_ive_image_to_dict(c_dst_mag, dst_mag)
        ax_ive_image_to_dict(c_dst_ang, dst_ang)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def sobel(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    SOBEL is used to extract the gradient information.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Sobel(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_SOBEL_CTRL_T *pstSobelCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = sobel(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source data. Only the U8C1 input image is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: The result of input image filtered by the input mask. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of sobel. :class:`AX_IVE_SOBEL_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_SOBEL_CTRL_T>` to extract ive sobel control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1024 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_SOBEL_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Sobel.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Sobel.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_SOBEL_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_sobel_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Sobel(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def gmm(src: dict, dst_fg: dict, dst_bg: dict, model: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Separate foreground and background using GMM(Gaussian Mixture Model) method; Gray or RGB GMM are supported.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_GMM(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstFg, AX_IVE_DST_IMAGE_T *pstBg, AX_IVE_MEM_INFO_T *pstModel, AX_IVE_GMM_CTRL_T *pstGmmCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = gmm(src, dst_fg, dst_bg, model, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source. Only support U8C1 or U8C3_PACKAGE input. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst_fg[IN/OUT]: Output foreground (Binary) image. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict dst_bg[IN/OUT]: Output background image. With the same type of src. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict model: Model data. :class:`AX_IVE_MEM_INFO_T <axcl.ive.axcl_ive_type.AX_IVE_MEM_INFO_T>` to extract ive memory information.
    :param dict ctrl: Control parameter of gmm. :class:`AX_IVE_GMM_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_GMM_CTRL_T>` to extract ive gmm control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1280x720 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst_fg = AX_IVE_DST_IMAGE_T()
    c_dst_bg = AX_IVE_DST_IMAGE_T()
    c_model = AX_IVE_MEM_INFO_T()
    c_ctrl = AX_IVE_GMM_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_GMM.restype = AX_S32
        libaxcl_ive.AXCL_IVE_GMM.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_MEM_INFO_T),
            POINTER(AX_IVE_GMM_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst_fg, c_dst_fg)
        dict_to_ax_ive_image(dst_bg, c_dst_bg)
        dict_to_ax_ive_mem_info(model, c_model)
        dict_to_ax_ive_gmm_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_GMM(byref(c_handle), byref(c_src), byref(c_dst_fg), byref(c_dst_bg), byref(c_model), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst_fg, dst_fg)
        ax_ive_image_to_dict(c_dst_bg, dst_bg)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def gmm2(src: dict, dst_fg: dict, dst_bg: dict, model: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Separate foreground and background using GMM(Gaussian Mixture Model) method; Gray or RGB GMM are supported.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_GMM2(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstFg, AX_IVE_DST_IMAGE_T *pstBg, AX_IVE_MEM_INFO_T *pstModel, AX_IVE_GMM2_CTRL_T *pstGmm2Ctrl, AX_BOOL bInstant);`
        **python**              `handle, ret = gmm2(src, dst_fg, dst_bg, model, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source. Only U8C1 or U8C3_PACKAGE input are supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst_fg[IN/OUT]: Output foreground (Binary) image. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict dst_bg[IN/OUT]: Output background image. With same type of src. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict model: Model data. :class:`AX_IVE_MEM_INFO_T <axcl.ive.axcl_ive_type.AX_IVE_MEM_INFO_T>` to extract ive memory information.
    :param dict ctrl: Control parameter of gmm2. :class:`AX_IVE_GMM2_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_GMM2_CTRL_T>` to extract ive gmm2 control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1280x720 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst_fg = AX_IVE_DST_IMAGE_T()
    c_dst_bg = AX_IVE_DST_IMAGE_T()
    c_model = AX_IVE_MEM_INFO_T()
    c_ctrl = AX_IVE_GMM2_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_GMM2.restype = AX_S32
        libaxcl_ive.AXCL_IVE_GMM2.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_MEM_INFO_T),
            POINTER(AX_IVE_GMM2_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst_fg, c_dst_fg)
        dict_to_ax_ive_image(dst_bg, c_dst_bg)
        dict_to_ax_ive_mem_info(model, c_model)
        dict_to_ax_ive_gmm2_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_GMM2(byref(c_handle), byref(c_src), byref(c_dst_fg), byref(c_dst_bg), byref(c_model), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst_fg, dst_fg)
        ax_ive_image_to_dict(c_dst_bg, dst_bg)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def thresh(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Thresh operation to the input image.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_Thresh(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_THRESH_CTRL_T *pstThrCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = thresh(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source data. Only the U8C1 input format is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of thresh. :class:`AX_IVE_THRESH_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_THRESH_CTRL_T>` to extract ive thresh control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_THRESH_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_Thresh.restype = AX_S32
        libaxcl_ive.AXCL_IVE_Thresh.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_THRESH_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_thresh_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_Thresh(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def ive_16bit_to_8bit(src: dict, dst: dict, ctrl: dict, instant: bool) -> tuple[int, int]:
    """
    Scale the input 16bit data to the output 8bit data.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_16BitTo8Bit(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_16BIT_TO_8BIT_CTRL_T *pst16BitTo8BitCtrl, AX_BOOL bInstant);`
        **python**              `handle, ret = ive_16bit_to_8bit(src, dst, ctrl, instant)`
        ======================= =====================================================

    :param dict src: Input source data. Only U16C1/S16C1 input is supported. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param dict ctrl: Control parameter of 16bit_to_8bit. :class:`AX_IVE_16BITTO8BIT_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_16BITTO8BIT_CTRL_T>` to extract ive 16bit_to_8bit control information.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True.
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task.
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 64x64 pixels to 1920x1080 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_DST_IMAGE_T()
    c_ctrl = AX_IVE_16BIT_TO_8BIT_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_16BitTo8Bit.restype = AX_S32
        libaxcl_ive.AXCL_IVE_16BitTo8Bit.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            POINTER(AX_IVE_16BIT_TO_8BIT_CTRL_T),
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        dict_to_ax_ive_16bit_to_8bit_ctrl(ctrl, c_ctrl)
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_16BitTo8Bit(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_instant)
        ax_ive_image_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def crop_image(src: dict, dst_list: list[dict], box_list: list[dict], ctrl: dict, engine: int, instant: bool) -> tuple[int, int]:
    """
    Crop image, support crop output multiple images.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CropImage(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pastDst[], AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_IMAGE_CTRL_T *pstCropImageCtrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);`
        **python**              `handle, ret = crop_image(src, dst_list, box_list, ctrl, engine, instant)`
        ======================= =====================================================

    :param dict src: Input source. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param list[dict] dst_list[IN/OUT]: Output result list. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param list[dict] box_list: Input crop region list. :class:`AX_IVE_RECT_U16_T <axcl.ive.axcl_ive_type.AX_IVE_RECT_U16_T>` to extract ive rect information.
    :param dict ctrl: Control parameter of crop image. :class:`AX_IVE_CROP_IMAGE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_CROP_IMAGE_CTRL_T>` to extract ive crop image control information.
    :param int engine: Hardware engine choise. :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task. (Reserved)
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x32 pixels to 4096x8192 pixels for VGP or VPP, from 32x1 pixels to 1920x1080 pixels for IVE.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = (POINTER(AX_IVE_DST_IMAGE_T) * len(dst_list))()
    c_box = (POINTER(AX_IVE_RECT_U16_T) * len(box_list))()
    c_ctrl = AX_IVE_CROP_IMAGE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CropImage.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CropImage.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(POINTER(AX_IVE_DST_IMAGE_T)),
            POINTER(POINTER(AX_IVE_RECT_U16_T)),
            POINTER(AX_IVE_CROP_IMAGE_CTRL_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_images(dst_list, c_dst)
        dict_to_ax_ive_rects(box_list, c_box)
        dict_to_ax_ive_crop_image_ctrl(ctrl, c_ctrl)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CropImage(byref(c_handle), byref(c_src), c_dst, c_box, byref(c_ctrl), c_engine, c_instant)
        ax_ive_images_to_dict(c_dst, dst_list, engine)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def crop_resize(src: dict, dst_list: list[dict], box_list: list[dict], ctrl: dict, engine: int, instant: bool) -> tuple[int, int]:
    """
    Crop and resize image, support output multiple images.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CropResize(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pastDst[], AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_RESIZE_CTRL_T *pstCropResizeCtrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);`
        **python**              `handle, ret = crop_resize(src, dst_list, box_list, ctrl, engine, instant)`
        ======================= =====================================================

    :param dict src: Input source. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param list[dict] dst_list[IN/OUT]: Output result list. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param list[dict] box_list: Input crop region list. :class:`AX_IVE_RECT_U16_T <axcl.ive.axcl_ive_type.AX_IVE_RECT_U16_T>` to extract ive rect information.
    :param dict ctrl: Control parameter of crop resize. :class:`AX_IVE_CROP_RESIZE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_CROP_RESIZE_CTRL_T>` to extract ive crop resize control information.
    :param int engine: Hardware engine choise. :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task. (Reserved)
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x32 pixels to 4096x8192 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = (POINTER(AX_IVE_DST_IMAGE_T) * len(dst_list))()
    c_box = (POINTER(AX_IVE_RECT_U16_T) * len(box_list))()
    c_ctrl = AX_IVE_CROP_RESIZE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CropResize.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CropResize.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(POINTER(AX_IVE_DST_IMAGE_T)),
            POINTER(POINTER(AX_IVE_RECT_U16_T)),
            POINTER(AX_IVE_CROP_RESIZE_CTRL_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_images(dst_list, c_dst)
        dict_to_ax_ive_rects(box_list, c_box)
        dict_to_ax_ive_crop_resize_ctrl(ctrl, c_ctrl)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CropResize(byref(c_handle), byref(c_src), c_dst, c_box, byref(c_ctrl), c_engine, c_instant)
        ax_ive_images_to_dict(c_dst, dst_list, engine)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def crop_resize_for_split_yuv(src1: dict, src2: dict, dst1_list: list[dict], dst2_list: list[dict], box_list: list[dict], ctrl: dict, engine: int, instant: bool) -> tuple[int, int]:
    """
    Crop and resize image, support output multiple images.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CropResizeForSplitYUV(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_DST_IMAGE_T *pastDst1[], AX_IVE_DST_IMAGE_T *pastDst2[], AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_RESIZE_CTRL_T *pstCropResizeCtrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);`
        **python**              `handle, ret = crop_resize_for_split_yuv(src1, src2, dst1_list, dst2_list, box_list, ctrl, engine, instant)`
        ======================= =====================================================

    :param dict src1: Input source1. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Input source2. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param list[dict] dst1_list[IN/OUT]: Output Y result list. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param list[dict] dst2_list[IN/OUT]: Output UV result list. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param list[dict] box_list: Input crop region list. :class:`AX_IVE_RECT_U16_T <axcl.ive.axcl_ive_type.AX_IVE_RECT_U16_T>` to extract ive rect information.
    :param dict ctrl: Control parameter of crop resize. :class:`AX_IVE_CROP_RESIZE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_CROP_RESIZE_CTRL_T>` to extract ive crop resize control information.
    :param int engine: Hardware engine choise. :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task. (Reserved)
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x32 pixels to 4096x8192 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst1 = (POINTER(AX_IVE_DST_IMAGE_T) * len(dst1_list))()
    c_dst2 = (POINTER(AX_IVE_DST_IMAGE_T) * len(dst2_list))()
    c_box = (POINTER(AX_IVE_RECT_U16_T) * len(box_list))()
    c_ctrl = AX_IVE_CROP_RESIZE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CropResizeForSplitYUV.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CropResizeForSplitYUV.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(POINTER(AX_IVE_DST_IMAGE_T)),
            POINTER(POINTER(AX_IVE_DST_IMAGE_T)),
            POINTER(POINTER(AX_IVE_RECT_U16_T)),
            POINTER(AX_IVE_CROP_RESIZE_CTRL_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_images(dst1_list, c_dst1)
        dict_to_ax_ive_images(dst2_list, c_dst2)
        dict_to_ax_ive_rects(box_list, c_box)
        dict_to_ax_ive_crop_resize_ctrl(ctrl, c_ctrl)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CropResizeForSplitYUV(byref(c_handle), byref(c_src1), byref(c_src2), c_dst1, c_dst2, c_box, byref(c_ctrl), c_engine, c_instant)
        ax_ive_images_to_dict(c_dst1, dst1_list, engine)
        ax_ive_images_to_dict(c_dst2, dst2_list, engine)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def csc(src: dict, dst: dict, engine: int, instant: bool) -> tuple[int, int]:
    """
    Color space conversion.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CSC(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);`
        **python**              `handle, ret = csc(src, dst, engine, instant)`
        ======================= =====================================================

    :param dict src: Input source. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param int engine: Hardware engine choise. :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task. (Reserved)
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x32 pixels to 4096x8192 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = AX_IVE_SRC_IMAGE_T()
    try:
        libaxcl_ive.AXCL_IVE_CSC.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CSC.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_DST_IMAGE_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_image(dst, c_dst)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CSC(byref(c_handle), byref(c_src), byref(c_dst), c_engine, c_instant)
        ax_ive_image_to_dict(c_dst, dst, engine)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def crop_resize2(src: dict, dst_list: list[dict], src_box_list: list[dict], dst_box_list: list[dict], ctrl: dict, engine: int, instant: bool) -> tuple[int, int]:
    """
    Crop and resize multiple sub-images from src image, then overlay to dst image, support for specified areas.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CropResize2(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_IMAGE_T *pastDst[], AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_RECT_U16_T *pastDstBoxs[], AX_IVE_CROP_IMAGE_CTRL_T *pstCropResize2Ctrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);;`
        **python**              `handle, ret = crop_resize2(src, dst_list, src_box_list, dst_box_list, ctrl, engine, instant)`
        ======================= =====================================================

    :param dict src2: Input source. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param list[dict] dst_list[IN/OUT]: Output result list. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param list[dict] src_box_list: Input crop region list. :class:`AX_IVE_RECT_U16_T <axcl.ive.axcl_ive_type.AX_IVE_RECT_U16_T>` to extract ive rect information.
    :param list[dict] dst_box_list: Output overlay region list. :class:`AX_IVE_RECT_U16_T <axcl.ive.axcl_ive_type.AX_IVE_RECT_U16_T>` to extract ive rect information.
    :param dict ctrl: Control parameter of crop resize. :class:`AX_IVE_CROP_RESIZE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_CROP_RESIZE_CTRL_T>` to extract ive crop resize control information.
    :param int engine: Hardware engine choise. :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task. (Reserved)
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x32 pixels to 4096x8192 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_SRC_IMAGE_T()
    c_dst = (POINTER(AX_IVE_DST_IMAGE_T) * len(dst_list))()
    c_src_box = (POINTER(AX_IVE_RECT_U16_T) * len(src_box_list))()
    c_dst_box = (POINTER(AX_IVE_RECT_U16_T) * len(dst_box_list))()
    c_ctrl = AX_IVE_CROP_IMAGE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CropResize2.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CropResize2.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(POINTER(AX_IVE_IMAGE_T)),
            POINTER(POINTER(AX_IVE_RECT_U16_T)),
            POINTER(POINTER(AX_IVE_RECT_U16_T)),
            POINTER(AX_IVE_CROP_IMAGE_CTRL_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        dict_to_ax_ive_image(src, c_src)
        dict_to_ax_ive_images(dst_list, c_dst)
        dict_to_ax_ive_rects(src_box_list, c_src_box)
        dict_to_ax_ive_rects(dst_box_list, c_dst_box)
        dict_to_ax_ive_crop_image_ctrl(ctrl, c_ctrl)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CropResize2(byref(c_handle), byref(c_src), c_dst, c_src_box, c_dst_box, byref(c_ctrl), c_engine, c_instant)
        ax_ive_images_to_dict(c_dst, dst_list, engine)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def crop_resize2_for_split_yuv(src1: dict, src2: dict, dst1_list: list[dict], dst2_list: list[dict], src_box_list: list[dict], dst_box_list: list[dict], ctrl: dict, engine: int, instant: bool) -> tuple[int, int]:
    """
    Crop and resize image for splite YUV, support output multiple images.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_S32 AXCL_IVE_CropResize2ForSplitYUV(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2, AX_IVE_IMAGE_T *pastDst1[], AX_IVE_IMAGE_T *pastDst2[], AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_RECT_U16_T *pastDstBoxs[], AX_IVE_CROP_IMAGE_CTRL_T *pstCropResize2Ctrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);`
        **python**              `handle, ret = crop_resize2_for_split_yuv(src1, src2, dst1_list, dst2_list, src_box_list, dst_box_list, ctrl, engine, instant)`
        ======================= =====================================================

    :param dict src1: Input source1. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param dict src2: Input source2. :class:`AX_IVE_SRC_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_SRC_IMAGE_T>` to extract ive src image information.
    :param list[dict] dst1_list[IN/OUT]: Output Y result list. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param list[dict] dst2_list[IN/OUT]: Output UV result list. :class:`AX_IVE_DST_IMAGE_T <axcl.ive.axcl_ive_type.AX_IVE_DST_IMAGE_T>` to extract ive dst image information.
    :param list[dict] src_box_list: Input crop region list. :class:`AX_IVE_RECT_U16_T <axcl.ive.axcl_ive_type.AX_IVE_RECT_U16_T>` to extract ive rect information.
    :param list[dict] dst_box_list: Output overlay region list. :class:`AX_IVE_RECT_U16_T <axcl.ive.axcl_ive_type.AX_IVE_RECT_U16_T>` to extract ive rect information.
    :param dict ctrl: Control parameter of crop resize. :class:`AX_IVE_CROP_RESIZE_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_CROP_RESIZE_CTRL_T>` to extract ive crop resize control information.
    :param int engine: Hardware engine choise. :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task. (Reserved)
        - **ret** (*int*) - 0 indicates success, otherwise failure.

    .. note::
        - The size of the input data ranges from 32x32 pixels to 4096x8192 pixels.
        - The stride must be 16-pixel-aligned.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src1 = AX_IVE_SRC_IMAGE_T()
    c_src2 = AX_IVE_SRC_IMAGE_T()
    c_dst1 = (POINTER(AX_IVE_IMAGE_T) * len(dst1_list))()
    c_dst2 = (POINTER(AX_IVE_IMAGE_T) * len(dst2_list))()
    c_src_box = (POINTER(AX_IVE_RECT_U16_T) * len(src_box_list))()
    c_dst_box = (POINTER(AX_IVE_RECT_U16_T) * len(dst_box_list))()
    c_ctrl = AX_IVE_CROP_IMAGE_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_CropResize2ForSplitYUV.restype = AX_S32
        libaxcl_ive.AXCL_IVE_CropResize2ForSplitYUV.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(AX_IVE_SRC_IMAGE_T),
            POINTER(POINTER(AX_IVE_IMAGE_T)),
            POINTER(POINTER(AX_IVE_IMAGE_T)),
            POINTER(POINTER(AX_IVE_RECT_U16_T)),
            POINTER(POINTER(AX_IVE_RECT_U16_T)),
            POINTER(AX_IVE_CROP_IMAGE_CTRL_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        dict_to_ax_ive_image(src1, c_src1)
        dict_to_ax_ive_image(src2, c_src2)
        dict_to_ax_ive_images(dst1_list, c_dst1)
        dict_to_ax_ive_images(dst2_list, c_dst2)
        dict_to_ax_ive_rects(src_box_list, c_src_box)
        dict_to_ax_ive_rects(dst_box_list, c_dst_box)
        dict_to_ax_ive_crop_image_ctrl(ctrl, c_ctrl)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_CropResize2ForSplitYUV(byref(c_handle), byref(c_src1), byref(c_src2), c_dst1, c_dst2, c_src_box, c_dst_box, byref(c_ctrl), c_engine, c_instant)
        ax_ive_images_to_dict(c_dst1, dst1_list, engine)
        ax_ive_images_to_dict(c_dst2, dst2_list, engine)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def mau_matmul(src: dict, dst: dict, ctrl: dict, engine: int, instant: bool) -> tuple[int, int]:
    """
    Calculate matrix mul using MAU.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_CSCAXCL_IVE_MAU_MatMul(AX_IVE_HANDLE *pIveHandle, AX_IVE_MAU_MATMUL_INPUT_T *pstSrc, AX_IVE_MAU_MATMUL_OUTPUT_T *pstDst, AX_IVE_MAU_MATMUL_CTRL_T *pstMatMulCtrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);`
        **python**              `handle, ret = mau_matmul(src, dst, ctrl, engine, instant)`
        ======================= =====================================================

    :param dict src: Input source. :class:`AX_IVE_MAU_MATMUL_INPUT_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_MATMUL_INPUT_T>` to extract ive matrix mul input information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_MAU_MATMUL_OUTPUT_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_MATMUL_OUTPUT_T>` to extract ive matrix mul ouput information.
    :param dict ctrl: Control parameter of matrix mul. :class:`AX_IVE_MAU_MATMUL_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_MATMUL_CTRL_T>` to extract ive matrix mul control information.
    :param int engine: Hardware engine choise(Reserved). :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: tuple[int, int]

        - **handle** (*int*) - Returned handle ID of a task. (Reserved)
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_handle = AX_IVE_HANDLE(-1)
    c_src = AX_IVE_MAU_MATMUL_INPUT_T()
    c_dst = AX_IVE_MAU_MATMUL_OUTPUT_T()
    c_ctrl = AX_IVE_MAU_MATMUL_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_MAU_MatMul.restype = AX_S32
        libaxcl_ive.AXCL_IVE_MAU_MatMul.argtypes = [
            POINTER(AX_IVE_HANDLE),
            POINTER(AX_IVE_MAU_MATMUL_INPUT_T),
            POINTER(AX_IVE_MAU_MATMUL_OUTPUT_T),
            POINTER(AX_IVE_MAU_MATMUL_CTRL_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        dict_to_ax_ive_mau_matmul_input(src, c_src)
        dict_to_ax_ive_mau_matmul_output(dst, c_dst)
        dict_to_ax_ive_mau_matmul_ctrl(ctrl, c_ctrl)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_MAU_MatMul(byref(c_handle), byref(c_src), byref(c_dst), byref(c_ctrl), c_engine, c_instant)
        ax_ive_mau_matmul_output_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def npu_create_matmul_handle(ctrl: dict) -> tuple[int, int]:
    """
    Create matrix mul handle for NPU engine.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_NPU_CreateMatMulHandle(AX_IVE_MATMUL_HANDLE *pHandle, AX_IVE_NPU_MATMUL_CTRL_T *pstMatMulCtrl);`
        **python**              `handle, ret = npu_create_matmul_handle(ctrl)`
        ======================= =====================================================

    :param dict ctrl: Control parameter of npu matrix mul. :class:`AX_IVE_NPU_MATMUL_CTRL_T <axcl.ive.axcl_ive_type.AX_IVE_NPU_MATMUL_CTRL_T>` to extract ive npu matrix mul control information.
    :returns: tuple[int, int]

        - **handle** (*int*) - Return MatMul handle.
        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_handle = AX_IVE_MATMUL_HANDLE(-1)
    c_ctrl = AX_IVE_NPU_MATMUL_CTRL_T()
    try:
        libaxcl_ive.AXCL_IVE_NPU_CreateMatMulHandle.restype = AX_S32
        libaxcl_ive.AXCL_IVE_NPU_CreateMatMulHandle.argtypes = [
            POINTER(AX_IVE_MATMUL_HANDLE),
            POINTER(AX_IVE_NPU_MATMUL_CTRL_T)
        ]
        dict_to_ax_ive_npu_matmul_ctrl(ctrl, c_ctrl)
        ret = libaxcl_ive.AXCL_IVE_NPU_CreateMatMulHandle(byref(c_handle), byref(c_ctrl))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_handle.value, ret


def npu_destroy_matmul_handle(handle: int) -> int:
    """
    Destroy matrix mul handle for NPU engine.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_NPU_DestroyMatMulHandle(AX_IVE_MATMUL_HANDLE *pHandle);`
        **python**              `handle, ret = npu_destroy_matmul_handle(handle)`
        ======================= =====================================================

    :param int handle: Input MatMul handle created.
    :returns: int

        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    try:
        libaxcl_ive.AXCL_IVE_NPU_DestroyMatMulHandle.restype = AX_S32
        libaxcl_ive.AXCL_IVE_NPU_DestroyMatMulHandle.argtypes = [
            POINTER(AX_IVE_MATMUL_HANDLE)
        ]
        c_handle = POINTER(AX_IVE_MATMUL_HANDLE)(handle)
        ret = libaxcl_ive.AXCL_IVE_NPU_DestroyMatMulHandle(c_handle)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def npu_matmul(handle: int, src: dict, dst: dict, engine: int, instant: bool) -> int:
    """
    Calculate matrix mul using NPU.

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_IVE_NPU_MatMul(AX_IVE_MATMUL_HANDLE hHandle, AX_IVE_MAU_MATMUL_INPUT_T *pstSrc, AX_IVE_MAU_MATMUL_OUTPUT_T *pstDst, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant);`
        **python**              `handle, ret = npu_matmul(handle, src, dict, engine, instant)`
        ======================= =====================================================

    :param dict handle: Handle for MatMul.
    :param dict src: Input source. :class:`AX_IVE_MAU_MATMUL_INPUT_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_MATMUL_INPUT_T>` to extract ive mat mul ouput information.
    :param dict dst[IN/OUT]: Output result. :class:`AX_IVE_MAU_MATMUL_OUTPUT_T <axcl.ive.axcl_ive_type.AX_IVE_MAU_MATMUL_OUTPUT_T>` to extract ive mat mul ouput information.
    :param int engine: Hardware engine choise(Reserved). :class:`AX_IVE_ENGINE_E  <axcl.ive.axcl_ive_type.AX_IVE_ENGINE_E>`.
    :param bool instant: Flag indicating whether to generate an interrupt. If the output result blocks the next operation, set instant to True. (Reserved)
    :returns: int

        - **ret** (*int*) - 0 indicates success, otherwise failure.
    """
    ret = -1
    c_src = AX_IVE_MAU_MATMUL_INPUT_T()
    c_dst = AX_IVE_MAU_MATMUL_OUTPUT_T()
    try:
        libaxcl_ive.AXCL_IVE_NPU_MatMul.restype = AX_S32
        libaxcl_ive.AXCL_IVE_NPU_MatMul.argtypes = [
            POINTER(AX_IVE_MATMUL_HANDLE),
            POINTER(AX_IVE_MAU_MATMUL_INPUT_T),
            POINTER(AX_IVE_MAU_MATMUL_OUTPUT_T),
            AX_IVE_ENGINE_E,
            AX_BOOL
        ]
        c_handle = handle
        dict_to_ax_ive_mau_matmul_input(src, c_src)
        dict_to_ax_ive_mau_matmul_output(dst, c_dst)
        c_engine = engine
        c_instant = AX_BOOL(1 if instant else 0)
        ret = libaxcl_ive.AXCL_IVE_NPU_MatMul(byref(c_handle), byref(c_src), byref(c_dst), c_engine, c_instant)
        ax_ive_mau_matmul_output_to_dict(c_dst, dst)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret
