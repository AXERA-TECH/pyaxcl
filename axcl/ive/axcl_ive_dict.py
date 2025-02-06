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
sys.path.append(BASE_DIR)

from axcl.ax_global_type import *
from axcl.ive.axcl_ive_type import *
from axcl.utils.axcl_utils import *

def ax_ive_data_to_dict(c_data: AX_IVE_DATA_T, dict):
    dict['phy_addr'] = c_data.u64PhyAddr
    dict['vir_addr'] = c_data.u64VirAddr
    dict['stride'] = c_data.u32Stride
    dict['width'] = c_data.u32Width
    dict['height'] = c_data.u32Height
    dict['reserved'] = c_data.u32Reserved

def ax_ive_image_to_dict(c_image: AX_IVE_IMAGE_T, dict, engine = AX_IVE_ENGINE_IVE):
    dict['phy_addr'] = list(c_image.au64PhyAddr)
    dict['vir_addr'] = list(c_image.au64VirAddr)
    dict['stride'] = list(c_image.au32Stride)
    dict['width'] = c_image.u32Width
    dict['height'] = c_image.u32Height

    dict['image_type'] = {}
    if engine == AX_IVE_ENGINE_IVE:
        dict['image_type']['type'] = c_image.uImageType.enType
    else:
        dict['image_type']['glb_type'] = c_image.uImageType.enGlbType

def ax_ive_images_to_dict(c_images: POINTER(AX_IVE_IMAGE_T), dict, engine = AX_IVE_ENGINE_IVE):
    for idx, image in enumerate(c_images):
        c_image = image.contents
        d = {}
        ax_ive_image_to_dict(c_image, d, engine)
        dict.append(d)

def ax_ive_mem_info_to_dict(c_mem_info: AX_IVE_MEM_INFO_T, dict):
    dict['phy_addr'] = c_mem_info.u64PhyAddr
    dict['vir_addr'] = c_mem_info.u64VirAddr
    dict['size'] = c_mem_info.u32Size

def ax_ive_mau_blob_to_dict(c_blob: AX_IVE_MAU_BLOB_T, dict):
    dict['phy_addr'] = c_blob.u64PhyAddr
    dict['vir_addr'] = c_blob.pVirAddr
    if c_blob.pShape:
        shape_list = []
        for i in range(c_blob.u8ShapeSize):
            shape_value = c_blob.pShape[i]
            if shape_value != 0:
                shape_list.append(shape_value)
            else:
                break
        dict['shape'] = shape_list
    else:
        dict['shape'] = []
    dict['type'] = c_blob.enDataType

def ax_ive_mau_matmul_output_to_dict(c_output: AX_IVE_MAU_MATMUL_OUTPUT_T, dict):
    mul_res_dict = {}
    ax_ive_mau_blob_to_dict(c_output.stMulRes, mul_res_dict)
    dict['mul_res'] = mul_res_dict

    top_n_res_dict = {}
    ax_ive_mau_blob_to_dict(c_output.stTopNRes, top_n_res_dict)
    dict['top_n_res'] = top_n_res_dict

def ax_ive_region_to_dict(c_region: AX_IVE_REGION_T, dict):
    dict['label_status'] = c_region.u8LabelStatus
    dict['area'] = c_region.u32Area
    dict['left'] = c_region.u16Left
    dict['right'] = c_region.u16Right
    dict['top'] = c_region.u16Top
    dict['bottom'] = c_region.u16Bottom

def ax_ive_ccblob_to_dict(c_ccblob: AX_IVE_CCBLOB_T, dict):
    if c_ccblob.astRegion:
        region_list = []
        for i in range(c_ccblob.u16RegionNum):
            c_region = {}
            region = c_ccblob.astRegion[i]
            ax_ive_region_to_dict(region, c_region)
            region_list.append(c_region)
        dict['region'] = region_list
    else:
        dict['region'] = []

def dict_to_ax_ive_data(dict, c_data: AX_IVE_DATA_T):
    c_data.u64PhyAddr = AX_U64(dict.get('phy_addr', 0))
    c_data.u64VirAddr = AX_U64(dict.get('vir_addr', 0))
    c_data.u32Stride = AX_U32(dict.get('stride', 0))
    c_data.u32Width = AX_U32(dict.get('width', 0))
    c_data.u32Height = AX_U32(dict.get('height', 0))
    c_data.u32Reserved = AX_U32(dict.get('reserved', 0))

