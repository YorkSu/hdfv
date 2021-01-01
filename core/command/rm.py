# -*- coding: utf-8 -*-
"""Rm HDFV Command
======

Rm HDFV Command
"""


from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils import path
from hdfv.utils.response import Response


class RmHdfv(Command):
    """Rm HDFV Command

    Delete Dataset, or delete Group (plus -r)
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()

        paths = []
        option = ''
        for a in args:
            if a[0] == '-':
                option += a[1:]
            else:
                paths.append(a)

        if not paths and not option:  # empty argument
            response.message = "rm: missing operand"
        elif not paths:  # no path argument
            response.message = f"rm: invalid option -- '{args[0][1:]}'"
        else:
            for p in paths:
                new_path = path.change(F.hdfv['pwd'], p)
                code = path.get_type(F.hdfv['h5'], new_path)
                
                if code == 100:
                    response.message = f"rm: {p}:Permission denied"
                elif code == 101:
                    if 'r' in option:
                        del F.hdfv['h5'][new_path]
                    else:
                        response.message = f"rm: cannot remove ‘{p}’: Is a directory"
                elif code == 102:
                    del F.hdfv['h5'][new_path]
                elif code == 400:
                    response.message = f"rm: unknown error: {p}"
                elif code == 404:
                    response.message = f"rm: cannot remove ‘{p}’: No such file or directory"

        if response.message:
            print(response.message)
        return response

