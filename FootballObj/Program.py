class Program:
    currentState = None
    gui = None
    def __init__(self):
        #create GUI
        #make connections
        return

    def start(self):
        if self.gui is not None:
            self.gui.start()

    def proceed(self, data):
        self.currentState.proceed(data)
