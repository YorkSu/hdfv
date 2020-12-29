# -*- coding: utf-8 -*-
"""Launcher
======

Launch HDFV shell with the specified filename.
"""


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
        if expression in ['exit']:
            F.launcher_exit = True
        else:
            print(f"echo {expression}")


# launcher = Launcher()


if __name__ == "__main__":
    launcher = Launcher()
    launcher.start()

