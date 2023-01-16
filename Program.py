from HTMLGUI import *
from FootballObj.FirstTour import *


class Program:
    currentState = None
    gui = None

    def __init__(self):
        self.gui = HTMLGUI()
        self.currentState = FirstTour()
        onDataReceived.add(self.proceed)

    def start(self, file):
        if self.gui is not None:
            self.gui.start(file)

    def proceed(self, data):
        if self.currentState is not None:
            self.currentState = self.currentState.proceed(data)

    def convertToSendableData(self):
        if type(self.currentState) is not FirstTour:
            return [i.convertToSendableData() for i in self.currentState.matches]
