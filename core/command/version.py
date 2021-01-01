# -*- coding: utf-8 -*-
"""Version Command
======

Version Command
"""


from hdfv.core.parse.command import Command
from hdfv.utils.flag import flags as F
from hdfv.utils.response import Response


class VersionCommand(Command):
    """Version Command

    Print the HDFV Version
    """
    def execute(self, *args, **kwargs) -> Response:
        conf = F.user_conf
        name = conf['meta']['name'].upper()
        version = conf['meta']['version']
        codename = conf['meta']['project']['codename']
        project_date = conf['meta']['project']['date']
        commits = conf['meta']['commits']
        latest = conf['meta']['latest']
        response = Response()

        count = '1'
        for arg in args:
            if arg in ['more', '+']:
                count = '2'

        count = str(kwargs.get('count', count))

        if count == '1':
            response.message = f"{name} {version}-{commits}"
        elif count.isdigit() and int(count) > 1:
            response.message = f"{name} {version}-{commits}"
            response.message += f" [{codename} {project_date}]"
            response.message += f" [Latest {latest}]"
        else:
            response.code = 417
            response.message = f"version: count {count} invalid"
        
        print(response.message)

        return response

