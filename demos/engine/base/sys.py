class System:
    def __init__(self):
        self._coms = []
    def addCom(self, com):
        self._coms.append(com)
    def update(self):
        for com in self._coms:
            com.update()

systems = {}

def addSystem(tag, system):
    if tag not in systems:
        systems[tag] = system
def removeSystemByTag(tag):
    pass
def removeSystem(system):
    pass

def addCom2Sys(sysTag, com):
    if sysTag in systems:
        systems[sysTag].addCom(com)

