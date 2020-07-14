import math
from Structure.TrajectoryStruct import initialNavData


class HelMethod:

    def __init__(self, id):
        self.r = 6343
        self.id=id
        self.lat=id.lat
        self.lon=id.lon
        self.x=id.x
        self.y=id.y
        self.z=id.z
        self.h=id.height

    def cartToCircl(self):
        lat=self.lat
        lon=self.lon
        x=self.x
        y=self.y
        z=self.z
        lat = math.atan2(y, x)
        lon = math.atan2(math.sqrt(x * x + y * y), z)

        self.id.lat = lat
        self.id.lon = lon
        return id

    def geoToCart(self):
        h=self.h
        lat=self.lat
        lon=self.lon
        x = (self.r + h) * math.sin(lat) * math.cos(lon)
        y = (self.r + h) * math.sin(lat) * math.sin(lon)
        z = (self.r + h) * math.cos(lon)

        self.id.x = x
        self.id.y = y
        self.id.z = z
        return id


id=initialNavData(lat=10,lon=11,height=1)
a = HelMethod(id)
m=a.cartToCircl()
print(m.x,m.y,m.z)
