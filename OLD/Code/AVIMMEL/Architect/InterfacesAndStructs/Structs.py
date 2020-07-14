class Data:
    def __init__(self, value=None, read=None, cont=None, corr=None, extr=None, time=None, state="Work"):
        self.value = value
        self.read = read
        self.cont = cont
        self.corr = corr
        self.extr = extr
        self.time = time
        self.state = state


class Angle:
    def __init__(self, degrees, minutes, seconds):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds


class State:
    def __init__(self, value=None, state="Work"):
        self.value = value
        self.state = state


class Fail:
    def __init__(self, isFailed=False, state="Work"):
        self.isFailed = isFailed
        self.state = state


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Borders:
    def __init__(self, min, max):
        self.min = min
        self.max = max