import unittest

from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Data
from Code.Devices.MFD.MFD382.Calculation.SpeedLimits import SpeedLimits


class TstSpeedLimits(unittest.TestCase):
    def test_v_min_lower(self):
        inpHData = [4000, 5000, 5400, 6000, 6150, 6300, 6500]
        corResData = [60, 60, 82, 115, 120, 125, 125]
        m_hel = Data(value=13200)
        for i in range(len(inpHData)):
            h_abs = Data(value=inpHData[i])
            SL = SpeedLimits()
            res = SL.calc_V_min(h_abs, m_hel)
            corRes = corResData[i]
            self.assertEqual(res, corRes)

    def test_v_min_higher(self):
        inpHData = [3000, 4000, 4500, 5000, 5200, 5600, 6000]
        corResData = [60, 60, 80, 100, 110, 130, 130]
        m_hel = Data(value=15200)
        for i in range(len(inpHData)):
            h_abs = Data(value=inpHData[i])
            SL = SpeedLimits()
            res = SL.calc_V_min(h_abs, m_hel)
            corRes = corResData[i]
            self.assertEqual(res, corRes)

    def test_v_max_lower(self):
        inpHData =   [500, 1000, 1500, 2000, 2500, 3000, 3400, 4000, 4500, 5000, 5200, 6000, 6120, 6300, 65000]
        corResData = [300, 300,  290,  280,  265,  250,  240,  225,  205,  185,  182,  170,  160,  145,  145]
        SL = SpeedLimits()
        m_hel = Data(value=13200)
        for i in range(len(inpHData)):
            h_abs = Data(value=inpHData[i])
            t_air = Data(value=SL.calc_t_mca(h_abs))
            res = SL.calc_V_max(t_air, h_abs, m_hel)
            corRes = corResData[i]
            self.assertEqual(res, corRes)

    def test_v_max_higher(self):
        inpHData =   [500, 1000, 1500, 2000, 2500, 3000, 3400, 4000, 4400, 5000, 5200, 5600, 6000]
        corResData = [290, 290,  270,  250,  235,  220,  206,  185,  183,  180,  170,  150,  150 ]
        SL = SpeedLimits()
        m_hel = Data(value=15200)
        for i in range(len(inpHData)):
            h_abs = Data(value=inpHData[i])
            t_air = Data(value=SL.calc_t_mca(h_abs))
            res = SL.calc_V_max(t_air, h_abs, m_hel)
            corRes = corResData[i]
            self.assertEqual(res, corRes)

    def test_v_max_ar(self):
        inpHData =   [2500, 3000, 3500]
        corResData = [200,  200,  130]
        for i in range(len(inpHData)):
            h_abs = Data(value=inpHData[i])
            SL = SpeedLimits()
            res = SL.calc_V_max_AR(h_abs)
            corRes = corResData[i]
            self.assertEqual(res, corRes)
