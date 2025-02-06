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

from axcl.sys.axcl_sys import init
from axcl.sys.axcl_sys import deinit
from axcl.sys.axcl_sys import mem_alloc
from axcl.sys.axcl_sys import mem_alloc_cached
from axcl.sys.axcl_sys import mem_free
from axcl.sys.axcl_sys import mmap
from axcl.sys.axcl_sys import mmap_cache
from axcl.sys.axcl_sys import mmap_fast
from axcl.sys.axcl_sys import mmap_cache_fast
from axcl.sys.axcl_sys import munmap
from axcl.sys.axcl_sys import mflush_cache
from axcl.sys.axcl_sys import minvalidate_cache
from axcl.sys.axcl_sys import mem_get_block_info_by_phy
from axcl.sys.axcl_sys import mem_get_block_info_by_virt
from axcl.sys.axcl_sys import mem_get_partition_info
from axcl.sys.axcl_sys import mem_set_config
from axcl.sys.axcl_sys import mem_get_config
from axcl.sys.axcl_sys import mem_query_status
from axcl.sys.axcl_sys import link
from axcl.sys.axcl_sys import unlink
from axcl.sys.axcl_sys import get_link_by_dest
from axcl.sys.axcl_sys import get_link_by_src
from axcl.sys.axcl_sys import get_cur_pts
from axcl.sys.axcl_sys import init_pts_base
from axcl.sys.axcl_sys import sync_pts
from axcl.sys.axcl_sys import get_chip_type
