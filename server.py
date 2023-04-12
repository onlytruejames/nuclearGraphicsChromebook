import os, base64
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit/", methods=["POST"])
def submit():
    f = request.files['file']
    f.save("../capture.jpeg")
    return ""

app.run()
