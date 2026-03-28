from datetime import date

from Models.Db import datebase_OPP2


def get_cursor_and_connection():
    db = datebase_OPP2()
    conn = db._get_connection()
    cursor = conn.cursor()
    return cursor, conn

class User(datebase_OPP2):

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        currentYear = date.today().year
        if age <= 18:
            raise ValueError("Users must be at least 18 years old")
        self.__age = currentYear - age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        split_name = name.split()
        if len(split_name) < 2:
            raise ValueError("Name must contain at least first and last name")
        self.__name = name

    def create(self):
        name = self.name.split()[0]
        last_name = self.name.split()[1]
        cursor, conn = get_cursor_and_connection()
        cursor.execute("INSERT INTO user (name, last_name, age) VALUES (%s, %s, %s)", (name, last_name, self.age))
        conn.commit()
        cursor.close()

    def showUsers(self):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
        return result

    def addCar(self, car, user_id):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("UPDATE user SET rented_car = %s WHERE id = %s", (car, user_id))
        conn.commit()
        cursor.close()

    def getCar(self, car_id):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("SELECT id, name, last_name  FROM user WHERE rented_car = %s", (str(car_id)))
        result = cursor.fetchone()
        cursor.close()
        return result




