#!/usr/bin/env python3
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
from ctypes import*

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

import axcl
from axcl.vdec.axcl_vdec import *
from ut_help import *


class TestVdec:
    def test_vdec_init(self):
        # prepare args
        c_mode_attr = create_random_struct_instance(AX_VDEC_MOD_ATTR_T)

        # invoke
        ret = axcl.vdec.init(c_mode_attr.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(c_mode_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_deinit(self):
        ret = axcl.vdec.deinit()
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(None, output_args)

    def test_vdec_extract_stream_header_info(self):
        # prepare args
        c_stream_buf = create_random_struct_instance(AX_VDEC_STREAM_T)
        video_type = PT_H264

        # invoke
        bit_stream_info, ret = axcl.vdec.extract_stream_header_info(c_stream_buf.struct2dict(), video_type)

        # check
        inputs_args = serialize_ctypes_args(c_stream_buf, AX_PAYLOAD_TYPE_E(video_type))
        c_bit_stream_info = AX_VDEC_BITSTREAM_INFO_T()
        c_bit_stream_info.dict2struct(bit_stream_info)
        output_args = serialize_ctypes_args(AX_S32(ret), c_bit_stream_info)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_create_grp(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        c_grp_attr = create_random_struct_instance(AX_VDEC_GRP_ATTR_T)

        # invoke
        ret = axcl.vdec.create_grp(grp, c_grp_attr.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), c_grp_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_create_grp_ex(self):
        # prepare args
        c_grp_attr = create_random_struct_instance(AX_VDEC_GRP_ATTR_T)

        # invoke
        grp, ret = axcl.vdec.create_grp_ex(c_grp_attr.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(c_grp_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), AX_VDEC_GRP(grp))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_get_grp_attr(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        grp_attr, ret = axcl.vdec.get_grp_attr(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        c_grp_attr = AX_VDEC_GRP_ATTR_T()
        c_grp_attr.dict2struct(grp_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), c_grp_attr)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_set_grp_attr(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        c_grp_attr = create_random_struct_instance(AX_VDEC_GRP_ATTR_T)

        # invoke
        ret = axcl.vdec.set_grp_attr(grp, c_grp_attr.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), c_grp_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_start_recv_stream(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        c_recv_param = create_random_struct_instance(AX_VDEC_RECV_PIC_PARAM_T)

        # invoke
        ret = axcl.vdec.start_recv_stream(grp, c_recv_param.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), c_recv_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_stop_recv_stream(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        ret = axcl.vdec.stop_recv_stream(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_query_status(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        grp_status, ret = axcl.vdec.query_status(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        c_grp_status = AX_VDEC_GRP_STATUS_T()
        c_grp_status.dict2struct(grp_status)
        output_args = serialize_ctypes_args(AX_S32(ret), c_grp_status)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_reset_grp(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        ret = axcl.vdec.reset_grp(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_set_grp_param(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        c_grp_param = create_random_struct_instance(AX_VDEC_GRP_PARAM_T)

        # invoke
        ret = axcl.vdec.set_grp_param(grp, c_grp_param.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), c_grp_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_get_grp_param(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        grp_param, ret = axcl.vdec.get_grp_param(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        c_grp_param = AX_VDEC_GRP_PARAM_T()
        c_grp_param.dict2struct(grp_param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_grp_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_select_grp(self):
        # prepare args
        ms = create_random_int(-1, 0xFFFFFFF)

        # invoke
        grp_set, ret = axcl.vdec.select_grp(ms)

        # check
        inputs_args = serialize_ctypes_args(AX_S32(ms))
        c_grp_set = AX_VDEC_GRP_SET_INFO_T()
        c_grp_set.dict2struct(grp_set)
        output_args = serialize_ctypes_args(AX_S32(ret), c_grp_set)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_send_stream(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        c_stream = create_random_struct_instance(AX_VDEC_STREAM_T)
        ms = create_random_int(-1, 0xFFFFFFF)

        # invoke
        ret = axcl.vdec.send_stream(grp, c_stream.struct2dict(), ms)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), c_stream, AX_S32(ms))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_get_chn_frame(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)
        ms = create_random_int(-1, 0xFFFFFFF)

        # invoke
        frame_info, ret = axcl.vdec.get_chn_frame(grp, chn, ms)

        # check
        input_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn), AX_S32(ms))
        c_frame_info = AX_VIDEO_FRAME_INFO_T()
        c_frame_info.dict2struct(frame_info)
        output_args = serialize_ctypes_args(AX_S32(ret), c_frame_info)
        assert 0 == check_input_output(input_args, output_args)

    def test_vdec_release_chn_frame(self):
        # prepare args
        c_frame_info = create_random_struct_instance(AX_VIDEO_FRAME_INFO_T)
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)

        # invoke
        ret = axcl.vdec.release_chn_frame(grp, chn, c_frame_info.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn), c_frame_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_get_user_data(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        user_data, ret = axcl.vdec.get_user_data(grp)

        # check
        input_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        c_user_data = AX_VDEC_USERDATA_T()
        c_user_data.dict2struct(user_data)
        output_args = serialize_ctypes_args(AX_S32(ret), c_user_data)
        assert 0 == check_input_output(input_args, output_args)

    def test_vdec_release_user_data(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        c_user_data = create_random_struct_instance(AX_VDEC_USERDATA_T)

        # invoke
        ret = axcl.vdec.release_user_data(grp, c_user_data.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), c_user_data)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_set_user_pic(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        c_user_pic = create_random_struct_instance(AX_VDEC_USRPIC_T)

        # invoke
        ret = axcl.vdec.set_user_pic(grp, c_user_pic.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), c_user_pic)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_enable_user_pic(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        ret = axcl.vdec.enable_user_pic(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_disable_user_pic(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        ret = axcl.vdec.disable_user_pic(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_set_display_mode(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        display_mode = create_random_int(AX_VDEC_DISPLAY_MODE_PREVIEW, AX_VDEC_DISPLAY_MODE_BUTT)

        # invoke
        ret = axcl.vdec.set_display_mode(grp, display_mode)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_DISPLAY_MODE_E(display_mode))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_get_display_mode(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        display_mode, ret = axcl.vdec.get_display_mode(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        c_display_mode = AX_VDEC_DISPLAY_MODE_E(display_mode)
        output_args = serialize_ctypes_args(AX_S32(ret), c_display_mode)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_attach_pool(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)
        pool = create_random_ctypes_instance(AX_POOL)

        # invoke
        ret = axcl.vdec.attach_pool(grp, chn, pool.value)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn), pool)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_detach_pool(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)

        # invoke
        ret = axcl.vdec.detach_pool(grp, chn)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_enable_chn(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)

        # invoke
        ret = axcl.vdec.enable_chn(grp, chn)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_disable_chn(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)

        # invoke
        ret = axcl.vdec.disable_chn(grp, chn)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_set_chn_attr(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)
        c_chn_attr = create_random_struct_instance(AX_VDEC_CHN_ATTR_T)

        # invoke
        ret = axcl.vdec.set_chn_attr(grp, chn, c_chn_attr.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn), c_chn_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_get_chn_attr(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)
        chn = create_random_int(0, AX_VDEC_MAX_CHN_NUM)

        # invoke
        chn_attr, ret = axcl.vdec.get_chn_attr(grp, chn)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp), AX_VDEC_CHN(chn))
        c_chn_attr = AX_VDEC_CHN_ATTR_T()
        c_chn_attr.dict2struct(chn_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), c_chn_attr)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_jpeg_decode_one_frame(self):
        # prepare args
        c_param = create_random_struct_instance(AX_VDEC_DEC_ONE_FRM_T)

        # invoke
        ret = axcl.vdec.jpeg_decode_one_frame(c_param.struct2dict())

        # check
        inputs_args = serialize_ctypes_args(c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_vdec_get_vui_param(self):
        # prepare args
        grp = create_random_int(0, AX_VDEC_MAX_GRP_NUM)

        # invoke
        vui_param, ret = axcl.vdec.get_vui_param(grp)

        # check
        inputs_args = serialize_ctypes_args(AX_VDEC_GRP(grp))
        c_vui_param = AX_VDEC_VUI_PARAM_T()
        c_vui_param.dict2struct(vui_param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_vui_param)
        assert 0 == check_input_output(inputs_args, output_args)
