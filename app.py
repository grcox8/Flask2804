from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hl")
def hasta_luego():
    return "<p>Hasta luego!</p>"

@app.route("/bv")
def bienvenido():
    return "<p>Bienvenido!</p>"