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

from axcl.pool.axcl_pool import set_config
from axcl.pool.axcl_pool import get_config
from axcl.pool.axcl_pool import init
from axcl.pool.axcl_pool import exit
from axcl.pool.axcl_pool import create_pool
from axcl.pool.axcl_pool import destroy_pool
from axcl.pool.axcl_pool import get_block
from axcl.pool.axcl_pool import release_block
from axcl.pool.axcl_pool import phy_addr_to_handle
from axcl.pool.axcl_pool import handle_to_phy_addr
from axcl.pool.axcl_pool import handle_to_meta_phy_addr
from axcl.pool.axcl_pool import handle_to_pool_id
from axcl.pool.axcl_pool import handle_to_blk_size
from axcl.pool.axcl_pool import mmap_pool
from axcl.pool.axcl_pool import munmap_pool
from axcl.pool.axcl_pool import get_block_vir_addr
from axcl.pool.axcl_pool import get_meta_vir_addr
from axcl.pool.axcl_pool import increase_ref_cnt
from axcl.pool.axcl_pool import decrease_ref_cnt
