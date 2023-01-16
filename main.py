from Program import *


@eel.expose
def readGameStateData():
    return program.convertToSendableData()


program = Program()
program.start("index.html")