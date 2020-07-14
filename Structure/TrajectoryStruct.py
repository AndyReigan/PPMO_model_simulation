class initialNavData:
    def __init__(self, x=None, y=None, z=None, lat=None, lon=None, wind=None, speed=None, course=None, windDir=None,
                 height=None, azimut=None,dist=None):
        # в зависимости от необходимости используются либо те
        # либо иные координаты!!!
        self.x = x
        self.y = y
        self.z = z
        self.lat = lat
        self.lon = lon
        self.wind = wind
        self.speed = speed
        self.course = course
        self.windDir = windDir
        self.height = height
        self.azimut = azimut
        self.dist=dist


class Angle:
    # минуты, секунды и так далее
    def __init__(self, degrees, minutes, seconds):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds


class Aircraft:
    pass
