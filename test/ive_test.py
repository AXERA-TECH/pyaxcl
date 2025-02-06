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
from axcl.ive.axcl_ive_type import *
from ut_help import *


IVE_IMAGE_TYPE_KEY = "type"
GLB_IMAGE_TYPE_KEY = "glb_type"

def random_ctypes_instance_ex(ctype_obj):
    ctype_obj.random_struct(ctype_obj)


def set_c_struct_image_type(obj, image_type_key, image_type_val):
    if image_type_key == IVE_IMAGE_TYPE_KEY:
        obj.uImageType.enType = image_type_val
    elif image_type_key == GLB_IMAGE_TYPE_KEY:
        obj.uImageType.enGlbType = image_type_val

def create_random_image_type_key():
    return choose_random_from_list([IVE_IMAGE_TYPE_KEY, GLB_IMAGE_TYPE_KEY])

def create_random_glb_image_type():
    return choose_random_from_list([AX_FORMAT_INVALID,
                                # YUV400 8 bit
                                AX_FORMAT_YUV400,
                                # YUV420 8 bit
                                AX_FORMAT_YUV420_PLANAR,
                                AX_FORMAT_YUV420_PLANAR_VU,
                                AX_FORMAT_YUV420_SEMIPLANAR,
                                AX_FORMAT_YUV420_SEMIPLANAR_VU,
                                # YUV422 8 bit
                                AX_FORMAT_YUV422_PLANAR,
                                AX_FORMAT_YUV422_PLANAR_VU,
                                AX_FORMAT_YUV422_SEMIPLANAR,
                                AX_FORMAT_YUV422_SEMIPLANAR_VU,
                                AX_FORMAT_YUV422_INTERLEAVED_YUVY,
                                AX_FORMAT_YUV422_INTERLEAVED_YUYV,
                                AX_FORMAT_YUV422_INTERLEAVED_UYVY,
                                AX_FORMAT_YUV422_INTERLEAVED_VYUY,
                                AX_FORMAT_YUV422_INTERLEAVED_YVYU,
                                # YUV444 8 bit
                                AX_FORMAT_YUV444_PLANAR,
                                AX_FORMAT_YUV444_PLANAR_VU,
                                AX_FORMAT_YUV444_SEMIPLANAR,
                                AX_FORMAT_YUV444_SEMIPLANAR_VU,
                                AX_FORMAT_YUV444_PACKED,
                                # YUV 10 bit
                                AX_FORMAT_YUV400_10BIT,
                                AX_FORMAT_YUV420_PLANAR_10BIT_UV_PACKED_4Y5B,
                                AX_FORMAT_YUV420_PLANAR_10BIT_I010,
                                AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P101010,
                                AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P010,
                                AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P016,
                                AX_FORMAT_YUV420_SEMIPLANAR_10BIT_I016,
                                AX_FORMAT_YUV420_SEMIPLANAR_10BIT_12P16B,
                                AX_FORMAT_YUV444_PACKED_10BIT_P010,
                                AX_FORMAT_YUV444_PACKED_10BIT_P101010,
                                AX_FORMAT_YUV422_SEMIPLANAR_10BIT_P101010,
                                AX_FORMAT_YUV422_SEMIPLANAR_10BIT_P010,
                                # BAYER RAW
                                AX_FORMAT_BAYER_RAW_8BPP,
                                AX_FORMAT_BAYER_RAW_10BPP,
                                AX_FORMAT_BAYER_RAW_12BPP,
                                AX_FORMAT_BAYER_RAW_14BPP,
                                AX_FORMAT_BAYER_RAW_16BPP,
                                AX_FORMAT_BAYER_RAW_10BPP_PACKED,
                                AX_FORMAT_BAYER_RAW_12BPP_PACKED,
                                AX_FORMAT_BAYER_RAW_14BPP_PACKED,
                                # RGB Format
                                AX_FORMAT_RGB565,
                                AX_FORMAT_RGB888,
                                AX_FORMAT_KRGB444,
                                AX_FORMAT_KRGB555,
                                AX_FORMAT_KRGB888,
                                AX_FORMAT_BGR888,
                                AX_FORMAT_BGR565,
                                AX_FORMAT_ARGB4444,
                                AX_FORMAT_ARGB1555,
                                AX_FORMAT_ARGB8888,
                                AX_FORMAT_ARGB8565,
                                AX_FORMAT_RGBA8888,
                                AX_FORMAT_RGBA5551,
                                AX_FORMAT_RGBA4444,
                                AX_FORMAT_RGBA5658,
                                AX_FORMAT_ABGR4444,
                                AX_FORMAT_ABGR1555,
                                AX_FORMAT_ABGR8888,
                                AX_FORMAT_ABGR8565,
                                AX_FORMAT_BGRA8888,
                                AX_FORMAT_BGRA5551,
                                AX_FORMAT_BGRA4444,
                                AX_FORMAT_BGRA5658,
                                AX_FORMAT_BITMAP,
                                AX_FORMAT_MAX])

