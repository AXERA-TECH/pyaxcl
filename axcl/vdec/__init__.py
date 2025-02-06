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

from axcl.vdec.axcl_vdec import get_buf_size
from axcl.vdec.axcl_vdec import init
from axcl.vdec.axcl_vdec import deinit
from axcl.vdec.axcl_vdec import extract_stream_header_info
from axcl.vdec.axcl_vdec import create_grp
from axcl.vdec.axcl_vdec import create_grp_ex
from axcl.vdec.axcl_vdec import destroy_grp
from axcl.vdec.axcl_vdec import get_grp_attr
from axcl.vdec.axcl_vdec import set_grp_attr
from axcl.vdec.axcl_vdec import start_recv_stream
from axcl.vdec.axcl_vdec import stop_recv_stream
from axcl.vdec.axcl_vdec import query_status
from axcl.vdec.axcl_vdec import reset_grp
from axcl.vdec.axcl_vdec import set_grp_param
from axcl.vdec.axcl_vdec import get_grp_param
from axcl.vdec.axcl_vdec import select_grp
from axcl.vdec.axcl_vdec import send_stream
from axcl.vdec.axcl_vdec import get_chn_frame
from axcl.vdec.axcl_vdec import release_chn_frame
from axcl.vdec.axcl_vdec import get_user_data
from axcl.vdec.axcl_vdec import release_user_data
from axcl.vdec.axcl_vdec import set_user_pic
from axcl.vdec.axcl_vdec import enable_user_pic
from axcl.vdec.axcl_vdec import disable_user_pic
from axcl.vdec.axcl_vdec import set_display_mode
from axcl.vdec.axcl_vdec import get_display_mode
from axcl.vdec.axcl_vdec import attach_pool
from axcl.vdec.axcl_vdec import detach_pool
from axcl.vdec.axcl_vdec import enable_chn
from axcl.vdec.axcl_vdec import disable_chn
from axcl.vdec.axcl_vdec import set_chn_attr
from axcl.vdec.axcl_vdec import get_chn_attr
from axcl.vdec.axcl_vdec import jpeg_decode_one_frame
from axcl.vdec.axcl_vdec import get_vui_param
