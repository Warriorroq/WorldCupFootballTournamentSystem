from FootballObj.Final import *
from FootballObj.Match import *
class SFinal:
    def __init__(self, matches=None):
        self.matches = matches or []

    def proceed(self):
        print("semi final")
        for i in self.matches:
            print(str(i))
        return Final([Match([self.matches[i * 2].getWinner(), self.matches[i * 2 + 1].getWinner()])
                      for i in range(len(self.matches) // 2)])