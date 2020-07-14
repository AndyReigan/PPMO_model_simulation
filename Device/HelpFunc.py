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
        self.azimut = id.azimut
        self.dist = id.dist

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

    def direct_task_sphere(self):
        azimut = self.azimut
        lat0 = self.lat
        lon0 = self.lon

        # добавить
        lat1 = None
        lon1 = None

        id1 = initialNavData()
        id1.lat = lat1
        id1.lon = lon1
        return id1

    @staticmethod
    # широта промежуточной точки, как функция долготы, выглядит прикольно, хотел использовать для захода чтобы сверится

    def lat_intermed_point(lat1, lon1, lat2, lon2, lon_x):
        a = math.tan(lat1) * math.sin(lon2 - lon_x) + math.tan(lat2) * math(lon_x - lon1)
        b = math.sin(lon2 - lon1)
        lat_x = math.atan2(a, b)
        return lat_x


# test
id1 = initialNavData(x=10, y=11, z=1)
a = HelMethod(id1)
m = a.cartToCircl()
print(m.lat, m.lon, m.z)

id2 = initialNavData(lat=0.8, lon=3, height=100)
m2 = HelMethod(id2)
m3 = m2.geoToCart()
print(m3.x, m3.y, m3.z)
