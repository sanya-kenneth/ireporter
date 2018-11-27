from api import create_app


app = create_app('Development')


# App entry point
if __name__ == '__main__':
    app.run()
