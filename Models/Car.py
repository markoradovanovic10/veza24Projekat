from datetime import datetime, date
from Models.Db import datebase_OPP2

def get_cursor_and_connection():
    db = datebase_OPP2()
    conn = db._get_connection()
    cursor = conn.cursor()
    return cursor, conn


class Car(datebase_OPP2):

    def __init__(self):
        self.__model = None
        self.__brand = None
        self.__year = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    def add_brand(self):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("SELECT id FROM brand_for_rent WHERE LOWER(brand) = %s",(self.__brand.lower(),))
        result = cursor.fetchone()
        if result is not None:
            raise ValueError("Brand already exists")
        print(f"Adding brand:  {self.__brand} to database")
        cursor.execute("INSERT INTO brand_for_rent (brand) VALUES (%s)", (self.__brand,))
        conn.commit()
        cursor.close()

    def add_model(self):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("SELECT id FROM brand_for_rent WHERE LOWER(brand) = %s",(self.__brand.lower(),))
        result = cursor.fetchone()

        if result is None:
            raise ValueError("Brand must be set before model")
        brand_id = result[0]

        cursor.execute("INSERT INTO models_for_rent (brand, model, year, rented, rented_date) VALUES (%s, %s, %s, %s, %s)",(brand_id, self.__model, self.__year, 0, None))
        conn.commit()
        cursor.close()

    def get_brand(self):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("SELECT brand FROM brand_for_rent")
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        return result

    def get_models(self):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("""SELECT m.id, b.brand, m.model, m.year, m.rented, m.rented_date FROM models_for_rent AS m JOIN brand_for_rent AS b ON m.brand = b.id""")
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        return result

    def rent_car(self, model_id, date_return):
        cursor, conn = get_cursor_and_connection()
        cursor.execute("UPDATE models_for_rent SET rented = %s, rented_date = %s WHERE id = %s",(1, date_return, model_id))
        conn.commit()
        cursor.close()




