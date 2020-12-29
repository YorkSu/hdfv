# -*- coding: utf-8 -*-
"""Exit Command
======

EXIT Command
"""


from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils.response import Response


class ExitCommand(Command):
    """Exit Command

    Exit the HDFV Shell
    """
    def execute(self, *args, **kwargs) -> Response:
        F.shell_exit = True
        return Response()

