from main_companies import companies_controller
from main_people import people_controller


def main():
    main_controller = input("Would you like to manage\n1. 🏢 companies or \n2. 👨 people?\nInsert number: ")

    if main_controller == "1":
        companies_controller()
        main()

    if main_controller == "2":
        people_controller()
        main()

    main()


main()
