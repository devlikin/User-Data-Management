import numpy as np


class Person:
    list = []

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @classmethod
    def load_file(cls):
        try:
            cls.list = list(np.load("people.npy"))
            print(cls.list)
        except:
            cls.list = []
            print("No file found, creating new list.")

    @classmethod
    def save_file(cls):
        np.save("people.npy", cls.list)

    @classmethod
    def controller(cls):
        user_controller = "0"

        while user_controller != "5":
            user_controller = input(
                "\n\nPlease press number to chose one of the following options:\n1. ➕ Add person\n2. ❌ Delete person\n3. 📄 List person\n4. 🔎 Search for person\n5. 🔴 Save and exit Program\n")

            if user_controller == "1": cls.get_person()
            if user_controller == "2": cls.delete_person()
            if user_controller == "3": cls.print_person()
            if user_controller == "4": cls.search_person()

        print("Goodbye!")

    @classmethod
    def get_person(cls):
        name = input("Enter name: ")
        age = input("Enter age: ")
        sex = input("Enter sex: ")
        cls.list.append([name, age, sex])

    @classmethod
    def print_person(cls):
        i = 1
        for sublist in cls.list:
            string = " ".join(sublist)
            print(i, string)
            i += 1

    @classmethod
    def delete_person(cls):
        cls.print_person()
        del_index = input("Which index number would you like to delete?:")
        cls.list.pop(int(del_index) - 1)

    @classmethod
    def search_person(cls):
        query = input("Who are you looking for:")
        for array in cls.list:
            for entry in array:
                if query in entry:
                    print("Found:", array)


Person.load_file()
Person.controller()
Person.save_file()
