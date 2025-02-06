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

def query_test():
    print("=========query api test begin=========")

    instant = True

    handle = AX_IVE_HANDLE(1)

    result_dst, ret = axcl.ive.query(handle, instant)

    if ret == 0:
        print("query operation completed successfully.")
        print(f"query handle[{handle.value}] finish: [{result_dst}]")
    else:
        print(f"query operation failed with error code {ret}.")

    print("==========query api test end==========")

def dma_test():
    print("=========dma api test begin=========")

    src = {
        'phy_addr': 0x10000000,
        'vir_addr': 0x20000000,
        'stride': 1920,
        'width': 1920,
        'height': 1080,
        'reserved': 0
    }

    dst = {
        'phy_addr': 0x30000000,
        'vir_addr': 0x40000000,
        'stride': 1920,
        'width': 1920,
        'height': 1080,
        'reserved': 0
    }

    ctrl = {
        'mode': AX_IVE_DMA_MODE_INTERVAL_COPY,
        'val': 0,
        'hor_seg_size': 16,
        'elem_size': 8,
        'ver_seg_rows': 4,
        'crp_x': 88,
        'crp_y': 99
    }

    instant = True

    handle, ret = axcl.ive.dma(src, dst, ctrl, instant)

    if ret == 0:
        print("dma operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"dma operation failed with error code {ret}.")

    print("==========dma api test end==========")

def add_test():
    print("=========add api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'x': 0x01,
        'y': 0x02
    }

    instant = True

    handle, ret = axcl.ive.add(src1, src2, dst, ctrl, instant)

    if ret == 0:
        print("add operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"add operation failed with error code {ret}.")

    print("==========add api test end==========")

def sub_test():
    print("=========sub api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'mode': AX_IVE_SUB_MODE_SHIFT
    }

    instant = True

    handle, ret = axcl.ive.sub(src1, src2, dst, ctrl, instant)

    if ret == 0:
        print("sub operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"sub operation failed with error code {ret}.")

    print("==========sub api test end==========")

def and_test():
    print("=========and api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    instant = True

    handle, ret = axcl.ive.ive_and(src1, src2, dst, instant)

    if ret == 0:
        print("and operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"and operation failed with error code {ret}.")

    print("==========and api test end==========")

def or_test():
    print("=========or api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    instant = True

    handle, ret = axcl.ive.ive_or(src1, src2, dst, instant)

    if ret == 0:
        print("or operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"or operation failed with error code {ret}.")

    print("==========or api test end==========")

def xor_test():
    print("=========xor api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    instant = True

    handle, ret = axcl.ive.xor(src1, src2, dst, instant)

    if ret == 0:
        print("xor operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"xor operation failed with error code {ret}.")

    print("==========xor api test end==========")

def mse_test():
    print("=========mse api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'coef': 0x02
    }

    instant = True

    handle, ret = axcl.ive.mse(src1, src2, dst, ctrl, instant)

    if ret == 0:
        print("mse operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"mse operation failed with error code {ret}.")

    print("==========mse api test end==========")

def canny_hys_edge_test():
    print("=========canny_hys_edge api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'low_thr': 0x10,
        'high_thr': 0x40,
    }

    instant = True

    handle, ret = axcl.ive.canny_hys_edge(src1, src2, dst, ctrl, instant)

    if ret == 0:
        print("canny_hys_edge operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"canny_hys_edge operation failed with error code {ret}.")

    print("==========canny_hys_edge api test end==========")

def canny_edge_test():
    print("=========canny_edge api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'thr': 0x20
    }

    instant = True

    handle, ret = axcl.ive.canny_edge(src, dst, ctrl, instant)

    if ret == 0:
        print("canny_edge operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"canny_edge operation failed with error code {ret}.")

    print("==========canny_edge api test end==========")

def ccl_test():
    print("=========ccl api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    blob = {
        'phy_addr': 0x50000000,
        'vir_addr': 0x60000000,
        'size': int(1920 * 1280 * 3 / 2)
    }

    ctrl = {
        'mode': AX_IVE_CCL_MODE_8C
    }

    instant = True

    handle, ret = axcl.ive.ccl(src, dst, blob, ctrl, instant)

    if ret == 0:
        print("ccl operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
        print(f"blob: {blob}")
    else:
        print(f"ccl operation failed with error code {ret}.")

    print("==========ccl api test end==========")

def erode_test():
    print("=========erode api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'mask': [0x11] * 25
    }

    instant = True

    handle, ret = axcl.ive.erode(src, dst, ctrl, instant)

    if ret == 0:
        print("erode operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"erode operation failed with error code {ret}.")

    print("==========erode api test end==========")

def dilate_test():
    print("=========dilate api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'mask': [0x22] * 25
    }

    instant = True

    handle, ret = axcl.ive.dilate(src, dst, ctrl, instant)

    if ret == 0:
        print("dilate operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"dilate operation failed with error code {ret}.")

    print("==========dilate api test end==========")

def filter_test():
    print("=========filter api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'mask': [0x33] * 25
    }

    instant = True

    handle, ret = axcl.ive.filter(src, dst, ctrl, instant)

    if ret == 0:
        print("filter operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"filter operation failed with error code {ret}.")

    print("==========filter api test end==========")

def hist_test():
    print("=========hist api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': 0x30000000,
        'vir_addr': 0x40000000,
        'size': int(1920 * 1280 * 3 / 2)
    }

    instant = True

    handle, ret = axcl.ive.hist(src, dst, instant)

    if ret == 0:
        print("hist operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"hist operation failed with error code {ret}.")

    print("==========hist api test end==========")

def equalize_hist_test():
    print("=========equalize_hist api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': 0x30000000,
        'vir_addr': 0x40000000,
        'size': int(1920 * 1280 * 3 / 2)
    }

    ctrl = {
        'coef': 0x80
    }

    instant = True

    handle, ret = axcl.ive.equalize_hist(src, dst, ctrl, instant)

    if ret == 0:
        print("equalize_hist operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"equalize_hist operation failed with error code {ret}.")

    print("==========equalize_hist api test end==========")

def integ_test():
    print("=========integ api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'ctrl': AX_IVE_INTEG_OUT_CTRL_SQSUM
    }

    instant = True

    handle, ret = axcl.ive.integ(src, dst, ctrl, instant)

    if ret == 0:
        print("integ operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"integ operation failed with error code {ret}.")

    print("==========integ api test end==========")

def mag_and_ang_test():
    print("=========mag_and_ang api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst_mag = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst_ang = {
        'phy_addr': [0x70000000, 0x7017BB00, 0x0],
        'vir_addr': [0x80000000, 0x8017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    instant = True

    handle, ret = axcl.ive.mag_and_ang(src1, src2, dst_mag, dst_ang, instant)

    if ret == 0:
        print("mag_and_ang operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst_mag: {dst_mag}")
        print(f"dst_ang: {dst_ang}")
    else:
        print(f"mag_and_ang operation failed with error code {ret}.")

    print("==========mag_and_ang api test end==========")

def sobel_test():
    print("=========sobel api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'mask': [0x44] * 25
    }

    instant = True

    handle, ret = axcl.ive.sobel(src, dst, ctrl, instant)

    if ret == 0:
        print("sobel operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"sobel operation failed with error code {ret}.")

    print("==========sobel api test end==========")

def gmm_test():
    print("=========gmm api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst_fg = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst_bg = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    model = {
        'phy_addr': 0x90000000,
        'vir_addr': 0xA0000000,
        'size': 0x10000
    }

    ctrl = {
        'init_var': 0x1,
        'min_var': 0x2,
        'init_weight': 0x3,
        'learn_rate': 0x4,
        'bg_ratio': 0x5,
        'var_thr': 0x6,
        'thr': 0x7
    }

    instant = True

    handle, ret = axcl.ive.gmm(src, dst_fg, dst_bg, model, ctrl, instant)

    if ret == 0:
        print("gmm operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst_fg: {dst_fg}")
        print(f"dst_bg: {dst_bg}")
    else:
        print(f"gmm operation failed with error code {ret}.")

    print("==========gmm api test end==========")

def gmm2_test():
    print("=========gmm2 api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst_fg = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst_bg = {
        'phy_addr': [0x50000000, 0x5017BB00, 0x0],
        'vir_addr': [0x60000000, 0x6017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    model = {
        'phy_addr': 0x90000000,
        'vir_addr': 0xA0000000,
        'size': 0x10000
    }

    ctrl = {
        'init_var': 0x1,
        'min_var': 0x2,
        'max_var': 0x3,
        'learn_rate': 0x4,
        'bg_ratio': 0x5,
        'var_thr': 0x6,
        'var_thr_check': 0x7,
        'ct': 0x8,
        'thr': 0x9
    }

    instant = True

    handle, ret = axcl.ive.gmm2(src, dst_fg, dst_bg, model, ctrl, instant)

    if ret == 0:
        print("gmm2 operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst_fg: {dst_fg}")
        print(f"dst_bg: {dst_bg}")
    else:
        print(f"gmm2 operation failed with error code {ret}.")

    print("==========gmm2 api test end==========")

def thresh_test():
    print("=========thresh api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'mode': AX_IVE_THRESH_MODE_TO_MINVAL,
        'low_thr': 0x1,
        'high_thr': 0x2,
        'min_val': 0x3,
        'mid_val': 0x4,
        'max_val': 0x5
    }

    instant = True

    handle, ret = axcl.ive.thresh(src, dst, ctrl, instant)

    if ret == 0:
        print("thresh operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"thresh operation failed with error code {ret}.")

    print("==========thresh api test end==========")

def _16bit_to_8bit_test():
    print("=========16bit_to_8bit api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'type': AX_IVE_IMAGE_TYPE_YUV420SP
        }
    }

    ctrl = {
        'mode': AX_IVE_THRESH_MODE_TO_MINVAL,
        'gain': 0x7,
        'bias': 0x8
    }

    instant = True

    handle, ret = axcl.ive.ive_16bit_to_8bit(src, dst, ctrl, instant)

    if ret == 0:
        print("16bit_to_8bit operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"16bit_to_8bit operation failed with error code {ret}.")

    print("==========16bit_to_8bit api test end==========")

def crop_image_test():
    print("=========crop_image api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    dst_list = [
        {
            'phy_addr': [0x30000000, 0x3017BB00, 0x0],
            'vir_addr': [0x40000000, 0x4017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        },
        {
            'phy_addr': [0x50000000, 0x5017BB00, 0x0],
            'vir_addr': [0x60000000, 0x6017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        }
    ]

    box_list = [
        {
            'x': 50,
            'y': 50,
            'w': 200,
            'h': 200
        },
        {
            'x': 300,
            'y': 300,
            'w': 150,
            'h': 150
        }
    ]

    ctrl = {
        'num': 2
    }

    engine = AX_IVE_ENGINE_VPP

    instant = True

    handle, ret = axcl.ive.crop_image(src, dst_list, box_list, ctrl, engine, instant)

    if ret == 0:
        print("crop_image operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst_list: {dst_list}")
    else:
        print(f"crop_image operation failed with error code {ret}.")

    print("==========crop_image api test end==========")

def crop_resize_test():
    print("=========crop_resize api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    dst_list = [
        {
            'phy_addr': [0x30000000, 0x3017BB00, 0x0],
            'vir_addr': [0x40000000, 0x4017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        },
        {
            'phy_addr': [0x50000000, 0x5017BB00, 0x0],
            'vir_addr': [0x60000000, 0x6017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        }
    ]

    box_list = [
        {
            'x': 50,
            'y': 50,
            'w': 200,
            'h': 200
        },
        {
            'x': 300,
            'y': 300,
            'w': 150,
            'h': 150
        }
    ]

    ctrl = {
        'num': 2,
        'align': [AX_IVE_ASPECT_RATIO_HORIZONTAL_CENTER, AX_IVE_ASPECT_RATIO_VERTICAL_CENTER],
        'border_color': 0xFFFFFFFF
    }

    engine = AX_IVE_ENGINE_VPP

    instant = True

    handle, ret = axcl.ive.crop_resize(src, dst_list, box_list, ctrl, engine, instant)

    if ret == 0:
        print("crop_resize operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst_list: {dst_list}")
    else:
        print(f"crop_resize operation failed with error code {ret}.")

    print("==========crop_resize api test end==========")

def crop_resize_for_split_yuv_test():
    print("=========crop_resize_for_split_yuv api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    dst1_list = [
        {
            'phy_addr': [0x50000000, 0x5017BB00, 0x0],
            'vir_addr': [0x60000000, 0x6017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        },
        {
            'phy_addr': [0x70000000, 0x7017BB00, 0x0],
            'vir_addr': [0x80000000, 0x8017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        }
    ]

    dst2_list = [
        {
            'phy_addr': [0x90000000, 0x9017BB00, 0x0],
            'vir_addr': [0xa0000000, 0xa017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        },
        {
            'phy_addr': [0xb0000000, 0xb017BB00, 0x0],
            'vir_addr': [0xc0000000, 0xc017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        }
    ]

    box_list = [
        {
            'x': 50,
            'y': 50,
            'w': 200,
            'h': 200
        },
        {
            'x': 300,
            'y': 300,
            'w': 150,
            'h': 150
        }
    ]

    ctrl = {
        'num': 2,
        'align': [AX_IVE_ASPECT_RATIO_HORIZONTAL_CENTER, AX_IVE_ASPECT_RATIO_VERTICAL_CENTER],
        'border_color': 0xFFFFFFFF
    }

    engine = AX_IVE_ENGINE_VPP

    instant = True

    handle, ret = axcl.ive.crop_resize_for_split_yuv(src1, src2, dst1_list, dst2_list, box_list, ctrl, engine, instant)

    if ret == 0:
        print("crop_resize_for_split_yuv operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst1_list: {dst1_list}")
        print(f"dst2_list: {dst2_list}")
    else:
        print(f"crop_resize_for_split_yuv operation failed with error code {ret}.")

    print("==========crop_resize_for_split_yuv api test end==========")

def csc_test():
    print("=========csc api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    dst = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    engine = AX_IVE_ENGINE_VPP

    instant = True

    handle, ret = axcl.ive.csc(src, dst, engine, instant)

    if ret == 0:
        print("csc operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"csc operation failed with error code {ret}.")

    print("==========csc api test end==========")

def crop_resize2_test():
    print("=========crop_resize2 api test begin=========")

    src = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    dst_list = [
        {
            'phy_addr': [0x30000000, 0x3017BB00, 0x0],
            'vir_addr': [0x40000000, 0x4017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        },
        {
            'phy_addr': [0x50000000, 0x5017BB00, 0x0],
            'vir_addr': [0x60000000, 0x6017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        }
    ]

    src_box_list = [
        {
            'x': 50,
            'y': 50,
            'w': 200,
            'h': 200
        },
        {
            'x': 300,
            'y': 300,
            'w': 150,
            'h': 150
        }
    ]

    dst_box_list = [
        {
            'x': 50,
            'y': 50,
            'w': 200,
            'h': 200
        },
        {
            'x': 300,
            'y': 300,
            'w': 150,
            'h': 150
        }
    ]

    ctrl = {
        'num': 2
    }

    engine = AX_IVE_ENGINE_VPP

    instant = True

    handle, ret = axcl.ive.crop_resize2(src, dst_list, src_box_list, dst_box_list, ctrl, engine, instant)

    if ret == 0:
        print("crop_resize2 operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst_list: {dst_list}")
    else:
        print(f"crop_resize2 operation failed with error code {ret}.")

    print("==========crop_resize2 api test end==========")

def crop_resize2_for_split_yuv_test():
    print("=========crop_resize2_for_split_yuv api test begin=========")

    src1 = {
        'phy_addr': [0x10000000, 0x1017BB00, 0x0],
        'vir_addr': [0x20000000, 0x2017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    src2 = {
        'phy_addr': [0x30000000, 0x3017BB00, 0x0],
        'vir_addr': [0x40000000, 0x4017BB00, 0x0],
        'stride': [1920, 1920, 0],
        'width': 1920,
        'height': 1080,
        'image_type': {
            'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
        }
    }

    dst1_list = [
        {
            'phy_addr': [0x50000000, 0x5017BB00, 0x0],
            'vir_addr': [0x60000000, 0x6017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        },
        {
            'phy_addr': [0x70000000, 0x7017BB00, 0x0],
            'vir_addr': [0x80000000, 0x8017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        }
    ]

    dst2_list = [
        {
            'phy_addr': [0x90000000, 0x9017BB00, 0x0],
            'vir_addr': [0xa0000000, 0xa017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        },
        {
            'phy_addr': [0xb0000000, 0xb017BB00, 0x0],
            'vir_addr': [0xc0000000, 0xc017BB00, 0x0],
            'stride': [1920, 1920, 0],
            'width': 1920,
            'height': 1080,
            'image_type': {
                'glb_type': AX_FORMAT_YUV420_SEMIPLANAR
            }
        }
    ]

    src_box_list = [
        {
            'x': 50,
            'y': 50,
            'w': 200,
            'h': 200
        },
        {
            'x': 300,
            'y': 300,
            'w': 150,
            'h': 150
        }
    ]

    dst_box_list = [
        {
            'x': 50,
            'y': 50,
            'w': 200,
            'h': 200
        },
        {
            'x': 300,
            'y': 300,
            'w': 150,
            'h': 150
        }
    ]

    ctrl = {
        'num': 2
    }

    engine = AX_IVE_ENGINE_VPP

    instant = True

    handle, ret = axcl.ive.crop_resize2_for_split_yuv(src1, src2, dst1_list, dst2_list, src_box_list, dst_box_list, ctrl, engine, instant)

    if ret == 0:
        print("crop_resize2_for_split_yuv operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst1_list: {dst1_list}")
        print(f"dst2_list: {dst2_list}")
    else:
        print(f"crop_resize2_for_split_yuv operation failed with error code {ret}.")

    print("==========crop_resize2_for_split_yuv api test end==========")

def mau_matmul_test():
    print("=========mau_matmul api test begin=========")

    src = {
        'mat_q' : {
            'phy_addr': 0x10000000,
            'vir_addr': 0x20000000,
            'shape': [0x01, 0x02, 0x03, 0x04, 0x05],
            'type': AX_IVE_MAU_DT_UINT8
        },
        'mat_b' : {
            'phy_addr': 0x30000000,
            'vir_addr': 0x40000000,
            'shape': [0x06, 0x07, 0x08, 0x09, 0x0a],
            'type': AX_IVE_MAU_DT_UINT8
        }
    }

    dst = {
        'mul_res' : {
            'phy_addr': 0x50000000,
            'vir_addr': 0x60000000,
            'shape': [0x0a, 0x09, 0x08, 0x07, 0x06],
            'type': AX_IVE_MAU_DT_UINT8
        },
        'top_n_res' : {
            'phy_addr': 0x70000000,
            'vir_addr': 0x80000000,
            'shape': [0x05, 0x04, 0x03, 0x02, 0x01],
            'type': AX_IVE_MAU_DT_UINT8
        }
    }

    ctrl = {
        'id': AX_IVE_MAU_ID_0,
        'ddr_read_bandwidth_limit': 0x01,
        'is_enable_mul_res': True,
        'is_enable_top_n_res': False,
        'order': 0x04,
        'top_n': 0x05
    }

    engine = AX_IVE_ENGINE_VPP

    instant = True

    handle, ret = axcl.ive.mau_matmul(src, dst, ctrl, engine, instant)

    if ret == 0:
        print("mau_matmul operation completed successfully.")
        print(f"return handle: {handle}")
        print(f"dst: {dst}")
    else:
        print(f"mau_matmul operation failed with error code {ret}.")

    print("==========mau_matmul api test end==========")

def npu_create_matmul_handle_test():
    print("=========npu_create_matmul_handle api test begin=========")

    ctrl = {
        'pch_mode_dir': c_char_p("/tmp/123".encode('utf-8')),
        'type': AX_IVE_MAU_DT_UINT8,
        'ksize': 0x1000
    }

    handle, ret = axcl.ive.npu_create_matmul_handle(ctrl)

    if ret == 0:
        print("npu_create_matmul_handle operation completed successfully.")
        print(f"return handle: {hex(handle)}")
    else:
        print(f"npu_create_matmul_handle operation failed with error code {ret}.")

    print("==========npu_create_matmul_handle api test end==========")

def npu_destroy_matmul_handle_test():
    print("=========npu_destroy_matmul_handle api test begin=========")

    handle = AX_IVE_MATMUL_HANDLE(1)

    ret = axcl.ive.npu_destroy_matmul_handle(handle)

    if ret == 0:
        print("npu_destroy_matmul_handle operation completed successfully.")
        print(f"handle[{handle.value}] destroied.")
    else:
        print(f"npu_destroy_matmul_handle operation failed with error code {ret}.")

    print("==========npu_destroy_matmul_handle api test end==========")

def npu_matmul_test():
    print("=========npu_matmul api test begin=========")

    src1_shape = (AX_S32 * 5)(0x01, 0x02, 0x03, 0x04, 0x05)
    src2_shape = (AX_S32 * 5)(0x06, 0x07, 0x08, 0x09, 0x0a)

    src = {
        'mat_q' : {
            'phy_addr': 0x10000000,
            'vir_addr': 0x20000000,
            'shape': src1_shape,
            'type': AX_IVE_MAU_DT_UINT8
        },
        'mat_b' : {
            'phy_addr': 0x30000000,
            'vir_addr': 0x40000000,
            'shape': src2_shape,
            'type': AX_IVE_MAU_DT_UINT8
        }
    }

    dst1_shape = (AX_S32 * 5)(0x0a, 0x09, 0x08, 0x07, 0x06)
    dst2_shape = (AX_S32 * 5)(0x05, 0x04, 0x03, 0x02, 0x01)

    dst = {
        'mul_res' : {
            'phy_addr': 0x50000000,
            'vir_addr': 0x60000000,
            'shape': dst1_shape,
            'type': AX_IVE_MAU_DT_UINT8
        },
        'top_n_res' : {
            'phy_addr': 0x70000000,
            'vir_addr': 0x80000000,
            'shape': dst2_shape,
            'type': AX_IVE_MAU_DT_UINT8
        }
    }

    engine = AX_IVE_ENGINE_NPU

    instant = True

    handle = AX_IVE_MATMUL_HANDLE(30)

    ret = axcl.ive.npu_matmul(handle, src, dst, engine, instant)

    if ret == 0:
        print("npu_matmul operation completed successfully.")
        print(f"dst: {dst}")
    else:
        print(f"npu_matmul operation failed with error code {ret}.")

    print("==========npu_matmul api test end==========")

if __name__ == '__main__':

    ret = axcl.ive.init()

    print(f"ive init:ret={ret}")

    query_test()

    dma_test()

    add_test()

    sub_test()

    and_test()

    or_test()

    xor_test()

    mse_test()

    canny_hys_edge_test()

    canny_edge_test()

    ccl_test()

    erode_test()

    dilate_test()

    filter_test()

    hist_test()

    equalize_hist_test();

    integ_test();

    mag_and_ang_test();

    sobel_test()

    gmm_test()

    gmm2_test()

    thresh_test()

    _16bit_to_8bit_test()

    crop_image_test()

    crop_resize_test()

    crop_resize_for_split_yuv_test()

    csc_test()

    crop_resize2_test()

    crop_resize2_for_split_yuv_test()

    mau_matmul_test()

    npu_create_matmul_handle_test()

    npu_destroy_matmul_handle_test()

    npu_matmul_test()

    axcl.ive.exit()

    print(f"ive exit")
