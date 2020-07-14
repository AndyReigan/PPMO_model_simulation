import unittest

from Code.AVIMMEL.Calculation.Filters.MoveAvg import MoveAvg


class TstMoveAvg(unittest.TestCase):
    def test001(self):
        MAvg = MoveAvg(3)
        dots = [3]
        res = MAvg.filtrate(dots[0])
        corRes = 3
        self.assertEquals(res, corRes)

    def test002(self):
        MAvg = MoveAvg(3)
        dots = [3, 5]
        res = None
        for dot in dots:
            res = MAvg.filtrate(dot)
        corRes = 4
        self.assertEquals(res, corRes)

    def test003(self):
        MAvg = MoveAvg(3)
        dots = [1, 2, 3, 4, 5]
        res = None
        for dot in dots:
            res = MAvg.filtrate(dot)
        corRes = 4
        self.assertEquals(res, corRes)

    def test004(self):
        MAvg = MoveAvg(3)
        dots = [1, 2, 3, 4, 5, 9]
        res = None
        for dot in dots:
            res = MAvg.filtrate(dot)
        corRes = 6
        self.assertEquals(res, corRes)

