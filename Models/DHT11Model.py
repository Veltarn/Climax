__author__ = 'Veltarn'
import datetime
from Record import AbstractRecord
from database.MySQLDataSource import MySQLDataSource
from database.Exceptions import MysqlConnectError

from Sensors.DHT11 import Humidity

class HumiditySensorModel:
    def __init__(self):
        pass

    def insert(self, humidity):
        if isinstance(humidity, Humidity):
            datasource = MySQLDataSource()
            insert_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

            try:
                affected_rows = datasource.insert("INSERT INTO humidity (humidity_value, measurement_date) VALUES(%s, %s)", (humidity.value, insert_time))
            except MysqlConnectError as e:
                print(e.message)
                return False
            else:
                return affected_rows
        else:
            print("Warning: trying to insert " + type(humidity).__name__ + " object, Humidity object expected")

    def load_all(self):
        datasource = MySQLDataSource()

        records = datasource.select_all("SELECT * FROM humidity", HumiditySensorRecord)

        return records


class HumiditySensorRecord(AbstractRecord):
    def __init__(self):
        self.pkey = None
        self.humidity_value = None
        self.measurement_date = None

    def from_db(self, row):
        self.pkey = row[0]
        self.humidity_value = row[1]
        self.measurement_date = row[2]
