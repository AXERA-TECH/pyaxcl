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
from abc import ABC, abstractmethod


class AxcliteObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass


class AxcliteSubject(object):
    def __init__(self):
        self._observers = []
        self._lock = threading.Lock()
        self._is_active = True

    def register(self, observer: AxcliteObserver):
        with self._lock:
            if observer not in self._observers:
                self._observers.append(observer)

    def unregister(self, observer: AxcliteObserver):
        with self._lock:
            if observer in self._observers:
                self._observers.remove(observer)

    def notify(self, data):
        with self._lock:
            if self._is_active:
                for observer in self._observers:
                    observer.update(data)

    def stop(self):
        with self._lock:
            self._is_active = False
            print("notifications is stopped")

    def resume(self):
        with self._lock:
            self._is_active = True
            print("notifications is resumed")
