import eel
import glob
eel.init("web")

@eel.expose
def readAllImages():
    images = []
    for source in [i.replace('web/', '').replace('\\', '/') for i in glob.glob('web/img/*.jpeg')]:
        countryName = source.replace('img/', '').replace('.jpeg', ' ').replace('_', ' ')
        images.append((countryName, source))
    return images

print(readAllImages())
@eel.expose
def printMessage(message):
    print(message)
    return message


eel.start("index.html", size=(1080, 720))