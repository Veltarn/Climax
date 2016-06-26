__author__ = 'Veltarn'

class MysqlConnectError(Exception):
    def __init__(self, hostname, username, database):
        msg = "Can't connect to " + database + " database on host " + hostname + " as " + username + "\n"
        msg += "Please check your credentials"

        super(MysqlConnectError, self).__init__(msg)
