from Models.Car import Car
from Models.User import User

option = None

while option is None:
    print(
        "Opcije: "
        "\n1. Dodaj korisnika "
        "\n2. Prikazi korisnike "
        "\n3. Prikazi raspoloziva vozila "
        "\n4. Prikazi rentirana vozila")

    availble_options = [1, 2, 3, 4]

    option = int(input("Odaberite opciju: \n"))

    if option not in availble_options:
        raise ValueError("Neispravna opcija")

    if option == 1:
        newUser = User()

        newUser.name = input("Unesite ime i prezime: ")
        newUser.age = int(input("Unesite godine: "))
        newUser.create()
    elif option == 2:
        print(User.ALL_USERS)
    elif option == 3 or option == 4:
        for car in Car.VALID_CARS:
            for model in Car.VALID_CARS[car]:
                if not model['rented'] and option == 3:
                    print(model)
                elif model['rented'] and option == 4:
                    print(model)

    option = input("Da li ste zavrsili (y/n): \n")
    if option == "n" or option == "N":
        option = None
