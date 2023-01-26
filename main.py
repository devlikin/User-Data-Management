from main_companies import companies_controller
from main_people import people_controller


def main():
    main_controller = "0"

    while main_controller != 3:

        main_controller = input("Would you like to manage\n1. 🏢 companies or \n2. 👨 people?\n3.Exit \nInsert number: ")

        if main_controller == "1":
            companies_controller()

        if main_controller == "2":
            people_controller()


main()
