#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 五 11/ 8 17:16:14 2019
# File Name: engine/gui/sys_gui.py
# Description:
"""
import base.sys as sys
class SysGUI(sys.System):
    def __init__(self):
        sys.System.__init__(self)
    def onActive(self):
        sys.System.onActive(self)
    def onPause(self):
        sys.System.onPause(self)
    def onStop(self):
        sys.System.onStop(self)
    def onUpdate(self):
        sys.System.onUpdate(self)



