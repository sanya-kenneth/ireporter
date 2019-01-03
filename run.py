from api import create_app


app = create_app('Development')


# Entry point to the app
if __name__ == '__main__':
    app.run()
