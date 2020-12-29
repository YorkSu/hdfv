# -*- coding: utf-8 -*-
"""Parser
======

Parser Interface
"""


import abc

from hdfv.utils.pattern import AbstractSingleton


class Parser(AbstractSingleton):
    """Parser Interface

    This is an Abstract Singleton Class
    """
    @abc.abstractmethod
    def parse(self, expression: str): ...



