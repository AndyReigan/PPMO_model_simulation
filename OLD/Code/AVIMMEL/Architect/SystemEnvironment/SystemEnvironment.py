import os

class SystemEnvironment:
    def __init__(self, projectName="HelicopterMathModels"):
        self.projectRoot = None
        self.projectName = projectName

    def getRoot(self):
        if self.projectRoot is None:
            fullRoot = os.getcwd()
            self.projectRoot = fullRoot.replace('/', '\\')[0:len(self.projectName) + fullRoot.find(self.projectName)]
            return self.projectRoot
        else:
            return self.projectRoot
