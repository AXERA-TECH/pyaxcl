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
import re
import sys
import platform
from setuptools import setup, find_packages

if platform.architecture()[0] != "64bit":
    print("This package requires a 64-bit Python interpreter.")
    sys.exit(1)


def get_sdk_version():
    v = "0.1.0"
    version_mak_path = os.path.abspath(os.path.join(os.getcwd(), "version.mak"))
    if os.path.exists(version_mak_path):
        with open(version_mak_path, "r") as f:
            content = f.read()

        m = re.search(r'^SDK_VERSION\s*=\s*([^\s_]+(?:\.[^\s_]+){2})', content, re.M)
        if m:
            v = m.group(1)
            if v.startswith("V"):
                v = v[1:]
    return v


setup(
    name="pyAXCL",
    version=get_sdk_version(),
    author="AXERA",
    description='AXCL python interface',
    url="https://github.com/AXERA-TECH",
    packages=find_packages(),
    install_requires=[
    ],
    python_requires='>=3.9'
)
