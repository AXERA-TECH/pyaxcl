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

from axcl.lib.axcl_lib import libaxcl_dmadim
from axcl.dmadim.axcl_dmadim_type import *
from axcl.utils.axcl_logger import *


def open(sync: bool) -> int:
    """
    Open

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMADIM_Open(AX_BOOL bSync);`
        **python**              `ret = axcl.dmadim.open(sync)`
        ======================= =====================================================

    :param bool sync: sync flag
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_dmadim.AXCL_DMADIM_Open.restype = AX_S32
        libaxcl_dmadim.AXCL_DMADIM_Open.argtypes = [AX_S32]
        c_sync = AX_S32(1 if sync else 0)
        ret = libaxcl_dmadim.AXCL_DMADIM_Open(c_sync)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def cfg(dma_chn: int, dma_msg: dict) -> int:
    """
    Configure

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMADIM_Cfg(AX_S32 s32DmaChn, AX_DMADIM_MSG_T *pDmaMsg);`
        **python**              `ret = axcl.dmadim.cfg(dma_chn, dma_msg)`
        ======================= =====================================================

    :param int dma_chn: dma channel
    :param list dma_msg: list of dma message
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_dma_msg = AX_DMADIM_MSG_T()
    try:
        libaxcl_dmadim.AXCL_DMADIM_Cfg.restype = AX_S32
        libaxcl_dmadim.AXCL_DMADIM_Cfg.argtypes = [AX_S32, POINTER(AX_DMADIM_MSG_T)]
        c_dma_chn = AX_S32(dma_chn)
        desc_buf = dma_msg.get('desc_buf')
        if desc_buf is not None:
            c_dma_msg.u32DescNum = len(desc_buf)
            desc = AX_DMADIM_DESC_T * c_dma_msg.u32DescNum
            desc_array = desc()
            for i in range(c_dma_msg.u32DescNum):
                desc_array[i].u64PhySrc = desc_buf[i].get('phy_src', 0)
                desc_array[i].u64PhyDst = desc_buf[i].get('phy_dst', 0)
                desc_array[i].u32Size = desc_buf[i].get('size', 0)
            c_dma_msg.pDescBuf = cast(desc_array, c_void_p)

        c_dma_msg.eEndian = AX_DMADIM_ENDIAN_E(dma_msg.get('endian', 0))
        callback = dma_msg.get('callback')
        if callback is not None:
            c_dma_msg.pfnCallBack = CFUNCTYPE(None, POINTER(AX_DMADIM_XFER_STAT_T), c_void_p)(callback)
        c_dma_msg.pCbArg = dma_msg.get('cb_arg', 0)
        c_dma_msg.eDmaMode = AX_DMADIM_XFER_MODE_E(dma_msg.get('dma_mode', 0))

        ret = libaxcl_dmadim.AXCL_DMADIM_Cfg(c_dma_chn, byref(c_dma_msg))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def start(dma_chn: int, dma_id: int) -> int:
    """
    Start

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMADIM_Start(AX_S32 s32DmaChn, AX_S32 s32Id);`
        **python**              `ret = axcl.dmadim.start(dma_chn, dma_id)`
        ======================= =====================================================

    :param int dma_chn: dma channel
    :param int dma_id: id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_dmadim.AXCL_DMADIM_Start.restype = AX_S32
        libaxcl_dmadim.AXCL_DMADIM_Start.argtypes = [AX_S32, AX_S32]
        c_dma_chn = AX_S32(dma_chn)
        c_id = AX_S32(dma_id)
        ret = libaxcl_dmadim.AXCL_DMADIM_Start(c_dma_chn, c_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def wait_done(dma_chn: int, dma_id: int, timeout: int) -> tuple[dict, int]:
    """
    Wait done

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMADIM_Waitdone(AX_S32 s32DmaChn, AX_DMADIM_XFER_STAT_T *pXferStat, AX_S32 s32Timeout);`
        **python**              `xfer_stat, ret = axcl.dmadim.wait_done(dma_chn, dma_id, timeout)`
        ======================= =====================================================

    :param int dma_chn: dma channel
    :param int dma_id: id
    :param int timeout: timeout
    :returns: tuple[dict, int]

        - **xfer_stat** (*dict*) - :class:`AX_DMADIM_XFER_STAT_T <axcl.dmadim.axcl_dmadim_type.AX_DMADIM_XFER_STAT_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_xfer_stat = AX_DMADIM_XFER_STAT_T()
    xfer_stat = {}
    try:
        libaxcl_dmadim.AXCL_DMADIM_Waitdone.restype = AX_S32
        libaxcl_dmadim.AXCL_DMADIM_Waitdone.argtypes = [AX_S32, POINTER(AX_DMADIM_XFER_STAT_T), AX_S32]
        c_dma_chn = AX_S32(dma_chn)
        c_timeout = AX_S32(timeout)
        c_xfer_stat.s32Id = dma_id

        ret = libaxcl_dmadim.AXCL_DMADIM_Waitdone(c_dma_chn, byref(c_xfer_stat), c_timeout)

        xfer_stat['id'] = c_xfer_stat.s32Id
        xfer_stat['checksum'] = c_xfer_stat.u32CheckSum
        xfer_stat['stat'] = c_xfer_stat.u32Stat
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return xfer_stat, ret


def close(dma_chn: int) -> int:
    """
    Close

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMADIM_Close(AX_S32 s32DmaChn);`
        **python**              `ret = axcl.dmadim.close(dma_chn)`
        ======================= =====================================================

    :param int dma_chn: dma channel
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_dmadim.AXCL_DMADIM_Close.restype = AX_S32
        libaxcl_dmadim.AXCL_DMADIM_Close.argtypes = [AX_S32]
        c_dma_chn = AX_S32(dma_chn)
        ret = libaxcl_dmadim.AXCL_DMADIM_Close(c_dma_chn)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_copy(phy_dst: int, phy_src: int, size: int) -> int:
    """
    Memory copy

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMA_MemCopy(AX_U64 u64PhyDst, AX_U64 u64PhySrc, AX_U64 U64Size);`
        **python**              `ret = axcl.dmadim.mem_copy(phy_dst, phy_src, size)`
        ======================= =====================================================

    :param int phy_dst: dest phy address
    :param int phy_src: src phy address
    :param int size: size to copy
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_dmadim.AXCL_DMA_MemCopy.restype = AX_S32
        libaxcl_dmadim.AXCL_DMA_MemCopy.argtypes = [AX_U64, AX_U64, AX_U64]
        if isinstance(phy_dst, c_void_p):
            c_phy_dst = AX_U64(phy_dst.value)
        else:
            c_phy_dst = AX_U64(phy_dst)
        if isinstance(phy_src, c_void_p):
            c_phy_src = AX_U64(phy_src.value)
        else:
            c_phy_src = AX_U64(phy_src)
        c_size = AX_U64(size)
        ret = libaxcl_dmadim.AXCL_DMA_MemCopy(c_phy_dst, c_phy_src, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_set(phy_dst: dict, init_val: int, size: int) -> int:
    """
    Memory set

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMA_MemSet(AX_U64 u64PhyDst, AX_U8 u8InitVal, AX_U64 U64Size);`
        **python**              `ret = axcl.dmadim.mem_set(phy_dst, init_val, size)`
        ======================= =====================================================

    :param int phy_dst: dest phy address
    :param int init_val: value to set
    :param int size: memory size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_dmadim.AXCL_DMA_MemSet.restype = AX_S32
        libaxcl_dmadim.AXCL_DMA_MemSet.argtypes = [AX_U64, AX_U8, AX_U64]
        if isinstance(phy_dst, c_void_p):
            c_phy_dst = AX_U64(phy_dst.value)
        else:
            c_phy_dst = AX_U64(phy_dst)
        c_init_val = AX_U8(init_val)
        c_size = AX_U64(size)
        ret = libaxcl_dmadim.AXCL_DMA_MemSet(c_phy_dst, c_init_val, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_copy_xd(dim_desc: dict, mode: int) -> int:
    """
    Memory copy xd

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMA_MemCopyXD(AX_DMADIM_DESC_XD_T tDimDesc, AX_DMADIM_XFER_MODE_E eMode);`
        **python**              `ret = axcl.dmadim.mem_copy_xd(dim_desc, mode)`
        ======================= =====================================================

    :param dict dim_desc: :class:`AX_DMADIM_DESC_XD_T <axcl.dmadim.axcl_dmadim_type.AX_DMADIM_DESC_XD_T>`
    :param int mode: :class:`AX_DMADIM_XFER_MODE_E <axcl.dmadim.axcl_dmadim_type.AX_DMADIM_XFER_MODE_E>`.
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_dim_desc = AX_DMADIM_DESC_XD_T()
    try:
        libaxcl_dmadim.AXCL_DMA_MemCopyXD.restype = AX_S32
        libaxcl_dmadim.AXCL_DMA_MemCopyXD.argtypes = [AX_DMADIM_DESC_XD_T, AX_DMADIM_XFER_MODE_E]
        c_mode = AX_DMADIM_XFER_MODE_E(mode)
        n_tiles = dim_desc.get('n_tiles')
        if n_tiles and isinstance(n_tiles, list):
            for i in range(len(n_tiles)):
                if i < 3:
                    c_dim_desc.u16Ntiles[i] = AX_U16(n_tiles[i])

        src_info = dim_desc.get('src_info')
        if src_info:
            c_dim_desc.tSrcInfo.u64PhyAddr = AX_U64(src_info.get('phy_addr', 0))
            c_dim_desc.tSrcInfo.u32Imgw = AX_U32(src_info.get('img_w', 0))
            stride = src_info.get('stride')
            if stride and isinstance(stride, list):
                for i in range(len(stride)):
                    c_dim_desc.tSrcInfo.u32Stride[i] = AX_U32(stride[i])

        dst_info = dim_desc.get('dst_info')
        if dst_info:
            c_dim_desc.tDstInfo.u64PhyAddr = AX_U64(dst_info.get('phy_addr', 0))
            c_dim_desc.tDstInfo.u32Imgw = AX_U32(dst_info.get('img_w', 0))
            stride = dst_info.get('stride')
            if stride and isinstance(stride, list):
                for i in range(len(stride)):
                    c_dim_desc.tDstInfo.u32Stride[i] = AX_U32(stride[i])

        ret = libaxcl_dmadim.AXCL_DMA_MemCopyXD(c_dim_desc, c_mode)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def checksum(phy_src: int, size: int) -> int:
    """
    Calculate checksum

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_DMA_CheckSum(AX_U32 *u32Result, AX_U64 u64PhySrc, AX_U64 U64Size);`
        **python**              `result, ret = axcl.dmadim.checksum(phy_src, size)`
        ======================= =====================================================

    :param int phy_src: src phy adddress
    :param int size: data size
    :returns: tuple[int, int]

        - **result** (*int*) - checksum result
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_result = AX_U32(0)
    try:
        libaxcl_dmadim.AXCL_DMA_CheckSum.restype = AX_S32
        libaxcl_dmadim.AXCL_DMA_CheckSum.argtypes = [POINTER(AX_U32), AX_U64, AX_U64]
        if isinstance(phy_src, c_void_p):
            c_phy_src = AX_U64(phy_src.value)
        else:
            c_phy_src = AX_U64(phy_src)
        c_size = AX_U64(size)

        ret = libaxcl_dmadim.AXCL_DMA_CheckSum(byref(c_result), c_phy_src, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return c_result.value, ret
