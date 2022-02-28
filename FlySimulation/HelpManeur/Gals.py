# -*- coding: utf-8 -*-
import os
import math
import _sqlite3
from Device.HelpFunc import HelpMethod
from Structure.TrajectoryStruct import initialNavData
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from time import gmtime, strftime
import sys

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

    def saveInDb(self):
        # save object to sql DB
        f=open('CurrentManeur','w')
        pass

    def saveInFile(A,A1):
        # save object to sql DB
        f=open(A1,'w')

        for i in range(0,len(A)):
            if i == 0:
                f.write('Id ' + ' lat' + '    lon'+'\n')
            f.write(A[i].status1+' '+str(round(A[i].lat,4))+' '+str(round(A[i].lon,4))+'\n')
        f.close()
        # pass

    def plot(A):
        # generate plot

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
        # plt.show()

    def plotOnMap(A,A1):
        x = np.zeros(len(A))
        y = np.zeros(len(A))
        name = []
        for i in range(0, len(A)):
            x[i] = HelpMethod.radTodeg(A[i].lat)
            y[i] = HelpMethod.radTodeg(A[i].lon)
            name.append(A[i].status1)
        fig = plt.figure()
        llcrnrlat=y[0] - 10
        llcrnrlon = x[0] - 10
        urcrnrlat = y[len(x) - 1] + 20
        urcrnrlon = x[len(y) - 1] + 20
        m = Basemap(llcrnrlat=llcrnrlat, llcrnrlon=llcrnrlon, urcrnrlat=urcrnrlat,
                    urcrnrlon=urcrnrlon)
        for i in range(1, len(x)):
            m.drawgreatcircle(x[i - 1], y[i - 1], x[i], y[i], color="red")
            i = +2
        m.drawcoastlines()
        m.fillcontinents()
        m.drawparallels(np.arange(0, 90, 10), labels=[1, 1, 0, 1])
        # draw meridians
        m.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1])
        for i in range(0, len(x)):
            plt.text(x[i], y[i], name[i])


        plt.savefig(A1)
        plt.close(fig)


m = initialNavData(lat=0.4, lon=0.3, azimut=0.2)
a = Gals(lp=2000 / (6343 * math.pi / 2), bp=3000 / (6343 * math.pi / 2), dist=200 / (6343 * math.pi / 2), rotate='Left',
         id=m)
diction = a.get()
A=strftime("%Y-%m-%d %H:%M:%S", gmtime())
Gals.plotOnMap(diction,A)
Gals.saveInFile(diction,A)

print("m")
sys.exit()