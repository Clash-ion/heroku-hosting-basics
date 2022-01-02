from flask import Flask

app = Flask(__name__)


@app.route("/")
def fun():
    return "<h1>hello world</h1>"