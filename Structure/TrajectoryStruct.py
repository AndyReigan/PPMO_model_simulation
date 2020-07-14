class initialNavData:
    def __init__(self, x, y, z, lat, lon, wind, speed, course, windDir):
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


class Angle:
    # минуты, секунды и так далее
    def __init__(self, degrees, minutes, seconds):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds


class Aircraft:
    pass