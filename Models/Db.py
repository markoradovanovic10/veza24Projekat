import pymysql


class datebase_OPP2:
    __connection = pymysql.connect(host="localhost", user="root", password="admin", db="oop_2")

    if __connection:
        cont = True
        print("Connection established")
    else:
        print("Connection failed")
        exit(1)

    def _get_connection(self):
        return datebase_OPP2.__connection

