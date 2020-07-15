import math
import _sqlite3
from Device.HelpFunc import HelpMethod
from Structure.TrajectoryStruct import initialNavData


class Gals:
    def __init__(self, lp, bp, id):
        self.lp = lp
        self.bp = bp
        self.angle_rot = id.azimut
        self.rotate = id.status1
        self.dist = id.dist

        self.id = id

    def get(self):

        A = []
        lp = self.lp
        bp = self.bp
        rotate = self.rotate
        dist = self.dist

        # количество галсов для зоны покрытия поиска
        n = bp // dist
        if bp - n * dist > dist / 2:
            n + 1

        k = n + 2  # общее число ППМ
        # инициализируем необходимые нам точки
        a0_point = HelpMethod(self.id)
        angle_rot = a0_point.azimut
        b0_point = a0_point.direct_task_sphere()

        if rotate == "Left":
            angle_rot + math.pi / 2
        elif rotate == "Right":
            angle_rot - math.pi / 2
        a0_point.azimut = angle_rot
        b0_point.azimut = angle_rot
        i = 0
        while i <= k // 2:
            point_id1 = initialNavData()
            point_id2 = initialNavData()
            a0_point.dist = i * dist
            current_point = a0_point.direct_task_sphere()

        return A

    def save(self):
        # save object to sql DB
        pass

    def plot(self):
        # generate plot
        pass
