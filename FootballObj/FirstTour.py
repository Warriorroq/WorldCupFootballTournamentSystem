from Match import *
from Round16 import *
class FirstTour:
    __groups = []
    def __init__(self, groups):
        self.__groups = groups

    def proceed(self):
        print("groups:")
        for i in self.__groups:
            print(str(i))
        return Round16([Match(i.getTwoBestTeams()) for i in self.__groups])