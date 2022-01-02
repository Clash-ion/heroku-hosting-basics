# from app.main import app
from flask import Flask

app = Flask(__name__)


@app.route("/")
def fun():
    return "<h1>hello world</h1>"


if __name__ == "__main__":
    from waitress import serve
    serve(app)
    # app.run()