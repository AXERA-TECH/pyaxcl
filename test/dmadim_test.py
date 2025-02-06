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
from axcl.dmadim.axcl_dmadim_type import *
from ut_help import *


class TestDmadim():
    def test_dmadim_open(self):
        sync = True if create_random_int(0, 1) > 0 else False

        ret = axcl.dmadim.open(sync)

        inputs_args = serialize_ctypes_args(AX_BOOL(1 if sync else 0))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_cfg(self):
        dma_chn = create_random_int()
        d_dma_msg = {
            'endian': choose_random_from_list([AX_DMADIM_ENDIAN_DEF, AX_DMADIM_ENDIAN_32, AX_DMADIM_ENDIAN_16]),
            'desc_buf': [
                {
                    'phy_src': create_random_int(0, MAX_UINT64),
                    'phy_dst': create_random_int(0, MAX_UINT64),
                    'size': create_random_int(0, MAX_UINT32)
                },
                {
                    'phy_src': create_random_int(0, MAX_UINT64),
                    'phy_dst': create_random_int(0, MAX_UINT64),
                    'size': create_random_int(0, MAX_UINT32)
                }
            ],
            'callback': None,
            'cb_arg': None,
            'dma_mode': choose_random_from_list([AX_DMADIM_1D, AX_DMADIM_2D, AX_DMADIM_3D, AX_DMADIM_4D, AX_DMADIM_MEMORY_INIT, AX_DMADIM_CHECKSUM])
        }
        ret = axcl.dmadim.cfg(dma_chn, d_dma_msg)

        c_dma_msg = AX_DMADIM_MSG_T()
        c_dma_msg.u32DescNum = len(d_dma_msg['desc_buf'])
        c_desc = (AX_DMADIM_DESC_T * c_dma_msg.u32DescNum)()
        for i in range(c_dma_msg.u32DescNum):
            c_desc[i].u64PhySrc = d_dma_msg['desc_buf'][i]['phy_src']
            c_desc[i].u64PhyDst = d_dma_msg['desc_buf'][i]['phy_dst']
            c_desc[i].u32Size = d_dma_msg['desc_buf'][i]['size']
        c_dma_msg.pDescBuf = cast(c_desc, c_void_p)
        c_dma_msg.eEndian = AX_DMADIM_ENDIAN_E(d_dma_msg['endian'])
        callback = d_dma_msg.get('callback', None)
        if callback:
            c_dma_msg.pfnCallBack = CFUNCTYPE(None, POINTER(AX_DMADIM_XFER_STAT_T), c_void_p)(callback)
        c_dma_msg.pCbArg = d_dma_msg.get('cb_arg', 0)
        c_dma_msg.eDmaMode = AX_DMADIM_XFER_MODE_E(d_dma_msg['dma_mode'])

        inputs_args = serialize_ctypes_args(AX_S32(dma_chn), AX_U32(c_dma_msg.u32DescNum), AX_U32(c_dma_msg.eEndian), AX_U32(c_dma_msg.eDmaMode), c_desc[0], c_desc[1])
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_start(self):
        dma_chn = create_random_int()
        dma_id = create_random_int()

        ret = axcl.dmadim.start(dma_chn, dma_id)

        inputs_args = serialize_ctypes_args(AX_S32(dma_chn), AX_S32(dma_id))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_wait_done(self):
        dma_chn = create_random_int()
        dma_id = create_random_int()
        timeout = create_random_int(-1, 1000000)

        xfer_stat, ret = axcl.dmadim.wait_done(dma_chn, dma_id, timeout)

        c_xfer_stat = AX_DMADIM_XFER_STAT_T()
        c_xfer_stat.dict2struct(xfer_stat)
        inputs_args = serialize_ctypes_args(AX_S32(dma_chn), AX_S32(dma_id), AX_S32(timeout))
        output_args = serialize_ctypes_args(AX_S32(ret), c_xfer_stat)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_close(self):
        dma_chn = create_random_int()
        ret = axcl.dmadim.close(dma_chn)
        inputs_args = serialize_ctypes_args(AX_S32(dma_chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_mem_copy(self):
        phy_dst = create_random_int(1, MAX_UINT64)
        phy_src = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)
        ret = axcl.dmadim.mem_copy(phy_dst, phy_src, size)
        inputs_args = serialize_ctypes_args(AX_U64(phy_dst), AX_U64(phy_src), AX_U64(size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_mem_set(self):
        phy_dst = create_random_int(1, MAX_UINT64)
        init_val = create_random_int(0, 255)
        size = create_random_int(1, MAX_UINT32)
        ret = axcl.dmadim.mem_set(phy_dst, init_val, size)
        inputs_args = serialize_ctypes_args(AX_U64(phy_dst), AX_U8(init_val), AX_U64(size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_mem_copy_xd(self):
        c_dim_desc = create_random_struct_instance(AX_DMADIM_DESC_XD_T)
        mode = choose_random_from_list([AX_DMADIM_1D, AX_DMADIM_2D, AX_DMADIM_3D, AX_DMADIM_4D])
        ret = axcl.dmadim.mem_copy_xd(c_dim_desc.struct2dict(), mode)
        inputs_args = serialize_ctypes_args(c_dim_desc, AX_DMADIM_XFER_MODE_E(mode))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_dmadim_checksum(self):
        phy_src = create_random_int(1, MAX_UINT64)
        size = create_random_int(1, MAX_UINT32)
        result, ret = axcl.dmadim.checksum(phy_src, size)
        inputs_args = serialize_ctypes_args(AX_U64(phy_src), AX_U64(size))
        output_args = serialize_ctypes_args(AX_S32(ret), AX_U32(result))
        assert 0 == check_input_output(inputs_args, output_args)
