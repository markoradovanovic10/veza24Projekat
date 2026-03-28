# from Db import DB


class User():
    ALL_USERS = []

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
        split_name = name.split()
        if len(split_name) < 2:
            raise ValueError("Name must contain at least first and last name")
        self.__name = name

    def create(self):
        if self.__name is None or self.__age is None:
            raise ValueError("Name and age must be set")
        User.ALL_USERS.append([self.name, self.age])
