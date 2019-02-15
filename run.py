from api import create_app
from api.database.db import Database



app = create_app('Development')
db = Database(app.config['DATABASE_URI'])
db.create_tables()


# Entry point to the app
if __name__ == '__main__':
    app.run()
