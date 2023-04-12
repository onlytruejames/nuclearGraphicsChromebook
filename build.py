txt = open("../main.py", "r").read()
open("../main.py", "w").write(txt.replace("from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB", """from cv2 import imread, cvtColor, COLOR_BGR2RGB
class VideoCapture:
    def read():
        img = imread("capture.jpeg")
        if img is None:
            return False, None
        return True, img
    def get(x):
        if x == 3:
            return Image.open("capture.jpeg").width
        else:
            return Image.open("capture.jpeg").height
""").replace("VideoCapture(", "VideoCapture#").replace("def list_ports():", """def list_ports():
    return [0]"""))
print("NuclearGraphics has been fixed. Run main.py in this directory and visit the right IP address to gain access. I'm not sure what that'll be but it's probably 127.0.0.1:5000. It can be very inconsistent, unfortunately.")
