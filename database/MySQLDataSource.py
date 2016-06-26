__author__ = 'Veltarn'

from Models.Record import AbstractRecord
from Exceptions import MysqlConnectError
from settings import db_settings
import MySQLdb as mysql

class MySQLDataSource:
    '''
    :class: MySQLDataSource
    Provide a connection context and basic intereaction methods to a MySQL server
    '''
    def __init__(self):
        self.hostname = db_settings.dbhost
        self.username = db_settings.dhuser
        self.password = db_settings.dbpass
        self.database = db_settings.dbname

    def _open(self):
        db_handle = mysql.connect(self.hostname, self.username, self.password, self.database)

        if not db_handle:
            raise MysqlConnectError(self.hostname, self.username, self.database)

        return db_handle


    def insert(self, sql_query, data):
        db_handle = self._open()

        with db_handle:
            cursor = db_handle.cursor()
            cursor.execute(sql_query, data)
            affected_rows = cursor.rowcount

        return affected_rows

    def insert_many(self, sql_query, datas):
        if isinstance(datas, list):
            db_handle = self._open()

            with db_handle:
                cursor = db_handle.cursor()
                cursor.executemany(sql_query, datas)

                affected_rows = cursor.rowcount
            return affected_rows
        else:
            raise TypeError("Expected list parameter, got " + type(datas).__name__)

    def select_all(self, sql_query, record_cls=None):
        '''
        Select all data from the given table
        :param sql_query:
        :param record_cls: Record class, the method will transform the raw result into this if provided. It will return a list of rows otherwise
        :return:
        '''
        db_handle = self._open()

        cursor = db_handle.cursor()
        cursor.execute(sql_query)

        rows = cursor.fetchall()

        if record_cls and isinstance(record_cls(), AbstractRecord):
            records = list()
            for row in rows:
                record = record_cls()
                record.from_db(row)
                records.append(record)

            return records
        else:
            return rows
