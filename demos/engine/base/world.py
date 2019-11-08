#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 五 11/ 8 17:06:46 2019
# File Name: engine/base/world.py
# Description:
"""
class World:
    def __init__(self):
        self._entitys = []
    def addEntity(self, entity):
        self._entitys.append(entity)
