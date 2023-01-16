import eel
import glob
import PyEvent


onDataReceived = PyEvent.Event()


class HTMLGUI:

    def __init__(self, folder = "web"):
        eel.init(folder)

    def start(self, file = "tournament.html"):
        eel.start(file, size = (1080, 720))


@eel.expose
def readDataFromFontEnd(data):
    onDataReceived.invoke(data)


@eel.expose
def readAllCountryImages():
    images = []
    for source in [i.replace('web/', '').replace('\\', '/') for i in glob.glob('web/images/country/*.jpeg')]:
        countryName = source.replace('images/country/', '').replace('.jpeg', ' ').replace('_', ' ').strip()
        images.append((countryName, source))
    return images