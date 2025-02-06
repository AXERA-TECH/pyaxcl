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

from ctypes import Structure

from axcl.ax_global_type import *

AX_INVALID_POOLID  = -1
AX_INVALID_BLOCKID = 0

AX_MAX_POOLS = 1024
AX_MAX_COMM_POOLS = 64
AX_MAX_BLKS_PER_POOL = 1024

AX_MAX_POOL_NAME_LEN = 32
AX_MAX_PARTITION_NAME_LEN = 32
AX_MAX_PARTITION_COUNT = 16

AX_MEM_CACHED = 1 << 1    # alloc mem is cached
AX_MEM_NONCACHED = 1 << 2 # alloc mem is not cached

class AX_PARTITION_INFO_T(Structure):
    """
    .. parsed-literal::

        dict_partition_info = {
            "phy_addr": int,
            "size_kbyte": int,
            "name": str
        }
    """
    _fields_ = [
        ("PhysAddr", AX_U64),
        ("SizeKB", AX_U32),
        ("Name", AX_CHAR * AX_MAX_PARTITION_NAME_LEN)
    ]

    field_aliases = {
        "PhysAddr": "phy_addr",
        "SizeKB": "size_kbyte",
        "Name": "name"
    }

class AX_CMM_PARTITION_INFO_T(Structure):
    _fields_ = [
        ("PartitionCnt", AX_U32),
        ("PartitionInfo", AX_PARTITION_INFO_T * AX_MAX_PARTITION_COUNT)
    ]


class AX_CMM_STATUS_T(Structure):
    """
    .. parsed-literal::

        dict_cmm_status = {
            "total_size": int,
            "remain_size": int,
            "block_cnt": int,
            "partition": list of :class:`AX_PARTITION_INFO_T <axcl.sys.axcl_sys_type.AX_PARTITION_INFO_T>`
        }
    """
    _fields_ = [
        ("TotalSize", AX_U32),
        ("RemainSize", AX_U32),
        ("BlockCnt", AX_U32),
        ("Partition", AX_CMM_PARTITION_INFO_T)
    ]

    field_aliases = {
        "TotalSize": "total_size",
        "RemainSize": "remain_size",
        "BlockCnt": "block_cnt",
        "Partition": "partition"
    }

AX_POOL = AX_U32
AX_BLK = AX_U32

AX_POOL_CACHE_MODE_E = AX_S32
"""
    pool cache mode

    .. parsed-literal::

        POOL_CACHE_MODE_NONCACHE = 0
        POOL_CACHE_MODE_CACHED   = 1
        POOL_CACHE_MODE_BUTT     = 2
"""
POOL_CACHE_MODE_NONCACHE = 0
POOL_CACHE_MODE_CACHED = 1
POOL_CACHE_MODE_BUTT = 2


AX_POOL_SOURCE_E = AX_S32
"""
    pool source

    .. parsed-literal::

        POOL_SOURCE_COMMON  = 0
        POOL_SOURCE_PRIVATE = 1
        POOL_SOURCE_USER    = 2
        POOL_SOURCE_BUTT    = 3
"""
POOL_SOURCE_COMMON = 0
POOL_SOURCE_PRIVATE = 1
POOL_SOURCE_USER = 2
POOL_SOURCE_BUTT = 3

class AX_POOL_CONFIG_T(Structure):
    """
    .. parsed-literal::

        dict_pool_config = {
            "meta_size": int,
            "blk_size": int,
            "blk_cnt": int,
            "is_merge_mode": bool,
            "cache_mode": :class:`AX_POOL_CACHE_MODE_E <axcl.sys.axcl_sys_type.AX_POOL_CACHE_MODE_E>`,
            "partition_name": str,
            "pool_name": str
        }
    """
    _fields_ = [
        ("MetaSize", AX_U64),
        ("BlkSize", AX_U64),
        ("BlkCnt", AX_U32),
        ("IsMergeMode", AX_BOOL),
        ("CacheMode", AX_POOL_CACHE_MODE_E),
        ("PartitionName", AX_S8 * AX_MAX_PARTITION_NAME_LEN),
        ("PoolName", AX_S8 * AX_MAX_POOL_NAME_LEN)
    ]

    field_aliases = {
        "MetaSize": "meta_size",
        "BlkSize": "blk_size",
        "BlkCnt": "blk_cnt",
        "IsMergeMode": "is_merge_mode",
        "CacheMode": "cache_mode",
        "PartitionName": "partition_name",
        "PoolName": "pool_name",
    }

class AX_POOL_FLOORPLAN_T(Structure):
    _fields_ = [
        ("CommPool", AX_POOL_CONFIG_T * AX_MAX_COMM_POOLS)
    ]

AX_CHIP_TYPE_E = AX_S32
"""
    chip type

    .. parsed-literal::

        NONE_CHIP_TYPE = 0
        AX650A_CHIP    = 1
        AX650N_CHIP    = 2
        AX650C_CHIP    = 3
        AX750_CHIP     = 4
        AX650_CHIP_MAX = 5
"""
NONE_CHIP_TYPE = 0
AX650A_CHIP = 1
AX650N_CHIP = 2
AX650C_CHIP = 3
AX750_CHIP = 4
AX650_CHIP_MAX = 5