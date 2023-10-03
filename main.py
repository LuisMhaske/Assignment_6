"""
Program for School Management, to manage student, teacher and homeroom teacher.

Program should start with following options:
1. Create
2. Manage
3. End

4. Create

"""
school = {}

class Student:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

while True:
    action = input("Enter 1 to Create\n 2 to Manage\n 3 to End: ")
    if action == "1":
        create_in = input("Enter 1 for Student entry \n 2 for Teacher entry\n 3 for Homeroom Teacher\n 4 to End.")
        if create_in == "4":
            print("Returning to main menu...")
            break
        elif create_in == "1":
            print("Create Student")
            continue
        elif create_in == "2":
            print("Create Teacher")
            continue
        elif create_in == "3":
            print("Create Homeroom Teacher")
            continue
