from flask import current_app as app
from urllib.parse import urlparse
import psycopg2


class Database:
    """This class connects to the database
    and has a set of methods for manipulating data sent and
    retrieved from the database """

    def __init__(self, Database_url):
        parsed_url = urlparse(Database_url)
        db = parsed_url.path[1:]
        username = parsed_url.username
        hostname = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.con = psycopg2.connect(database=db, user=username,
                                    password=password, host=hostname,
                                    port=port)
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
                    phoneNumber bigint NOT NULL,
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
                    incident_location TEXT [] NOT NULL,
                    incident_image_name TEXT,
                    comment TEXT NOT NULL,
                    incident_status VARCHAR(50) NOT NULL
                    )
                    """
        )

        for command in commands:
            self.cursor.execute(command)

    def select_all_incidents(self, record_type):
        sql = ("""SELECT * from incident_table WHERE record_type = '{}'"""
               .format(record_type))
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_one_record(self, table_name, criteria, input_data):
        sql = ("""SELECT * from {} WHERE {} = '{}' """
               .format(table_name, criteria, input_data))
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def select_one_incident(self, table_name, criteria, input_data, record_type):
        sql = ("""SELECT * from {} WHERE {} = '{}' AND record_type = '{}'"""
               .format(table_name, criteria, input_data, record_type))
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def add_incident_record(self, createdOn, createdBy, record_type,
                            incident_location_lat, incident_location_long,
                            comment, incident_status):
        sql = ("""INSERT INTO incident_table(createdOn, createdBy, record_type,
                incident_location, comment, incident_status)
        VALUES ('{}', '{}', '{}', ARRAY['{}','{}'], '{}', '{}');"""
               .format(createdOn, createdBy, record_type, incident_location_lat,
               incident_location_long, comment, incident_status))
        return self.cursor.execute(sql)
        

    def add_user(self, firstname, lastname, othernames, username, useremail,
                 phoneNumber, userpassword, registered, isAdmin):
        sql = ("""INSERT INTO user_table(firstname, lastname, othernames, username,
               useremail, phoneNumber, userpassword, registered, isAdmin)
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
               .format(firstname, lastname, othernames, username, useremail,
                       phoneNumber, userpassword, registered, isAdmin))
        return self.cursor.execute(sql)

    def update_incident_record(self, field_to_update, incident_id_in,
                               input_data, record_type):
        sql = ("""UPDATE incident_table SET {} = '{}' WHERE incidentid = '{}' AND record_type = '{}'"""
               .format(field_to_update, input_data, incident_id_in, record_type))
        return self.cursor.execute(sql)

    def update_incident_record_location(self,  incident_id_in,
                               input_data1, input_data2, record_type):
        sql = ("""UPDATE incident_table SET incident_location [ 1 ] = '{}',
        incident_location [ 2 ] = '{}' WHERE incidentid = '{}' AND record_type = '{}'"""
               .format(input_data1, input_data2, incident_id_in, record_type))
        return self.cursor.execute(sql)

    def delete_incident_record(self, incident_id, record_type):
        sql = ("""DELETE from incident_table WHERE incidentid = '{}' AND record_type = '{}' """
               .format(incident_id, record_type))
        return self.cursor.execute(sql)

    def drop_tables(self):
        command = ("""DROP TABLE user_table """,
                   """DROP TABLE incident_table  """)
        for comm in command:
            self.cursor.execute(comm)


def db_handler():
    database_obj = Database(app.config['DATABASE_URI'])
    return database_obj
