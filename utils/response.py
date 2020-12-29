# -*- coding: utf-8 -*-
"""Response
======

Response Class
"""


class Response:
    def __init__(self):
        self.code = 200
        self.message = ''

    def get(self, key):
        """Get value from specified key"""
        return self.__getattribute__(key)

    def set(self, key, value):
        """Set value from specified key"""
        self.__setattr__(key, value)

    def keys(self):
        """Get the list of argument keys"""
        return list(self.__dict__.keys())

    def json(self):
        return self.__dict__

