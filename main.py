

from Models.Car import Car
from Models.User import User
from datetime import date, datetime

option = None

while option is None:
    #Starting of menu
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
    #Checking if these options are available
    availble_options = [1, 2, 3, 4, 5, 6, 7]

    option = int(input("Odaberite opciju: \n"))

    if option not in availble_options:
        raise ValueError("Neispravna opcija")

    #Creating the user
    if option == 1:
        newUser = User()
        newUser.name = input("Unesite ime i prezime: ")
        newUser.age = int(input("Unesite godine: "))
        newUser.create()
    #Showing the users
    elif option == 2:
        showUsers = User()
        for user in showUsers.showUsers():
            print(f"Korisnik: Ime {user[2]} Prezime {user[3]} godiste: {user[4]}")
    #Showing the cars available for rent or not
    elif option == 3 or option == 4:
        i = 1
        car = Car()
        user = User()
        todays_date = date.today()
        for key in car.get_models():
            # Showing only available cars that have false(not rented) in the 4th column
            if key[4] == 0 and option == 3:
                print(f"{i}. Brend {key[1]}, model {key[2]}, godina {key[3]}")
                i += 1
            #showing only rented cars that have true (rented) in the 4th column
            elif key[4] == 1 and option == 4:
                #Show the cars that is rented
                print(f"{i}. Brend {key[1]}, model {key[2]}, godina {key[3]}")
                carRent = user.getCar(key[0])
                #Show the user that rented the car
                print(f"Izdato: {carRent[1]} {carRent[2]} do {key[5]}")
                returned_date_str = key[5]
                returned_date = returned_date_str.date()
                days_diff = (returned_date - todays_date).days
                #Showing how many days have left to return the car
                if days_diff > 1:
                    print(f"Preostalo dana do vracanja: {days_diff}")
                else:
                #Showing how many hours have left to return the car
                    now = datetime.now()
                    print(f"Preostalo sati do vraćanja{key[5]- now}")
                i += 1
    elif option == 5:
        #Creating the new brand of the car
        car = Car()
        car.brand = input("Unesite marku: ")
        car.add_brand()
    elif option == 6:
        #creating the new model of the car
        i = 1
        car = Car()
        #Getting the brand of the car from DB
        print("Unesite brend automobila iz liste: ")
        for key in car.get_brand():
            print(f"{i}. {key[0]}")
            i += 1
        #Creating the new model of the car
        newModel = input("Unestite novi model u formatu: brend, model, godina.\n")
        car.brand = newModel.split(",")[0]
        car.model = newModel.split(",")[1].strip()
        car.year = int(newModel.split(",")[2])
        car.add_model()
    elif option == 7:
        #Renting the car
        i = 1
        showUsers = User()
        USER_ID = {}
        todays_date = date.today()
        #Showing the users from DB
        for user in showUsers.showUsers():
            #Showing only the users that have not rented a car yet
            if user[1] == None:
                print(f"{i}. {user[2]} {user[3]} {user[4]}")
                USER_ID[i] =[user[0]]
                i += 1
        #Choosing the user by the ID
        userID = inpt = int(input("Unesite ID korisnika iz liste: "))
        #Choosing the car by the brand and model
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
        #Converting the date to the format that is accepted by the DB
        pydate = date(int(datum[2]), int(datum[1]), int(datum[0]))
        #Checking if the date is not in the past
        if todays_date > pydate:
            raise ValueError("Datum ne moze biti manji od danas")
        #Creating the rental record
        car.rent_car(CAR_ID[carID], pydate)
        #Adding the car to the user
        showUsers.addCar(CAR_ID[carID], USER_ID[userID])





    option = input("Da li ste zavrsili (y/n): \n")
    if option == "n" or option == "N":
        option = None
