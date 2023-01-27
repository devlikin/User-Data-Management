from person import Person


def load_file(list):
    print("loading...")
    file = open("people.txt", "r")
    string = file.read()

    print(string)
    string_list = ""
    string_list = string.split("\n")
    print(string_list)

    person_string = ""
    list = []

    for person_string in string_list:
        entry_list = person_string.split(",")

        name = entry_list[0]
        age = int(entry_list[1])
        sex = entry_list[2]

        print("nas", name, age, sex)

        list.append(Person(name, age, sex))

    print("list", list)

    print("creating file")
    open("people.txt", "w")
    return list


def save_file(list):
    string = ""

    for person in list:
        string = string + person.name + ","
        string = string + str(person.age) + ","
        string = string + person.sex + "\n"
    string = string[:-1]

    file = open("people.txt", "w")
    file.write(string)
    return list


def people_controller():
    list = []
    list = load_file(list)

    user_controller = "0"

    while user_controller != "6":
        user_controller = input(
            "\n\nPlease press number to chose one of the following options:\n1. ➕ Add person\n2. ❌ Delete person\n3. 📄 List person\n4. 🔎 Search for person\n5. 👩➡👨‍ Update person\n6. 🔴 Save and exit Program\n")

        if user_controller == "1": get_person(list)
        if user_controller == "2": delete_person(list)
        if user_controller == "3": print_person(list)
        if user_controller == "4": search_person(list)
        if user_controller == "5": update_person(list)

    save_file(list)
    print("Goodbye!")


def get_person(list):
    name = input("Enter name: ")
    if len(name) < 3:
        print("name too short!")
        input("press enter to continue")
        return

    age = int(input("Enter age: "))

    if (age < 0) or (age > 130):
        print("invalid age!")
        input("press enter to continue")
        return

    sex = input("Enter sex: ")

    if (sex != "male") and (sex != "female"):
        print("invalid sex!")
        input("press enter to continue")
        return

    list.append(Person(name, age, sex))
    save_file(list)
    return list


def print_person(list):
    if len(list) == 0:
        print("No entry found. List is empty!")
    else:
        for person in list:
            print(person.name, person.age, person.sex)

    input("press enter to continue...")
    return (list)


def delete_person(list):
    index = 1
    for person in list:
        print(index, person.name, person.age, person.sex)
        index += 1

    del_index = int(input("Which index number would you like to delete?: "))

    if (del_index <= len(list)) and (del_index > 0):
        list.pop(int(del_index) - 1)
        save_file(list)
    else:
        print("invalid index!")
        input("press enter to continue")
        return
    return list


def search_person(list):
    user_controller = "0"
    user_controller = input("Search for person by:\n1.Name\n2.Age\n3.Sex\nPlease press the corresponding number: ")

    if user_controller == "1":
        query = input("Who are you looking for: ")
        for person in list:
            if query in person.name:
                print(person.name, "found!")

    if user_controller == "2":
        query = input("Person of what age are you looking for: ")
        for person in list:
            if query in str(person.age):
                print(person.name, person.age, "found!")

    if user_controller == "3":
        query = input("Person of what sex are you looking for: ")
        for person in list:
            if query == person.sex:
                print(person.name, person.sex, "found!")
    return list


def update_person(list):
    index = 1
    for person in list:
        print(index, person.name, person.age, person.sex)
        index += 1

    person_index = int(input("Which person would you like to update? "))
    person_index -= 1

    attribute_index = input("Which attribute would you like to update? 1. Name 2. Age 3.Sex?")

    if attribute_index == "1":

        name = input("Enter name: ")
        if len(name) < 3:
            print("name too short!")
            input("press enter to continue")
            return
        else:
            list[person_index].name = name

    if attribute_index == "2":

        age = int(input("Enter age: "))

        if (age < 0) or (age > 130):
            print("invalid age!")
            input("press enter to continue")
            people_controller()
        else:
            list[person_index].age = age

    if attribute_index == "3":

        sex = input("Enter sex: ")

        if (sex != "male") and (sex != "female"):
            print("invalid sex!")
            input("press enter to continue")
            people_controller()
        else:
            list[person_index].sex = sex

    return list
