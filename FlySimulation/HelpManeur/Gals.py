# -*- coding: utf-8 -*-
import os
import math
import _sqlite3
from Device.HelpFunc import HelpMethod
from Structure.TrajectoryStruct import initialNavData
import numpy as np
import matplotlib.pyplot as plt
# from basemap import Basemap

class Gals:
    def __init__(self, lp, bp, dist, rotate, id):
        self.lp = lp
        self.bp = bp
        self.angle_rot = id.azimut
        self.rotate = rotate

        self.dist = dist

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
        a0_point.dist = lp
        a0_point.azimut = angle_rot
        b0_point = a0_point.direct_task_sphere()
        b0_point.dist = a0_point.dist
        b0_point = HelpMethod(b0_point)
        if rotate == "Left":
            angle_rot = + math.pi / 2
        elif rotate == "Right":
            angle_rot = - math.pi / 2
        a0_point.azimut = angle_rot
        b0_point.azimut = angle_rot
        i = 1
        while i <= k:
            a0_point.dist = i * dist
            b0_point.dist = i * dist
            current_point1 = a0_point.direct_task_sphere()
            current_point2 = b0_point.direct_task_sphere()


            if i % 2 != 0:
                current_point1.status1 = 'A' + str(i)
                A.append(current_point1)

                current_point2.status1 = 'B' + str(i)
                A.append(current_point2)
            elif i % 2 == 0:
                current_point2.status1 = 'B' + str(i)
                A.append(current_point2)
                current_point1.status1 = 'A' + str(i)
                A.append(current_point1)
            i = i + 1
        return A

    def save(self):
        # save object to sql DB

        pass

    def plot(A):
        # generate plot
        pass

        x = np.zeros(len(A))
        y = np.zeros(len(A))
        name = []
        for i in range(0, len(A)):
            x[i] = A[i].lat
            y[i] = A[i].lon
            name.append(A[i].status1)

        plt.plot(x, y)
        for i in range(0, len(x)):
            plt.text(x[i], y[i], name[i])
        plt.show()


m = initialNavData(lat=0.6, lon=0.72, azimut=0.2)
a = Gals(lp=1000 / (6343 * math.pi / 2), bp=1000 / (6343 * math.pi / 2), dist=200 / (6343 * math.pi / 2), rotate='Left',
         id=m)
diction = a.get()
Gals.plot(diction)
print(diction)