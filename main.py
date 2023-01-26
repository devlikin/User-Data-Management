def main():
    main_controller = input("Would you like to manage\n1. 🏢 companies or \n2. 👨 people?\nInsert number: ")

    if main_controller == "1":
        from main_companies import controller

        controller()
        main()

    if main_controller == "2":
        from main_people import controller

        controller()
        main()


main()
