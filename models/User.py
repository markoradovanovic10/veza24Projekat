from Db import DB


class User(DB):

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 18:
            raise ValueError("Users must be at least 18 years old")
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
