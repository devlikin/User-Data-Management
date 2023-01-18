class Person:
    def __init__ (self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Solution:
    def NameProc(self):

        open("lista de nume.txt", "a")
        file= open("lista de nume.txt", "r")

        names_string = file.read()
        people_lst = names_string.split("\n")
        user_ctrl = 0

        while user_ctrl != 5:

            print("\n\nPlease press number to chose one of the following options:\n1. ➕ Add Personal Details\n2. ❌ Delete Name\n3. 📄 List Names\n4. 🔎 Search Name\n5. 🔴 Exit Program")

            try:
                user_ctrl = int(input())

                if user_ctrl == 1:
                    add_person_function(people_lst)

                if user_ctrl == 2:
                    delete_person_function(people_lst)

                if user_ctrl == 3:
                    list_person_function(people_lst)

                if user_ctrl == 4:
                    search_person_function(people_lst)

                if user_ctrl != 1 and user_ctrl != 2 and user_ctrl != 3 and user_ctrl != 4 and user_ctrl != 5:
                    print("The choice you have entered is invalid.")

            except:
                print("Invalid option")

        if user_ctrl == 5:
            print("Good bye!")



def add_person_function(people_lst):


    Person.name = input("\nPlease enter name:")

    

def delete_person_function(people_lst):

    print("Please enter the number corresponding to which name you would like to delete:\n")
    for name_index in range(1, len(people_lst[1::]) + 1):
        print(name_index, people_lst[name_index])

    name_to_del_index = input()

    people_lst.pop(int(name_to_del_index))
    names_string = "\n".join(people_lst)
    print(names_string)
    print("nl", people_lst)

    with open("lista de nume.txt", "w") as file:
        file.write(names_string)



def list_person_function(people_lst):



    print("\nThe names are:")
    names_string = "\n".join(people_lst)
    print(names_string)



def search_person_function(people_lst):

    search_query = (input("Please enter a search query:"))
    for search_index in people_lst:
        if search_query in search_index:
            print(people_lst.index(search_index), search_index, "found!")



Solution().NameProc()