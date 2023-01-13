from SemiFinal import *
from Match import *
class QFinal:
    def __init__(self, matches):
        self.matches = matches or []

    def proceed(self):
        print("quarter final")
        for i in self.matches:
            print(str(i))
        return SFinal([Match([self.matches[i * 2].getWinner(), self.matches[i * 2 + 1].getWinner()]) for i in
                           range(len(self.matches) // 2)])
