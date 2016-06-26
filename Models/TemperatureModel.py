__author__ = 'Veltarn'

from settings import db_settings
import datetime
import MySQLdb as mysql

class TemperatureModel:
    def __init__(self):
        pass

    def load_all(self):
        db_handle = mysql.connect(db_settings.dbhost, db_settings.dhuser, db_settings.dbpass, db_settings.dbname)

        cursor = db_handle.cursor()
        cursor.execute("SELECT * FROM temperature")

        rows = cursor.fetchall()

        #todo transformer cette horreur en objet Record
        temps_list = list()
        for row in rows:
            temps_list.append(row)

        return temps_list

    def insert(self, temp):
        temp = int(temp.raw_value())
        insert_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

        db_handle = mysql.connect(db_settings.dbhost, db_settings.dhuser, db_settings.dbpass, db_settings.dbname)

        with db_handle:
            cursor = db_handle.cursor()
            cursor.execute("INSERT INTO temperature(temperature, measurement_date) VALUES(%s, %s)", (temp, insert_time))

            affected_rows = cursor.rowcount

        return affected_rows
