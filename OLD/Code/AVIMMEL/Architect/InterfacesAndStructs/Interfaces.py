from abc import ABCMeta, abstractmethod

class Device:
    def __init__(self, name=None):
        self.name = name
        self.deviceData = {"Fail": {}, "State": {}, "Data": {}}
        self.deviceOutput = {"Fail": {}, "State": {}, "Data": {}}

    @abstractmethod
    def imitErr(self):
        pass

    def add(self, key, data):
        marker = type(data).__name__
        self.deviceData[marker][key] = data

    def get(self, marker, key):
        if marker in self.deviceData:
            if key in self.deviceData[marker]:
                return self.deviceData[marker][key]
            else:
                print("Incorrect key (" + key + ")")
        else:
            print("Incorrect marker (" + marker + ")")

class Task(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def _count(self):
        pass
