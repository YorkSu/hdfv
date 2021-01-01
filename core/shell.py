# -*- coding: utf-8 -*-
"""Shell
======

Interactive Shell for HDFV file
"""


from hdfv.core.parse.ampersand import and_parser
from hdfv.core.parse.argument import argument_parser
from hdfv.core.parse.cmd import command_parser
from hdfv.utils.flag import flags as F
from hdfv.utils.parse import Parser


class Shell(Parser):
    def __init__(self):
        F.hdfv = dict()
        F.hdfv['h5'] = None
        F.hdfv['pwd'] = ''

    def parse(self, expression: str) -> None:
        expression = expression.strip()
        if not expression:
            return
        expressions = and_parser.parse(expression)
        for exp in expressions:
            command = command_parser.parse(exp)
            args, kwargs = argument_parser.parse(exp)
            if command is None:
                print("Invalid Command: "
                     f"{command_parser.name(exp)}")
                continue
            response = command.execute(*args, **kwargs)

    def start(self) -> None:
        F.hdfv['pwd'] = '/'
        F.shell_exit = False
        while not F.shell_exit:
            expression = input(f"{F.hdfv['pwd']}# ")
            self.parse(expression)


shell = Shell()


if __name__ == "__main__":
    import h5py
    F.hdfv['h5'] = h5py.File('sample/mlp.h5', mode='a')
    shell.start()

