# -*- coding: utf-8 -*-
"""Command Parser
======

Parse Command in the expression
"""


from typing import Optional

from hdfv.core.parse.command import Command
from hdfv.core.parse.loader import command_loader
from hdfv.utils.parse import Parser


class CommandParser(Parser):
    """Command Parser
    
    Parse the Command in the expression

    This is an Singleton Class
    """
    def parse(self, expression: str) -> Optional[Command]:
        expression = expression.strip()
        command = expression.split(' ', 1)[0]
        command = command.upper()
        return command_loader.get(command)

    def name(self, expression: str) -> str:
        expression = expression.strip()
        command = expression.split(' ', 1)[0]
        return command.upper()


command_parser = CommandParser()

