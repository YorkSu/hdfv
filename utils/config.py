# -*- coding: utf-8 -*-
"""Config
======

The Manager for the configuration
"""


import os
import json

from hdfv import ROOT_PATH
from hdfv.utils.pattern import Singleton


class Config(Singleton):
    """Config
    
    This is a Singleton Class
    """
    def __init__(self):
        self._configs = dict()

    def user(self) -> dict:
        return self.load('user')

    def load(self, conf_name: str) -> dict:
        conf_name = conf_name.rstrip('.conf')
        if conf_name not in self._configs:
            # print(f"Loading conf: {conf_name}")  # debuging
            conf_path = os.path.join(
                ROOT_PATH,
                conf_name + '.conf'
            )
            try:
                conf = json.load(open(conf_path))
            except Exception as e:
                print(e)
                conf = dict()
            self._configs[conf_name] = conf
        return self._configs.get(conf_name, dict())


config = Config()


if __name__ == "__main__":
    config = Config()
    print(config.user())
    print(config.load('user'))
    print(config.load('user.conf'))
    print(config.load('notexist'))
    print(config.load('notexist.conf'))

