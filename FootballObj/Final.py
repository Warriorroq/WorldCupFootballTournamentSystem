from FootballObj.Match import *


class Final:
    def __init__(self, match):
        self.matches = match

    def proceed(self, data):
        self.readData(data[0])
        return self

    def readData(self, data):
        for i in range(len(data)):
            self.matches[i].teams[0].goals = int(data[i][0])
            self.matches[i].teams[1].goals = int(data[i][1])