from FootballObj.Round16 import *
from FootballObj.Group import *


class FirstTour:
    __groups = []

    def readIncomeData(self, data):
        data = data[0]
        for i in range(len(data)//4):
            self.__groups.append(Group(data[i*4:(i+1)*4]))
        return

    def proceed(self, data):
        self.readIncomeData(data)
        return Round16([Match(i.getTwoBestTeams()) for i in self.__groups])