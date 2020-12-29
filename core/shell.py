# -*- coding: utf-8 -*-
"""Shell
======

Interactive Shell for HDFV file
"""


import os

from hdfv.core.parse.ampersand import and_parser
from hdfv.core.parse.argument import argument_parser
from hdfv.core.parse.cmd import command_parser
from hdfv.utils.flag import flags as F
from hdfv.utils.parse import Parser


class Shell(Parser):
    def __init__(self):
        ...

    def parse(self, expression: str) -> None:
        expressions = and_parser.parse(expression)
        for expression in expressions:
            command = command_parser.parse(expression)
            args, kwargs = argument_parser.parse(expression)
            if command is None:
                print("Invalid Command: "
                     f"{command_parser.name(expression)}")
                continue
            response = command.execute(*args, **kwargs)

    def start(self, filename: str) -> None:
        if not os.path.exists(filename):
            print(f"Error: {filename} not found.")
            return
        # open file
        F.shell_exit = False
        while not F.shell_exit:
            # before `#` is group name
            expression = input("# ")
            self.parse(expression)


if __name__ == "__main__":
    shell = Shell()
    shell.start('sample/mlp.h5')

