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
        angle_rot = self.angle_rot
        # количество галсов для зоны покрытия поиска
        n = bp // dist
        if bp - n * dist > dist / 2:
            n + 1

        k = n + 2  # общее число ППМ
        # инициализируем необходимые нам точки
        a0_point = HelpMethod(self.id)

        b0_point = a0_point.direct_task_sphere()
        b0_point = HelpMethod(b0_point)
        if rotate == "Left":
            angle_rot + math.pi / 2
        elif rotate == "Right":
            angle_rot - math.pi / 2
        a0_point.azimut = angle_rot
        b0_point.azimut = angle_rot
        i = 0
        while i <= k // 2:
            a0_point.dist = i * dist
            b0_point.dist = i * dist
            current_point1 = a0_point.direct_task_sphere()
            A.append(current_point1)
            current_point2 = b0_point.direct_task_sphere()
            A.append(current_point2)
        return A

    def save(self):
        # save object to sql DB
        pass

    def plot(self):
        # generate plot
        pass


m = initialNavData(lat=0.5, lon=0.7, azimut=0.7, dist=100)
a = Gals(lp=100, bp=1000, id=m)
diction=a.get()

print(diction)
