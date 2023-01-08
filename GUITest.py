import eel
import glob
eel.init("web")

@eel.expose
def readAllCountryImages():
    images = []
    for source in [i.replace('web/', '').replace('\\', '/') for i in glob.glob('web/images/country/*.jpeg')]:
        countryName = source.replace('images/country/', '').replace('.jpeg', ' ').replace('_', ' ')
        images.append((countryName, source))
    return images

print(readAllCountryImages())
@eel.expose
def printMessage(message):
    print(message)
    return message


eel.start("index.html", size=(1080, 720))