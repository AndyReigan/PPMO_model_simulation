import math
import _sqlite3


class Gals:
    def __init__(self, lp, bp, angleRot, rotate, dist):
        self.lp = lp
        self.bp = bp
        self.angleRot = angleRot
        self.rotate = rotate
        self.dist = dist

    def get(self):
        A = []

        lp = self.lp
        bp = self.bp
        angleRot = self.angleRot
        rotate = self.rotate
        dist = self.dist

        return A

    def save(self):
        # save object to sql DB
        pass

    def plot(self):
        # generate plot
        pass
