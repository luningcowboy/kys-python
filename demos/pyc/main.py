#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 一 11/11 19:37:09 2019
# File Name: main.py
# Description:
"""
import ctypes
ll = ctypes.cdll.LoadLibrary
lib = ll("./libpycall.so")
lib.foo(1, 3)
print("finish")
