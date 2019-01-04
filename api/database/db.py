from flask import current_app as app
from urllib.parse import urlparse
import psycopg2


class Database:
    """This class connects to the database 
    and has a set of methods for manipulating data sent and
    retrieved from the database """

    def __init__(self,Database_url):
        parsed_url = urlparse(Database_url)
        db = parsed_url.path[1:]
        username = parsed_url.username
        hostname = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.con = psycopg2.connect(database=db,user=username,password=password,
                                    host=hostname, port=port)
        self.con.autocommit = True
        self.cursor = self.con.cursor()

    
    def create_tables(self):
        commands = (
        """
        CREATE TABLE IF NOT EXISTS user_table(
        userid SERIAL PRIMARY KEY,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        othernames VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        useremail VARCHAR(50) NOT NULL,
        phoneNumber INT NOT NULL,
        userpassword TEXT NOT NULL,
        registered TEXT NOT NULL,
        isAdmin BOOL NOT NULL
        )
        """,
        """ CREATE TABLE IF NOT EXISTS incident_table(
        incidentid SERIAL PRIMARY KEY,
        createdOn TEXT NOT NULL,
        createdBy VARCHAR(50) NOT NULL,
        record_type VARCHAR(50) NOT NULL,
        incident_location TEXT NOT NULL,
        incident_image TEXT NOT NULL,
        incident_video TEXT NOT NULL,
        comment TEXT NOT NULL,
        incident_status VARCHAR(50) NOT NULL
        )
        """
        )

        for command in commands:
            self.cursor.execute(command)

    
    def select_all_incidents(self):
        sql = ("""SELECT * from incident_table """)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def select_one_incident_record(self, incident_id_in):
        sql = ("""SELECT * from incident_table WHERE incidentid = {} """\
        .format(incident_id_in))
        self.cursor.execute(sql)
        return self.cursor.fetchone()


    def add_incident_record(self, createdOn, createdBy, record_type, incident_location,
                            incident_image, incident_video, comment, incident_status):
        sql = ("""INSERT INTO user_table(username, useremail, userpassword,adminstatus) 
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""\
        .format(createdOn, createdBy, record_type, incident_location,
                incident_image, incident_video, comment, incident_status))
        return self.cursor.execute(sql)


    def update_incident_record(self, field_to_update, incident_id_in, input_data):
        sql = ("""UPDATE incident_table SET {} = '{}' WHERE incidentid = '{}'"""\
        .format(field_to_update, incident_id_in, input_data))
        return self.cursor.execute(sql)


    def delete_incident_record(self, incident_id):
        sql = ("""DELETE from incident_table WHERE incidentid = '{}' """.format(incident_id))
        return self.cursor.execute(sql)


    def drop_tables(self):
        command = ("""DROP TABLE user_table """,
                    """DROP TABLE incident_table  """)
        for comm in command:
            self.cursor.execute(comm)


def db_handler():
    database_obj = Database(app.config['DATABASE_URI'])
    return database_obj
