import unittest


from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Dot
from Code.AVIMMEL.Calculation.Approximation.Extrapolation import Extrapolation as Exterp


class TstExtrapolation(unittest.TestCase):
    def test001(self):
        x_0 = -2.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = Exterp.zero(dots, x_0)
        corRes = dots[0].y
        self.assertEqual(res, corRes)

    def test002(self):
        x_0 = 2.5
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = Exterp.zero(dots, x_0)
        corRes = dots[-1].y
        self.assertEqual(res, corRes)

    def test003(self):
        x_0 = -2
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = Exterp.zero(dots, x_0)
        corRes = dots[0].y
        self.assertEqual(res, corRes)

    def test004(self):
        x_0 = 2
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = Exterp.zero(dots, x_0)
        corRes = dots[-1].y
        self.assertEqual(res, corRes)

    def test005(self):
        x_0 = 0
        dots = [Dot(-2, 0), Dot(-1, -1), Dot(0, 1), Dot(1, -1), Dot(2, 0)]
        res = Exterp.zero(dots, x_0)
        corRes = None
        self.assertEqual(res, corRes)

