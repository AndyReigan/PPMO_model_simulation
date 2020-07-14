import math
from Structure.TrajectoryStruct import initialNavData


class HelMethod:
    id = initialNavData()
    R = 6343

    def cartToCircl(self, x, y, z):
        lat = math.atan2(y, x)
        lon = math.atan2(math.sqrt(x * x + y * y), z)

        id.lat = lat
        id.lon = lon
        return id

    def geoToCart(self, lat, lon, h):
        x = (R + h) * math.sin(lat) * math.cos(lon)
        y = (R + h) * math.sin(lat) * math.sin(lon)
        z = (R + h) * math.cos(lon)
        id = initialNavData()
        id.x = x
        id.y = y
        id.z = z
        return id
