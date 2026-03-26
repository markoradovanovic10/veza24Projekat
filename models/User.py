
from Db import DB

class User(DB):

    def __init__(self):
        super().__init__()
        con = self._get_connection()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self.__name = name

    def set_age(self, age):
        if age <= 18:
            raise ValueError("Users must be at least 18 years old")
        self.__age = age

    def get_age(self):
        return self.__age
