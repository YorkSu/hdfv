# -*- coding: utf-8 -*-
"""Lazy Loader
======

Lazy Loader Class
"""


import importlib
from types import ModuleType
from typing import Optional

from hdfv.utils.pattern import Singleton


class LazyLoader(Singleton):
    """Lazy Loader

    This is an Singleton Class
    """
    def __init__(self):
        self.__modules = {}

    def __import(self, name: str) -> dict:
        """Thread-safe Import method"""
        if name not in self.__modules:
            with self._lock:
                if name not in self.__modules:
                    module = None
                    e = ''
                    try:
                        module = importlib.import_module(name)
                    except ImportError as _e:
                        e = _e
                    self.__modules[name] = {
                        'module': module,
                        'e': e
                    }
        return self.__modules.get(name)

    def lazy_import(self, name: str) -> Optional[ModuleType]:
        """Lazy Import Method"""
        _module = self.__import(name)
        if _module['e']:
            print(f"[Error] {_module['e']}")
        return _module['module']


loader = LazyLoader()

