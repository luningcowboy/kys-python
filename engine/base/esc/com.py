#!/usr/bin/env python
# -*- coding=utf8 -*-
from base import sys
class Component(object):
    def __init__(self):
        self._tag = ""
        self._sysTag = ""
    def add2Sys(self):
        sys.addSystem(self._sysTag, self)
    def active(self):
        pass
    def update(self):
        pass
