from pyexpat import model

from pip._internal import models


class Car:
    models = {
        "audi": [
            {"name": "a4", "year": 2010},
            {"name": "a5", "year": 2011},
            {"name": "a6", "year": 2012}
        ],
        "bmw": [
            {"name": "m3", "year": 2010},
            {"name": "m5", "year": 2011},
            {"name": "m6", "year": 2012}
        ],
        "mercedes": [
            {"name": "c180", "year": 2010},
            {"name": "c200", "year": 2011},
            {"name": "c250", "year": 2012}
        ]
    }

    def __init__(self):
        self.__model = None
        self.__brand = None
        self.__year = None


    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("Brand must be set before model")
        validated_models = []

        for car in Car.models[self.__brand]:
            validated_models.append(car["name"])

        if model not in validated_models:
            raise ValueError("Invalid model")

        self.__model = model

        for car_model in Car.models[self.__brand]:
            if car_model["name"] == model:
                self.__year = car_model["year"]

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):

        if brand not in Car.models:
            raise ValueError("Invalid brand")
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if self.__model is None:
            raise ValueError("Model must be set before year")
        if self.__model is not None and self.__year is not None:
            raise ValueError("Year must be set before model")
        self.__year = year


Audi = Car()
Audi.brand = "audi"
Audi.model = "a4"
print(Audi.model + " " + Audi.brand + " " + str(Audi.year))