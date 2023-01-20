list = []


class Person:

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex


def load_file():
    file = open("people.txt", "r")
    string = file.read()

    print(string)
    string_list = ""
    string_list = string.split("\n")
    print(string_list)

    person_string = ""
    entry_list = []

    for person_string in string_list:
        entry_list = person_string.split(",")

        name = entry_list[0]
        age = int(entry_list[1])
        sex = entry_list[2]

        print("nas", name, age, sex)

        list.append(Person(name, age, sex))

    print("list", list)


def save_file():
    string = ""

    for Person in list:
        string = string + Person.name + ","
        string = string + str(Person.age) + ","
        string = string + Person.sex + "\n"
    string = string[:-1]

    file = open("people.txt", "w")
    file.write(string)


def controller():
    user_controller = "0"

    while user_controller != "5":
        user_controller = input(
            "\n\nPlease press number to chose one of the following options:\n1. ➕ Add person\n2. ❌ Delete person\n3. 📄 List person\n4. 🔎 Search for person\n5. 🔴 Save and exit Program\n")

        if user_controller == "1": get_person()
        if user_controller == "2": delete_person()
        if user_controller == "3": print_person()
        if user_controller == "4": search_person()

    print("Goodbye!")


def get_person():
    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
    except:
        print("error! age probably not digits")

    sex = input("Enter sex: ")
    list.append(Person(name, age, sex))


def print_person():
    for Person in list:
        print(Person.name, Person.age, Person.sex)


def delete_person():
    index = 1
    for Person in list:
        print(index, Person.name, Person.age, Person.sex)
        index += 1

    del_index = input("Which index number would you like to delete?:")
    list.pop(int(del_index) - 1)


def search_person():
    query = input("Who are you looking for:")
    for Person in list:
        if query in Person.name:
            print(Person.name, "found!")


load_file()
controller()
save_file()
