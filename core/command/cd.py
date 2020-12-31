# -*- coding: utf-8 -*-
"""Cd HDFV Command
======

Cd HDFV Command
"""


import h5py

from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils.response import Response


class CdHdfv(Command):
    """Cd HDFV Command

    Open the catalog. You can use absolute and relative paths. 
    Back to the next level of use: `..`
    Back to the root to use `/`
    """
    def next(self, pwd: str) -> str:
        if pwd != '/':  # Ignore root
            pwd = '/' + '/'.join(pwd.split('/')[1:-1])
        return pwd

    def add(self, pwd: str, path: str) -> str:
        if pwd == '/':  # root directory
            pwd += path
        else:
            pwd += '/' + path
        return pwd

    def single(self, pwd: str, path: str) -> str:
        if path == '.':  # this directary
            pass
        elif path == '..':  # next directory
            pwd = self.next(pwd)
        else:
            pwd = self.add(pwd, path)
        return pwd

    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        
        # empty argument
        if not args:
            return response

        tmp_pwd = F.hdfv['pwd']
        d = args[0]
        # root directory
        if d[0] == '/':  # absolute path
            tmp_pwd = d
        elif '/' in d:  # including / in relative path
            for p in d.split('/'):
                tmp_pwd = self.single(tmp_pwd, p)
        else:  # relative path
            tmp_pwd = self.single(tmp_pwd, d)

        try:
            pwd = F.hdfv['h5'][tmp_pwd]
            # Ensure pwd is Group
            if isinstance(pwd, h5py.Group):
                F.hdfv['pwd'] = tmp_pwd
            else:
                response.message = f"cd: {d}: Not directory"
        except Exception:
            response.message = f"cd: {d}: No such directory"

        if response.message:
            print(response.message)
        return response

