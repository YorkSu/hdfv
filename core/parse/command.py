# -*- coding: utf-8 -*-
"""Command
======

Command Interface
"""


import abc


class Command(abc.ABC):
    """Command Interface"""
    @abc.abstractmethod
    def execute(self, *args, **kwargs): ...

