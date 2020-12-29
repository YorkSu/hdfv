# -*- coding: utf-8 -*-
"""Command Loader
======

Command Loader
"""


from typing import Optional, Callable

from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils.loader import loader
from hdfv.utils.pattern import Singleton


class CommandLoader(Singleton):
    """Command Loader
    
    This is an Singleton Class
    """
    def __init__(self):
        self._members = dict()
        self.init()

    @property
    def members(self):
        return self._members

    def contains(self, expression: str) -> bool:
        return expression in self._members

    def load(self,
            name: str,
            cls_name: str,
            default=None) -> Callable:
        def module() -> Optional[Command]:
            _module = loader.lazy_import(name)
            if _module is None:
                return None
            return getattr(_module, cls_name, default)()
        return module

    def init(self):
        conf = F.user_conf
        default_path = conf.get("shell").get("path").get("command", '')
        commands = conf.get("command", {})
        for c in commands.values():
            if c.get('location') == '/':
                c['location'] = default_path
            imp_name = '.'.join([
                conf.get('meta').get('name'),
                c.get('location'),
                c.get('entrance'),
            ])
            function = self.load(
                imp_name,
                c.get('classname')
            )
            self._members[c.get('command')] = function
            if c.get('alias'):
                for a in c.get('alias'):
                    self._members[a] = function

    def get(self, expression: str) -> Optional[Command]:
        output = self._members.get(expression, None)
        if callable(output):
            output = output()
        return output


command_loader = CommandLoader()

