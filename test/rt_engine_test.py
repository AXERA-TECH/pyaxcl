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
from ctypes import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

import axcl
from axcl.rt.axcl_rt_type import *
from axcl.rt.axcl_rt_engine_type import *
from ut_help import *


axclrtEngineSet = c_uint32
axclrtEvent = c_void_p
axclrtContext = c_void_p
axclrtStream = c_void_p
axclrtEngineIOInfo = c_void_p
axclrtEngineIO = c_void_p
axclrtStream = c_void_p


class TestRtEngine():
    def test_engine_init(self):
        npu_kind = choose_random_from_list([
            AXCL_VNPU_DISABLE,
            AXCL_VNPU_ENABLE,
            AXCL_VNPU_BIG_LITTLE,
            AXCL_VNPU_LITTLE_BIG])

        ret = axcl.rt.engine_init(npu_kind)

        inputs_args = serialize_ctypes_args(axclrtEngineVNpuKind(npu_kind))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_vnpu_kind(self):
        npu_kind, ret = axcl.rt.engine_get_vnpu_kind()

        output_args = serialize_ctypes_args(axclError(ret), axclrtEngineVNpuKind(npu_kind))
        assert 0 == check_input_output(None, output_args)

    def test_engine_finalize(self):
        ret = axcl.rt.engine_finalize()

        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(None, output_args)

    def test_engine_load_from_file(self):
        model_path = '/usr/bin/yolo11.xxmodel'

        model_id, ret = axcl.rt.engine_load_from_file(model_path)

        inputs_args = serialize_ctypes_args(create_data_array_from_str(model_path))
        output_args = serialize_ctypes_args(axclError(ret), c_uint64(model_id))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_load_from_mem(self):
        model_size = create_random_int(1024, 1*1024*1024)
        content = os.urandom(model_size)
        model = axcl.utils.bytes_to_ptr(content)

        model_id, ret = axcl.rt.engine_load_from_mem(model, model_size)

        darray = DataArray()
        darray.data = c_void_p(model)
        darray.size = len(content)
        inputs_args = serialize_ctypes_args(darray)
        output_args = serialize_ctypes_args(axclError(ret), c_uint64(model_id))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_unload(self):
        model_id = create_random_int(1, MAX_UINT64)

        ret = axcl.rt.engine_unload(model_id)

        inputs_args = serialize_ctypes_args(c_uint64(model_id))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_model_compiler_version(self):
        model_id = create_random_int(1, MAX_UINT64)

        version = axcl.rt.engine_get_model_compiler_version(model_id)

        inputs_args = serialize_ctypes_args(c_uint64(model_id))
        output_args = serialize_ctypes_args(create_data_array_from_str(version))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_set_affinity(self):
        model_id = create_random_int(1, MAX_UINT64)
        mask = create_random_int(1, MAX_UINT32)

        ret = axcl.rt.engine_set_affinity(model_id, mask)

        inputs_args = serialize_ctypes_args(c_uint64(model_id), axclrtEngineSet(mask))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_affinity(self):
        model_id = create_random_int(1, MAX_UINT64)

        mask, ret = axcl.rt.engine_get_affinity(model_id)
        inputs_args = serialize_ctypes_args(c_uint64(model_id))
        output_args = serialize_ctypes_args(axclError(ret), axclrtEngineSet(mask))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_usage(self):
        model_path = '/usr/bin/yolo11.xxmodel'

        sys_size, cmm_size, ret = axcl.rt.engine_get_usage(model_path)

        inputs_args = serialize_ctypes_args(create_data_array_from_str(model_path))
        output_args = serialize_ctypes_args(axclError(ret), c_int64(sys_size), c_int64(cmm_size))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_usage_from_mem(self):
        model_size = create_random_int(1024, 1*1024*1024)
        content = os.urandom(model_size)
        model = axcl.utils.bytes_to_ptr(content)

        sys_size, cmm_size, ret = axcl.rt.engine_get_usage_from_mem(model, model_size)

        darray = DataArray()
        darray.data = c_void_p(model)
        darray.size = len(content)
        inputs_args = serialize_ctypes_args(darray)
        output_args = serialize_ctypes_args(axclError(ret), c_int64(sys_size), c_int64(cmm_size))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_usage_from_mode_id(self):
        model_id = create_random_int(1, MAX_UINT64)

        sys_size, cmm_size, ret = axcl.rt.engine_get_usage_from_mode_id(model_id)

        inputs_args = serialize_ctypes_args(c_uint64(model_id))
        output_args = serialize_ctypes_args(axclError(ret), c_int64(sys_size), c_int64(cmm_size))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_model_type(self):
        model_path = '/usr/bin/yolo11.xxmodel'

        model_type, ret = axcl.rt.engine_get_model_type(model_path)

        inputs_args = serialize_ctypes_args(create_data_array_from_str(model_path))
        output_args = serialize_ctypes_args(axclError(ret), axclrtEngineModelKind(model_type))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_model_type_from_mem(self):
        model_size = create_random_int(1024, 1*1024*1024)
        content = os.urandom(model_size)
        model = axcl.utils.bytes_to_ptr(content)

        model_type, ret = axcl.rt.engine_get_model_type_from_mem(model, model_size)

        darray = DataArray()
        darray.data = c_void_p(model)
        darray.size = len(content)
        inputs_args = serialize_ctypes_args(darray)
        output_args = serialize_ctypes_args(axclError(ret), axclrtEngineModelKind(model_type))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_model_type_from_model_id(self):
        model_id = create_random_int(1, MAX_UINT64)

        model_type, ret = axcl.rt.engine_get_model_type_from_model_id(model_id)

        inputs_args = serialize_ctypes_args(c_uint64(model_id))
        output_args = serialize_ctypes_args(axclError(ret), axclrtEngineModelKind(model_type))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_io_info(self):
        model_id = create_random_int(1, MAX_UINT64)

        io_info, ret = axcl.rt.engine_get_io_info(model_id)

        inputs_args = serialize_ctypes_args(c_uint64(model_id))
        output_args = serialize_ctypes_args(axclError(ret), axclrtEngineIOInfo(io_info))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_destroy_io_info(self):
        io_info = create_random_int(1, MAX_UINT64)

        ret = axcl.rt.engine_destroy_io_info(io_info)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_shape_groups_count(self):
        io_info = create_random_int(1, MAX_UINT64)

        count, ret = axcl.rt.engine_get_shape_groups_count(io_info)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info))
        output_args = serialize_ctypes_args(axclError(ret), c_int32(count))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_num_inputs(self):
        io_info = create_random_int(1, MAX_UINT64)

        num_inputs = axcl.rt.engine_get_num_inputs(io_info)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info))
        output_args = serialize_ctypes_args(c_uint32(num_inputs))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_num_outputs(self):
        io_info = create_random_int(1, MAX_UINT64)

        num_outputs = axcl.rt.engine_get_num_outputs(io_info)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info))
        output_args = serialize_ctypes_args(c_uint32(num_outputs))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_size_by_index(self):
        io_info = create_random_int(1, MAX_UINT64)
        group = create_random_int(0, MAX_UINT32)
        index = create_random_int(0, MAX_UINT32)

        size = axcl.rt.engine_get_input_size_by_index(io_info, group, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(group), c_uint32(index))
        output_args = serialize_ctypes_args(c_uint64(size))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_size_by_index(self):
        io_info = create_random_int(1, MAX_UINT64)
        group = create_random_int(0, MAX_UINT32)
        index = create_random_int(0, MAX_UINT32)

        size = axcl.rt.engine_get_output_size_by_index(io_info, group, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(group), c_uint32(index))
        output_args = serialize_ctypes_args(c_uint64(size))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_name_by_index(self):
        io_info = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        name = axcl.rt.engine_get_input_name_by_index(io_info, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(index))
        output_args = serialize_ctypes_args(create_data_array_from_str(name))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_name_by_index(self):
        io_info = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        name = axcl.rt.engine_get_output_name_by_index(io_info, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(index))
        output_args = serialize_ctypes_args(create_data_array_from_str(name))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_index_by_name(self):
        io_info = create_random_int(1, MAX_UINT64)
        name = 'yolo11.xxmodel'

        index = axcl.rt.engine_get_input_index_by_name(io_info, name)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), create_data_array_from_str(name))
        output_args = serialize_ctypes_args(c_int32(index))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_index_by_name(self):
        io_info = create_random_int(1, MAX_UINT64)
        name = 'yolo11.xxmodel'

        index = axcl.rt.engine_get_output_index_by_name(io_info, name)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), create_data_array_from_str(name))
        output_args = serialize_ctypes_args(c_int32(index))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_dims(self):
        io_info = create_random_int(1, MAX_UINT64)
        group = create_random_int(0, MAX_UINT32)
        index = create_random_int(0, MAX_UINT32)

        dims, ret = axcl.rt.engine_get_input_dims(io_info, group, index)

        c_dims = axclrtEngineIODims()
        c_dims.dimCount = len(dims)
        for i in range(c_dims.dimCount):
            c_dims.dims[i] = dims[i]

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(group), c_uint32(index))
        output_args = serialize_ctypes_args(axclError(ret), c_dims)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_dims(self):
        io_info = create_random_int(1, MAX_UINT64)
        group = create_random_int(0, MAX_UINT32)
        index = create_random_int(0, MAX_UINT32)

        dims, ret = axcl.rt.engine_get_output_dims(io_info, group, index)

        c_dims = axclrtEngineIODims()
        c_dims.dimCount = len(dims)
        for i in range(c_dims.dimCount):
            c_dims.dims[i] = dims[i]

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(group), c_uint32(index))
        output_args = serialize_ctypes_args(axclError(ret), c_dims)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_data_type(self):
        io_info = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        type, ret = axcl.rt.engine_get_input_data_type(io_info, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(index))
        output_args = serialize_ctypes_args(c_int32(ret), axclrtEngineDataType(type))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_data_type(self):
        io_info = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        type, ret = axcl.rt.engine_get_output_data_type(io_info, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(index))
        output_args = serialize_ctypes_args(c_int32(ret), axclrtEngineDataType(type))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_data_layout(self):
        io_info = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        layout, ret = axcl.rt.engine_get_input_data_layout(io_info, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(index))
        output_args = serialize_ctypes_args(c_int32(ret), axclrtEngineDataLayout(layout))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_data_layout(self):
        io_info = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        layout, ret = axcl.rt.engine_get_output_data_layout(io_info, index)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info), c_uint32(index))
        output_args = serialize_ctypes_args(c_int32(ret), axclrtEngineDataLayout(layout))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_create_io(self):
        io_info = create_random_int(1, MAX_UINT64)

        io, ret = axcl.rt.engine_create_io(io_info)

        inputs_args = serialize_ctypes_args(axclrtEngineIOInfo(io_info))
        output_args = serialize_ctypes_args(axclError(ret), axclrtEngineIO(io))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_destroy_io(self):
        io = create_random_int(1, MAX_UINT64)

        ret = axcl.rt.engine_destroy_io(io)

        inputs_args = serialize_ctypes_args(axclrtEngineIO(io))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_set_input_buffer_by_index(self):
        io = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)
        size = create_random_int(1024, 1*1024*1024)
        buff = os.urandom(size)
        data_buffer = axcl.utils.bytes_to_ptr(buff)

        ret = axcl.rt.engine_set_input_buffer_by_index(io, index, data_buffer, size)

        darray = DataArray()
        darray.data = c_void_p(data_buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), c_uint32(index), darray)
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_set_output_buffer_by_index(self):
        io = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)
        size = create_random_int(1024, 1*1024*1024)
        buff = os.urandom(size)
        data_buffer = axcl.utils.bytes_to_ptr(buff)

        ret = axcl.rt.engine_set_output_buffer_by_index(io, index, data_buffer, size)

        darray = DataArray()
        darray.data = c_void_p(data_buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), c_uint32(index), darray)
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_set_input_buffer_by_name(self):
        io = create_random_int(1, MAX_UINT64)
        name = 'name'
        size = create_random_int(1024, 1*1024*1024)
        buff = os.urandom(size)
        data_buffer = axcl.utils.bytes_to_ptr(buff)

        ret = axcl.rt.engine_set_input_buffer_by_name(io, name, data_buffer, size)

        darray = DataArray()
        darray.data = c_void_p(data_buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), create_data_array_from_str(name), darray)
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_set_output_buffer_by_name(self):
        io = create_random_int(1, MAX_UINT64)
        name = 'name'
        size = create_random_int(1024, 1*1024*1024)
        buff = os.urandom(size)
        data_buffer = axcl.utils.bytes_to_ptr(buff)

        ret = axcl.rt.engine_set_output_buffer_by_name(io, name, data_buffer, size)

        darray = DataArray()
        darray.data = c_void_p(data_buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), create_data_array_from_str(name), darray)
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_buffer_by_index(self):
        io = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        buffer, size, ret = axcl.rt.engine_get_input_buffer_by_index(io, index)

        darray = DataArray()
        darray.data = c_void_p(buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), c_uint32(index))
        output_args = serialize_ctypes_args(axclError(ret), darray)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_buffer_by_index(self):
        io = create_random_int(1, MAX_UINT64)
        index = create_random_int(0, MAX_UINT32)

        buffer, size, ret = axcl.rt.engine_get_output_buffer_by_index(io, index)

        darray = DataArray()
        darray.data = c_void_p(buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), c_uint32(index))
        output_args = serialize_ctypes_args(axclError(ret), darray)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_input_buffer_by_name(self):
        io = create_random_int(1, MAX_UINT64)
        name = 'name'

        buffer, size, ret = axcl.rt.engine_get_input_buffer_by_name(io, name)

        darray = DataArray()
        darray.data = c_void_p(buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), create_data_array_from_str(name))
        output_args = serialize_ctypes_args(axclError(ret), darray)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_get_output_buffer_by_name(self):
        io = create_random_int(1, MAX_UINT64)
        name = 'name'

        buffer, size, ret = axcl.rt.engine_get_output_buffer_by_name(io, name)

        darray = DataArray()
        darray.data = c_void_p(buffer)
        darray.size = size
        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), create_data_array_from_str(name))
        output_args = serialize_ctypes_args(axclError(ret), darray)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_set_dynamic_batch_size(self):
        io = create_random_int(1, MAX_UINT64)
        batch_size = create_random_int(1, MAX_UINT32)

        ret = axcl.rt.engine_set_dynamic_batch_size(io, batch_size)

        inputs_args = serialize_ctypes_args(axclrtEngineIO(io), c_uint32(batch_size))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_create_context(self):
        model_id = create_random_int(1, MAX_UINT64)

        context, ret = axcl.rt.engine_create_context(model_id)

        inputs_args = serialize_ctypes_args(c_uint64(model_id))
        output_args = serialize_ctypes_args(axclError(ret), c_uint64(context))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_execute(self):
        model_id = create_random_int(1, MAX_UINT64)
        context_id = create_random_int(1, MAX_UINT64)
        group = create_random_int(0, MAX_UINT32)
        io = create_random_int(1, MAX_UINT64)

        ret = axcl.rt.engine_execute(model_id, context_id, group, io)

        inputs_args = serialize_ctypes_args(c_uint64(model_id), c_uint64(context_id), c_uint32(group), axclrtEngineIO(io))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_engine_execute_async(self):
        model_id = create_random_int(1, MAX_UINT64)
        context_id = create_random_int(1, MAX_UINT64)
        group = create_random_int(0, MAX_UINT32)
        io = create_random_int(1, MAX_UINT64)
        stream = create_random_int(1, MAX_UINT64)

        ret = axcl.rt.engine_execute_async(model_id, context_id, group, io, stream)

        inputs_args = serialize_ctypes_args(c_uint64(model_id), c_uint64(context_id), c_uint32(group), axclrtEngineIO(io), axclrtStream(stream))
        output_args = serialize_ctypes_args(axclError(ret))
        assert 0 == check_input_output(inputs_args, output_args)
