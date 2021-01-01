# -*- coding: utf-8 -*-
"""Launcher
======

Launch HDFV shell with the specified filename.
"""


import os

import h5py

from hdfv.core.parse.argument import argument_parser
from hdfv.core.shell import shell
from hdfv.utils.flag import flags as F
from hdfv.utils.parse import Parser


class Launcher(Parser):
    def __init__(self):
        self.hello = F.user_conf.get('launcher', dict()).get('hello')

    def start(self) -> None:
        if self.hello is not None:
            print(self.hello)
        F.launcher_exit = False
        while not F.launcher_exit:
            try:
                expression = input('==> ')
            except KeyboardInterrupt:
                print("\nGot Ctrl+C, exiting")
                F.launcher_exit = True  # Redundant Code
                break
            self.parse(expression)
        
    def parse(self, expression: str) -> None:
        expression = expression.strip()
        if not expression:
            return

        command = expression.split(' ', 1)[0].upper()
        args, kwargs = argument_parser.parse(expression)
        if command in ['EXIT']:
            F.launcher_exit = True
        elif command in ['OPEN', 'O']:
            expressions = expression.split(' ')
            if len(expressions) == 1:
                print(f"open: file name must be given")
            else:
                filename = expressions[1]
                # process arguments
                if not os.path.exists(filename):
                    print(f"open: {filename} not found.")
                else:
                    try:
                        F.hdfv['h5'] = h5py.File(filename, mode='a')
                    except Exception:
                        print(f"open: {filename} failed")
                        return
                    shell.start()
                    F.hdfv['h5'].close()  # close hdf5 file
        elif command in ['ECHO']:
            print(f"echo {expression}")
        else:
            print(f"echo {expression}")


# launcher = Launcher()


if __name__ == "__main__":
    launcher = Launcher()
    launcher.start()

