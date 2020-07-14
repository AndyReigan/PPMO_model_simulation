from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Dot
from Code.AVIMMEL.Calculation.Approximation.SimpleFunctionRepair import SimpleFunctionRepair as SFR


class SpeedLimits:
    def __init__(self):
        self.dotsLightV_min = [Dot(5000, 60), Dot(6000, 115), Dot(6300, 125)]
        self.dotsLightV_max = [Dot(1000, 300), Dot(2000, 280), Dot(3000, 250), Dot(4000, 225),
                               Dot(5000, 185), Dot(6000, 170), Dot(6300, 145)]
        self.dotsHeavyV_min = [Dot(4000, 60), Dot(5000, 100), Dot(5600, 130)]
        self.dotsHeavyV_max = [Dot(1000, 290), Dot(2000, 250), Dot(3000, 220), Dot(4000, 185),
                               Dot(5000, 180), Dot(5600, 150)]
        self.dotsT_mca = [Dot(0, 288.150), Dot(250, 286.525), Dot(500, 284.900), Dot(750, 283.276), Dot(1000, 281.651),
                          Dot(1500, 278.402), Dot(2000, 275.154), Dot(2500, 271.906), Dot(3000, 268.659),
                          Dot(3500, 265.413), Dot(4000, 262.166), Dot(4500, 258.921), Dot(5000, 255.676),
                          Dot(5500, 252.431), Dot(6000, 249.187), Dot(6500, 245.943), Dot(7000, 242.700),
                          Dot(7500, 239.457), Dot(8000, 236.215), Dot(8500, 232.974), Dot(9000, 229.733),
                          Dot(9500, 226.492), Dot(10000, 223.252), Dot(10500, 220.013), Dot(11000, 216.774),
                          Dot(11500, 216.650)]
        self.mass = 14200

    def calcMinSpeed(self, h_abs, m_hel):
        if h_abs.state != "Work" and m_hel.state != "Work":
            res = 60
        else:
            if m_hel.value <= self.mass:
                res = SFR.extra_0_inter_1(self.dotsLightV_min, h_abs.value)
            else:
                res = SFR.extra_0_inter_1(self.dotsHeavyV_min, h_abs.value)
        return res

    def calcMaxSpeed(self, t_air, h_abs, m_hel):
        if t_air.state != "Work" and h_abs.state != "Work" and m_hel.state != "Work":
            return None
        else:
            t_mca = self.calcISATemp(h_abs)
            if m_hel.value <= self.mass:
                v_max = SFR.extra_0_inter_1(self.dotsLightV_max, h_abs.value)
            else:
                v_max = SFR.extra_0_inter_1(self.dotsHeavyV_max, h_abs.value)
            if t_air.value != t_mca:
                return v_max + int(abs(t_air.value - t_mca))
            else:
                return v_max

    def calcISATemp(self, h_abs):
        return SFR.extra_0_inter_1(self.dotsT_mca, h_abs.value) - 273.15

    def calcMaxSpeedAR(self, h_abs):
        if h_abs.state != "Work":
            res = None
        elif h_abs.value <= 3000:
            res = 200
        else:
            res = 130
        return res

