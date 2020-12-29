# -*- coding: utf-8 -*-
"""Flag
======

Global Argument Manager
"""


from typing import Any, Optional

from hdfv.utils.config import config
from hdfv.utils.pattern import Singleton


class Flags(Singleton):
    """Global Argument Manager
    
    This is a Singleton Class
    """
    def __init__(self):
        self.init()

    def __setattr__(self, key: str, value: Any) -> None:
        super(Flags, self).__setattr__(key, value)

    def __getattribute__(self, key: str, default=None) -> Optional[Any]:
        try:
            output = super(Flags, self).__getattribute__(key)
        except AttributeError:
            output = default
        return output

    def get(self, key: str, default=None) -> Optional[Any]:
        """Get value from specified key
        
        if not found, return default
        """
        return self.__getattribute__(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set the value of specified key"""
        self.__setattr__(key, value)

    def init(self) -> None:
        # Initial Definition
        self.set("user_conf", config.user())


flags = Flags()

