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

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

import axcl
from axcl.ax_global_type import *
from axcl.sys.axcl_sys_type import *
from ut_help import *


def get_pool_config_from_dict(pool_config: dict) -> AX_POOL_CONFIG_T:
    c_pool_config = AX_POOL_CONFIG_T()
    c_pool_config.MetaSize = pool_config['meta_size']
    c_pool_config.BlkSize = pool_config['blk_size']
    c_pool_config.BlkCnt = pool_config['blk_cnt']
    c_pool_config.IsMergeMode = pool_config['is_merge_mode']
    c_pool_config.CacheMode = pool_config['cache_mode']
    c_pool_config.PartitionName = dict_array_to_array(pool_config['partition_name'], AX_S8, AX_MAX_PARTITION_NAME_LEN)
    c_pool_config.PoolName = dict_array_to_array(pool_config['pool_name'], AX_S8, AX_MAX_POOL_NAME_LEN)
    return c_pool_config


def get_pool_floor_plan_struct_from_list(pool_floor_plan: list) -> AX_POOL_FLOORPLAN_T:
    c_pool_floor_plan = AX_POOL_FLOORPLAN_T()
    for i in range(len(pool_floor_plan)):
        c_pool_floor_plan.CommPool[i] = get_pool_config_from_dict(pool_floor_plan[i])
    return c_pool_floor_plan


class TestPool():
    def test_set_config(self):
        pool_floor_plan = []
        count = create_random_int(1, AX_MAX_COMM_POOLS)
        for i in range(count):
            pool_floor_plan.append({
                'meta_size': create_random_int(1, 1024*1024),
                'blk_size': create_random_int(1, 1024*1024),
                'blk_cnt': create_random_int(1, 1024*1024),
                'is_merge_mode': choose_random_from_list([True, False]),
                'cache_mode': choose_random_from_list([POOL_CACHE_MODE_NONCACHE, POOL_CACHE_MODE_CACHED]),
                'partition_name': "part{}".format(i),
                'pool_name': "pool{}".format(i)
            })

        ret = axcl.pool.set_config(pool_floor_plan)

        inputs_args = serialize_ctypes_args(get_pool_floor_plan_struct_from_list(pool_floor_plan))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_config(self):
        pool_floor_plan, ret = axcl.pool.get_config()

        output_args = serialize_ctypes_args(AX_S32(ret), get_pool_floor_plan_struct_from_list(pool_floor_plan))
        assert 0 == check_input_output(None, output_args)

    def test_init(self):
        ret = axcl.pool.init()

        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(None, output_args)

    def test_exit(self):
        ret = axcl.pool.exit()

        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(None, output_args)

    def test_create_pool(self):
        pool_config = {
            'meta_size': create_random_int(1, 1024*1024),
            'blk_size': create_random_int(1, 1024*1024),
            'blk_cnt': create_random_int(1, 1024*1024),
            'is_merge_mode': choose_random_from_list([True, False]),
            'cache_mode': choose_random_from_list([POOL_CACHE_MODE_NONCACHE, POOL_CACHE_MODE_CACHED]),
            'partition_name': "part{}".format(create_random_int(0, 255)),
            'pool_name': "pool{}".format(create_random_int(0, 255))
        }

        pool_id = axcl.pool.create_pool(pool_config)

        inputs_args = serialize_ctypes_args(get_pool_config_from_dict(pool_config))
        output_args = serialize_ctypes_args(AX_POOL(pool_id))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_destroy_pool(self):
        pool_id = create_random_int(0, 255)

        ret = axcl.pool.destroy_pool(pool_id)

        inputs_args = serialize_ctypes_args(AX_POOL(pool_id))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_block(self):
        pool_id = create_random_int(0, 255)
        blk_size = create_random_int(1, 1024*1024)
        partition_name = choose_random_from_list(['name', None, ''])

        blk_id = axcl.pool.get_block(pool_id, blk_size, partition_name)

        if partition_name and len(partition_name) > 0:
            c_partition_name = create_data_array_from_str(partition_name)
            inputs_args = serialize_ctypes_args(AX_POOL(pool_id), AX_U64(blk_size), c_partition_name)
        else:
            inputs_args = serialize_ctypes_args(AX_POOL(pool_id), AX_U64(blk_size))
        output_args = serialize_ctypes_args(AX_BLK(blk_id))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_release_block(self):
        blk_id = create_random_int(1, MAX_UINT32)

        ret = axcl.pool.release_block(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_phy_addr_to_handle(self):
        phy_addr = create_random_int(1, MAX_UINT64)

        blk_id = axcl.pool.phy_addr_to_handle(phy_addr)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr))
        output_args = serialize_ctypes_args(AX_BLK(blk_id))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_handle_to_phy_addr(self):
        blk_id = create_random_int(1, MAX_UINT32)

        phy_addr = axcl.pool.handle_to_phy_addr(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(AX_U64(phy_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_handle_to_meta_phy_addr(self):
        blk_id = create_random_int(1, MAX_UINT32)

        phy_addr = axcl.pool.handle_to_meta_phy_addr(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(AX_U64(phy_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_handle_to_pool_id(self):
        blk_id = create_random_int(1, MAX_UINT32)

        pool_id = axcl.pool.handle_to_pool_id(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(AX_POOL(pool_id))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_handle_to_blk_size(self):
        blk_id = create_random_int(1, MAX_UINT32)

        blk_size = axcl.pool.handle_to_blk_size(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(AX_U64(blk_size))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mmap_pool(self):
        pool_id = create_random_int(1, 255)

        ret = axcl.pool.mmap_pool(pool_id)

        inputs_args = serialize_ctypes_args(AX_POOL(pool_id))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_munmap_pool(self):
        pool_id = create_random_int(1, 255)

        ret = axcl.pool.munmap_pool(pool_id)

        inputs_args = serialize_ctypes_args(AX_POOL(pool_id))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_block_vir_addr(self):
        blk_id = create_random_int(1, MAX_UINT32)

        vir_addr = axcl.pool.get_block_vir_addr(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_meta_vir_addr(self):
        blk_id = create_random_int(1, MAX_UINT32)

        vir_addr = axcl.pool.get_meta_vir_addr(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_increase_ref_cnt(self):
        blk_id = create_random_int(1, MAX_UINT32)

        ret = axcl.pool.increase_ref_cnt(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_decrease_ref_cnt(self):
        blk_id = create_random_int(1, MAX_UINT32)

        ret = axcl.pool.decrease_ref_cnt(blk_id)

        inputs_args = serialize_ctypes_args(AX_BLK(blk_id))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)
