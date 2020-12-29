# -*- coding: utf-8 -*-
"""And Parser
======

Parse position and keyword parameters in the expression
"""


import argparse
import re
from typing import Tuple

from hdfv.utils.parse import Parser


class ArgumentParser(Parser):
    """Argument Parser

    Parse position and keyword parameters in the expression
    
    This is an Singleton Class
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse(self, expression: str) -> Tuple[list, dict]:
        expression = expression.strip()
        expressions = expression.split(' ', 1)
        if len(expressions) == 1:
            return [], {}
        argument = expressions[-1]
        argv = re.findall(r'.*\"[^\"]+\"|.+', argument)

        args = []
        kwargs = {}

        for item in argv:
            if '=' in item:
                element = item.split('=', 1)
                k = element[0]
                v = re.sub(r'\"', '', element[1])
                kwargs[k] = v
            else:
                args.append(re.sub(r'\"', '', item))

        return args, kwargs


argument_parser = ArgumentParser()

