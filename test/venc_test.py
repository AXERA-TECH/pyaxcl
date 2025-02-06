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
from axcl.venc.axcl_venc_comm import *
from ut_help import *


def create_random_payload_type():
    return choose_random_from_list([PT_H264, PT_H265, PT_MJPEG, PT_JPEG])


def create_random_rc_mode():
    return choose_random_from_list([AX_VENC_RC_MODE_H264CBR,
                                    AX_VENC_RC_MODE_H264VBR,
                                    AX_VENC_RC_MODE_H264AVBR,
                                    AX_VENC_RC_MODE_H264QVBR,
                                    AX_VENC_RC_MODE_H264CVBR,
                                    AX_VENC_RC_MODE_H264FIXQP,
                                    AX_VENC_RC_MODE_H264QPMAP,
                                    AX_VENC_RC_MODE_MJPEGCBR,
                                    AX_VENC_RC_MODE_MJPEGVBR,
                                    AX_VENC_RC_MODE_MJPEGFIXQP,
                                    AX_VENC_RC_MODE_H265CBR,
                                    AX_VENC_RC_MODE_H265VBR,
                                    AX_VENC_RC_MODE_H265AVBR,
                                    AX_VENC_RC_MODE_H265QVBR,
                                    AX_VENC_RC_MODE_H265CVBR,
                                    AX_VENC_RC_MODE_H265FIXQP,
                                    AX_VENC_RC_MODE_H265QPMAP])


def create_random_gop_mode():
    return choose_random_from_list([AX_VENC_GOPMODE_NORMALP, AX_VENC_GOPMODE_ONELTR, AX_VENC_GOPMODE_SVC_T])


