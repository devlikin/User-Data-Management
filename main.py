class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_user_info(self):
        self.name = input("Enter name:")
        self.age = input("Enter age:")
        self.sex = input("Enter sex:")

    def write_user_info(self):
        self.append([self.name, self.age,self.sex])

