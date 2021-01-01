# -*- coding: utf-8 -*-
"""And Parser
======

Parse position and keyword parameters in the expression
"""


import re
from typing import Tuple

from hdfv.utils.parse import Parser


class ArgumentParser(Parser):
    """Argument Parser

    Parse position and keyword parameters in the expression
    
    This is an Singleton Class
    """
    def parse(self, expression: str) -> Tuple[list, dict]:
        expression = expression.strip()
        expressions = expression.split(' ', 1)
        if len(expressions) == 1:
            return [], {}
        
        argument = expressions[-1]
        strings = re.findall(r'\S*=\"[^\"]+\"|\"[^\"]+\"', argument)  # match `key="xxx"` or `"xxx"`
        for string in strings:
            argument = argument.replace(string, '')
        argv = argument.split(' ') + strings

        args = []
        args_key = []
        kwargs = {}

        for item in argv:
            if not item:
                continue
            if '=' in item:
                element = item.split('=', 1)
                if not all(element):
                    continue
                k = element[0]
                v = re.sub(r'\"', '', element[1])
                kwargs[k] = v
            elif item[0] == '-':
                args_key.append(re.sub(r'\"', '', item))
            else:
                args.append(re.sub(r'\"', '', item))

        return args + args_key, kwargs


argument_parser = ArgumentParser()


if __name__ == '__main__':
    def test(i):
        print(argument_parser.parse(i))

    test('rm -r "123" foo=bar a="b c" d= =e ="f"')
    test('open 123')
    test('rm -r 123 456')
    test('rm 123 -r')
    test('rm "123" "456" "789" -r ccc')
    test('rm ssh=123 "retry=1"')
    test('rm foo="123 456"')
    test('rm ="789" foo=')

