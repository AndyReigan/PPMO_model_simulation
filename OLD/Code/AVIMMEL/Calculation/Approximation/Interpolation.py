class Interpolation:
    @staticmethod
    def liner(dots, x_0):
        prevDot = None
        if x_0 < dots[0].x or x_0 > dots[-1].x:
            return None
        else:
            for dot in dots:
                if dot.x == x_0:
                    return dot.y
                elif dot.x > x_0:
                    return prevDot.y + (dot.y - prevDot.y) / (dot.x - prevDot.x) * (x_0 - prevDot.x)
                prevDot = dot