# -*- coding: utf-8 -*-
"""Cd HDFV Command
======

Cd HDFV Command
"""


import h5py

from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils import path
from hdfv.utils.response import Response


class CdHdfv(Command):
    """Cd HDFV Command

    Open the catalog. You can use absolute and relative paths. 
    Back to the next level of use: `..`
    Back to the root to use `/`
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        
        if not args:  # empty argument
            return response

        new_pwd = path.change(F.hdfv['pwd'], args[0])
        code = path.get_type(F.hdfv['h5'], new_pwd)
        if code in [100, 101]:
            F.hdfv['pwd'] = new_pwd
        elif code in [102, 400]:
            response.message = f"cd: {args[0]}: Not directory"
        elif code == 404:
            response.message = f"cd: {args[0]}: No such directory"

        if response.message:
            print(response.message)
        return response

