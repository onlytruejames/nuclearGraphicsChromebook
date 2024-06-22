from PIL import Image

print("Make sure nuclearGraphicsChromebook has been renamed to 'camera'")

global lastImg
lastImg = Image.new("RGBA", (100, 100))

def callback(image):
    global lastImg
    try:
        img = Image.open("effects/camera/capture.png").resize(image.size)
        lastImg = img
    except:
        pass
    return lastImg.resize(image.size)
