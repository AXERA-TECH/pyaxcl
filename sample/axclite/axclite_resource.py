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

import threading
import atexit
from abc import ABC, abstractmethod


REGISTER = 0
UNREGISTER = 1


class AxcliteResource(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def destroy(self):
        pass


class AxcliteResourceManager(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.resources = []
        self._lock = threading.Lock()
        atexit.register(self.cleanup)

    def cleanup(self):
        self.destroy()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def register(self, resource: AxcliteResource):
        with self._lock:
            if any(item["resource"] == resource for item in self.resources):
                return

            item = {"resource": resource, "status": REGISTER}
            self.resources.append(item)

    def unregister(self, resource: AxcliteResource):
        """
        If registered resource release by itself and no longer managed by ResourceManager,
        should call unregister to remove from ResourceManager
        """
        with self._lock:
            for item in self.resources:
                if resource == item["resource"]:
                    item["status"] = UNREGISTER

    def destroy(self):
        while self.resources:
            item = self.resources.pop()  # FILO
            if item["status"] == REGISTER:
                item["resource"].destroy()
                item["status"] = UNREGISTER


axclite_resource_manager = AxcliteResourceManager()
