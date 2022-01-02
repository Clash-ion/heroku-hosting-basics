from app.main import app

if __name__ == "__main__":
    from waitress import serve
    serve(app)
    # app.run()