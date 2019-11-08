class System:
    def __init__(self):
        self._coms = []
        self._isActive = False
        self._isRunning = False
    def active(self):
        self._isActive = True
        self._isRunning = True
        self.onActive()
    def pause(self):
        self._isRunning = False 
        self.onPause()
    def stop(self):
        self._isRunning = False
        self._isActive = False
        self.onStop()
    def addCom(self, com):
        self._coms.append(com)
    def update(self):
        self.onUpdate()
        for com in self._coms:
            com.update()
    def onActive(self):
        pass
    def onPause(self):
        pass
    def onStop(self):
        pass
    def onUpdate(self):
        pass

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

