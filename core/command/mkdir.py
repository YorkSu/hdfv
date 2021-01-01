# -*- coding: utf-8 -*-
"""Mkdir HDFV Command
======

Mkdir HDFV Command
"""


from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils import path
from hdfv.utils.response import Response


class MkdirHdfv(Command):
    """Mkdir HDFV Command

    Create a Group
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()

        if not args:  # empty argument
            response.message = "mkdir: missing operand"
        else:
            new_group = path.change(F.hdfv['pwd'], args[0])
            code = path.get_type(F.hdfv['h5'], new_group)
            if code in [100, 101, 102]:
                response.message = f"mkdir: cannot create directory ‘{args[0]}’: File exists"
            elif code == 400:
                response.message = f"mkdir: unknown error: {args[0]}"
            elif code == 404:
                F.hdfv['h5'].create_group(new_group)

        if response.message:
            print(response.message)
        return response

