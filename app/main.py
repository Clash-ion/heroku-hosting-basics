from flask import Flask

server = Flask(__name__)


@server.route("/")
def fun():
    return "<h1>hello world</h1>"