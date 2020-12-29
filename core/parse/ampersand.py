# -*- coding: utf-8 -*-
"""And Parser
======

Parse the `&` in the expression
"""


from typing import Sequence

from hdfv.utils.parse import Parser


class AndParser(Parser):
    """And Parser

    Parse the `&` in the expression

    This is an Singleton Class
    """
    def parse(self, expression: str) -> Sequence[str]:
        expression = expression.strip()
        expressions = expression.split('&')
        return expressions


and_parser = AndParser()

