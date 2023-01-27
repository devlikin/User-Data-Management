from company import Company


def load_file(list):
    print("loading...")
    file = open("companies.txt", "r")
    string = file.read()

    print(string)
    string_list = ""
    string_list = string.split("\n")
    print(string_list)

    company_string = ""
    entry_list = []
    list = []

    for company_string in string_list:
        entry_list = company_string.split(",")

        name = entry_list[0]
        slogan = entry_list[1]

        print("nas", name, slogan)

        list.append(Company(name, slogan))

    print("list", list)
    return list


def save_file(list):
    string = ""

    for company in list:
        string = string + company.name + ","
        string = string + company.slogan + "\n"
    string = string[:-1]

    file = open("companies.txt", "w")
    file.write(string)
    return list


def companies_controller():
    list = []
    list = load_file(list)

    user_controller = "0"

    while user_controller != "6":
        user_controller = input(
            "\n\nPlease press number to chose one of the following options:\n1. ➕ Add company\n2. ❌ Delete company\n3. 📄 List company\n4. 🔎 Search for company\n5. 💒 Update company\n6. 🔴 Save and exit Program\n")

        if user_controller == "1": get_company(list)
        if user_controller == "2": delete_company(list)
        if user_controller == "3": print_company(list)
        if user_controller == "4": search_company(list)
        if user_controller == "5": update_company(list)

    save_file(list)
    print("Goodbye!")


def get_company(list):
    name = input("Enter name: ")
    if len(name) < 3:
        print("name too short!")
        input("press enter to continue")
        return

    slogan = input("Enter slogan: ")
    list.append(Company(name, slogan))
    save_file(list)
    return list


def print_company(list):
    if len(list) == 0:
        print("No entry found. List is empty!")
    else:
        for company in list:
            print(company.name, company.slogan)

    input("press enter to continue...")
    return (list)


def delete_company(list):
    index = 1
    for company in list:
        print(index, company.name, company.slogan)
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


def search_company(list):
    user_controller = "0"
    user_controller = input("Search for company by:\n1.Name\n2.Slogan\nPlease press the corresponding number: ")

    if user_controller == "1":
        query = input("Who are you looking for: ")
        for company in list:
            if query in company.name:
                print(company.name, "found!")

    if user_controller == "2":
        query = input("company of what slogan are you looking for: ")
        for company in list:
            if query in company.slogan:
                print(company.name, company.slogan, "found!")
    return list


def update_company(list):
    index = 1
    for company in list:
        print(index, company.name, company.slogan)
        index += 1

    company_index = int(input("Which company would you like to update? "))
    company_index -= 1

    attribute_index = input("Which attribute would you like to update? 1. Name 2.  3.slogan?")

    if attribute_index == "1":

        name = input("Enter name: ")
        if len(name) < 3:
            print("name too short!")
            input("press enter to continue")
            return
        else:
            list[company_index].name = name

    if attribute_index == "2":
        slogan = input("Enter slogan: ")
        list[company_index].slogan = slogan
    return list
