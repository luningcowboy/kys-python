#!/usr/bin/env python
# -*- coding=utf8 -*-
class Entity(object):
    def __init__(self):
        self._coms = []
    def addCom(self, com):
        self._coms.append(com)
    def active(self):
        pass
    def destroy(self):
        pass
