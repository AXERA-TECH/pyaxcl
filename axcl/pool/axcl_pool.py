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
from axcl.utils.axcl_utils import *
from axcl.utils.axcl_logger import *


def set_config(pool_floor_plan: list) -> int:
    """
    Set cmm pool configure

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_SetConfig(const AX_POOL_FLOORPLAN_T *pPoolFloorPlan);`
        **python**              `ret = axcl.pool.set_config(pool_floor_plan)`
        ======================= =====================================================

    :param list pool_floor_plan: list of pool :class:`AX_POOL_CONFIG_T <axcl.sys.axcl_sys_type.AX_POOL_CONFIG_T>`
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    plan = AX_POOL_FLOORPLAN_T()
    try:
        libaxcl_sys.AXCL_POOL_SetConfig.restype = AX_S32
        libaxcl_sys.AXCL_POOL_SetConfig.argtypes=[POINTER(AX_POOL_FLOORPLAN_T)]
        if pool_floor_plan:
            i = 0
            for pool in pool_floor_plan:
                plan.CommPool[i].MetaSize = AX_U64(pool.get('meta_size',0))
                plan.CommPool[i].BlkSize = AX_U64(pool.get('blk_size',0))
                plan.CommPool[i].BlkCnt = AX_U32(pool.get('blk_cnt',0))
                plan.CommPool[i].IsMergeMode = AX_BOOL(1 if pool.get('is_merge_mode', False) else 0)
                plan.CommPool[i].CacheMode = AX_POOL_CACHE_MODE_E(pool.get('cache_mode',0))
                partition_name = pool.get('partition_name', [])
                plan.CommPool[i].PartitionName = dict_array_to_array(partition_name, AX_S8, AX_MAX_PARTITION_NAME_LEN)

                pool_name = pool.get('pool_name', [])
                plan.CommPool[i].PoolName = dict_array_to_array(pool_name, AX_S8, AX_MAX_POOL_NAME_LEN)

                i = i + 1

            ret = libaxcl_sys.AXCL_POOL_SetConfig(byref(plan))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_config() -> tuple[list, int]:
    """
    Get cmm pool configure

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_GetConfig(AX_POOL_FLOORPLAN_T *pPoolFloorPlan);`
        **python**              `pool_floor_plan, ret = axcl.pool.get_config()`
        ======================= =====================================================

    :returns: tuple[list, int]

        - **pool_floor_plan** (*list*) - list of pool :class:`AX_POOL_CONFIG_T <axcl.sys.axcl_sys_type.AX_POOL_CONFIG_T>`
        - **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    plan = AX_POOL_FLOORPLAN_T()
    pool_floor_plan = []
    try:
        libaxcl_sys.AXCL_POOL_GetConfig.restype = AX_S32
        libaxcl_sys.AXCL_POOL_GetConfig.argtypes=[POINTER(AX_POOL_FLOORPLAN_T)]
        ret = libaxcl_sys.AXCL_POOL_GetConfig(byref(plan))
        if ret == 0:
            for i in range(AX_MAX_COMM_POOLS):
                if plan.CommPool[i].BlkSize > 0:
                    pool = {}
                    pool['meta_size'] = plan.CommPool[i].MetaSize
                    pool['blk_size'] = plan.CommPool[i].BlkSize
                    pool['blk_cnt'] = plan.CommPool[i].BlkCnt
                    pool['is_merge_mode'] = False if plan.CommPool[i].IsMergeMode == 0 else True
                    pool['cache_mode'] = plan.CommPool[i].CacheMode
                    pool['partition_name'] = cast(plan.CommPool[i].PartitionName, c_char_p).value.decode('utf-8')
                    pool['pool_name'] = cast(plan.CommPool[i].PoolName, c_char_p).value.decode('utf-8')
                    pool_floor_plan.append(pool)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return pool_floor_plan, ret


def init() -> int:
    """
    Init cmm pool

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_Init(AX_VOID);`
        **python**              `ret = axcl.pool.init()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_Init.restype = AX_S32
        ret = libaxcl_sys.AXCL_POOL_Init()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def exit() -> int:
    """
    Exit cmm pool

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_Exit(AX_VOID);`
        **python**              `ret = axcl.pool.exit()`
        ======================= =====================================================

    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_Exit.restype = AX_S32
        ret = libaxcl_sys.AXCL_POOL_Exit()
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def create_pool(pool_config: dict) -> int:
    """
    Create cmm pool

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_POOL AXCL_POOL_CreatePool(AX_POOL_CONFIG_T *pPoolConfig);`
        **python**              `pool_id = axcl.pool.create_pool(pool_config)`
        ======================= =====================================================

    :param dict pool_config: pool configure :class:`AX_POOL_CONFIG_T <axcl.sys.axcl_sys_type.AX_POOL_CONFIG_T>`
    :returns: **pool_id** (*int*) - pool id, -1 indicates failure, otherwise success
    """
    pool_id = AX_INVALID_POOLID
    config = AX_POOL_CONFIG_T()
    try:
        libaxcl_sys.AXCL_POOL_CreatePool.restype = AX_POOL
        libaxcl_sys.AXCL_POOL_CreatePool.argtypes=[POINTER(AX_POOL_CONFIG_T)]

        if pool_config:
            config.MetaSize = AX_U64(pool_config.get('meta_size', 0))
            config.BlkSize = AX_U64(pool_config.get('blk_size', 0))
            config.BlkCnt = AX_U32(pool_config.get('blk_cnt', 0))
            config.IsMergeMode = AX_BOOL(1 if pool_config.get('is_merge_mode', False) else 0)
            config.CacheMode = AX_POOL_CACHE_MODE_E(pool_config.get('cache_mode', 0))
            partition_name = pool_config.get('partition_name', [])
            config.PartitionName = dict_array_to_array(partition_name, AX_S8, AX_MAX_PARTITION_NAME_LEN)

            pool_name = pool_config.get('pool_name', [])
            config.PoolName = dict_array_to_array(pool_name, AX_S8, AX_MAX_POOL_NAME_LEN)

            pool_id = libaxcl_sys.AXCL_POOL_CreatePool(byref(config))
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return pool_id


