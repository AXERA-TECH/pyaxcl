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

from axcl.npu.axcl_npu import get_version
from axcl.npu.axcl_npu import npu_reset
from axcl.npu.axcl_npu import init
from axcl.npu.axcl_npu import get_npu_attr
from axcl.npu.axcl_npu import deinit
from axcl.npu.axcl_npu import get_model_type
from axcl.npu.axcl_npu import create_handle
from axcl.npu.axcl_npu import create_handle_v2
from axcl.npu.axcl_npu import destroy_handle
from axcl.npu.axcl_npu import get_handle_model_type
from axcl.npu.axcl_npu import get_io_info
from axcl.npu.axcl_npu import get_group_io_info_count
from axcl.npu.axcl_npu import get_group_io_info
from axcl.npu.axcl_npu import create_context
from axcl.npu.axcl_npu import create_context_v2
from axcl.npu.axcl_npu import run_sync
from axcl.npu.axcl_npu import run_sync_v2
from axcl.npu.axcl_npu import run_group_io_sync
from axcl.npu.axcl_npu import get_affinity
from axcl.npu.axcl_npu import set_affinity
from axcl.npu.axcl_npu import get_cmm_usage
from axcl.npu.axcl_npu import get_model_tools_version
