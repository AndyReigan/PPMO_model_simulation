from Code.AVIMMEL.Architect.InterfacesAndStructs.Interfaces import Device
from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Data, Fail, State

from Code.AVIMMEL.Architect.SystemEnvironment.SystemEnvironment import SystemEnvironment


class Repository:
    def __init__(self, repoDict=None):
        if repoDict is None:
            repoDict = {}
        self.repoDict = repoDict

    def addDevice(self, name):
        self.repoDict[name] = Device(name)

    def add(self, device, key, data):
        self.repoDict[device].add(key, data)

    def get(self, device, marker, key):
        if device in self.repoDict:
            return self.repoDict[device].get(marker, key)


class RepoBuilder:
    def __init__(self, devName, deviceType):
        self.devName = devName
        self.devType = deviceType

        self.repo = Repository()
        self.projectDir = SystemEnvironment().getRoot()



    def build(self):
        self._loadVars()
        return self.repo

    def _loadVars(self):
        fullPath = self.projectDir + "Code/Devices" + self.devType + "/" + self.devName + "Settings/VarSettings.txt"
        file = open(fullPath, 'r')
        for line in file:
            lineList = line.strip().split()
            lineListSize = len(lineList)
            if lineListSize == 1:
                self.repo.addDevice(lineList[0])
                self.devName = lineList[0]
            elif lineListSize > 1:
                if lineList[1] == "vr":
                    self.repo.add(self.devName, lineList[0], Data())
                elif lineList[1] == "st":
                    self.repo.add(self.devName, lineList[0], State())
                elif lineList[1] == "fl":
                    self.repo.add(self.devName, lineList[0], Fail())