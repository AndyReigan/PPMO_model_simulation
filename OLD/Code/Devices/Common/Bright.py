from scipy.optimize import fsolve
import numpy as np

class Bright:
    def __init__(self, bright, angle, dotsInDayTime, switchBright):
        self.__calcCoefs(bright, angle, dotsInDayTime, switchBright)

    def __calcCoefs(self, bright, angle, dotsInDayTime, switchBright):
        self.a = (bright.max - bright.min) / (angle.max - angle.min)
        self.b = bright.max - angle.max * self.a
        self.k = fsolve(lambda k: np.exp((self.a * angle.min + self.b) * k) -
                                  np.exp((self.a * angle.max + self.b) * k) -
                                  (bright.min - bright.max), 0.000001)[0]
        self.c = bright.min - np.exp((self.a * angle.min + self.b) * self.k)
        self.switchAngle = round(((np.log(switchBright - self.c) / self.k) - self.b) / self.a, 2)
        self.angles = []
        nightStep = (self.switchAngle - angle.min) / (dotsInDayTime["Night"] - 1)
        for i in range(dotsInDayTime["Night"]):
            self.angles.append(angle.min + i * nightStep)
        dayStep = (angle.max - self.switchAngle) / (dotsInDayTime["Day"] - 1)
        for i in range(dotsInDayTime["Day"]):
            self.angles.append(self.switchAngle + i * dayStep)

    def calcBrightDot(self, angle):
        return np.exp((self.a * angle + self.b) * self.k) + self.c

    def calcBrightTable(self):
        table = []
        for angle in self.angles:
            table.append((angle, self.calcBrightDot(angle)))
        return table

    def showTable(self):
        table = self.calcBrightTable()
        print("a: %f" % self.a)
        print("b: %f" % self.b)
        print("c: %f" % self.c)
        print("k: %f" % self.k)
        print("Switch Angle: {:.1f}".format(self.switchAngle))
        print("Angle: Bright:")
        for elem in table:
            print("%s %s" % ("{:.1f}".format(elem[0]), "{:.1f}".format(elem[1])))