def dict_to_ax_ive_image(dict, c_image: AX_IVE_IMAGE_T):
    phy_addr = dict.get('phy_addr', [])
    c_image.au64PhyAddr = dict_array_to_array(phy_addr, AX_U64, 3)

    vir_addr = dict.get('vir_addr', [])
    c_image.au64VirAddr = dict_array_to_array(vir_addr, AX_U64, 3)

    stride = dict.get('stride', [])
    c_image.au32Stride = dict_array_to_array(stride, AX_U32, 3)

    c_image.u32Width = AX_U32(dict.get('width', 0))
    c_image.u32Height = AX_U32(dict.get('height', 0))
    image_type = dict.get('image_type')
    if image_type:
        if image_type.get('type') is not None:
            c_image.uImageType.enType = AX_IVE_IMAGE_TYPE_E(image_type['type'])
        elif image_type.get('glb_type') is not None:
            c_image.uImageType.enGlbType = AX_IMG_FORMAT_E(image_type['glb_type'])

def dict_to_ax_ive_mem_info(dict, c_mem_info: AX_IVE_MEM_INFO_T):
    c_mem_info.u64PhyAddr = AX_U64(dict.get('phy_addr', 0))
    c_mem_info.u64VirAddr = AX_U64(dict.get('vir_addr', 0))
    c_mem_info.u32Size = AX_U32(dict.get('size', 0))

def dict_to_ax_ive_point(dict, c_point: AX_IVE_POINT_S16_T):
    c_point.s16X = AX_U16(dict.get('x', 0))
    c_point.s16Y = AX_U16(dict.get('y', 0))

def dict_to_ax_ive_rect(dict, c_rect: AX_IVE_RECT_U16_T):
    c_rect.u16X = AX_U16(dict.get('x', 0))
    c_rect.u16Y = AX_U16(dict.get('y', 0))
    c_rect.u16Width = AX_U16(dict.get('w', 0))
    c_rect.u16Height = AX_U16(dict.get('h', 0))

def dict_to_ax_ive_mau_blob(dict, c_mau_blob: AX_IVE_MAU_BLOB_T):
    c_mau_blob.u64PhyAddr = AX_U64(dict.get('phy_addr', 0))
    c_mau_blob.pVirAddr = c_void_p(dict.get('vir_addr', 0))

    shape_list = dict.get('shape', [])
    if shape_list:
        shape_size = len(shape_list)
        shape_array = (AX_S32 * shape_size)(*shape_list)
        c_mau_blob.pShape = POINTER(AX_S32)(shape_array)
    else:
        shape_size = 0
        c_mau_blob.pShape = POINTER(AX_S32)(None)

    c_mau_blob.u8ShapeSize = shape_size
    c_mau_blob.enDataType = AX_IVE_MAU_DATA_TYPE_E(dict.get('type', 0))

def dict_to_ax_ive_mau_matmul_input(dict, c_input: AX_IVE_MAU_MATMUL_INPUT_T):
    c_mat_q = AX_IVE_MAU_BLOB_T()
    c_mat_b = AX_IVE_MAU_BLOB_T()

    mat_q = dict.get('mat_q')
    if mat_q:
        dict_to_ax_ive_mau_blob(mat_q, c_mat_q)

    mat_b = dict.get('mat_b')
    if mat_b:
        dict_to_ax_ive_mau_blob(mat_b, c_mat_b)

    c_input.stMatQ = c_mat_q
    c_input.stMatB = c_mat_b

def dict_to_ax_ive_mau_matmul_output(dict, c_output: AX_IVE_MAU_MATMUL_OUTPUT_T):
    c_mul_res = AX_IVE_MAU_BLOB_T()
    c_top_n_res = AX_IVE_MAU_BLOB_T()

    mul_res = dict.get('mul_res')
    if mul_res:
        dict_to_ax_ive_mau_blob(mul_res, c_mul_res)

    top_n_res = dict.get('top_n_res')
    if top_n_res:
        dict_to_ax_ive_mau_blob(top_n_res, c_top_n_res)

    c_output.stMulRes = c_mul_res
    c_output.stTopNRes = c_top_n_res

def dict_to_ax_ive_images(dict, c_images: POINTER(AX_IVE_IMAGE_T)):
    for idx, d in enumerate(dict):
        c_image = AX_IVE_IMAGE_T()
        dict_to_ax_ive_image(d, c_image)
        c_images[idx] = POINTER(AX_IVE_IMAGE_T)(c_image)

def dict_to_ax_ive_rects(dict, c_rects: POINTER(AX_IVE_RECT_U16_T)):
    for idx, d in enumerate(dict):
        c_rect = AX_IVE_RECT_U16_T()
        dict_to_ax_ive_rect(d, c_rect)
        c_rects[idx] = POINTER(AX_IVE_RECT_U16_T)(c_rect)

