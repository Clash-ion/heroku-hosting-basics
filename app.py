# from app.main import app
from flask import Flask
# def helpful_function():
app = Flask(__name__)
# application = app

@app.route("/")
def fun():
    return "<h1>hello world</h1>"

    # return app


if __name__ == "__main__":
    # from waitress import serve
    # serve(app)
    app.run()