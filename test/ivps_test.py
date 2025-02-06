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
import random
from ctypes import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR+'/..')

import axcl
from axcl.ivps.axcl_ivps_type import *
from axcl.ivps.axcl_ivps import *
from axcl.utils.axcl_utils import *
from ut_help import *


def create_random_int(min_value=0, max_value=100):
    """
    Generate a random integer between min_value and max_value.

    Parameters:
        min_value (int): The minimum value of the random integer (inclusive).
        max_value (int): The maximum value of the random integer (inclusive).

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def create_random_ctypes_instance_ex(ctype):
    obj = ctype()
    obj.random_struct(obj)
    return obj


def random_ctypes_instance_ex(ctype_obj):
    ctype_obj.random_struct(ctype_obj)


class TestIvps:
    def test_init(self):
        # prepare input
        # No input needed, as init has no parameters

        # invoke
        ret = axcl.ivps.init()

        # check output
        assert 0 == ret

    def test_deinit(self):
        # prepare input
        # No input needed, as deinit has no parameters

        # invoke
        ret = axcl.ivps.deinit()

        # check output
        assert 0 == ret

    def test_create_grp(self):
        # prepare input
        ivps_grp = create_random_int()
        c_grp_attr = create_random_ctypes_instance_ex(AX_IVPS_GRP_ATTR_T)
        d_grp_attr = c_grp_attr.struct2dict()

        # invoke
        ret = axcl.ivps.create_grp(ivps_grp, d_grp_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_grp_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_create_grp_ex(self):
        # prepare input
        c_grp_attr = create_random_ctypes_instance_ex(AX_IVPS_GRP_ATTR_T)
        d_grp_attr = c_grp_attr.struct2dict()

        # invoke
        ivps_grp, ret = axcl.ivps.create_grp_ex(d_grp_attr)

        # check output
        input_args = serialize_ctypes_args(c_grp_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), c_int32(ivps_grp))
        assert 0 == check_input_output(input_args, output_args)

    def test_destroy_grp(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        ret = axcl.ivps.destroy_grp(ivps_grp)

        # check output
        assert 0 == ret

    def test_set_pipeline_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        c_pipeline_attr = create_random_ctypes_instance_ex(AX_IVPS_PIPELINE_ATTR_T)
        d_pipeline_attr = c_pipeline_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_pipeline_attr(ivps_grp, d_pipeline_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_pipeline_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_pipeline_attr(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        d_pipeline_attr, ret = axcl.ivps.get_pipeline_attr(ivps_grp)
        c_pipeline_attr = AX_IVPS_PIPELINE_ATTR_T()
        c_pipeline_attr.dict2struct(d_pipeline_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp))
        output_args = serialize_ctypes_args(AX_S32(ret), c_pipeline_attr)
        assert 0 == check_input_output(input_args, output_args)

    def test_start_grp(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        ret = axcl.ivps.start_grp(ivps_grp)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_stop_grp(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        ret = axcl.ivps.stop_grp(ivps_grp)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_enable_chn(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()

        # invoke
        ret = axcl.ivps.enable_chn(ivps_grp, ivps_chn)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_disable_chn(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()

        # invoke
        ret = axcl.ivps.disable_chn(ivps_grp, ivps_chn)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_send_frame(self):
        # prepare input
        ivps_grp = create_random_int()
        millisec = create_random_int()
        c_frame_info = AX_VIDEO_FRAME_T()
        d_frame_info = c_frame_info.struct2dict()

        # invoke
        ret = axcl.ivps.send_frame(ivps_grp, d_frame_info, millisec)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_frame_info, AX_S32(millisec))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_chn_frame(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        millisec = create_random_int()

        # invoke
        d_frame_info, ret = axcl.ivps.get_chn_frame(ivps_grp, ivps_chn, millisec)
        c_frame_info = AX_VIDEO_FRAME_T()
        c_frame_info.dict2struct(d_frame_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), AX_S32(millisec))
        output_args = serialize_ctypes_args(AX_S32(ret), c_frame_info)
        assert 0 == check_input_output(input_args, output_args)

    def test_release_chn_frame(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        c_frame_info = AX_VIDEO_FRAME_T()
        d_frame_info = c_frame_info.struct2dict()

        # invoke
        ret = axcl.ivps.release_chn_frame(ivps_grp, ivps_chn, d_frame_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), c_frame_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_grp_frame(self):
        # prepare input
        ivps_grp = create_random_int()
        millisec = create_random_int()

        # invoke
        d_frame_info, ret = axcl.ivps.get_grp_frame(ivps_grp, millisec)
        c_frame_info = AX_VIDEO_FRAME_T()
        c_frame_info.dict2struct(d_frame_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), AX_S32(millisec))
        output_args = serialize_ctypes_args(AX_S32(ret), c_frame_info)
        assert 0 == check_input_output(input_args, output_args)

    def test_release_grp_frame(self):
        # prepare input
        ivps_grp = create_random_int()
        c_frame_info = AX_VIDEO_FRAME_T()
        d_frame_info = c_frame_info.struct2dict()

        # invoke
        ret = axcl.ivps.release_grp_frame(ivps_grp, d_frame_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_frame_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    # def test_get_chn_fd(self):
    #     # prepare input
    #     ivps_grp = create_random_int()
    #     ivps_chn = create_random_int()

    #     # invoke
    #     fd = axcl.ivps.get_chn_fd(ivps_grp, ivps_chn)

    #     # check output
    #     input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn))
    #     output_args = serialize_ctypes_args(AX_S32(fd))
    #     assert 0 == check_input_output(input_args, output_args)

    def test_get_debug_fifo_frame(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        d_frame_info, ret = axcl.ivps.get_debug_fifo_frame(ivps_grp)
        c_frame_info = AX_VIDEO_FRAME_T()
        c_frame_info.dict2struct(d_frame_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp))
        output_args = serialize_ctypes_args(AX_S32(ret), c_frame_info)
        assert 0 == check_input_output(input_args, output_args)

    def test_release_debug_fifo_frame(self):
        # prepare input
        ivps_grp = create_random_int()
        c_frame_info = AX_VIDEO_FRAME_T()
        d_frame_info = c_frame_info.struct2dict()

        # invoke
        ret = axcl.ivps.release_debug_fifo_frame(ivps_grp, d_frame_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_frame_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    # def test_close_all_fd(self):
    #     # prepare input
    #     # No input needed, as close_all_fd has no parameters

    #     # invoke
    #     ret = axcl.ivps.close_all_fd()

    #     # check output
    #     self.assertEqual(0, ret)

    def test_set_grp_ldc_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_filter = create_random_int()
        c_ldc_attr = create_random_ctypes_instance_ex(AX_IVPS_LDC_ATTR_T)
        d_ldc_attr = c_ldc_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_grp_ldc_attr(ivps_grp, ivps_filter, d_ldc_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_FILTER(ivps_filter), c_ldc_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_grp_ldc_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_filter = create_random_int()

        c_ldc_attr = AX_IVPS_LDC_ATTR_T()

        # invoke
        d_ldc_attr, ret = axcl.ivps.get_grp_ldc_attr(ivps_grp, ivps_filter)
        c_ldc_attr.dict2struct(d_ldc_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_FILTER(ivps_filter))
        output_args = serialize_ctypes_args(AX_S32(ret), c_ldc_attr)
        assert 0 == check_input_output(input_args, output_args)

    def test_set_chn_ldc_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        ivps_filter = create_random_int()
        c_ldc_attr = create_random_ctypes_instance_ex(AX_IVPS_LDC_ATTR_T)
        d_ldc_attr = c_ldc_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_chn_ldc_attr(ivps_grp, ivps_chn, ivps_filter, d_ldc_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), IVPS_FILTER(ivps_filter), c_ldc_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_chn_ldc_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        ivps_filter = create_random_int()

        # invoke
        d_ldc_attr, ret = axcl.ivps.get_chn_ldc_attr(ivps_grp, ivps_chn, ivps_filter)
        c_ldc_attr = AX_IVPS_LDC_ATTR_T()
        c_ldc_attr.dict2struct(d_ldc_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), IVPS_FILTER(ivps_filter))
        output_args = serialize_ctypes_args(AX_S32(ret), c_ldc_attr)
        assert 0 == check_input_output(input_args, output_args)

    def test_set_grp_pool_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        c_pool_attr = create_random_ctypes_instance_ex(AX_IVPS_POOL_ATTR_T)
        d_pool_attr = c_pool_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_grp_pool_attr(ivps_grp, d_pool_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_pool_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_set_chn_pool_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        c_pool_attr = create_random_ctypes_instance_ex(AX_IVPS_POOL_ATTR_T)
        d_pool_attr = c_pool_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_chn_pool_attr(ivps_grp, ivps_chn, d_pool_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), c_pool_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_set_grp_user_frc(self):
        # prepare input
        ivps_grp = create_random_int()
        c_framerate_attr = create_random_ctypes_instance_ex(AX_IVPS_USER_FRAME_RATE_CTRL_T)
        d_framerate_attr = c_framerate_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_grp_user_frc(ivps_grp, d_framerate_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_framerate_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_set_chn_user_frc(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        c_framerate_attr = create_random_ctypes_instance_ex(AX_IVPS_USER_FRAME_RATE_CTRL_T)
        d_framerate_attr = c_framerate_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_chn_user_frc(ivps_grp, ivps_chn, d_framerate_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), c_framerate_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_set_grp_crop(self):
        # prepare input
        ivps_grp = create_random_int()
        c_crop_info = create_random_ctypes_instance_ex(AX_IVPS_CROP_INFO_T)
        d_crop_info = c_crop_info.struct2dict()

        # invoke
        ret = axcl.ivps.set_grp_crop(ivps_grp, d_crop_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), c_crop_info)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_grp_crop(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        d_crop_info, ret = axcl.ivps.get_grp_crop(ivps_grp)
        c_crop_info = AX_IVPS_CROP_INFO_T()
        c_crop_info.dict2struct(d_crop_info)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp))
        output_args = serialize_ctypes_args(AX_S32(ret), c_crop_info)
        assert 0 == check_input_output(input_args, output_args)

    def test_set_chn_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        ivps_filter = create_random_int()
        c_chn_attr = create_random_ctypes_instance_ex(AX_IVPS_CHN_ATTR_T)
        d_chn_attr = c_chn_attr.struct2dict()

        # invoke
        ret = axcl.ivps.set_chn_attr(ivps_grp, ivps_chn, ivps_filter, d_chn_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), IVPS_FILTER(ivps_filter), c_chn_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_chn_attr(self):
        # prepare input
        ivps_grp = create_random_int()
        ivps_chn = create_random_int()
        ivps_filter = create_random_int()

        # invoke
        d_chn_attr, ret = axcl.ivps.get_chn_attr(ivps_grp, ivps_chn, ivps_filter)
        c_chn_attr = AX_IVPS_CHN_ATTR_T()
        c_chn_attr.dict2struct(d_chn_attr)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), IVPS_CHN(ivps_chn), IVPS_FILTER(ivps_filter))
        output_args = serialize_ctypes_args(AX_S32(ret), c_chn_attr)
        assert 0 == check_input_output(input_args, output_args)

    def test_enable_backup_frame(self):
        # prepare input
        ivps_grp = create_random_int()
        fifo_depth = create_random_int()

        # invoke
        ret = axcl.ivps.enable_backup_frame(ivps_grp, fifo_depth)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp), AX_U8(fifo_depth))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_disable_backup_frame(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        ret = axcl.ivps.disable_backup_frame(ivps_grp)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_reset_grp(self):
        # prepare input
        ivps_grp = create_random_int()

        # invoke
        ret = axcl.ivps.reset_grp(ivps_grp)

        # check output
        input_args = serialize_ctypes_args(IVPS_GRP(ivps_grp))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_engine_duty_cycle(self):
        # invoke
        d_duty_cycle_info, ret = axcl.ivps.get_engine_duty_cycle()
        c_duty_cycle_info = AX_IVPS_DUTY_CYCLE_ATTR_T()
        c_duty_cycle_info.dict2struct(d_duty_cycle_info)

        # check output
        input_args = serialize_ctypes_args()
        output_args = serialize_ctypes_args(AX_S32(ret), c_duty_cycle_info)
        assert 0 == check_input_output(input_args, output_args)

    def test_rgn_create(self):
        # invoke
        handle = axcl.ivps.rgn_create()
        if handle is not None:
            # check output
            input_args = serialize_ctypes_args()
            output_args = serialize_ctypes_args(IVPS_RGN_HANDLE(handle))
            assert 0 == check_input_output(input_args, output_args)

    def test_rgn_destroy(self):
        # prepare input
        region = create_random_int()

        # invoke
        ret = axcl.ivps.rgn_destroy(region)

        # check output
        input_args = serialize_ctypes_args(IVPS_RGN_HANDLE(region))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_rgn_attach_to_filter(self):
        # prepare input
        region = create_random_int()
        ivps_grp = create_random_int()
        ivps_filter = create_random_int()

        # invoke
        ret = axcl.ivps.rgn_attach_to_filter(region, ivps_grp, ivps_filter)

        # check output
        input_args = serialize_ctypes_args(IVPS_RGN_HANDLE(region), IVPS_GRP(ivps_grp), IVPS_FILTER(ivps_filter))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_rgn_detach_from_filter(self):
        # prepare input
        region = create_random_int()
        ivps_grp = create_random_int()
        ivps_filter = create_random_int()

        # invoke
        ret = axcl.ivps.rgn_detach_from_filter(region, ivps_grp, ivps_filter)

        # check output
        input_args = serialize_ctypes_args(IVPS_RGN_HANDLE(region), IVPS_GRP(ivps_grp), IVPS_FILTER(ivps_filter))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_rgn_update(self):
        # prepare input
        region = create_random_int()

        c_rgn_chn_attr = create_random_ctypes_instance_ex(AX_IVPS_RGN_CHN_ATTR_T)
        d_rgn_chn_attr = c_rgn_chn_attr.struct2dict()

        num = AX_IVPS_REGION_MAX_DISP_NUM

        c_disp_list = (AX_IVPS_RGN_DISP_T * num)()
        d_disp_list = []
        for i in range(len(c_disp_list)):
            random_ctypes_instance_ex(c_disp_list[i])
            d_disp_list.append(c_disp_list[i].struct2dict(c_disp_list[i]))

        c_disp = AX_IVPS_RGN_DISP_GROUP_T()
        c_disp.nNum = len(d_disp_list)
        c_disp.tChnAttr.dict2struct(d_rgn_chn_attr)
        for i in range(c_disp.nNum):
            c_disp.arrDisp[i].dict2struct(d_disp_list[i], c_disp.arrDisp[i])

        # invoke
        ret = axcl.ivps.rgn_update(region, d_rgn_chn_attr, d_disp_list)

        # check output
        input_args = serialize_ctypes_args(IVPS_RGN_HANDLE(region), c_disp)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_cmm_copy_tdp(self):
        # prepare input
        src_phy_addr = create_random_int()
        dst_phy_addr = create_random_int()
        mem_size = create_random_int()

        # invoke
        ret = axcl.ivps.cmm_copy_tdp(src_phy_addr, dst_phy_addr, mem_size)

        # check output
        input_args = serialize_ctypes_args(AX_U64(src_phy_addr), AX_U64(dst_phy_addr), AX_U64(mem_size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_flip_and_rotation_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        flip_mode = create_random_int()
        rotation = create_random_int()

        # invoke
        ret = axcl.ivps.flip_and_rotation_tdp(d_src, flip_mode, rotation, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, AX_IVPS_CHN_FLIP_MODE_E(flip_mode), AX_IVPS_ROTATION_E(rotation), c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_csc_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.csc_tdp(d_src, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        # invoke
        ret = axcl.ivps.crop_resize_tdp(d_src, d_dst, d_aspect_ratio)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst, c_aspect_ratio)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_v2_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_box_list = (AX_IVPS_RECT_T * num)()
        d_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_box_list[i])
            d_box_list.append(c_box_list[i].struct2dict())

        c_dst_list = (AX_VIDEO_FRAME_T * num)()
        d_dst_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst_list[i])
            d_dst_list.append(c_dst_list[i].struct2dict())

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        # invoke
        ret = axcl.ivps.crop_resize_v2_tdp(d_src, d_box_list, d_dst_list, d_aspect_ratio)

        # check output
        input_args = serialize_ctypes_args(c_src, c_box_list[0], AX_U32(num), c_dst_list[0], c_aspect_ratio)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_alpha_blending_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_overlay = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_overlay = c_overlay.struct2dict()

        c_offset = create_random_ctypes_instance_ex(AX_IVPS_POINT_T)
        d_offset = c_offset.struct2dict()

        alpha = create_random_int()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.alpha_blending_tdp(d_src, d_overlay, d_offset, alpha, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_overlay, c_offset, AX_U8(alpha), c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_alpha_blending_v3_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_overlay = create_random_ctypes_instance_ex(AX_OVERLAY_T)
        d_overlay = c_overlay.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.alpha_blending_v3_tdp(d_src, d_overlay, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_overlay, c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_osd_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_bmp_list = (AX_OSD_BMP_ATTR_T * num)()
        d_bmp_list = []
        for i in range(len(c_bmp_list)):
            d_bmp_list.append(c_bmp_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.draw_osd_tdp(d_src, d_bmp_list)

        # check output
        input_args = serialize_ctypes_args(c_src, c_bmp_list[0], AX_U32(num))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_mosaic_tdp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_mosaic_list = (AX_IVPS_RGN_MOSAIC_T * num)()
        d_mosaic_list = []
        for i in range(len(c_mosaic_list)):
            random_ctypes_instance_ex(c_mosaic_list[i])
            d_mosaic_list.append(c_mosaic_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.draw_mosaic_tdp(d_src, d_mosaic_list)

        # check output
        input_args = serialize_ctypes_args(c_src, c_mosaic_list[0], AX_U32(num))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_cmm_copy_vpp(self):
        # prepare input
        src_phy_addr = create_random_int()
        dst_phy_addr = create_random_int()
        mem_size = create_random_int()

        # invoke
        ret = axcl.ivps.cmm_copy_vpp(src_phy_addr, dst_phy_addr, mem_size)

        # check output
        input_args = serialize_ctypes_args(AX_U64(src_phy_addr), AX_U64(dst_phy_addr), AX_U64(mem_size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_vpp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.crop_resize_vpp(d_src, d_dst, d_aspect_ratio)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst, c_aspect_ratio)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_v2_vpp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_box_list =  (AX_IVPS_RECT_T * num)()
        d_box_list = []
        for i in range(len(c_box_list)):
            random_ctypes_instance_ex(c_box_list[i])
            d_box_list.append(c_box_list[i].struct2dict())

        c_dst_list =  (AX_VIDEO_FRAME_T * num)()
        d_dst_list = []
        for i in range(len(c_dst_list)):
            random_ctypes_instance_ex(c_dst_list[i])
            d_dst_list.append(c_dst_list[i].struct2dict())

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        # invoke
        ret = axcl.ivps.crop_resize_v2_vpp(d_src, d_box_list, d_dst_list, d_aspect_ratio)

        # check output
        input_args = serialize_ctypes_args(c_src, c_box_list[0], AX_U32(num), c_dst_list[0], c_aspect_ratio)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_v3_vpp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        c_dst_list =  (AX_VIDEO_FRAME_T * num)()
        d_dst_list = []
        for i in range(len(c_dst_list)):
            random_ctypes_instance_ex(c_dst_list[i])
            d_dst_list.append(c_dst_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.crop_resize_v3_vpp(d_src, d_dst_list, d_aspect_ratio)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst_list[0], AX_U32(num), c_aspect_ratio)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_csc_vpp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.csc_vpp(d_src, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_mosaic_vpp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_mosaic_list = (AX_IVPS_RGN_MOSAIC_T * num)()
        d_mosaic_list = []
        for i in range(len(c_mosaic_list)):
            d_mosaic_list.append(c_mosaic_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.draw_mosaic_vpp(d_src, d_mosaic_list)

        # check output
        input_args = serialize_ctypes_args(c_src, c_mosaic_list[0], AX_U32(num))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_set_scale_coef_level_vpp(self):
        # prepare input
        c_scale_range = create_random_ctypes_instance_ex(AX_IVPS_SCALE_RANGE_T)
        d_scale_range = c_scale_range.struct2dict()
        c_coef_level = create_random_ctypes_instance_ex(AX_IVPS_SCALE_COEF_LEVEL_T)
        d_coef_level = c_coef_level.struct2dict()

        # invoke
        ret = axcl.ivps.set_scale_coef_level_vpp(d_scale_range, d_coef_level)

        # check output
        input_args = serialize_ctypes_args(c_scale_range, c_coef_level)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_scale_coef_level_vpp(self):
        # prepare input
        c_scale_range = create_random_ctypes_instance_ex(AX_IVPS_SCALE_RANGE_T)
        d_scale_range = c_scale_range.struct2dict()

        c_coef_level = AX_IVPS_SCALE_COEF_LEVEL_T()

        # invoke
        d_coef_level, ret = axcl.ivps.get_scale_coef_level_vpp(d_scale_range)
        c_coef_level.dict2struct(d_coef_level)

        # check output
        input_args = serialize_ctypes_args(c_scale_range)
        output_args = serialize_ctypes_args(AX_S32(ret), c_coef_level)
        assert 0 == check_input_output(input_args, output_args)

    def test_cmm_copy_vgp(self):
        # prepare input
        src_phy_addr = create_random_int()
        dst_phy_addr = create_random_int()
        mem_size = create_random_int()

        # invoke
        ret = axcl.ivps.cmm_copy_vgp(src_phy_addr, dst_phy_addr, mem_size)

        # check output
        input_args = serialize_ctypes_args(AX_U64(src_phy_addr), AX_U64(dst_phy_addr), AX_U64(mem_size))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_csc_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.csc_vgp(d_src, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        # invoke
        ret = axcl.ivps.crop_resize_vgp(d_src, d_dst, d_aspect_ratio)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst, c_aspect_ratio)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_v2_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_box_list = (AX_IVPS_RECT_T * num)()
        d_box_list = []
        for i in range(len(c_box_list)):
            random_ctypes_instance_ex(c_box_list[i])
            d_box_list.append(c_box_list[i].struct2dict())

        c_dst_list =  (AX_VIDEO_FRAME_T * num)()
        d_dst_list = []
        for i in range(len(c_dst_list)):
            random_ctypes_instance_ex(c_dst_list[i])
            d_dst_list.append(c_dst_list[i].struct2dict())

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        # invoke
        ret = axcl.ivps.crop_resize_v2_vgp(d_src, d_box_list, d_dst_list, d_aspect_ratio)

        # check output
        input_args = serialize_ctypes_args(c_src, c_box_list[0], AX_U32(num), c_dst_list[0], c_aspect_ratio)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_v4_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        c_aspect_ratio = create_random_ctypes_instance_ex(AX_IVPS_ASPECT_RATIO_T)
        d_aspect_ratio = c_aspect_ratio.struct2dict()

        c_scale_step = create_random_ctypes_instance_ex(AX_IVPS_SCALE_STEP_T)
        d_scale_step = c_scale_step.struct2dict()

        # invoke
        ret = axcl.ivps.crop_resize_v4_vgp(d_src, d_dst, d_aspect_ratio, d_scale_step)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst, c_aspect_ratio, c_scale_step)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_alpha_blending_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_overlay = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_overlay = c_overlay.struct2dict()

        c_offset = create_random_ctypes_instance_ex(AX_IVPS_POINT_T)
        d_offset = c_offset.struct2dict()

        alpha = create_random_int()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.alpha_blending_vgp(d_src, d_overlay, d_offset, alpha, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_overlay, c_offset, AX_U8(alpha), c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_alpha_blending_v2_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_overlay = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_overlay = c_overlay.struct2dict()

        c_offset = create_random_ctypes_instance_ex(AX_IVPS_POINT_T)
        d_offset = c_offset.struct2dict()

        c_alpha_lut = create_random_ctypes_instance_ex(AX_IVPS_ALPHA_LUT_T)
        d_alpha_lut = c_alpha_lut.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.alpha_blending_v2_vgp(d_src, d_overlay, d_offset, d_alpha_lut, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_overlay, c_offset, c_alpha_lut, c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_alpha_blending_v3_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_overlay = create_random_ctypes_instance_ex(AX_OVERLAY_T)
        d_overlay = c_overlay.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.alpha_blending_v3_vgp(d_src, d_overlay, d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_overlay, c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_osd_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_bmp_list = (AX_OSD_BMP_ATTR_T * num)()
        d_bmp_list = []
        for i in range(len(c_bmp_list)):
            random_ctypes_instance_ex(c_bmp_list[i])
            d_bmp_list.append(c_bmp_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.draw_osd_vgp(d_src, d_bmp_list)

        # check output
        input_args = serialize_ctypes_args(c_src, c_bmp_list[0], AX_S32(num))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_mosaic_vgp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        num = 1

        c_mosaic_list = (AX_IVPS_RGN_MOSAIC_T * num)()
        d_mosaic_list = []
        for i in range(len(c_mosaic_list)):
            random_ctypes_instance_ex(c_mosaic_list[i])
            d_mosaic_list.append(c_mosaic_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.draw_mosaic_vgp(d_src, d_mosaic_list)

        # check output
        input_args = serialize_ctypes_args(c_src, c_mosaic_list[0], AX_U32(num))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_set_scale_coef_level_vgp(self):
        # prepare input
        c_scale_range = create_random_ctypes_instance_ex(AX_IVPS_SCALE_RANGE_T)
        d_scale_range = c_scale_range.struct2dict()

        c_coef_level = create_random_ctypes_instance_ex(AX_IVPS_SCALE_COEF_LEVEL_T)
        d_coef_level = c_coef_level.struct2dict()

        # invoke
        ret = axcl.ivps.set_scale_coef_level_vgp(d_scale_range, d_coef_level)

        # check output
        input_args = serialize_ctypes_args(c_scale_range, c_coef_level)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_get_scale_coef_level_vgp(self):
        # prepare input
        c_scale_range = create_random_ctypes_instance_ex(AX_IVPS_SCALE_RANGE_T)
        d_scale_range = c_scale_range.struct2dict()

        # invoke
        d_coef_level, ret = axcl.ivps.get_scale_coef_level_vgp(d_scale_range)
        c_coef_level = AX_IVPS_SCALE_COEF_LEVEL_T()
        c_coef_level.dict2struct(d_coef_level)

        # check output
        input_args = serialize_ctypes_args(c_scale_range)
        output_args = serialize_ctypes_args(AX_S32(ret), c_coef_level)
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_line(self):
        # prepare input
        c_canvas = create_random_ctypes_instance_ex(AX_IVPS_RGN_CANVAS_INFO_T)
        d_canvas = c_canvas.struct2dict()

        c_gdi_attr = create_random_ctypes_instance_ex(AX_IVPS_GDI_ATTR_T)
        d_gdi_attr = c_gdi_attr.struct2dict()

        num = 1

        c_point_list = (AX_IVPS_POINT_T * num)()
        d_point_list = []
        for i in range(len(c_point_list)):
            random_ctypes_instance_ex(c_point_list[i])
            d_point_list.append(c_point_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.draw_line(d_canvas, d_gdi_attr, d_point_list)

        # check output
        input_args = serialize_ctypes_args(c_canvas, c_gdi_attr, c_point_list[0], AX_U32(num))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_polygon(self):
        # prepare input
        c_canvas = create_random_ctypes_instance_ex(AX_IVPS_RGN_CANVAS_INFO_T)
        d_canvas = c_canvas.struct2dict()

        c_gdi_attr = create_random_ctypes_instance_ex(AX_IVPS_GDI_ATTR_T)
        d_gdi_attr = c_gdi_attr.struct2dict()

        num = 1

        c_point_list = (AX_IVPS_POINT_T * num)()
        d_point_list = []
        for i in range(len(c_point_list)):
            d_point_list.append(c_point_list[i].struct2dict())

        # invoke
        ret = axcl.ivps.draw_polygon(d_canvas, d_gdi_attr, d_point_list)

        # check output
        input_args = serialize_ctypes_args(c_canvas, c_gdi_attr, c_point_list[0], AX_U32(num))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_draw_rect(self):
        # prepare input
        c_canvas = create_random_ctypes_instance_ex(AX_IVPS_RGN_CANVAS_INFO_T)
        d_canvas = c_canvas.struct2dict()

        c_gdi_attr = create_random_ctypes_instance_ex(AX_IVPS_GDI_ATTR_T)
        d_gdi_attr = c_gdi_attr.struct2dict()

        c_rect = create_random_ctypes_instance_ex(AX_IVPS_RECT_T)
        d_rect = c_rect.struct2dict()

        # invoke
        ret = axcl.ivps.draw_rect(d_canvas, d_gdi_attr, d_rect)

        # check output
        input_args = serialize_ctypes_args(c_canvas, c_gdi_attr, c_rect)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_dewarp(self):
        # prepare input
        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        c_dewarp_attr = create_random_ctypes_instance_ex(AX_IVPS_DEWARP_ATTR_T)
        d_dewarp_attr = c_dewarp_attr.struct2dict()

        # invoke
        ret = axcl.ivps.dewarp(d_src, d_dst, d_dewarp_attr)

        # check output
        input_args = serialize_ctypes_args(c_src, c_dst, c_dewarp_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_pyra_lite_gen(self):
        # prepare input
        c_src_pyra = create_random_ctypes_instance_ex(AX_PYRA_FRAME_T)
        d_src_pyra = c_src_pyra.struct2dict()

        c_dst_pyra = create_random_ctypes_instance_ex(AX_PYRA_FRAME_T)
        d_dst_pyra = c_dst_pyra.struct2dict()

        mask = True

        # invoke
        ret = axcl.ivps.pyra_lite_gen(d_src_pyra, d_dst_pyra, mask)

        # check output
        input_args = serialize_ctypes_args(c_src_pyra, c_dst_pyra, AX_BOOL(mask))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_pyra_lite_rcn(self):
        # prepare input
        c_src_pyra = create_random_ctypes_instance_ex(AX_PYRA_FRAME_T)
        d_src_pyra = c_src_pyra.struct2dict()

        c_dst_pyra = create_random_ctypes_instance_ex(AX_PYRA_FRAME_T)
        d_dst_pyra = c_dst_pyra.struct2dict()

        bottom = True

        # invoke
        ret = axcl.ivps.pyra_lite_rcn(d_src_pyra, d_dst_pyra, bottom)

        # check output
        input_args = serialize_ctypes_args(c_src_pyra, c_dst_pyra, AX_BOOL(bottom))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_gdc_work_create(self):
        # prepare input
        # No input needed for this function

        # invoke
        gdc_handle, ret = axcl.ivps.gdc_work_create()

        # check output
        input_args = serialize_ctypes_args()
        output_args = serialize_ctypes_args(AX_S32(ret), GDC_HANDLE(gdc_handle))
        assert 0 == check_input_output(input_args, output_args)

    def test_gdc_work_attr_set(self):
        # prepare input
        gdc_handle = create_random_int()

        c_gdc_attr = create_random_ctypes_instance_ex(AX_IVPS_GDC_ATTR_T)
        d_gdc_attr = c_gdc_attr.struct2dict()

        # invoke
        ret = axcl.ivps.gdc_work_attr_set(gdc_handle, d_gdc_attr)

        # check output
        input_args = serialize_ctypes_args(GDC_HANDLE(gdc_handle), c_gdc_attr)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_gdc_work_run(self):
        # prepare input
        gdc_handle = create_random_int()

        c_src = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_ctypes_instance_ex(AX_VIDEO_FRAME_T)
        d_dst = c_dst.struct2dict()

        # invoke
        ret = axcl.ivps.gdc_work_run(gdc_handle, d_src, d_dst)

        # check output
        input_args = serialize_ctypes_args(GDC_HANDLE(gdc_handle), c_src, c_dst)
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_gdc_work_destroy(self):
        # prepare input
        gdc_handle = create_random_int()

        # invoke
        ret = axcl.ivps.gdc_work_destroy(gdc_handle)

        # check output
        input_args = serialize_ctypes_args(GDC_HANDLE(gdc_handle))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_fisheye_point_query_dst2src(self):
        # prepare input
        c_dst_point = create_random_ctypes_instance_ex(AX_IVPS_POINT_NICE_T)
        d_dst_point = c_dst_point.struct2dict()

        input_w = create_random_int()
        input_h = create_random_int()
        rgn_idx = create_random_int()

        c_fisheye_attr = create_random_ctypes_instance_ex(AX_IVPS_FISHEYE_ATTR_T)
        d_fisheye_attr = c_fisheye_attr.struct2dict()

        # invoke
        d_src_point, ret = axcl.ivps.fisheye_point_query_dst2src(d_dst_point, input_w, input_h, rgn_idx, d_fisheye_attr)
        c_src_point = AX_IVPS_POINT_NICE_T()
        c_src_point.dict2struct(d_src_point)

        # check output
        input_args = serialize_ctypes_args(c_dst_point, AX_U16(input_w), AX_U16(input_h), AX_U8(rgn_idx), c_fisheye_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), c_src_point)
        assert 0 == check_input_output(input_args, output_args)

    def test_fisheye_point_query_src2dst(self):
        # prepare input
        c_src_point = create_random_ctypes_instance_ex(AX_IVPS_POINT_NICE_T)
        d_src_point = c_src_point.struct2dict()

        input_w = create_random_int()
        input_h = create_random_int()
        rgn_idx = create_random_int()

        c_fisheye_attr = create_random_ctypes_instance_ex(AX_IVPS_FISHEYE_ATTR_T)
        d_fisheye_attr = c_fisheye_attr.struct2dict()

        # invoke
        d_dst_point, ret = axcl.ivps.fisheye_point_query_src2dst(d_src_point, input_w, input_h, rgn_idx, d_fisheye_attr)
        c_dst_point = AX_IVPS_POINT_NICE_T()
        c_dst_point.dict2struct(d_dst_point)

        # check output
        input_args = serialize_ctypes_args(c_src_point, AX_U16(input_w), AX_U16(input_h), AX_U8(rgn_idx), c_fisheye_attr)
        output_args = serialize_ctypes_args(AX_S32(ret), c_dst_point)
        assert 0 == check_input_output(input_args, output_args)