def dict_to_ax_ive_dma_ctrl(dict, c_ctrl: AX_IVE_DMA_CTRL_T):
    c_ctrl.enMode = AX_IVE_DMA_MODE_E(dict.get('mode', AX_IVE_DMA_MODE_DIRECT_COPY))
    c_ctrl.u64Val = AX_U64(dict.get('val', 0))
    c_ctrl.u8HorSegSize = AX_U8(dict.get('hor_seg_size', 0))
    c_ctrl.u8ElemSize = AX_U8(dict.get('elem_size', 0))
    c_ctrl.u8VerSegRows = AX_U8(dict.get('ver_seg_rows', 0))
    c_ctrl.u16CrpX0 = AX_U16(dict.get('crp_x', 0))
    c_ctrl.u16CrpY0 = AX_U16(dict.get('crp_y', 0))

def dict_to_ax_ive_add_ctrl(dict, c_ctrl: AX_IVE_ADD_CTRL_T):
    c_ctrl.u1q7X = AX_U1Q7(dict.get('x', 0))
    c_ctrl.u1q7Y = AX_U1Q7(dict.get('y', 0))

def dict_to_ax_ive_sub_ctrl(dict, c_ctrl: AX_IVE_SUB_CTRL_T):
    c_ctrl.enMode = AX_IVE_SUB_MODE_E(dict.get('mode', AX_IVE_SUB_MODE_ABS))

def dict_to_ax_ive_mse_ctrl(dict, c_ctrl: AX_IVE_MSE_CTRL_T):
    c_ctrl.u1q15MseCoef = AX_U1Q15(dict.get('coef', 0))

def dict_to_ax_ive_hys_edge_ctrl(dict, c_ctrl: AX_IVE_HYS_EDGE_CTRL_T):
    c_ctrl.u16LowThr = AX_U16(dict.get('low_thr', 0))
    c_ctrl.u16HighThr = AX_U16(dict.get('high_thr', 0))

def dict_to_ax_ive_canny_edge_ctrl(dict, c_ctrl: AX_IVE_CANNY_EDGE_CTRL_T):
    c_ctrl.u8Thr = AX_U8(dict.get('thr', 0))

def dict_to_ax_ive_ccl_ctrl(dict, c_ctrl: AX_IVE_CCL_CTRL_T):
    c_ctrl.enMode = AX_IVE_CCL_MODE_E(dict.get('mode', AX_IVE_CCL_MODE_4C))

def dict_to_ax_ive_erode_ctrl(dict, c_ctrl: AX_IVE_ERODE_CTRL_T):
    mask = dict.get('mask', [])
    c_ctrl.au8Mask = dict_array_to_array(mask, AX_U8, 25)

def dict_to_ax_ive_dilate_ctrl(dict, c_ctrl: AX_IVE_DILATE_CTRL_T):
    mask = dict.get('mask', [])
    c_ctrl.au8Mask = dict_array_to_array(mask, AX_U8, 25)

def dict_to_ax_ive_filter_ctrl(dict, c_ctrl: AX_IVE_FILTER_CTRL_T):
    mask = dict.get('mask', [])
    c_ctrl.as6q10Mask = dict_array_to_array(mask, AX_S6Q10, 25)

def dict_to_ax_ive_equalize_hist_ctrl(dict, c_ctrl: AX_IVE_EQUALIZE_HIST_CTRL_T):
    c_ctrl.u0q20HistEqualCoef = AX_U0Q20(dict.get('coef', 0))

def dict_to_ax_ive_integ_ctrl(dict, c_ctrl: AX_IVE_INTEG_CTRL_T):
    c_ctrl.enOutCtrl = AX_IVE_INTEG_OUT_CTRL_E(dict.get('ctrl', AX_IVE_INTEG_OUT_CTRL_SUM))

def dict_to_ax_ive_sobel_ctrl(dict, c_ctrl: AX_IVE_SOBEL_CTRL_T):
    mask = dict.get('mask', [])
    c_ctrl.as6q10Mask = dict_array_to_array(mask, AX_S6Q10, 25)

def dict_to_ax_ive_gmm_ctrl(dict, c_ctrl: AX_IVE_GMM_CTRL_T):
    c_ctrl.u14q4InitVar = AX_U14Q4(dict.get('init_var', 0))
    c_ctrl.u14q4MinVar = AX_U14Q4(dict.get('min_var', 0))
    c_ctrl.u1q10InitWeight = AX_U1Q10(dict.get('init_weight', 0))
    c_ctrl.u1q7LearnRate = AX_U1Q7(dict.get('learn_rate', 0))
    c_ctrl.u1q7BgRatio = AX_U1Q7(dict.get('bg_ratio', 0))
    c_ctrl.u4q4VarThr = AX_U4Q4(dict.get('var_thr', 0))
    c_ctrl.u8Thr = AX_U8(dict.get('thr', 1))

