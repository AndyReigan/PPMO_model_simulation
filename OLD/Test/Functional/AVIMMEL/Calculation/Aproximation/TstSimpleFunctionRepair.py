import unittest

import matplotlib.pyplot as plt
import numpy as np

from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Dot
from Code.AVIMMEL.Calculation.Approximation.SimpleFunctionRepair import SimpleFunctionRepair as SFR


class TstSimpleFunctionRepair(unittest.TestCase):
    def test001(self):
        x_0 = -2.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = dots[0].y
        self.assertEqual(res, corRes)

    def test002(self):
        x_0 = 2.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = dots[-1].y
        self.assertEqual(res, corRes)

    def test003(self):
        x_0 = -2
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = dots[0].y
        self.assertEqual(res, corRes)

    def test004(self):
        x_0 = 2
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = dots[-1].y
        self.assertEqual(res, corRes)

    def test005(self):
        x_0 = -1.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = -0.5
        self.assertEqual(res, corRes)

    def test006(self):
        x_0 = 1.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = -0.5
        self.assertEqual(res, corRes)

    def test007(self):
        x_0 = -0.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = 0
        self.assertEqual(res, corRes)

    def test008(self):
        x_0 = 0.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = SFR.extra_0_inter_1(dots, x_0)
        corRes = 0
        self.assertEqual(res, corRes)
