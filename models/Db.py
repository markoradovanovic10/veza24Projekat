import pymysql


class DB:
    def __init__(self):
        self.__connection = pymysql.connect(host="localhost", user="root", password="admin", db="oop_2")

    def _get_connection(self):
        return self.__connection