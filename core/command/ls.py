# -*- coding: utf-8 -*-
"""Ls HDFV Command
======

Ls HDFV Command
"""


import h5py

from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils.response import Response


class LsHdfv(Command):
    """Ls HDFV Command

    View datasets and groups in the current directory, including .meta
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        pwd = F.hdfv['h5'][F.hdfv['pwd']]
        outputs = []
        for k, v in pwd.items():
            if isinstance(v, h5py.Group):
                v = 'g'
            else:
                v = 'd'
            outputs.append(f"{k}:{v}")

        response.message = ', '.join(outputs)
        if response.message:
            print(response.message)
        return response

