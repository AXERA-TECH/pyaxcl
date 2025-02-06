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

from axcl.rt.axcl_rt import get_version
from axcl.rt.axcl_rt import get_soc_name

from axcl.rt.axcl_rt_device import set_device
from axcl.rt.axcl_rt_device import reset_device
from axcl.rt.axcl_rt_device import get_device
from axcl.rt.axcl_rt_device import get_device_count
from axcl.rt.axcl_rt_device import get_device_list
from axcl.rt.axcl_rt_device import synchronize_device
from axcl.rt.axcl_rt_device import get_device_utilization_rate

from axcl.rt.axcl_rt_context import create_context
from axcl.rt.axcl_rt_context import destroy_context
from axcl.rt.axcl_rt_context import set_current_context
from axcl.rt.axcl_rt_context import get_current_context
from axcl.rt.axcl_rt_context import get_default_context

from axcl.rt.axcl_rt_stream import create_stream
from axcl.rt.axcl_rt_stream import destroy_stream
from axcl.rt.axcl_rt_stream import destroy_stream_force
from axcl.rt.axcl_rt_stream import synchronize_stream
from axcl.rt.axcl_rt_stream import synchronize_stream_with_timeout

from axcl.rt.axcl_rt_memory import malloc
from axcl.rt.axcl_rt_memory import malloc_cached
from axcl.rt.axcl_rt_memory import free
from axcl.rt.axcl_rt_memory import mem_flush
from axcl.rt.axcl_rt_memory import mem_invalidate
from axcl.rt.axcl_rt_memory import malloc_host
from axcl.rt.axcl_rt_memory import free_host
from axcl.rt.axcl_rt_memory import memset
from axcl.rt.axcl_rt_memory import memcpy
from axcl.rt.axcl_rt_memory import memcmp


from axcl.rt.axcl_rt_engine import engine_init
from axcl.rt.axcl_rt_engine import engine_get_vnpu_kind
from axcl.rt.axcl_rt_engine import engine_finalize
from axcl.rt.axcl_rt_engine import engine_load_from_file
from axcl.rt.axcl_rt_engine import engine_load_from_mem
from axcl.rt.axcl_rt_engine import engine_unload
from axcl.rt.axcl_rt_engine import engine_get_model_compiler_version
from axcl.rt.axcl_rt_engine import engine_set_affinity
from axcl.rt.axcl_rt_engine import engine_get_affinity
from axcl.rt.axcl_rt_engine import engine_get_usage
from axcl.rt.axcl_rt_engine import engine_get_usage_from_mem
from axcl.rt.axcl_rt_engine import engine_get_usage_from_mode_id
from axcl.rt.axcl_rt_engine import engine_get_model_type
from axcl.rt.axcl_rt_engine import engine_get_model_type_from_mem
from axcl.rt.axcl_rt_engine import engine_get_model_type_from_model_id
from axcl.rt.axcl_rt_engine import engine_get_io_info
from axcl.rt.axcl_rt_engine import engine_destroy_io_info
from axcl.rt.axcl_rt_engine import engine_get_shape_groups_count
from axcl.rt.axcl_rt_engine import engine_get_num_inputs
from axcl.rt.axcl_rt_engine import engine_get_num_outputs
from axcl.rt.axcl_rt_engine import engine_get_input_size_by_index
from axcl.rt.axcl_rt_engine import engine_get_output_size_by_index
from axcl.rt.axcl_rt_engine import engine_get_input_name_by_index
from axcl.rt.axcl_rt_engine import engine_get_output_name_by_index
from axcl.rt.axcl_rt_engine import engine_get_input_index_by_name
from axcl.rt.axcl_rt_engine import engine_get_output_index_by_name
from axcl.rt.axcl_rt_engine import engine_get_input_data_type
from axcl.rt.axcl_rt_engine import engine_get_output_data_type
from axcl.rt.axcl_rt_engine import engine_get_input_data_layout
from axcl.rt.axcl_rt_engine import engine_get_output_data_layout
from axcl.rt.axcl_rt_engine import engine_get_input_dims
from axcl.rt.axcl_rt_engine import engine_get_output_dims
from axcl.rt.axcl_rt_engine import engine_create_io
from axcl.rt.axcl_rt_engine import engine_destroy_io
from axcl.rt.axcl_rt_engine import engine_set_input_buffer_by_index
from axcl.rt.axcl_rt_engine import engine_set_output_buffer_by_index
from axcl.rt.axcl_rt_engine import engine_set_input_buffer_by_name
from axcl.rt.axcl_rt_engine import engine_set_output_buffer_by_name
from axcl.rt.axcl_rt_engine import engine_get_input_buffer_by_index
from axcl.rt.axcl_rt_engine import engine_get_output_buffer_by_index
from axcl.rt.axcl_rt_engine import engine_get_input_buffer_by_name
from axcl.rt.axcl_rt_engine import engine_get_output_buffer_by_name
from axcl.rt.axcl_rt_engine import engine_set_dynamic_batch_size
from axcl.rt.axcl_rt_engine import engine_create_context
from axcl.rt.axcl_rt_engine import engine_execute
from axcl.rt.axcl_rt_engine import engine_execute_async


# const var
from axcl.rt.axcl_rt_type import AXCL_MEM_MALLOC_HUGE_FIRST
from axcl.rt.axcl_rt_type import AXCL_MEM_MALLOC_HUGE_ONLY
from axcl.rt.axcl_rt_type import AXCL_MEM_MALLOC_NORMAL_ONLY

from axcl.rt.axcl_rt_type import AXCL_MEMCPY_HOST_TO_HOST
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_HOST_TO_DEVICE
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_DEVICE_TO_HOST
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_DEVICE_TO_DEVICE
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_HOST_PHY_TO_DEVICE
from axcl.rt.axcl_rt_type import AXCL_MEMCPY_DEVICE_TO_HOST_PHY

from axcl.rt.axcl_rt_engine_type import AXCL_MODEL_TYPE_1CORE
from axcl.rt.axcl_rt_engine_type import AXCL_MODEL_TYPE_2CORE
from axcl.rt.axcl_rt_engine_type import AXCL_MODEL_TYPE_3CORE

from axcl.rt.axcl_rt_engine_type import AXCL_VNPU_DISABLE
from axcl.rt.axcl_rt_engine_type import AXCL_VNPU_ENABLE
from axcl.rt.axcl_rt_engine_type import AXCL_VNPU_BIG_LITTLE
from axcl.rt.axcl_rt_engine_type import AXCL_VNPU_LITTLE_BIG



