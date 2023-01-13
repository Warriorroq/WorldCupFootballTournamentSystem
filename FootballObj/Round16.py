from QuarterFinal import *
from Match import *
class Round16:
    def __init__(self, matches=None):
        self.matches = matches or []

    def proceed(self):
        print("round 16")
        for i in self.matches:
            print(str(i))
        return QFinal([Match([self.matches[i*2].getWinner(), self.matches[i*2 + 1].getWinner()]) for i in range(len(self.matches)//2)])
