from base import sys
class Component:
    def __init__(self):
        self._tag = ""
        self._sysTag = ""
    def add2Sys(self):
        sys.addSystem(self._sysTag, self)
    def update(self):
        pass
