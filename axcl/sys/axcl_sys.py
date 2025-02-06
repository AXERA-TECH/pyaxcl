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

from axcl.lib.axcl_lib import libaxcl_sys
from axcl.sys.axcl_sys_type import *
from axcl.ax_global_type import *
from axcl.utils.axcl_logger import *


def init() -> int:
    """
    Init

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_Init(AX_VOID);`
        **python**              `ret = axcl.sys.init()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_Init.restype = AX_S32
        ret = libaxcl_sys.AXCL_SYS_Init()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def deinit() -> int:
    """
    Init

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_Deinit(AX_VOID);`
        **python**              `ret = axcl.sys.deinit()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_Deinit.restype = AX_S32
        ret = libaxcl_sys.AXCL_SYS_Deinit()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_alloc(size: int, align: int, token: str) -> tuple[int, int, int]:
    """
    Allocate CMM memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemAlloc(AX_U64 *phyaddr, AX_VOID **pviraddr, AX_U32 size, AX_U32 align, const AX_S8 *token);`
        **python**              `phy_addr, vir_addr, ret = axcl.sys.mem_alloc(size, align, token)`
        ======================= =====================================================

    :param int size: memory size
    :param int align: memory size align
    :param str token: token
    :returns: tuple[int, int, int]

        - **phy_addr** (*int*) - memory physical address
        - **vir_addr** (*int*) - memory virtual address
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    phy_addr = AX_U64(0)
    vir_addr = c_void_p(0)
    try:
        libaxcl_sys.AXCL_SYS_MemAlloc.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemAlloc.argtypes=[POINTER(AX_U64), POINTER(c_void_p), AX_U32, AX_U32, c_char_p]
        c_size = AX_U32(size)
        c_align = AX_U32(align)

        if token and len(token):
            c_token = c_char_p(token.encode('utf-8'))
        else:
            c_token = c_char_p(0)

        ret = libaxcl_sys.AXCL_SYS_MemAlloc(byref(phy_addr), byref(vir_addr), c_size, c_align, c_token)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return phy_addr.value, vir_addr.value, ret


def mem_alloc_cached(size: int, align: int, token: str) -> tuple[int, int, int]:
    """
    Allocate cached CMM memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemAllocCached(AX_U64 *phyaddr, AX_VOID **pviraddr, AX_U32 size, AX_U32 align, const AX_S8 *token);`
        **python**              `phy_addr, vir_addr, ret = axcl.sys.mem_alloc_cached(size, align, token)`
        ======================= =====================================================

    :param int size: memory size
    :param int align: memory size align
    :param str token: token
    :returns: tuple[int, int, int]

        - **phy_addr** (*int*) - memory physical address
        - **vir_addr** (*int*) - memory virtual address
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    phy_addr = AX_U64(0)
    vir_addr = c_void_p(0)
    try:
        libaxcl_sys.AXCL_SYS_MemAllocCached.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemAllocCached.argtypes=[POINTER(AX_U64), POINTER(c_void_p), AX_U32, AX_U32, c_char_p]
        c_size = AX_U32(size)
        c_align = AX_U32(align)

        if token and len(token):
            c_token = c_char_p(token.encode('utf-8'))
        else:
            c_token = c_char_p(0)

        ret = libaxcl_sys.AXCL_SYS_MemAllocCached(byref(phy_addr), byref(vir_addr), c_size, c_align, c_token)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return phy_addr.value, vir_addr.value, ret


def mem_free(phy_addr: int, vir_addr: int) -> int:
    """
    Free CMM memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemFree(AX_U64 phyaddr, AX_VOID *pviraddr);`
        **python**              `ret = axcl.sys.mem_free(phy_addr, vir_addr)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :param int vir_addr: memory virtual address
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_MemFree.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemFree.argtypes=[AX_U64, c_void_p]
        c_phy_addr = AX_U64(phy_addr)
        c_vir_addr = c_void_p(vir_addr)

        ret = libaxcl_sys.AXCL_SYS_MemFree(c_phy_addr, c_vir_addr)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mmap(phy_addr: int, size: int) -> int:
    """
    Map memory physical address to virtual address

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID *AXCL_SYS_Mmap(AX_U64 phyaddr, AX_U32 size);`
        **python**              `vir_addr = axcl.sys.mmap(phy_addr, size)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :param int size: memory size
    :returns: **vir_addr** (*int*) - virtual address
    """
    vir_addr = c_void_p(0)
    try:
        libaxcl_sys.AXCL_SYS_Mmap.restype = c_void_p
        libaxcl_sys.AXCL_SYS_Mmap.argtypes=[AX_U64, AX_U32]
        c_phy_addr = AX_U64(phy_addr)
        c_size = AX_U32(size)

        vir_addr = libaxcl_sys.AXCL_SYS_Mmap(c_phy_addr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return vir_addr


def mmap_cache(phy_addr: int, size: int) -> int:
    """
    Map memory physical address to cached virtual address

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID *AXCL_SYS_MmapCache(AX_U64 phyaddr, AX_U32 size);`
        **python**              `vir_addr = axcl.sys.mmap_cache(phy_addr, size)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :param int size: memorysize
    :returns: **vir_addr** (*int*) - virtual address
    """
    vir_addr = None
    try:
        libaxcl_sys.AXCL_SYS_MmapCache.restype = c_void_p
        libaxcl_sys.AXCL_SYS_MmapCache.argtypes=[AX_U64, AX_U32]
        c_phy_addr = AX_U64(phy_addr)
        c_size = AX_U32(size)

        vir_addr = libaxcl_sys.AXCL_SYS_MmapCache(c_phy_addr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return vir_addr


def mmap_fast(phy_addr: int, size: int) -> int:
    """
    Map memory physical address to virtual address fast

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID *AXCL_SYS_MmapFast(AX_U64 phyaddr, AX_U32 size);`
        **python**              `vir_addr = axcl.sys.mmap_fast(phy_addr, size)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :param int size: memory size
    :returns: **vir_addr** (*int*) - virtual address
    """
    vir_addr = None
    try:
        libaxcl_sys.AXCL_SYS_MmapFast.restype = c_void_p
        libaxcl_sys.AXCL_SYS_MmapFast.argtypes=[AX_U64, AX_U32]
        c_phy_addr = AX_U64(phy_addr)
        c_size = AX_U32(size)

        vir_addr = libaxcl_sys.AXCL_SYS_MmapFast(c_phy_addr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return vir_addr


def mmap_cache_fast(phy_addr: int, size: int) -> int:
    """
    Map memory physical address to cached virtual address fast

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID *AXCL_SYS_MmapCacheFast(AX_U64 phyaddr, AX_U32 size);`
        **python**              `vir_addr = axcl.sys.mmap_cache_fast(phy_addr, size)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :param int size: memory size
    :returns: **vir_addr** (*int*) - virtual address
    """
    vir_addr = None
    try:
        libaxcl_sys.AXCL_SYS_MmapCacheFast.restype = c_void_p
        libaxcl_sys.AXCL_SYS_MmapCacheFast.argtypes=[AX_U64, AX_U32]
        c_phy_addr = AX_U64(phy_addr)
        c_size = AX_U32(size)

        vir_addr = libaxcl_sys.AXCL_SYS_MmapCacheFast(c_phy_addr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return vir_addr


def munmap(vir_addr: int, size: int) -> int:
    """
    Unmap memory virtual address

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_Munmap(AX_VOID *pviraddr, AX_U32 size);`
        **python**              `ret = axcl.sys.munmap(vir_addr, size)`
        ======================= =====================================================

    :param int vir_addr: memory virtual address
    :param int size: memorysize
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_Munmap.restype = AX_S32
        libaxcl_sys.AXCL_SYS_Munmap.argtypes=[c_void_p, AX_U32]
        c_size = AX_U32(size)
        if vir_addr:
            c_vir_addr = c_void_p(vir_addr)
            ret = libaxcl_sys.AXCL_SYS_Munmap(c_vir_addr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mflush_cache(phy_addr: int, vir_addr: int, size: int) -> int:
    """
    Flush cached memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MflushCache(AX_U64 phyaddr, AX_VOID *pviraddr, AX_U32 size);`
        **python**              `ret = axcl.sys.mflush_cache(phy_addr, vir_addr, size)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :param int vir_addr: memory virtual address
    :param int size: memory size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_MflushCache.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MflushCache.argtypes=[AX_U64, c_void_p, AX_U32]
        c_phy_addr = AX_U64(phy_addr)
        c_size = AX_U32(size)
        if vir_addr:
            c_vir_addr = c_void_p(vir_addr)
            ret = libaxcl_sys.AXCL_SYS_MflushCache(c_phy_addr, c_vir_addr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def minvalidate_cache(phy_addr: int, vir_addr: int, size: int) -> int:
    """
    Flush cached memory

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MinvalidateCache(AX_U64 phyaddr, AX_VOID *pviraddr, AX_U32 size);`
        **python**              `ret = axcl.sys.minvalidate_cache(phy_addr, vir_addr, size)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :param int vir_addr: memory virtual address
    :param int size: memory size
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_MinvalidateCache.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MinvalidateCache.argtypes=[AX_U64, c_void_p, AX_U32]
        c_phy_addr = AX_U64(phy_addr)
        c_size = AX_U32(size)
        if vir_addr:
            c_vir_addr = c_void_p(vir_addr)
            ret = libaxcl_sys.AXCL_SYS_MinvalidateCache(c_phy_addr, c_vir_addr, c_size)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_get_block_info_by_phy(phy_addr: int) -> tuple[int, int, int, int]:
    """
    Get cmm memory block info by physical address

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemGetBlockInfoByPhy(AX_U64 phyaddr, AX_S32 *pmemType, AX_VOID **pviraddr, AX_U32 *pblockSize);`
        **python**              `mem_type, vir_addr, block_size, ret = axcl.sys.mem_get_block_info_by_phy(phy_addr)`
        ======================= =====================================================

    :param int phy_addr: memory physical address
    :returns: tuple[int, int, int, int]

        - **mem_type** (*int*) - cmm memory type
        - **vir_addr** (*int*) - cmm memory virtual address
        - **block_size** (*int*) - cmm memory block size
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    mem_type = AX_S32(0)
    vir_addr = c_void_p(0)
    block_size = AX_U32(0)
    try:
        libaxcl_sys.AXCL_SYS_MemGetBlockInfoByPhy.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemGetBlockInfoByPhy.argtypes=[AX_U64, POINTER(AX_S32), POINTER(c_void_p), POINTER(AX_U32)]
        c_phy_addr = AX_U64(phy_addr)

        ret = libaxcl_sys.AXCL_SYS_MemGetBlockInfoByPhy(c_phy_addr, byref(mem_type), byref(vir_addr), byref(block_size))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return mem_type.value, vir_addr.value, block_size.value, ret


def mem_get_block_info_by_virt(vir_addr: int) -> tuple[int, int, int]:
    """
    Get cmm memory block info by virtual address

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemGetBlockInfoByVirt(AX_VOID *pviraddr, AX_U64 *phyaddr, AX_S32 *pmemType);`
        **python**              `phy_addr, mem_type, ret = axcl.sys.mem_get_block_info_by_virt(vir_addr)`
        ======================= =====================================================

    :param int vir_addr: memory virtual address
    :returns: tuple[int, int, int]

        - **phy_addr** (*int*) - cmm memory physical address
        - **mem_type** (*int*) - cmm memory type
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    phy_addr = AX_U64(0)
    mem_type = AX_S32(0)
    try:
        libaxcl_sys.AXCL_SYS_MemGetBlockInfoByVirt.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemGetBlockInfoByVirt.argtypes=[c_void_p, POINTER(AX_U64), POINTER(AX_S32)]
        if vir_addr:
            c_vir_addr = c_void_p(vir_addr)
            ret = libaxcl_sys.AXCL_SYS_MemGetBlockInfoByVirt(c_vir_addr, byref(phy_addr), byref(mem_type))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return phy_addr.value, mem_type.value, ret


def mem_get_partition_info() -> tuple[list, int]:
    """
    Get cmm partition information

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemGetPartitionInfo(AX_CMM_PARTITION_INFO_T *pCmmPartitionInfo);`
        **python**              `cmm_part_info, ret = axcl.sys.mem_get_partition_info()`
        ======================= =====================================================

    :returns: tuple[list, int]

        - **cmm_part_info** (*list*) - list of cmm partition information :class:`AX_PARTITION_INFO_T <axcl.sys.axcl_sys_type.AX_PARTITION_INFO_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    cmm_partition_info = AX_CMM_PARTITION_INFO_T(0)
    cmm_part_info = []

    try:
        libaxcl_sys.AXCL_SYS_MemGetPartitionInfo.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemGetPartitionInfo.argtypes=[POINTER(AX_CMM_PARTITION_INFO_T)]

        ret = libaxcl_sys.AXCL_SYS_MemGetPartitionInfo(byref(cmm_partition_info))
        if ret == 0:
            for i in range(cmm_partition_info.PartitionCnt):
                part_info = {
                    "phy_addr": cmm_partition_info.PartitionInfo[i].PhysAddr,
                    "size_kbyte": cmm_partition_info.PartitionInfo[i].SizeKB,
                    "name": cast(cmm_partition_info.PartitionInfo[i].Name, c_char_p).value.decode('utf-8')
                }
                cmm_part_info.append(part_info)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return cmm_part_info, ret


def mem_set_config(mod_info: dict, partition_name: str) -> int:
    """
    Set modual cmm configure

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemSetConfig(const AX_MOD_INFO_T *pModInfo, const AX_S8 *pPartitionName);`
        **python**              `ret = axcl.sys.mem_set_config(mod_info, partition_name)`
        ======================= =====================================================

    :param dict mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :param str partition_name: partition name
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_mod_info = AX_MOD_INFO_T()
    try:
        libaxcl_sys.AXCL_SYS_MemSetConfig.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemSetConfig.argtypes=[POINTER(AX_MOD_INFO_T), c_char_p]
        if partition_name and len(partition_name) > 0:
            c_partition_name = c_char_p(partition_name.encode('utf-8'))
        else:
            c_partition_name = c_char_p(0)

        c_mod_info.enModId = AX_S32(mod_info.get('mod_id', 0))
        c_mod_info.s32GrpId = AX_S32(mod_info.get('grp_id', 0))
        c_mod_info.s32ChnId = AX_S32(mod_info.get('chn_id', 0))

        ret = libaxcl_sys.AXCL_SYS_MemSetConfig(byref(c_mod_info), c_partition_name)

    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def mem_get_config(mod_info: dict) -> tuple[str, int]:
    """
    Get cmm configure by modual

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemGetConfig(const AX_MOD_INFO_T *pModInfo, AX_S8 *pPartitionName);`
        **python**              `partition_name, ret = axcl.sys.mem_get_config(mod_info)`
        ======================= =====================================================

    :param dict mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :returns: tuple[str, int]

        - **partition_name** (*str*) - partition name
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_mod_info = AX_MOD_INFO_T()
    c_partition_name = create_string_buffer(AX_MAX_PARTITION_NAME_LEN)
    partition_name = None
    try:
        libaxcl_sys.AXCL_SYS_MemGetConfig.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemGetConfig.argtypes=[POINTER(AX_MOD_INFO_T), c_char_p]

        c_mod_info.enModId = AX_S32(mod_info.get('mod_id', 0))
        c_mod_info.s32GrpId = AX_S32(mod_info.get('grp_id', 0))
        c_mod_info.s32ChnId = AX_S32(mod_info.get('chn_id', 0))
        ret = libaxcl_sys.AXCL_SYS_MemGetConfig(byref(c_mod_info), c_partition_name)
        if ret == 0:
            partition_name = c_partition_name.value.decode('utf-8')
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return partition_name, ret


def mem_query_status() -> tuple[dict, int]:
    """
    Query cmm status

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_MemQueryStatus(AX_CMM_STATUS_T *pCmmStatus);`
        **python**              `cmm_status, ret = axcl.sys.mem_query_status()`
        ======================= =====================================================

    :returns: tuple[dict, int]

        - **cmm_status** (*dict*) - cmm status :class:`AX_CMM_STATUS_T <axcl.sys.axcl_sys_type.AX_CMM_STATUS_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    c_cmm_status = AX_CMM_STATUS_T()
    cmm_status = {}
    try:
        libaxcl_sys.AXCL_SYS_MemQueryStatus.restype = AX_S32
        libaxcl_sys.AXCL_SYS_MemQueryStatus.argtypes=[POINTER(AX_CMM_STATUS_T)]

        ret = libaxcl_sys.AXCL_SYS_MemQueryStatus(byref(c_cmm_status))
        if ret == 0:
            cmm_status['total_size'] = c_cmm_status.TotalSize
            cmm_status['remain_size'] = c_cmm_status.RemainSize
            cmm_status['block_cnt'] = c_cmm_status.BlockCnt
            cmm_status['partition'] = []
            for i in range(c_cmm_status.Partition.PartitionCnt):
                part_info = {
                    "phy_addr": c_cmm_status.Partition.PartitionInfo[i].PhysAddr,
                    "size_kbyte": c_cmm_status.Partition.PartitionInfo[i].SizeKB,
                    "name": cast(c_cmm_status.Partition.PartitionInfo[i].Name, c_char_p).value.decode('utf-8')
                }
                cmm_status['partition'].append(part_info)

    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return cmm_status, ret


def link(src_mod_info: dict, dst_mod_info: dict) -> int:
    """
    Link moduals

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_Link(const AX_MOD_INFO_T *pSrc, const AX_MOD_INFO_T *pDest);`
        **python**              `ret = axcl.sys.link(src_mod_info, dst_mod_info)`
        ======================= =====================================================

    :param dict src_mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :param dict dst_mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    src = AX_MOD_INFO_T()
    dst = AX_MOD_INFO_T()
    try:
        libaxcl_sys.AXCL_SYS_Link.restype = AX_S32
        libaxcl_sys.AXCL_SYS_Link.argtypes=[POINTER(AX_MOD_INFO_T), POINTER(AX_MOD_INFO_T)]
        if src_mod_info and dst_mod_info:
            src.enModId = AX_S32(src_mod_info.get('mod_id', 0))
            src.s32GrpId = AX_S32(src_mod_info.get('grp_id', 0))
            src.s32ChnId = AX_S32(src_mod_info.get('chn_id', 0))

            dst.enModId = AX_S32(dst_mod_info.get('mod_id', 0))
            dst.s32GrpId = AX_S32(dst_mod_info.get('grp_id', 0))
            dst.s32ChnId = AX_S32(dst_mod_info.get('chn_id', 0))

            ret = libaxcl_sys.AXCL_SYS_Link(byref(src), byref(dst))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def unlink(src_mod_info: dict, dst_mod_info: dict) -> int:
    """
    Unlink moduals

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_UnLink(const AX_MOD_INFO_T *pSrc, const AX_MOD_INFO_T *pDest);`
        **python**              `ret = axcl.sys.unlink(src_mod_info, dst_mod_info)`
        ======================= =====================================================

    :param dict src_mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :param dict dst_mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    src = AX_MOD_INFO_T()
    dst = AX_MOD_INFO_T()
    try:
        libaxcl_sys.AXCL_SYS_UnLink.restype = AX_S32
        libaxcl_sys.AXCL_SYS_UnLink.argtypes=[POINTER(AX_MOD_INFO_T), POINTER(AX_MOD_INFO_T)]
        if src_mod_info and dst_mod_info:
            src.enModId = AX_S32(src_mod_info.get('mod_id', 0))
            src.s32GrpId = AX_S32(src_mod_info.get('grp_id', 0))
            src.s32ChnId = AX_S32(src_mod_info.get('chn_id', 0))

            dst.enModId = AX_S32(dst_mod_info.get('mod_id', 0))
            dst.s32GrpId = AX_S32(dst_mod_info.get('grp_id', 0))
            dst.s32ChnId = AX_S32(dst_mod_info.get('chn_id', 0))

            ret = libaxcl_sys.AXCL_SYS_UnLink(byref(src), byref(dst))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_link_by_dest(dst_mod_info: dict) -> tuple[dict, int]:
    """
    Get link source modual information by destination modual

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_GetLinkByDest(const AX_MOD_INFO_T *pDest, AX_MOD_INFO_T *pSrc);`
        **python**              `src_mod_info, ret = axcl.sys.get_link_by_dest(dst_mod_info)`
        ======================= =====================================================

    :param dict dst_mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :returns:

        - **src_mod_info** (*dict*) - :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    src = AX_MOD_INFO_T()
    dst = AX_MOD_INFO_T()
    src_mod_info = {
        'mod_id': 0,
        'grp_id': 0,
        'chn_id': 0
    }
    try:
        libaxcl_sys.AXCL_SYS_GetLinkByDest.restype = AX_S32
        libaxcl_sys.AXCL_SYS_GetLinkByDest.argtypes=[POINTER(AX_MOD_INFO_T), POINTER(AX_MOD_INFO_T)]
        if dst_mod_info:
            dst.enModId = AX_S32(dst_mod_info.get('mod_id', 0))
            dst.s32GrpId = AX_S32(dst_mod_info.get('grp_id', 0))
            dst.s32ChnId = AX_S32(dst_mod_info.get('chn_id', 0))

            ret = libaxcl_sys.AXCL_SYS_GetLinkByDest(byref(dst), byref(src))
            if ret == 0:
                src_mod_info['mod_id'] = src.enModId
                src_mod_info['grp_id'] = src.s32GrpId
                src_mod_info['chn_id'] = src.s32ChnId
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return src_mod_info, ret


def get_link_by_src(src_mod_info: dict) -> tuple[list, int]:
    """
    Get link destination modual information by source modual

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_GetLinkBySrc(const AX_MOD_INFO_T *pSrc, AX_LINK_DEST_T *pLinkDest);`
        **python**              `dst_link, ret = axcl.sys.get_link_by_src(src_mod_info)`
        ======================= =====================================================

    :param dict src_mod_info: :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
    :returns:

        - **dst_link** (*list*) - list of :class:`AX_MOD_INFO_T <axcl.ax_global_type.AX_MOD_INFO_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    src = AX_MOD_INFO_T()
    dst = AX_LINK_DEST_T()
    dst_link = []
    try:
        libaxcl_sys.AXCL_SYS_GetLinkBySrc.restype = AX_S32
        libaxcl_sys.AXCL_SYS_GetLinkBySrc.argtypes=[POINTER(AX_MOD_INFO_T), POINTER(AX_LINK_DEST_T)]
        if src_mod_info:
            src.enModId = AX_S32(src_mod_info.get('mod_id', 0))
            src.s32GrpId = AX_S32(src_mod_info.get('grp_id', 0))
            src.s32ChnId = AX_S32(src_mod_info.get('chn_id', 0))

            ret = libaxcl_sys.AXCL_SYS_GetLinkBySrc(byref(src), byref(dst))
            if ret == 0:
                for i in range(dst.u32DestNum):
                    dst_link.append({'mod_id': dst.astDestMod[i].enModId, 'grp_id': dst.astDestMod[i].s32GrpId, 'chn_id': dst.astDestMod[i].s32ChnId})
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return dst_link, ret


def get_cur_pts() -> tuple[int, int]:
    """
    Get current pts

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_GetCurPTS(AX_U64 *pu64CurPTS);`
        **python**              `cur_pts, ret = axcl.sys.get_cur_pts()`
        ======================= =====================================================

    :returns: tuple[int, int]

        - **cur_pts** (*int*) - current pts
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    cur_pts = AX_U64(0)
    try:
        libaxcl_sys.AXCL_SYS_GetCurPTS.restype = AX_S32
        libaxcl_sys.AXCL_SYS_GetCurPTS.argtypes=[POINTER(AX_U64)]

        ret = libaxcl_sys.AXCL_SYS_GetCurPTS(byref(cur_pts))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return cur_pts.value, ret


def init_pts_base(pts_base: int) -> int:
    """
    Init pts base

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_InitPTSBase(AX_U64 u64PTSBase);`
        **python**              `ret = axcl.sys.init_pts_base(pts_base)`
        ======================= =====================================================

    :param int pts_base: pts base
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_InitPTSBase.restype = AX_S32
        libaxcl_sys.AXCL_SYS_InitPTSBase.argtypes=[AX_U64]
        c_pts_base = AX_U64(pts_base)

        ret = libaxcl_sys.AXCL_SYS_InitPTSBase(c_pts_base)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def sync_pts(pts_base: int) -> int:
    """
    Init pts base

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_SYS_SyncPTS(AX_U64 u64PTSBase);`
        **python**              `ret = axcl.sys.sync_pts(pts_base)`
        ======================= =====================================================

    :param int pts_base: pts base
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_SYS_SyncPTS.restype = AX_S32
        libaxcl_sys.AXCL_SYS_SyncPTS.argtypes=[AX_U64]
        c_pts_base = AX_U64(pts_base)

        ret = libaxcl_sys.AXCL_SYS_SyncPTS(c_pts_base)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_chip_type() -> int:
    """
    Get chip type

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_CHIP_TYPE_E AXCL_SYS_GetChipType(AX_VOID);`
        **python**              `chip_type = axcl.sys.get_chip_type()`
        ======================= =====================================================

    :returns: **chip_type** (*int*) - chip type: :class:`AX_CHIP_TYPE_E <axcl.sys.axcl_sys_type.AX_CHIP_TYPE_E>`,
    """
    chip_type = 0
    try:
        libaxcl_sys.AXCL_SYS_GetChipType.restype = AX_S32

        chip_type = libaxcl_sys.AXCL_SYS_GetChipType()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return chip_type
