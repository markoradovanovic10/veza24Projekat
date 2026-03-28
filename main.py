from Models.Car import Car
from Models.User import User
from datetime import date, datetime

option = None

while option is None:
    print(
        "Opcije: "
        "\n1. Dodaj korisnika "
        "\n2. Prikazi korisnike "
        "\n3. Prikazi raspoloziva vozila "
        "\n4. Prikazi rentirana vozila"
        "\n5. Dodaj brend vozila"
        "\n6. Dodaj novi model"
        "\n7. Izadaj vozilo"
    )

    availble_options = [1, 2, 3, 4, 5, 6, 7]

    option = int(input("Odaberite opciju: \n"))

    if option not in availble_options:
        raise ValueError("Neispravna opcija")

    if option == 1:
        newUser = User()
        newUser.name = input("Unesite ime i prezime: ")
        newUser.age = int(input("Unesite godine: "))
        newUser.create()
    elif option == 2:
        showUsers = User()
        for user in showUsers.showUsers():
            print(f"Korisnik: Ime {user[2]} Prezime {user[3]} godiste: {user[4]}")
    elif option == 3 or option == 4:
        i = 1
        car = Car()
        user = User()
        todays_date = date.today()
        for key in car.get_models():
            if key[4] == 0 and option == 3:
                print(f"{i}. Brend {key[1]}, model {key[2]}, godina {key[3]}")
                i += 1
            elif key[4] == 1 and option == 4:
                print(f"{i}. Brend {key[1]}, model {key[2]}, godina {key[3]}")
                carRent = user.getCar(key[0])
                print(f"Izdato: {carRent[1]} {carRent[2]} do {key[5]}")
                returned_date_str = key[5]
                returned_date = returned_date_str.date()
                days_diff = (returned_date - todays_date).days
                if days_diff > 1:
                    print(f"Preostalo dana do vracanja: {days_diff}")
                else:
                    now = datetime.now()
                    print(f"Preostalo sati do vraćanja{key[5]- now}")
                i += 1
    elif option == 5:
        car = Car()
        car.brand = input("Unesite marku: ")
        car.add_brand()
    elif option == 6:
        i = 1
        car = Car()
        print("Unesite brend automobila iz liste: ")
        for key in car.get_brand():
            print(f"{i}. {key[0]}")
            i += 1
        newModel = input("Unestite novi model u formatu: brend, model, godina.\n")
        car.brand = newModel.split(",")[0]
        car.model = newModel.split(",")[1].strip()
        car.year = int(newModel.split(",")[2])
        car.add_model()
    elif option == 7:
        i = 1
        showUsers = User()
        USER_ID = {}
        todays_date = date.today()
        for user in showUsers.showUsers():
            print(f"{i}. {user[2]} {user[3]} {user[4]}")
            USER_ID[i] =[user[0]]
            i += 1
        userID = inpt = int(input("Unesite ID korisnika iz liste: "))

        y = 1
        car = Car()
        CAR_ID = {}
        for key in car.get_models():
            if key[4] == 0:
                print(f"{y}. Brend {key[1]}, model {key[2]}, godina {key[3]}")
                CAR_ID[y] = [key[0]]
                y += 1
        carID = int(input("Unesite ID vozila iz liste: "))

        datum = input("Unesite datum vracanja vozila (format: dd.mm.yyyy): ").split(".")
        pydate = date(int(datum[2]), int(datum[1]), int(datum[0]))
        if todays_date > pydate:
            raise ValueError("Datum ne moze biti manji od danas")

        car.rent_car(CAR_ID[carID], pydate)
        showUsers.addCar(CAR_ID[carID], USER_ID[userID])





    option = input("Da li ste zavrsili (y/n): \n")
    if option == "n" or option == "N":
        option = None
