from app.main import server

if __name__ == "__main__":
    from waitress import serve
    serve(server)
    # app.run()