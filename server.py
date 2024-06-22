from flask import Flask, render_template, request

app = Flask(__name__)

global midiUpdate
midiUpdate = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit/", methods=["POST"])
def submit():
    f = request.files['file']
    f.save("capture.png")
    return ""

@app.route('/midi/')
def midiIn():
    global midiUpdate
    midiUpdate += 1
    return ""

@app.route('/midiReq/')
def midiReq():
    global midiUpdate
    if midiUpdate > 0:
        midiUpdate -= 1
        return "note_on"
    return "no"

app.run()
