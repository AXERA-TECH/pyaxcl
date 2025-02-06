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
import axcl
from axclite.axclite_resource import AxcliteResource


class AxclitePool(AxcliteResource):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.blk_size = 0
        self.pool_id = axcl.AX_INVALID_POOLID

    def create(self, blk_size: int, blk_cnt: int, name: str, cached=False):
        pool_config = {
            'meta_size': 4096,
            'blk_size': blk_size,
            'blk_cnt': blk_cnt,
            'is_merge_mode': False,
            'cache_mode': axcl.POOL_CACHE_MODE_CACHED if cached else axcl.POOL_CACHE_MODE_NONCACHE,
            'partition_name': '',
            'pool_name': name if name else ''
        }

        self.blk_size = blk_size
        self.pool_id = axcl.pool.create_pool(pool_config)
        return self.pool_id

    def destroy(self):
        if self.pool_id != axcl.AX_INVALID_POOLID:
            axcl.pool.destroy_pool(self.pool_id)
            self.pool_id = axcl.AX_INVALID_POOLID

    def mmap(self):
        return axcl.pool.mmap_pool(self.pool_id)

    def munmap(self):
        return axcl.pool.munmap_pool(self.pool_id)

    def get_blk(self):
        return axcl.pool.get_block(self.pool_id, self.blk_size, None)

    @staticmethod
    def release_blk(blk_id):
        return axcl.pool.release_block(blk_id)

    @staticmethod
    def get_blk_phy_addr(blk_id):
        return axcl.pool.handle_to_phy_addr(blk_id)

    @staticmethod
    def get_blk_vir_addr(blk_id):
        return axcl.pool.get_block_vir_addr(blk_id)

    @staticmethod
    def increase_blk_ref_cnt(blk_id):
        return axcl.pool.increase_ref_cnt(blk_id)

    @staticmethod
    def decrease_blk_ref_cnt(blk_id):
        return axcl.pool.decrease_ref_cnt(blk_id)
