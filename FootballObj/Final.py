from Match import *
class Final:
    def __init__(self, match):
        self.matches = match

    def proceed(self):
        print("final")
        for i in self.matches:
            print(str(i))
        return Final([Match([self.matches[i * 2].getWinner(), self.matches[i * 2 + 1].getWinner()])
                      for i in range(len(self.matches) // 2)])