from matplotlib.pyplot import *
from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Data
from Code.Devices.MFD.MFD382.Calculation.SpeedLimits import SpeedLimits


class AnlzSpeedLimits:
    def __init__(self, m_hel):
        self.SL = SpeedLimits()
        self.m_hel = m_hel

    def buildplot(self, hight_max, temprMove):
        h_abs = Data()
        t_air = Data()
        v = []
        h = []
        for hight in range(hight_max, 0, -50):
            h_abs.value = hight
            t_air.value = self.SL.calcISATemp(h_abs) + temprMove
            v.insert(0, self.SL.calcMinSpeed(h_abs, self.m_hel))
            v.append(self.SL.calcMaxSpeed(t_air, h_abs, self.m_hel))
            h.insert(0, hight)
            h.append(hight)
        plot(v, h)
        show()
