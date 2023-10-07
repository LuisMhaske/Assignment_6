"""
Program for School Management, to manage student, teacher and homeroom teacher.

Program should start with following options:
1. Create
2. Manage
3. End

4. Create

"""


class SchoolManagementSystem:
    def __init__(self):
        self.user = {
            "students": [],
            "teacher": [],
            "homeroom_teacher": []
        }
        self.classes = {}

    def create_student(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        class_name = input("Enter the class name (e.g., '3C'): ")
        subject_taken = []
        while True:
            subject_name = input("Enter the name of classes/subject they take (or press Enter to finish): ")
            if not subject_name:
                break  # Break the loop when the user presses Enter (empty string)
            subject_taken.append(subject_name)
        student = {"first_name": first_name, "last_name": last_name, "class": class_name,
                   "subject_taken": subject_taken}

        self.user["students"].append(student)

    def create_teacher(self):
        first_name = input("Enter Teacher's first name: ")
        last_name = input("Enter Teacher's first name: ")
        subject = input("Enter the subject they taught: ")
        classes_taught = []
        while True:
            class_name = input("Enter the name of classes/subject they take (or press Enter to finish): ")
            if not class_name:
                break  # Break the loop when user presses Enter (empty string)
            classes_taught.append(class_name)
        teacher = {"first_name": first_name, "last_name": last_name, "subject": subject,
                   "classes_taught": classes_taught}
        self.user["teacher"].append(teacher)

    def create_homeroom_teacher(self):
        first_name = input("Enter Teacher's first name: ")
        last_name = input("Enter Teacher's first name: ")
        class_name = input("Enter the class led: ")
        if class_name not in self.user["homeroom_teacher"]:
            self.user["homeroom_teacher"][class_name] = {"first_name": None, "last_name": None}

        homeroom = {"first_name": first_name, "last_name": last_name, "class_name": class_name}
        self.user["homeroom_teacher"].append(homeroom)

    def manage_class(self):
        class_name = input("Please enter the class name you wish to check(e.g. 3C): ")
        if class_name in self.classes:
            print(f"Student in class {class_name}:")
            for student in self.classes[class_name]["student"]:
                print(f"Student name: {student['first_name']} {student['last_name']}")


    def run(self):
        print("\n Main Menu:\n 1. Create\n 2. Manage\n 3. End\n")
        option = input("Select one option: ")
        while True:
            if option == "3":
                print("Thank you!! see you soon")
                break
            elif option == "1":
                self.create_user_menu()
            elif option == "2":
                self.manage_menu()
                print("Manage module")
            else:
                print("Invalid option selected")

    def create_user_menu(self):
        create_in = input("\nEnter 1 for Student entry \n 2 for Teacher entry\n 3 for Homeroom Teacher\n 4 to End.")
        while True:
            if create_in == "4":
                print("Returning to main menu...")
                break
            elif create_in == "1":
                self.create_student()
                continue
            elif create_in == "2":
                self.create_teacher()
                continue
            elif create_in == "3":
                self.create_homeroom_teacher()
                continue
            else:
                print("Invalid option selected.")

    def manage_menu(self):
        manage_in = input("\n Enter 1 for Class\n 2 for Student\n 3 for Teacher\n 4 for Homeroom\n 5 for main menu:")
        while True:
            if manage_in == "5":
                print("Returning to main menu...")
                break
            elif manage_in == "1":
                print("Manage class")
                continue
            elif manage_in == "2":
                print("Manage student")
                continue
            elif manage_in == "3":
                print("Manage teacher")
                continue
            elif manage_in == "4":
                print("Manage homeroom")
                continue
            else:
                print("Invalid option selected")

__name__ == "main"
SchoolManagement = SchoolManagementSystem()
SchoolManagement.run()