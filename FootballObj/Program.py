import random
from Group import *
from Team import *
from FirstTour import *

class Program:
    currentState = None
    gui = None

    def __init__(self, groups):
        self.currentState = FirstTour(groups)
        # create GUI
        # make connections
        return

    def start(self):
        if self.gui is not None:
            self.gui.start()

    def proceed(self):
        if self.currentState is not None:
            self.currentState = self.currentState.proceed()

teams = []

for i in range(33):
    teams.append(Team(f"dummy{i}", random.randint(0, 100)))


groups = [
    Group("Group A", teams[:4]),
    Group("Group B", teams[4:8]),
    Group("Group C", teams[8:12]),
    Group("Group D", teams[12:16]),
    Group("Group E", teams[16:20]),
    Group("Group F", teams[20:24]),
    Group("Group G", teams[24:28]),
    Group("Group H", teams[28:32])
]

p = Program(groups)
p.proceed()
p.proceed()
p.proceed()
p.proceed()
p.proceed()