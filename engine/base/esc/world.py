#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
管理所有的Entitys
"""
class World(object):
    def __init__(self):
        self._entitys = []
    def addEntity(self, entity):
        self._entitys.append(entity)
