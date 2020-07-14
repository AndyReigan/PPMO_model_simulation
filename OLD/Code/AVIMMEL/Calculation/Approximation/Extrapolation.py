class Extrapolation:
    @staticmethod
    def zero(dots, x_0):
        if x_0 <= dots[0].x:
            return dots[0].y
        elif x_0 >= dots[-1].x:
            return dots[-1].y
        else:
            return None
