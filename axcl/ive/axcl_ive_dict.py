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

IVE_IMAGE_TYPE_KEY = "type"
GLB_IMAGE_TYPE_KEY = "glb_type"

def dict_to_ive_image(d_obj: dict, c_obj):
    c_obj.dict2struct(d_obj)
    if IVE_IMAGE_TYPE_KEY in d_obj:
        c_obj.uImageType.enType = d_obj.get(IVE_IMAGE_TYPE_KEY, AX_IVE_IMAGE_TYPE_BUTT)
    else: # GLB_IMAGE_TYPE_KEY in d_obj:
        c_obj.uImageType.enGlbType = d_obj.get(GLB_IMAGE_TYPE_KEY, AX_FORMAT_INVALID)

def ive_image_to_dict(c_obj, d_obj: dict, engine=AX_IVE_ENGINE_BUTT):
    d_obj.update(c_obj.struct2dict())
    if engine == AX_IVE_ENGINE_BUTT:
        if IVE_IMAGE_TYPE_KEY in d_obj:
            d_obj[IVE_IMAGE_TYPE_KEY] = c_obj.uImageType.enType
        else: # GLB_IMAGE_TYPE_KEY in d_obj:
            d_obj[GLB_IMAGE_TYPE_KEY] = c_obj.uImageType.enGlbType
    else:
        if engine == AX_IVE_ENGINE_IVE:
            d_obj[IVE_IMAGE_TYPE_KEY] = c_obj.uImageType.enType
        else:
            d_obj[GLB_IMAGE_TYPE_KEY] = c_obj.uImageType.enGlbType
