import math
from Structure.TrajectoryStruct import initialNavData


class HelMethod:

    def __init__(self, id):
        self.r = 6343
        self.id = id
        self.lat = id.lat
        self.lon = id.lon
        self.x = id.x
        self.y = id.y
        self.z = id.z
        self.h = id.height

    def cartToCircl(self):
        x = self.x
        y = self.y
        z = self.z
        lat = math.atan2(y, x)
        lon = math.atan2(math.sqrt(x * x + y * y), z)

        id.lat = lat
        id.lon = lon
        return id

    def geoToCart(self):
        h = self.h
        lat = self.lat
        lon = self.lon
        x = (self.r + h) * math.sin(lat) * math.cos(lon)
        y = (self.r + h) * math.sin(lat) * math.sin(lon)
        z = (self.r + h) * math.cos(lon)

        id.x = x
        id.y = y
        id.z = z
        return id


id = initialNavData(x=10, y=11, z=1)
a = HelMethod(id)
m = a.cartToCircl()
print(m.lat, m.lon, m.z)
