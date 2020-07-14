class MoveAvg:
    def __init__(self, frameNum):
        self.frameNum = frameNum
        self.vals = []

    def filtrate(self, newCount):
        if len(self.vals) >= self.frameNum:
            del self.vals[0]
        self.vals.append(newCount)
        return sum(self.vals) / len(self.vals)

    def changeFrameNum(self, newFrameNum):
        self.frameNum = newFrameNum
        self.vals = []

