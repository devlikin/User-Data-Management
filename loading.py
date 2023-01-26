from person import person


def load_file():
    try:
        print("loading...")
        file = open("test.txt", "r")
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

            list.append(person(name, age, sex))

        print("list", list)
    except:
        open("test.txt", "w")


load_file()