def dict_to_ax_ive_gmm2_ctrl(dict, c_ctrl: AX_IVE_GMM2_CTRL_T):
    c_ctrl.u14q4InitVar = AX_U14Q4(dict.get('init_var', 0))
    c_ctrl.u14q4MinVar = AX_U14Q4(dict.get('min_var', 0))
    c_ctrl.u14q4MaxVar = AX_U14Q4(dict.get('max_var', 0))
    c_ctrl.u1q7LearnRate = AX_U1Q7(dict.get('learn_rate', 0))
    c_ctrl.u1q7BgRatio = AX_U1Q7(dict.get('bg_ratio', 0))
    c_ctrl.u4q4VarThr = AX_U4Q4(dict.get('var_thr', 0))
    c_ctrl.u4q4VarThrCheck = AX_U4Q4(dict.get('var_thr_check', 0))
    c_ctrl.s1q7CT = AX_S1Q7(dict.get('ct', 0))
    c_ctrl.u8Thr = AX_U8(dict.get('thr', 1))

def dict_to_ax_ive_thresh_ctrl(dict, c_ctrl: AX_IVE_THRESH_CTRL_T):
    c_ctrl.enMode = AX_IVE_THRESH_MODE_E(dict.get('mode', AX_IVE_THRESH_MODE_BINARY))
    c_ctrl.u8LowThr = AX_U8(dict.get('low_thr', 0))
    c_ctrl.u8HighThr = AX_U8(dict.get('high_thr', 0))
    c_ctrl.u8MinVal = AX_U8(dict.get('min_val', 0))
    c_ctrl.u8MidVal = AX_U8(dict.get('mid_val', 0))
    c_ctrl.u8MaxVal = AX_U8(dict.get('max_val', 0))

def dict_to_ax_ive_16bit_to_8bit_ctrl(dict, c_ctrl: AX_IVE_16BIT_TO_8BIT_CTRL_T):
    c_ctrl.enMode = AX_IVE_16BIT_TO_8BIT_MODE_E(dict.get('mode', AX_IVE_16BIT_TO_8BIT_MODE_S16_TO_S8))
    c_ctrl.s1q14Gain = AX_S1Q14(dict.get('gain', 0))
    c_ctrl.s16Bias = AX_S16(dict.get('bias', 0))

def dict_to_ax_ive_crop_image_ctrl(dict, c_ctrl: AX_IVE_CROP_IMAGE_CTRL_T):
    c_ctrl.u16Num = AX_U16(dict.get('num', 0))

def dict_to_ax_ive_crop_resize_ctrl(dict, c_ctrl: AX_IVE_CROP_RESIZE_CTRL_T):
    c_ctrl.u16Num = AX_U16(dict.get('num', 0))

    align = dict.get('align', [])
    c_ctrl.enAlign = dict_array_to_array(align, AX_IVE_ASPECT_RATIO_ALIGN_MODE_E, 2, AX_IVE_ASPECT_RATIO_FORCE_RESIZE)

    c_ctrl.u32BorderColor = AX_U32(dict.get('border_color', 0))

def dict_to_ax_ive_npu_matmul_ctrl(dict, c_ctrl: AX_IVE_NPU_MATMUL_CTRL_T):
    if dict.get('pch_mode_dir') is not None:
        pch_mode_dir = cast(dict['pch_mode_dir'], POINTER(AX_CHAR))
        c_ctrl.pchModelDir = pch_mode_dir
    else:
        c_ctrl.pchModelDir = POINTER(AX_CHAR)(None)

    c_ctrl.enDataType = AX_IVE_MAU_DATA_TYPE_E(dict.get('type', AX_IVE_MAU_DT_UINT8))
    c_ctrl.s32KSize = AX_S32(dict.get('ksize', 0))

def dict_to_ax_ive_mau_matmul_ctrl(dict, c_ctrl: AX_IVE_MAU_MATMUL_CTRL_T):
    c_ctrl.enMauId = AX_IVE_MAU_ID_E(dict.get('id', AX_IVE_MAU_ID_0))
    c_ctrl.s32DdrReadBandwidthLimit = AX_S32(dict.get('ddr_read_bandwidth_limit', 0))
    c_ctrl.bEnableMulRes = AX_BOOL(1 if dict.get('is_enable_mul_res', False) else 0)
    c_ctrl.bEnableTopNRes = AX_BOOL(1 if dict.get('is_enable_top_n_res', False) else 0)
    c_ctrl.enOrder = AX_IVE_MAU_ORDER_E(dict.get('order', AX_IVE_MAU_ORDER_ASCEND))
    c_ctrl.s32TopN = AX_S32(dict.get('top_n', 0))