class TestVenc:
    def test_venc_init(self):
        c_mode_attr = create_random_struct_instance(AX_VENC_MOD_ATTR_T)
        ret = axcl.venc.init(c_mode_attr.struct2dict())
        inputs_args = serialize_ctypes_args(c_mode_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_deinit(self):
        ret = axcl.venc.deinit()
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(None, output_args)

    def test_venc_create_chn(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)

        c_attr = AX_VENC_CHN_ATTR_T()
        ctypes.memset(ctypes.byref(c_attr), 0, ctypes.sizeof(c_attr))
        c_attr.stVencAttr.enType = create_random_payload_type()
        c_attr.stRcAttr.enRcMode = create_random_rc_mode()
        c_attr.stGopAttr.enGopMode = create_random_gop_mode()
        c_attr = create_random_struct_instance(AX_VENC_CHN_ATTR_T, c_attr)
        ret = axcl.venc.create_chn(chn, c_attr.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_create_chn_ex(self):
        c_attr = AX_VENC_CHN_ATTR_T()
        ctypes.memset(ctypes.byref(c_attr), 0, ctypes.sizeof(c_attr))
        c_attr.stVencAttr.enType = create_random_payload_type()
        c_attr.stRcAttr.enRcMode = create_random_rc_mode()
        c_attr.stGopAttr.enGopMode = create_random_gop_mode()
        c_attr = create_random_struct_instance(AX_VENC_CHN_ATTR_T, c_attr)
        chn, ret = axcl.venc.create_chn_ex(c_attr.struct2dict())
        inputs_args = serialize_ctypes_args(c_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), VENC_CHN(chn))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_destroy_chn(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        ret = axcl.venc.destroy_chn(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_send_frame(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_frame = create_random_struct_instance(AX_VIDEO_FRAME_INFO_T)
        ms = create_random_int(-1, 0xFFFFFFF)
        ret = axcl.venc.send_frame(chn, c_frame.struct2dict(), ms)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_frame, AX_S32(ms))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_send_frame_ex(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_frame = create_random_struct_instance(AX_USER_FRAME_INFO_T)
        ms = create_random_int(-1, 0xFFFFFFF)
        ret = axcl.venc.send_frame_ex(chn, c_frame.struct2dict(), ms)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_frame, AX_S32(ms))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_select_grp(self):
        grp = create_random_int(0, MAX_VENC_GRP_NUM)
        ms = create_random_int(-1, 0xFFFFFFF)
        strm_state, ret = axcl.venc.select_grp(grp, ms)
        inputs_args = serialize_ctypes_args(VENC_GRP(grp), AX_S32(ms))
        c_strm_state = AX_CHN_STREAM_STATUS_T()
        c_strm_state.dict2struct(strm_state)
        output_args = serialize_ctypes_args(AX_S32(ret), c_strm_state)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_clear_grp(self):
        grp = create_random_int(0, MAX_VENC_GRP_NUM)
        ret = axcl.venc.select_clear_grp(grp)
        inputs_args = serialize_ctypes_args(VENC_GRP(grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_select_grp_add_chn(self):
        grp = create_random_int(0, MAX_VENC_GRP_NUM)
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        ret = axcl.venc.select_grp_add_chn(grp, chn)
        inputs_args = serialize_ctypes_args(VENC_GRP(grp), VENC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_select_grp_delete_chn(self):
        grp = create_random_int(0, MAX_VENC_GRP_NUM)
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        ret = axcl.venc.select_grp_delete_chn(grp, chn)
        inputs_args = serialize_ctypes_args(VENC_GRP(grp), VENC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_select_grp_query(self):
        grp = create_random_int(0, MAX_VENC_GRP_NUM)
        param, ret = axcl.venc.select_grp_query(grp)
        inputs_args = serialize_ctypes_args(VENC_GRP(grp))
        c_param = AX_VENC_SELECT_GRP_PARAM_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_stream(self):
        pass

    def test_venc_release_stream(self):
        pass

    def test_venc_get_stream_buf_info(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        stream_buf_info, ret = axcl.venc.get_stream_buf_info(chn)
        inputs_args = serialize_ctypes_args(VENC_GRP(chn))
        c_stream_buf_info = AX_VENC_STREAM_BUF_INFO_T()
        c_stream_buf_info.dict2struct(stream_buf_info)
        output_args = serialize_ctypes_args(AX_S32(ret), c_stream_buf_info)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_start_recv_frame(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_recv_param = create_random_struct_instance(AX_VENC_RECV_PIC_PARAM_T)
        ret = axcl.venc.start_recv_frame(chn, c_recv_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_recv_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_stop_recv_frame(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        ret = axcl.venc.stop_recv_frame(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_reset_chn(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        ret = axcl.venc.reset_chn(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_roi_attr(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_roi_attr = create_random_struct_instance(AX_VENC_ROI_ATTR_T)
        ret = axcl.venc.set_roi_attr(chn, c_roi_attr.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_roi_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_roi_attr(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        index = create_random_int(0, 8)
        roi_attr, ret = axcl.venc.get_roi_attr(chn, index)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), AX_U32(index))
        c_roi_attr = AX_VENC_ROI_ATTR_T()
        c_roi_attr.dict2struct(roi_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), c_roi_attr)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_rc_param(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_param = create_random_struct_instance(AX_VENC_RC_PARAM_T)
        ret = axcl.venc.set_rc_param(chn, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_rc_param(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        param, ret = axcl.venc.get_rc_param(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_param = AX_VENC_RC_PARAM_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_mod_param(self):
        mode_type = choose_random_from_list([AX_VENC_VIDEO_ENCODER, AX_VENC_JPEG_ENCODER, AX_VENC_MULTI_ENCODER])
        c_param = create_random_struct_instance(AX_VENC_MOD_PARAM_T)
        ret = axcl.venc.set_mod_param(mode_type, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(AX_VENC_ENCODER_TYPE_E(mode_type), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_mod_param(self):
        mode_type = choose_random_from_list([AX_VENC_VIDEO_ENCODER, AX_VENC_JPEG_ENCODER, AX_VENC_MULTI_ENCODER])
        param, ret = axcl.venc.get_mod_param(mode_type)
        inputs_args = serialize_ctypes_args(AX_VENC_ENCODER_TYPE_E(mode_type))
        c_param = AX_VENC_MOD_PARAM_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_vui_param(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_param = create_random_struct_instance(AX_VENC_VUI_PARAM_T)
        ret = axcl.venc.set_vui_param(chn, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_vui_param(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        param, ret = axcl.venc.get_vui_param(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_param = AX_VENC_VUI_PARAM_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_chn_attr(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_attr = create_random_struct_instance(AX_VENC_CHN_ATTR_T)
        ret = axcl.venc.set_chn_attr(chn, c_attr.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_chn_attr(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        attr, ret = axcl.venc.get_chn_attr(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_attr = AX_VENC_CHN_ATTR_T()
        c_attr.dict2struct(attr)
        output_args = serialize_ctypes_args(AX_S32(ret), c_attr)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_rate_jam_strategy(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_param = create_random_struct_instance(AX_VENC_RATE_JAM_CFG_T)
        ret = axcl.venc.set_rate_jam_strategy(chn, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_rate_jam_strategy(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        param, ret = axcl.venc.get_rate_jam_strategy(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_param = AX_VENC_RATE_JAM_CFG_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_supper_frame_strategy(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_param = create_random_struct_instance(AX_VENC_SUPERFRAME_CFG_T)
        ret = axcl.venc.set_supper_frame_strategy(chn, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_supper_frame_strategy(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        param, ret = axcl.venc.get_supper_frame_strategy(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_param = AX_VENC_SUPERFRAME_CFG_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_intra_refresh(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_param = create_random_struct_instance(AX_VENC_INTRA_REFRESH_T)
        ret = axcl.venc.set_intra_refresh(chn, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_intra_refresh(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        param, ret = axcl.venc.get_intra_refresh(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_param = AX_VENC_INTRA_REFRESH_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_usr_data(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_usr_data = create_random_struct_instance(AX_VENC_USR_DATA_T)
        ret = axcl.venc.set_usr_data(chn, c_usr_data.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_usr_data)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_usr_data(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_usr_data = create_random_struct_instance(AX_VENC_USR_DATA_T)
        output, ret = axcl.venc.get_usr_data(chn, c_usr_data.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_usr_data)
        c_output = AX_VENC_USR_DATA_T()
        c_output.dict2struct(output)
        output_args = serialize_ctypes_args(AX_S32(ret), c_output)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_slice_split(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_param = create_random_struct_instance(AX_VENC_SLICE_SPLIT_T)
        ret = axcl.venc.set_slice_split(chn, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_slice_split(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        param, ret = axcl.venc.get_slice_split(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_param = AX_VENC_SLICE_SPLIT_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_request_idr(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        instant = create_random_int(0, 1)
        ret = axcl.venc.request_idr(chn, instant)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_query_status(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        status, ret = axcl.venc.query_status(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_status = AX_VENC_CHN_STATUS_T()
        c_status.dict2struct(status)
        output_args = serialize_ctypes_args(AX_S32(ret), c_status)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_set_jpeg_param(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        c_param = create_random_struct_instance(AX_VENC_JPEG_PARAM_T)
        ret = axcl.venc.set_jpeg_param(chn, c_param.struct2dict())
        inputs_args = serialize_ctypes_args(VENC_CHN(chn), c_param)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_get_jpeg_param(self):
        chn = create_random_int(0, MAX_VENC_CHN_NUM)
        param, ret = axcl.venc.get_jpeg_param(chn)
        inputs_args = serialize_ctypes_args(VENC_CHN(chn))
        c_param = AX_VENC_JPEG_PARAM_T()
        c_param.dict2struct(param)
        output_args = serialize_ctypes_args(AX_S32(ret), c_param)
        assert 0 == check_input_output(inputs_args, output_args)

    def test_venc_jpeg_encode_one_frame(self):
        c_param = create_random_struct_instance(AX_JPEG_ENCODE_ONCE_PARAMS_T)
        output, ret = axcl.venc.jpeg_encode_one_frame(c_param.struct2dict())
        inputs_args = serialize_ctypes_args(c_param)
        c_output = AX_JPEG_ENCODE_ONCE_PARAMS_T()
        c_output.dict2struct(output)
        output_args = serialize_ctypes_args(AX_S32(ret), c_output)
        assert 0 == check_input_output(inputs_args, output_args)
