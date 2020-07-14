
from Code.AVIMMEL.Calculation.Approximation.Interpolation import Interpolation
from Code.AVIMMEL.Calculation.Approximation.Extrapolation import Extrapolation


class SimpleFunctionRepair:

    @staticmethod
    def extra_0_inter_1 (dots, x_0):
        if x_0 < dots[0].x or x_0 > dots[-1].x:
            return Extrapolation.zero(dots, x_0)
        else:
            return Interpolation.liner(dots, x_0)
