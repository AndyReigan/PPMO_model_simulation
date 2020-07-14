from Structure.TrajectoryStruct import initialNavData

class BoxMot:

    def create(self,curLoc):
        #текущие координаты
        initLoc=initialNavData()
        initLoc.x=curLoc[0]
        initLoc.y=curLoc[1]
        initLoc.z=curLoc[2]
        # генерация файла траектории по точкам
        pass


    def generatePlot(self):
        pass


    def autoPilotControlSignals(self):
        pass