def create_random_ive_image_type():
    return choose_random_from_list([AX_IVE_IMAGE_TYPE_U8C1,
                                AX_IVE_IMAGE_TYPE_S8C1,
                                AX_IVE_IMAGE_TYPE_YUV420SP,
                                AX_IVE_IMAGE_TYPE_YUV422SP,
                                AX_IVE_IMAGE_TYPE_YUV420P,
                                AX_IVE_IMAGE_TYPE_YUV422P,
                                AX_IVE_IMAGE_TYPE_S8C2_PACKAGE,
                                AX_IVE_IMAGE_TYPE_S8C2_PLANAR,
                                AX_IVE_IMAGE_TYPE_S16C1,
                                AX_IVE_IMAGE_TYPE_U16C1,
                                AX_IVE_IMAGE_TYPE_U8C3_PACKAGE,
                                AX_IVE_IMAGE_TYPE_U8C3_PLANAR,
                                AX_IVE_IMAGE_TYPE_S32C1,
                                AX_IVE_IMAGE_TYPE_U32C1,
                                AX_IVE_IMAGE_TYPE_S64C1,
                                AX_IVE_IMAGE_TYPE_U64C1,
                                AX_IVE_IMAGE_TYPE_BUTT
                                ])

class TestIve:
    def test_init(self):
        # prepare input
        # No input needed, as init has no parameters

        # invoke
        ret = axcl.ive.init()

        # check output
        assert 0 == ret

    def test_exit(self):
        pass

    def test_query(self):
        # prepare input
        handle = AX_IVE_HANDLE(1)
        block = True

        # invoke
        ret_finish, ret = axcl.ive.query(handle, block)

        # check output
        input_args = serialize_ctypes_args(handle, AX_BOOL(block))
        output_args = serialize_ctypes_args(AX_BOOL(ret_finish), AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_dma(self):
        # prepare input
        c_src = create_random_struct_instance(AX_IVE_SRC_DATA_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_struct_instance(AX_IVE_DST_DATA_T)
        d_dst = c_dst.struct2dict()

        c_ctrl = create_random_struct_instance(AX_IVE_DMA_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.dma(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_DATA_T()
        c_dst_r.dict2struct(d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_add(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_ADD_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()
        instant = True

        # invoke
        handle, ret = axcl.ive.add(d_src1, d_src2, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_sub(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_SUB_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.sub(d_src1, d_src2, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_ive_and(self):

        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        instant = True

        # invoke
        handle, ret = axcl.ive.ive_and(d_src1, d_src2, d_dst, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_ive_or(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        instant = True

        # invoke
        handle, ret = axcl.ive.ive_or(d_src1, d_src2, d_dst, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_xor(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        instant = True

        # invoke
        handle, ret = axcl.ive.xor(d_src1, d_src2, d_dst, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_mse(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_MSE_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.mse(d_src1, d_src2, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_canny_hys_edge(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_HYS_EDGE_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.canny_hys_edge(d_src1, d_src2, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_canny_edge(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_CANNY_EDGE_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.canny_edge(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_ccl(self):

        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_blob = create_random_struct_instance(AX_IVE_DST_MEM_INFO_T)
        d_blob = c_blob.struct2dict()

        c_ctrl = create_random_struct_instance(AX_IVE_CCL_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.ccl(d_src, d_dst, d_blob, d_ctrl, instant)

        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        c_blob_r = AX_IVE_DST_MEM_INFO_T()
        c_blob_r.dict2struct(d_blob)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, c_blob_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_erode(self):

        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_ERODE_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.erode(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_dilate(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_DILATE_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.dilate(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_filter(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_FILTER_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.filter(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_hist(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_MEM_INFO_T)
        d_dst = c_dst.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.hist(d_src, d_dst, instant)
        c_dst_r = AX_IVE_DST_MEM_INFO_T()
        c_dst_r.dict2struct(d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_equalize_hist(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_MEM_INFO_T)
        d_dst = c_dst.struct2dict()

        c_ctrl = create_random_struct_instance(AX_IVE_EQUALIZE_HIST_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.equalize_hist(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_MEM_INFO_T()
        c_dst_r.dict2struct(d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_integ(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_INTEG_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.integ(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_mag_and_ang(self):

        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst_mag = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst_mag = c_dst_mag.struct2dict()
        d_dst_mag[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst_mag, image_type_key, image_type_val)

        c_dst_ang = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst_ang = c_dst_ang.struct2dict()
        d_dst_ang[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst_ang, image_type_key, image_type_val)

        instant = True

        # invoke
        handle, ret = axcl.ive.mag_and_ang(d_src1, d_src2, d_dst_mag, d_dst_ang, instant)

        c_dst_mag_r = AX_IVE_DST_IMAGE_T()
        c_dst_mag_r.dict2struct(d_dst_mag)
        set_c_struct_image_type(c_dst_mag_r, image_type_key, image_type_val)

        c_dst_ang_r = AX_IVE_DST_IMAGE_T()
        c_dst_ang_r.dict2struct(d_dst_ang)
        set_c_struct_image_type(c_dst_ang_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_mag_r, c_dst_ang_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_sobel(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_SOBEL_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.sobel(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_gmm(self):

        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst_fg = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst_fg = c_dst_fg.struct2dict()
        d_dst_fg[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst_fg, image_type_key, image_type_val)

        c_dst_bg = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst_bg = c_dst_bg.struct2dict()
        d_dst_bg[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst_bg, image_type_key, image_type_val)

        c_model = create_random_struct_instance(AX_IVE_MEM_INFO_T)
        d_model = c_model.struct2dict()

        c_ctrl = create_random_struct_instance(AX_IVE_GMM_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.gmm(d_src, d_dst_fg, d_dst_bg, d_model, d_ctrl, instant)

        c_dst_fg_r = AX_IVE_DST_IMAGE_T()
        c_dst_fg_r.dict2struct(d_dst_fg)
        set_c_struct_image_type(c_dst_fg_r, image_type_key, image_type_val)

        c_dst_bg_r = AX_IVE_DST_IMAGE_T()
        c_dst_bg_r.dict2struct(d_dst_bg)
        set_c_struct_image_type(c_dst_bg_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_model, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_fg_r, c_dst_bg_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_gmm2(self):
         # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst_fg = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst_fg = c_dst_fg.struct2dict()
        d_dst_fg[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst_fg, image_type_key, image_type_val)

        c_dst_bg = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst_bg = c_dst_bg.struct2dict()
        d_dst_bg[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst_bg, image_type_key, image_type_val)

        c_model = create_random_struct_instance(AX_IVE_MEM_INFO_T)
        d_model = c_model.struct2dict()

        c_ctrl = create_random_struct_instance(AX_IVE_GMM2_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.gmm2(d_src, d_dst_fg, d_dst_bg, d_model, d_ctrl, instant)

        c_dst_fg_r = AX_IVE_DST_IMAGE_T()
        c_dst_fg_r.dict2struct(d_dst_fg)
        set_c_struct_image_type(c_dst_fg_r, image_type_key, image_type_val)

        c_dst_bg_r = AX_IVE_DST_IMAGE_T()
        c_dst_bg_r.dict2struct(d_dst_bg)
        set_c_struct_image_type(c_dst_bg_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_model, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_fg_r, c_dst_bg_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_thresh(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_THRESH_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.thresh(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_ive_16bit_to_8bit(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        c_ctrl = create_random_struct_instance(AX_IVE_16BIT_TO_8BIT_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        instant = True

        # invoke
        handle, ret = axcl.ive.ive_16bit_to_8bit(d_src, d_dst, d_ctrl, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_image(self):

        # prepare input
        num = 1
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst_list = (AX_IVE_DST_IMAGE_T * num)()
        d_dst_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst_list[i])
            d_dst = c_dst_list[i].struct2dict()
            d_dst[image_type_key] = image_type_val
            set_c_struct_image_type(c_dst_list[i], image_type_key, image_type_val)
            d_dst_list.append(d_dst)

        c_box_list = (AX_IVE_RECT_U16_T * num)()
        d_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_box_list[i])
            d_box = c_box_list[i].struct2dict()
            d_box_list.append(d_box)

        c_ctrl = create_random_struct_instance(AX_IVE_CROP_IMAGE_CTRL_T)
        c_ctrl.u16Num = 1
        d_ctrl = c_ctrl.struct2dict()

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        handle, ret = axcl.ive.crop_image(d_src, d_dst_list, d_box_list, d_ctrl, engine, instant)
        c_dst_list_r = (AX_IVE_DST_IMAGE_T * num)()
        for i in range(num):
            c_dst_list_r[i].dict2struct(d_dst_list[i])
            set_c_struct_image_type(c_dst_list_r[i], image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_box_list[0], c_ctrl, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_list_r[0], AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize(self):
        # prepare input
        num = 1
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst_list = (AX_IVE_DST_IMAGE_T * num)()
        d_dst_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst_list[i])
            d_dst = c_dst_list[i].struct2dict()
            d_dst[image_type_key] = image_type_val
            set_c_struct_image_type(c_dst_list[i], image_type_key, image_type_val)
            d_dst_list.append(d_dst)

        c_box_list = (AX_IVE_RECT_U16_T * num)()
        d_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_box_list[i])
            d_box = c_box_list[i].struct2dict()
            d_box_list.append(d_box)

        c_ctrl = create_random_struct_instance(AX_IVE_CROP_RESIZE_CTRL_T)
        c_ctrl.u16Num = 1
        d_ctrl = c_ctrl.struct2dict()

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        handle, ret = axcl.ive.crop_resize(d_src, d_dst_list, d_box_list, d_ctrl, engine, instant)
        c_dst_list_r = (AX_IVE_DST_IMAGE_T * num)()
        for i in range(num):
            c_dst_list_r[i].dict2struct(d_dst_list[i])
            set_c_struct_image_type(c_dst_list_r[i], image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_box_list[0], c_ctrl, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_list_r[0], AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize_for_split_yuv(self):
        # prepare input
        num = 1
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst1_list = (AX_IVE_DST_IMAGE_T * num)()
        d_dst1_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst1_list[i])
            d_dst = c_dst1_list[i].struct2dict()
            d_dst[image_type_key] = image_type_val
            set_c_struct_image_type(c_dst1_list[i], image_type_key, image_type_val)
            d_dst1_list.append(d_dst)

        c_dst2_list = (AX_IVE_DST_IMAGE_T * num)()
        d_dst2_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst2_list[i])
            d_dst = c_dst2_list[i].struct2dict()
            d_dst[image_type_key] = image_type_val
            set_c_struct_image_type(c_dst2_list[i], image_type_key, image_type_val)
            d_dst2_list.append(d_dst)

        c_box_list = (AX_IVE_RECT_U16_T * num)()
        d_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_box_list[i])
            d_box = c_box_list[i].struct2dict()
            d_box_list.append(d_box)

        c_ctrl = create_random_struct_instance(AX_IVE_CROP_RESIZE_CTRL_T)
        c_ctrl.u16Num = 1
        d_ctrl = c_ctrl.struct2dict()

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        handle, ret = axcl.ive.crop_resize_for_split_yuv(d_src1, d_src2, d_dst1_list, d_dst2_list, d_box_list, d_ctrl, engine, instant)
        c_dst1_list_r = (AX_IVE_DST_IMAGE_T * num)()
        for i in range(num):
            c_dst1_list_r[i].dict2struct(d_dst1_list[i])
            set_c_struct_image_type(c_dst1_list_r[i], image_type_key, image_type_val)

        c_dst2_list_r = (AX_IVE_DST_IMAGE_T * num)()
        for i in range(num):
            c_dst2_list_r[i].dict2struct(d_dst2_list[i])
            set_c_struct_image_type(c_dst2_list_r[i], image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, c_box_list[0], c_ctrl, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst1_list_r[0], c_dst2_list_r[0], AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_csc(self):
        # prepare input
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst = create_random_struct_instance(AX_IVE_DST_IMAGE_T)
        d_dst = c_dst.struct2dict()
        d_dst[image_type_key] = image_type_val
        set_c_struct_image_type(c_dst, image_type_key, image_type_val)

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        handle, ret = axcl.ive.csc(d_src, d_dst, engine, instant)
        c_dst_r = AX_IVE_DST_IMAGE_T()
        c_dst_r.dict2struct(d_dst)
        set_c_struct_image_type(c_dst_r, image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize2(self):
        # prepare input
        num = 1
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src = c_src.struct2dict()
        d_src[image_type_key] = image_type_val
        set_c_struct_image_type(c_src, image_type_key, image_type_val)

        c_dst_list = (AX_IVE_DST_IMAGE_T * num)()
        d_dst_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst_list[i])
            d_dst = c_dst_list[i].struct2dict()
            d_dst[image_type_key] = image_type_val
            set_c_struct_image_type(c_dst_list[i], image_type_key, image_type_val)
            d_dst_list.append(d_dst)

        c_src_box_list = (AX_IVE_RECT_U16_T * num)()
        d_src_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_src_box_list[i])
            d_box = c_src_box_list[i].struct2dict()
            d_src_box_list.append(d_box)

        c_dst_box_list = (AX_IVE_RECT_U16_T * num)()
        d_dst_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst_box_list[i])
            d_box = c_dst_box_list[i].struct2dict()
            d_dst_box_list.append(d_box)

        c_ctrl = create_random_struct_instance(AX_IVE_CROP_IMAGE_CTRL_T)
        c_ctrl.u16Num = 1
        d_ctrl = c_ctrl.struct2dict()

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        handle, ret = axcl.ive.crop_resize2(d_src, d_dst_list, d_src_box_list, d_dst_box_list, d_ctrl, engine, instant)
        c_dst_list_r = (AX_IVE_DST_IMAGE_T * num)()
        for i in range(num):
            c_dst_list_r[i].dict2struct(d_dst_list[i])
            set_c_struct_image_type(c_dst_list_r[i], image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src, c_src_box_list[0], c_dst_box_list[0], c_ctrl, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_list_r[0], AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_crop_resize2_for_split_yuv(self):
         # prepare input
        num = 1
        image_type_key = create_random_image_type_key()
        image_type_val = create_random_ive_image_type() if image_type_key == IVE_IMAGE_TYPE_KEY else create_random_glb_image_type()

        c_src1 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src1 = c_src1.struct2dict()
        d_src1[image_type_key] = image_type_val
        set_c_struct_image_type(c_src1, image_type_key, image_type_val)

        c_src2 = create_random_struct_instance(AX_IVE_SRC_IMAGE_T)
        d_src2 = c_src2.struct2dict()
        d_src2[image_type_key] = image_type_val
        set_c_struct_image_type(c_src2, image_type_key, image_type_val)

        c_dst1_list = (AX_IVE_DST_IMAGE_T * num)()
        d_dst1_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst1_list[i])
            d_dst = c_dst1_list[i].struct2dict()
            d_dst[image_type_key] = image_type_val
            set_c_struct_image_type(c_dst1_list[i], image_type_key, image_type_val)
            d_dst1_list.append(d_dst)

        c_dst2_list = (AX_IVE_DST_IMAGE_T * num)()
        d_dst2_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst2_list[i])
            d_dst = c_dst2_list[i].struct2dict()
            d_dst[image_type_key] = image_type_val
            set_c_struct_image_type(c_dst2_list[i], image_type_key, image_type_val)
            d_dst2_list.append(d_dst)

        c_src_box_list = (AX_IVE_RECT_U16_T * num)()
        d_src_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_src_box_list[i])
            d_box = c_src_box_list[i].struct2dict()
            d_src_box_list.append(d_box)

        c_dst_box_list = (AX_IVE_RECT_U16_T * num)()
        d_dst_box_list = []
        for i in range(num):
            random_ctypes_instance_ex(c_dst_box_list[i])
            d_box = c_dst_box_list[i].struct2dict()
            d_dst_box_list.append(d_box)

        c_ctrl = create_random_struct_instance(AX_IVE_CROP_IMAGE_CTRL_T)
        c_ctrl.u16Num = 1
        d_ctrl = c_ctrl.struct2dict()

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        handle, ret = axcl.ive.crop_resize2_for_split_yuv(d_src1, d_src2, d_dst1_list, d_dst2_list, d_src_box_list, d_dst_box_list, d_ctrl, engine, instant)
        c_dst1_list_r = (AX_IVE_DST_IMAGE_T * num)()
        for i in range(num):
            c_dst1_list_r[i].dict2struct(d_dst1_list[i])
            set_c_struct_image_type(c_dst1_list_r[i], image_type_key, image_type_val)

        c_dst2_list_r = (AX_IVE_DST_IMAGE_T * num)()
        for i in range(num):
            c_dst2_list_r[i].dict2struct(d_dst2_list[i])
            set_c_struct_image_type(c_dst2_list_r[i], image_type_key, image_type_val)

        # check output
        input_args = serialize_ctypes_args(c_src1, c_src2, c_src_box_list[0], c_dst_box_list[0], c_ctrl, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst1_list_r[0], c_dst2_list_r[0], AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_mau_matmul(self):
        # prepare input
        c_src = create_random_struct_instance(AX_IVE_MAU_MATMUL_INPUT_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_struct_instance(AX_IVE_MAU_MATMUL_OUTPUT_T)
        d_dst = c_dst.struct2dict()

        c_ctrl = create_random_struct_instance(AX_IVE_MAU_MATMUL_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        handle, ret = axcl.ive.mau_matmul(d_src, d_dst, d_ctrl, engine, instant)
        c_dst_r = AX_IVE_MAU_MATMUL_OUTPUT_T()
        c_dst_r.dict2struct(d_dst)

        # check output
        input_args = serialize_ctypes_args(c_src, c_ctrl, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(AX_IVE_HANDLE(handle), c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)


    def test_npu_create_matmul_handle(self):
        # prepare input
        c_ctrl = create_random_struct_instance(AX_IVE_NPU_MATMUL_CTRL_T)
        d_ctrl = c_ctrl.struct2dict()

        # invoke
        handle, ret = axcl.ive.npu_create_matmul_handle(d_ctrl)

        # check output
        input_args = serialize_ctypes_args(c_ctrl)
        output_args = serialize_ctypes_args(AX_IVE_MATMUL_HANDLE(handle), AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_npu_destroy_matmul_handle(self):
        # prepare input
        handle = 1

        # invoke
        ret = axcl.ive.npu_destroy_matmul_handle(AX_IVE_MATMUL_HANDLE(handle))

        # check output
        input_args = serialize_ctypes_args(AX_U64(handle))
        output_args = serialize_ctypes_args(AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)

    def test_npu_matmul(self):

        # prepare input
        handle = AX_IVE_MATMUL_HANDLE(1)

        c_src = create_random_struct_instance(AX_IVE_MAU_MATMUL_INPUT_T)
        d_src = c_src.struct2dict()

        c_dst = create_random_struct_instance(AX_IVE_MAU_MATMUL_OUTPUT_T)
        d_dst = c_dst.struct2dict()

        engine = AX_IVE_ENGINE_VPP

        instant = True

        # invoke
        ret = axcl.ive.npu_matmul(handle, d_src, d_dst, engine, instant)

        c_dst_r = AX_IVE_MAU_MATMUL_OUTPUT_T()
        c_dst_r.dict2struct(d_dst)

        # check output
        input_args = serialize_ctypes_args(AX_U64(ctypes.addressof(handle)), c_src, AX_S32(engine), AX_BOOL(instant))
        output_args = serialize_ctypes_args(c_dst_r, AX_S32(ret))
        assert 0 == check_input_output(input_args, output_args)