def destroy_pool(pool_id: int) -> int:
    """
    Create cmm pool

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_DestroyPool(AX_POOL PoolId);`
        **python**              `ret = axcl.pool.destroy_pool(pool_id)`
        ======================= =====================================================

    :param int pool_id: pool id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_DestroyPool.restype = AX_S32
        libaxcl_sys.AXCL_POOL_DestroyPool.argtypes=[AX_POOL]
        c_pool_id = AX_POOL(pool_id)
        ret = libaxcl_sys.AXCL_POOL_DestroyPool(c_pool_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_block(pool_id: int, blk_size: int, partition_name: str) -> int:
    """
    Get block

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_BLK AXCL_POOL_GetBlock(AX_POOL PoolId, AX_U64 BlkSize, const AX_S8 *pPartitionName);`
        **python**              `blk_id = axcl.pool.get_block(pool_id, blk_size, partition_name)`
        ======================= =====================================================

    :param int pool_id: pool id
    :param int blk_size: block size
    :param str partition_name: partition name
    :returns: **blk_id** (*int*) - 0 indicates failure, otherwise success
    """
    blk_id = AX_INVALID_BLOCKID
    try:
        libaxcl_sys.AXCL_POOL_GetBlock.restype = AX_BLK
        libaxcl_sys.AXCL_POOL_GetBlock.argtypes=[AX_POOL, AX_U64, c_char_p]
        c_pool_id = AX_POOL(pool_id)
        c_blk_size = AX_U64(blk_size)
        c_partition_name = c_char_p(0)
        if partition_name and len(partition_name) > 0:
            c_partition_name = c_char_p(partition_name.encode('utf-8'))

        blk_id = libaxcl_sys.AXCL_POOL_GetBlock(c_pool_id, c_blk_size, c_partition_name)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return blk_id


def release_block(blk_id: int) -> int:
    """
    Release block

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_ReleaseBlock(AX_BLK BlockId);`
        **python**              `ret = axcl.pool.release_block(blk_id)`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_ReleaseBlock.restype = AX_U32
        libaxcl_sys.AXCL_POOL_ReleaseBlock.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        ret = libaxcl_sys.AXCL_POOL_ReleaseBlock(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def phy_addr_to_handle(phy_addr: int) -> int:
    """
    Convert physical address to block id

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AX_BLK AXCL_POOL_PhysAddr2Handle(AX_U64 PhysAddr);`
        **python**              `blk_id = axcl.pool.phy_addr_to_handle(phy_addr)`
        ======================= =====================================================

    :param int phy_addr: physical address
    :returns: **blk_id** (*int*) - 0 indicates failure, otherwise success
    """
    blk_id = AX_INVALID_BLOCKID
    try:
        libaxcl_sys.AXCL_POOL_PhysAddr2Handle.restype = AX_BLK
        libaxcl_sys.AXCL_POOL_PhysAddr2Handle.argtypes=[AX_U64]
        c_phy_addr = AX_U64(phy_addr)

        blk_id = libaxcl_sys.AXCL_POOL_PhysAddr2Handle(c_phy_addr)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return blk_id


def handle_to_phy_addr(blk_id: int) -> int:
    """
    Convert block id to physical address

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_U64 AXCL_POOL_Handle2PhysAddr(AX_BLK BlockId);`
        **python**              `phy_addr = axcl.pool.handle_to_phy_addr(blk_id)`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **phy_addr** (*int*) - physical address
    """
    phy_addr = AX_U64(0)
    try:
        libaxcl_sys.AXCL_POOL_Handle2PhysAddr.restype = AX_U64
        libaxcl_sys.AXCL_POOL_Handle2PhysAddr.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        phy_addr = libaxcl_sys.AXCL_POOL_Handle2PhysAddr(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return phy_addr


def handle_to_meta_phy_addr(blk_id: int) -> int:
    """
    Convert block id to meta physical address

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_U64 AXCL_POOL_Handle2MetaPhysAddr(AX_BLK BlockId);`
        **python**              `phy_addr = axcl.pool.handle_to_meta_phy_addr(blk_id)`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **phy_addr** (*int*) - meta physical address
    """
    phy_addr = AX_U64(0)
    try:
        libaxcl_sys.AXCL_POOL_Handle2MetaPhysAddr.restype = AX_U64
        libaxcl_sys.AXCL_POOL_Handle2MetaPhysAddr.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        phy_addr = libaxcl_sys.AXCL_POOL_Handle2MetaPhysAddr(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return phy_addr


def handle_to_pool_id(blk_id: int) -> int:
    """
    Convert block id to pool id

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_POOL AXCL_POOL_Handle2PoolId(AX_BLK BlockId);`
        **python**              `pool_id = axcl.pool.handle_to_pool_id(blk_id)`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **pool_id** (*int*) - pool id, -1 indicates failure, otherwise success
    """
    pool_id = AX_INVALID_POOLID
    try:
        libaxcl_sys.AXCL_POOL_Handle2PoolId.restype = AX_POOL
        libaxcl_sys.AXCL_POOL_Handle2PoolId.argtypes=[AX_BLK]
        c_blk_id = AX_U32(blk_id)

        pool_id = libaxcl_sys.AXCL_POOL_Handle2PoolId(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return pool_id


def handle_to_blk_size(blk_id: int) -> int:
    """
    Get block size by block id

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_U64 AXCL_POOL_Handle2BlkSize(AX_BLK BlockId);`
        **python**              `blk_size = axcl.pool.handle_to_blk_size(blk_id)`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **blk_size** (*int*) - block size
    """
    blk_size = AX_U64(0)
    try:
        libaxcl_sys.AXCL_POOL_Handle2BlkSize.restype = AX_U64
        libaxcl_sys.AXCL_POOL_Handle2BlkSize.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        blk_size = libaxcl_sys.AXCL_POOL_Handle2BlkSize(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return blk_size


def mmap_pool(pool_id: int) -> int:
    """
    Map cmm pool

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_MmapPool(AX_POOL PoolId);`
        **python**              `ret = axcl.pool.mmap_pool(pool_id)`
        ======================= =====================================================

    :param int pool_id: pool id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_MmapPool.restype = AX_S32
        libaxcl_sys.AXCL_POOL_MmapPool.argtypes=[AX_POOL]
        c_pool_id = AX_POOL(pool_id)

        ret = libaxcl_sys.AXCL_POOL_MmapPool(c_pool_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def munmap_pool(pool_id: int) -> int:
    """
    Unmap cmm pool

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_MunmapPool(AX_POOL PoolId);`
        **python**              `ret = axcl.pool.munmap_pool(pool_id)`
        ======================= =====================================================

    :param int pool_id: pool id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_MunmapPool.restype = AX_S32
        libaxcl_sys.AXCL_POOL_MunmapPool.argtypes=[AX_POOL]
        c_pool_id = AX_POOL(pool_id)

        ret = libaxcl_sys.AXCL_POOL_MunmapPool(c_pool_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def get_block_vir_addr(blk_id: int) -> int:
    """
    Get virtual address of block

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID *AXCL_POOL_GetBlockVirAddr(AX_BLK BlockId);`
        **python**              `vir_addr = axcl.pool.get_block_vir_addr(blk_id))`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **vir_addr** (*int*) - virtual address
    """
    vir_addr = None
    try:
        libaxcl_sys.AXCL_POOL_GetBlockVirAddr.restype = c_void_p
        libaxcl_sys.AXCL_POOL_GetBlockVirAddr.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        vir_addr = libaxcl_sys.AXCL_POOL_GetBlockVirAddr(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return vir_addr


def get_meta_vir_addr(blk_id: int) -> int:
    """
    Get meta virtual address of block

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_VOID *AXCL_POOL_GetMetaVirAddr(AX_BLK BlockId);`
        **python**              `vir_addr = axcl.pool.get_meta_vir_addr(blk_id))`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **vir_addr** (*int*) - virtual address
    """
    vir_addr = None
    try:
        libaxcl_sys.AXCL_POOL_GetMetaVirAddr.restype = c_void_p
        libaxcl_sys.AXCL_POOL_GetMetaVirAddr.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        vir_addr = libaxcl_sys.AXCL_POOL_GetMetaVirAddr(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return vir_addr


def increase_ref_cnt(blk_id: int) -> int:
    """
    Increase reference count of block

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_IncreaseRefCnt(AX_BLK BlockId);`
        **python**              `ret = axcl.pool.increase_ref_cnt(blk_id))`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_IncreaseRefCnt.restype = AX_S32
        libaxcl_sys.AXCL_POOL_IncreaseRefCnt.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        ret = libaxcl_sys.AXCL_POOL_IncreaseRefCnt(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret


def decrease_ref_cnt(blk_id: int) -> int:
    """
    Decrease reference count of block

    .. table::

        ======================= =====================================================
        **Language**            **Function Prototype**
        ======================= =====================================================
        **C**                   `AX_S32 AXCL_POOL_DecreaseRefCnt(AX_BLK BlockId);`
        **python**              `ret = axcl.pool.decrease_ref_cnt(blk_id))`
        ======================= =====================================================

    :param int blk_id: block id
    :returns: **ret** (*int*) - 0 indicates success, otherwise failure
    """
    ret = -1
    try:
        libaxcl_sys.AXCL_POOL_DecreaseRefCnt.restype = AX_S32
        libaxcl_sys.AXCL_POOL_DecreaseRefCnt.argtypes=[AX_BLK]
        c_blk_id = AX_BLK(blk_id)

        ret = libaxcl_sys.AXCL_POOL_DecreaseRefCnt(c_blk_id)
    except:
        log_error(sys.exc_info())
        log_error(traceback.format_exc())
    finally:
        return ret
