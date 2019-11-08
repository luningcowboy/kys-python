#!/usr/bin/env python
# -*- coding=utf8 -*-
class World:
    def __init__(self):
        self._entitys = []
    def addEntity(self, entity):
        self._entitys.append(entity)
