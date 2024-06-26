print("If you are running this for the first time, run:")
print("sudo apt install python3-tk (if on Linux, for mac or pc look up how to install tkinter)")
print("pip install opencv-python")
print("pip install PIL")
print("pip install scikit-image")
print("pip install face-library")
print("pip install pykuwahara")
print("pip install mido")
print("pip install python-rtmidi")
import json, tkinter
from PIL import Image, ImageTk
import mido, rtmidi
import importlib
import os

callbacks = {}
for module in os.listdir(os.path.dirname('effects/')):
    try:
        callbacks[module] = importlib.import_module("effects." + module)
    except Exception as e:
        print(e)

global currentCallback, clb
currentCallback = []
clb = -1

set = json.load(open("set.json", "r"))
isMidi = set["midi"]
if isMidi:
    import requests
    midiAddress = input("Input local ip of server in server.py")
    class message:
        def __init__(self, type):
            self.type=type
    class midiIn:
        def poll():
            x = requests.get(f"{midiAddress}/midiReq")
            return message(x.text)
midiOn = False
sequence = set["sequence"]

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def callback(e):
    global dims, transparent
    root.bind("<Button-1>", nextCallback)
    nextCallback(e)
    while True:
        msg = midiIn.poll()
        if msg:
            if msg.type == "note_on":
                nextCallback(e)
        try:
            newDims = (int(root.winfo_reqwidth() / 3), int(root.winfo_reqheight() / 3))
            if not dims == newDims:
                dims = newDims
                for cb in currentCallback:
                    try:
                        try:
                            changeDims = callbacks[cb["name"]].changeDims
                        except:
                            continue
                        changeDims(newDims)
                    except Exception as ex:
                        print(ex)
            image = Image.new("RGBA", dims)
            for cb in currentCallback:
                try:
                    newImage = callbacks[cb["name"]].callback(image, cb["variables"]).convert("RGBA")
                except:
                    newImage = callbacks[cb["name"]].callback(image).convert("RGBA")
                image = Image.blend(image, newImage, cb["amount"])
            image = Image.alpha_composite(Image.new("RGBA", dims, (0, 0, 0, 255)), image)
            winWidth = root.winfo_width()
            winHeight = root.winfo_height()
            if winWidth / dims[0] > winHeight / dims[1]:
                resize = winHeight / dims[1]
            else:
                resize = winWidth / dims[0]
            img = image.resize((
                int(dims[0] * resize),
                int(dims[1] * resize)
            ))
            img = ImageTk.PhotoImage(img)
            label.configure(image = img)
            label.image = img
            root.update()
        except Exception as e:
            root.quit()
            raise e

def changeCallback():
    global currentCallback, clb, root, dims, prevCallback
    prevCallback = currentCallback
    names = [m["name"] for m in prevCallback]
    currentCallback = sequence[clb]
    #modes = currentCallback['names']
    #for mode in modes:
    #    variables[mode] = callbacks[mode].variables(cam, clb)
    for cb in currentCallback:
        try:
            changeVars = cb["changeVars"]
        except:
            changeVars = True
        if (changeVars and cb["name"] in names) or (not cb["name"] in names):
            try:
                callbacks[cb["name"]].variables(dims, clb)
            except:
                continue
        try:
            callbacks[cb["name"]].changeDims(dims)
        except:
            continue
    #root.title(f"{currentCallback['names'][0].upper()}{currentCallback['names'][1:]}")

def nextCallback(e):
    global clb
    clb += 1
    clb = clb % len(sequence)
    changeCallback()

def prevCallback(e):
    global clb
    if clb == 0:
        clb = len(sequence)
    clb -= 1
    changeCallback()

global dims, transparent

root = tkinter.Tk()
dims = (root.winfo_reqwidth(), root.winfo_reqheight())
transparent = Image.new("RGBA", dims, (0, 0, 0, 0))

root.title("NuclearGraphics")

img1 = ImageTk.PhotoImage(Image.open("nuclearGraphics.png"))

label = tkinter.Label(root, image = img1, borderwidth=0, highlightthickness=0)
label.pack()

root.bind("<Right>", nextCallback)
root.bind("<Left>", prevCallback)
root.bind("<Return>", callback)
root.configure(bg='black')
root.mainloop()
