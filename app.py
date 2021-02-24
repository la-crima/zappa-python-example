from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello"


@app.route("/index")
def index():
    return "Index"
