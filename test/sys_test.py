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


class TestSys():
    def test_init(self):
        ret = axcl.sys.init()

        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(None, output_args)

    def test_deinit(self):
        ret = axcl.sys.deinit()

        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(None, output_args)

    def test_mem_alloc(self):
        size = create_random_int(1, 4*1024*1024*1024)
        align = create_random_int(1, 1024*1024)
        token = choose_random_from_list(['name', '', None])

        phy_addr, vir_addr, ret = axcl.sys.mem_alloc(size, align, token)

        if token and len(token) > 0:
            c_token = create_data_array_from_str(token)
            inputs_args = serialize_ctypes_args(AX_U32(size), AX_U32(align), c_token)
        else:
            inputs_args = serialize_ctypes_args(AX_U32(size), AX_U32(align))
        output_args = serialize_ctypes_args(AX_S32(ret), AX_U64(phy_addr), c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_alloc_cached(self):
        size = create_random_int(1, 4*1024*1024*1024)
        align = create_random_int(1, 1024*1024)
        token = choose_random_from_list(['name', '', None])

        phy_addr, vir_addr, ret = axcl.sys.mem_alloc_cached(size, align, token)

        if token and len(token) > 0:
            c_token = create_data_array_from_str(token)
            inputs_args = serialize_ctypes_args(AX_U32(size), AX_U32(align), c_token)
        else:
            inputs_args = serialize_ctypes_args(AX_U32(size), AX_U32(align))
        output_args = serialize_ctypes_args(AX_S32(ret), AX_U64(phy_addr), c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_free(self):
        phy_addr = create_random_int(1, MAX_UINT64)
        vir_addr = create_random_int(1, MAX_UINT64)

        ret = axcl.sys.mem_free(phy_addr, vir_addr)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr), c_void_p(vir_addr))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mmap(self):
        phy_addr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)

        vir_addr = axcl.sys.mmap(phy_addr, size)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr), AX_U32(size))
        output_args = serialize_ctypes_args(c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mmap_cache(self):
        phy_addr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)

        vir_addr = axcl.sys.mmap_cache(phy_addr, size)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr), AX_U32(size))
        output_args = serialize_ctypes_args(c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mmap_fast(self):
        phy_addr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)

        vir_addr = axcl.sys.mmap_fast(phy_addr, size)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr), AX_U32(size))
        output_args = serialize_ctypes_args(c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mmap_cache_fast(self):
        phy_addr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)

        vir_addr = axcl.sys.mmap_cache_fast(phy_addr, size)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr), AX_U32(size))
        output_args = serialize_ctypes_args(c_void_p(vir_addr))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_munmap(self):
        vir_addr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)

        ret = axcl.sys.munmap(vir_addr, size)

        inputs_args = serialize_ctypes_args(c_void_p(vir_addr), AX_U32(size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mflush_cache(self):
        phy_addr = create_random_int(1, MAX_UINT64)
        vir_addr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)

        ret = axcl.sys.mflush_cache(phy_addr, vir_addr, size)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr), c_void_p(vir_addr), AX_U32(size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_minvalidate_cache(self):
        phy_addr = create_random_int(1, MAX_UINT64)
        vir_addr = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)

        ret = axcl.sys.minvalidate_cache(phy_addr, vir_addr, size)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr), c_void_p(vir_addr), AX_U32(size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_get_block_info_by_phy(self):
        phy_addr = create_random_int(1, MAX_UINT64)

        mem_type, vir_addr, block_size, ret = axcl.sys.mem_get_block_info_by_phy(phy_addr)

        inputs_args = serialize_ctypes_args(AX_U64(phy_addr))
        output_args = serialize_ctypes_args(AX_S32(ret), AX_S32(mem_type), c_void_p(vir_addr), AX_U32(block_size))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_get_block_info_by_virt(self):
        vir_addr = create_random_int(1, MAX_UINT64)

        phy_addr, mem_type, ret = axcl.sys.mem_get_block_info_by_virt(vir_addr)

        inputs_args = serialize_ctypes_args(c_void_p(vir_addr))
        output_args = serialize_ctypes_args(AX_S32(ret), AX_U64(phy_addr), AX_S32(mem_type))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_get_partition_info(self):
        d_cmm_part_info, ret = axcl.sys.mem_get_partition_info()

        c_cmm_part_info = AX_CMM_PARTITION_INFO_T()
        c_cmm_part_info.PartitionCnt = len(d_cmm_part_info)
        for i in range(c_cmm_part_info.PartitionCnt):
            c_cmm_part_info.PartitionInfo[i].PhysAddr = d_cmm_part_info[i]['phy_addr']
            c_cmm_part_info.PartitionInfo[i].SizeKB = d_cmm_part_info[i]['size_kbyte']
            c_cmm_part_info.PartitionInfo[i].Name = d_cmm_part_info[i]['name'].encode('utf-8')
        output_args = serialize_ctypes_args(AX_S32(ret), c_cmm_part_info)
        assert 0 == check_input_output(None, output_args)

    def test_mem_set_config(self):
        c_mod_info = create_random_struct_instance(AX_MOD_INFO_T)
        partition_name = choose_random_from_list(['name', '', None])

        ret = axcl.sys.mem_set_config(c_mod_info.struct2dict(), partition_name)

        if partition_name and len(partition_name) > 0:
            c_partition_name = create_data_array_from_str(partition_name)
            inputs_args = serialize_ctypes_args(c_mod_info, c_partition_name)
        else:
            inputs_args = serialize_ctypes_args(c_mod_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_get_config(self):
        c_mod_info = create_random_struct_instance(AX_MOD_INFO_T)

        partition_name, ret = axcl.sys.mem_get_config(c_mod_info.struct2dict())

        inputs_args = serialize_ctypes_args(c_mod_info)
        if partition_name and len(partition_name) > 0:
            c_partition_name = create_data_array_from_str(partition_name)
            output_args = serialize_ctypes_args(AX_S32(ret), c_partition_name)
        else:
            output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_mem_query_status(self):
        d_cmm_status, ret = axcl.sys.mem_query_status()

        c_cmm_status = AX_CMM_STATUS_T()
        c_cmm_status.TotalSize = d_cmm_status['total_size']
        c_cmm_status.RemainSize = d_cmm_status['remain_size']
        c_cmm_status.BlockCnt = d_cmm_status['block_cnt']
        c_cmm_status.Partition.PartitionCnt = len(d_cmm_status['partition'])
        for i in range(c_cmm_status.Partition.PartitionCnt):
            c_cmm_status.Partition.PartitionInfo[i].PhysAddr = d_cmm_status['partition'][i]['phy_addr']
            c_cmm_status.Partition.PartitionInfo[i].SizeKB = d_cmm_status['partition'][i]['size_kbyte']
            c_cmm_status.Partition.PartitionInfo[i].Name = d_cmm_status['partition'][i]['name'].encode('utf-8')
        output_args = serialize_ctypes_args(AX_S32(ret), c_cmm_status)
        assert 0 == check_input_output(None, output_args)

    def test_link(self):
        c_src_mod_info = create_random_struct_instance(AX_MOD_INFO_T)
        c_dst_mod_info = create_random_struct_instance(AX_MOD_INFO_T)

        ret = axcl.sys.link(c_src_mod_info.struct2dict(), c_dst_mod_info.struct2dict())

        inputs_args = serialize_ctypes_args(c_src_mod_info, c_dst_mod_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_unlink(self):
        c_src_mod_info = create_random_struct_instance(AX_MOD_INFO_T)
        c_dst_mod_info = create_random_struct_instance(AX_MOD_INFO_T)

        ret = axcl.sys.unlink(c_src_mod_info.struct2dict(), c_dst_mod_info.struct2dict())

        inputs_args = serialize_ctypes_args(c_src_mod_info, c_dst_mod_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_link_by_dest(self):
        c_dst_mod_info = create_random_struct_instance(AX_MOD_INFO_T)

        d_src_mod_info, ret = axcl.sys.get_link_by_dest(c_dst_mod_info.struct2dict())

        inputs_args = serialize_ctypes_args(c_dst_mod_info)
        c_src_mod_info = AX_MOD_INFO_T()
        c_src_mod_info.dict2struct(d_src_mod_info)
        output_args = serialize_ctypes_args(AX_S32(ret), c_src_mod_info)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_link_by_src(self):
        c_src_mod_info = create_random_struct_instance(AX_MOD_INFO_T)

        d_dst_link, ret = axcl.sys.get_link_by_src(c_src_mod_info.struct2dict())

        inputs_args = serialize_ctypes_args(c_src_mod_info)
        c_dst_link = AX_LINK_DEST_T()
        c_dst_link.u32DestNum = len(d_dst_link)
        for i in range(c_dst_link.u32DestNum):
            c_dst_link.astDestMod[i].enModId = d_dst_link[i]['mod_id']
            c_dst_link.astDestMod[i].s32GrpId = d_dst_link[i]['grp_id']
            c_dst_link.astDestMod[i].s32ChnId = d_dst_link[i]['chn_id']

        output_args = serialize_ctypes_args(AX_S32(ret), c_dst_link)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_cur_pts(self):
        cur_pts, ret = axcl.sys.get_cur_pts()

        output_args = serialize_ctypes_args(AX_S32(ret), AX_U64(cur_pts))
        assert 0 == check_input_output(None, output_args)

    def test_init_pts_base(self):
        pts_base = create_random_int(1, MAX_UINT64)

        ret = axcl.sys.init_pts_base(pts_base)

        inputs_args = serialize_ctypes_args(AX_U64(pts_base))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_sync_pts(self):
        pts_base = create_random_int(1, MAX_UINT64)

        ret = axcl.sys.sync_pts(pts_base)

        inputs_args = serialize_ctypes_args(AX_U64(pts_base))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_get_chip_type(self):
        chip_type = axcl.sys.get_chip_type()
        assert AX650N_CHIP == chip_type
