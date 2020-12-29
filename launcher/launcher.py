# -*- coding: utf-8 -*-
"""Launcher
======

Launch HDFV shell with the specified filename.
"""


from hdfv.utils.config import config
from hdfv.utils.flag import flags as F
from hdfv.utils.parse import Parser


class Launcher(Parser):
    def __init__(self):
        self.config = config.user().get('launcher', dict())
        self.hello = self.config.get('hello')

    def start(self):
        if self.hello is not None:
            print(self.hello)
        F.exit = False
        while not F.exit:
            try:
                expression = input('==> ')
            except KeyboardInterrupt:
                print("\nGot Ctrl+C, exiting")
                F.exit = True  # Redundant Code
                break
            self.parse(expression)
        
    def parse(self, expression: str):
        if expression in ['exit']:
            F.exit = True
        else:
            print(f"echo {expression}")


# launcher = Launcher()


if __name__ == "__main__":
    launcher = Launcher()
    launcher.start()

