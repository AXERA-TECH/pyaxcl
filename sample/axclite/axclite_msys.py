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
import axcl
from axclite.axclite_singleton import AxcliteSingleton
from axclite.axclite_vdec import AxcliteVdec
from axclite.axclite_venc import AxcliteVenc
from axclite.axclite_ivps import AxcliteIvps

AXCL_LITE_NONE = 0
AXCL_LITE_VDEC = (1 << 0)
AXCL_LITE_VENC = (1 << 1)
AXCL_LITE_IVPS = (1 << 2)
AXCL_LITE_JDEC = (1 << 3)
AXCL_LITE_JENC = (1 << 4)
AXCL_LITE_DEFAULT = (AXCL_LITE_VDEC | AXCL_LITE_VENC | AXCL_LITE_IVPS)


class AxcliteMSys(AxcliteSingleton):
    def __init__(self):
        self._modules = []
        self._link_table = {}

    def init(self, mask, **kwargs):
        max_vdec_grp = kwargs.get('max_vdec_grp', 32)
        max_venc_thrd = kwargs.get('max_venc_thrd', 2)

        ret = axcl.sys.init()
        if ret != axcl.AXCL_SUCC:
            return ret
        else:
            module = {'name': 'msys', 'deinit': axcl.sys.deinit}
            self._modules.append(module)
            # print(f"module {module['name']} is created")

        if (AXCL_LITE_VDEC == mask & AXCL_LITE_VDEC) or (AXCL_LITE_JDEC == mask & AXCL_LITE_JDEC):
            AxcliteVdec.max_grp_num = max_vdec_grp
            if (AXCL_LITE_VDEC == mask & AXCL_LITE_VDEC) and (AXCL_LITE_JDEC == mask & AXCL_LITE_JDEC):
                AxcliteVdec.decode_mode = axcl.AX_ENABLE_BOTH_VDEC_JDEC
            elif AXCL_LITE_VDEC == mask & AXCL_LITE_VDEC:
                AxcliteVdec.decode_mode = axcl.AX_ENABLE_ONLY_VDEC
            else:
                AxcliteVdec.decode_mode = axcl.AX_ENABLE_ONLY_JDEC

            ret = AxcliteVdec.init()
            if ret != axcl.AXCL_SUCC:
                self.deinit()
                return ret
            else:
                module = {'name': 'vdec', 'deinit': AxcliteVdec.deinit}
                self._modules.append(module)
                # print(f"module {module['name']} is created")

        if (AXCL_LITE_VENC == mask & AXCL_LITE_VENC) or (AXCL_LITE_JENC == mask & AXCL_LITE_JENC):
            AxcliteVenc.total_thread_num = max_venc_thrd
            if (AXCL_LITE_VENC == mask & AXCL_LITE_VENC) and (AXCL_LITE_JENC == mask & AXCL_LITE_JENC):
                AxcliteVenc.venc_type = axcl.AX_VENC_MULTI_ENCODER
            elif AXCL_LITE_VENC == mask & AXCL_LITE_VENC:
                AxcliteVenc.venc_type = axcl.AX_VENC_VIDEO_ENCODER
            else:
                AxcliteVenc.venc_type = axcl.AX_VENC_JPEG_ENCODER

            ret = AxcliteVenc.init()
            if ret != axcl.AXCL_SUCC:
                self.deinit()
                return ret
            else:
                module = {'name': 'venc', 'deinit': AxcliteVenc.deinit}
                self._modules.append(module)
                # print(f"module {module['name']} is created")

        if AXCL_LITE_IVPS == mask & AXCL_LITE_IVPS:
            ret = AxcliteIvps.init()
            if ret != axcl.AXCL_SUCC:
                self.deinit()
                return ret
            else:
                module = {'name': 'ivps', 'deinit': AxcliteIvps.deinit}
                self._modules.append(module)
                # print(f"module {module['name']} is created")

        return axcl.AXCL_SUCC

    def deinit(self):
        for module in reversed(self._modules):
            if module['deinit']:
                module['deinit']()
                # print(f"module {module['name']} is destroyed")

        self._modules.clear()

    def link(self, src: dict, dst: dict):
        ret = axcl.sys.link(src, dst)
        if ret != axcl.AXCL_SUCC:
            return ret

        key = tuple(src.values())
        val = tuple(dst.values())
        if key in self._link_table:
            self._link_table[key].append(val)
        else:
            self._link_table[key] = [val]

        # print(f"src: {src} link to dst: {dst} success")
        return axcl.AXCL_SUCC

    def unlink(self, src: dict, dst: dict):
        ret = axcl.sys.unlink(src, dst)
        if ret != axcl.AXCL_SUCC:
            return ret

        key = tuple(src.values())
        val = tuple(dst.values())
        if key in self._link_table and val in self._link_table[key]:
            self._link_table[key].remove(val)
            if len(self._link_table[key] == 0):
                self._link_table.pop(key)

        # print(f"src: {src} unlink with dst: {dst} success")
        return axcl.AXCL_SUCC

    def unlink_all(self):
        for key, val in self._link_table.items():
            src = {'mod_id': key[0], 'grp_id': key[1], 'chn_id': key[2]}
            for v in val:
                dst = {'mod_id': v[0], 'grp_id': v[1], 'chn_id': v[2]}
                axcl.sys.unlink(src, dst)
                # print(f"src: {src} unlink with dst: {dst} success")

        self._link_table.clear()
