# -*- coding: utf-8 -*-
"""Pwd HDFV Command
======

Pwd HDFV Command
"""


from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils.response import Response


class PwdHdfv(Command):
    """Pwd HDFV Command

    View the current directory
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        response.message = F.hdfv['pwd']
        print(response.message)
        return response

