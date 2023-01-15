from FootballObj.QuarterFinal import *
from FootballObj.Match import *


class Round16:
    def __init__(self, matches=None):
        self.matches = matches or []

    def proceed(self, data):
        self.readData(data[0])
        print("round 16")
        for i in self.matches:
            print(str(i))
        return QFinal([Match([self.matches[i*2].getWinner(), self.matches[i*2 + 1].getWinner()])
                       for i in range(len(self.matches)//2)])

    def readData(self, data):
        for i in range(len(data)):
            self.matches[i].teams[0].goals = int(data[i][0])
            self.matches[i].teams[1].goals = int(data[i][1])
