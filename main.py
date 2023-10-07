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
            subject_taken.append(subject_name)  # Append the subject_name to the list

        student = {"first_name": first_name, "last_name": last_name, "class_name": class_name,
                   "subject_taken": subject_taken}

        self.user["students"].append(student)

    def create_teacher(self):
        first_name = input("Enter Teacher's first name: ")
        last_name = input("Enter Teacher's last name: ")
        subject_taught = input("Enter the subject they taught: ")
        classes_taught = []
        while True:
            class_name = input("Enter the name of classes they teach (or press Enter to finish): ")
            if not class_name:
                break  # Break the loop when user presses Enter (empty string)
            classes_taught.append(class_name)
        teacher = {"first_name": first_name, "last_name": last_name, "subject_taught": subject_taught,
                   "classes_taught": classes_taught}
        self.user["teacher"].append(teacher)
        print(teacher)

    def create_homeroom_teacher(self):
        first_name = input("Enter Teacher's first name: ")
        last_name = input("Enter Teacher's last name: ")
        class_led = input("Enter the class led: ")

        homeroom = {"first_name": first_name, "last_name": last_name, "class_led": class_led}
        self.user["homeroom_teacher"].append(homeroom)

    def manage_class(self):
        class_name = input("Please enter the class name you wish to check (e.g., 2C): ")
        # Check if the class_name exists in the students
        student_in_class = []
        for student in self.user["students"]:
            if student["class_name"] == class_name:
                student_in_class.append(student)
        if student_in_class:
            print(f"Students in class {class_name}:")
            for student in student_in_class:
                print(f"Student name: {student['first_name']} {student['last_name']}")
        # Check if the class_name exists in the homeroom_teacher
        homeroom_teacher = None
        for teacher in self.user["homeroom_teacher"]:
            if teacher["class_led"] == class_name:
                homeroom_teacher = teacher
                break
        if homeroom_teacher:
            print(f"Homeroom Teacher: {homeroom_teacher['first_name']} {homeroom_teacher['last_name']}")
        else:
            print(f"Class {class_name} not found")

    def manage_student(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        for student in self.user["students"]:
            if student["first_name"] == first_name and student["last_name"] == last_name:
                print(f"\n{first_name} {last_name} is in the following classes: ")
                for subject_taken in student["subject_taken"]:
                    print(f"{subject_taken} ")

                    print("Teacher: ")
                    subject_teacher = None
                    for teacher in self.user["teacher"]:
                        if subject_taken in teacher["subject_taught"]:
                            subject_teacher = teacher
                            print(
                                f" {subject_teacher['first_name']} {subject_teacher['last_name']} is the teacher for "
                                f"{subject_taken}")
                            break
                    if not subject_teacher:
                        print("Teacher not found!!!")
                break
        else:
            print("Student not found!!!")

    def manage_teacher(self):
        first_name = input("Enter Teacher's first name: ")
        last_name = input("Enter Teacher's last name: ")

        teacher_found = False

        for teacher in self.user["teacher"]:
            if teacher["first_name"] == first_name and teacher["last_name"] == last_name:
                print(f"\n{first_name} {last_name} teaches the following subjects:{teacher['subject_taught']} ")
                # for subject in teacher["subject_taught"]:
                #     print(subject)

                print(f"Classes they teach:{teacher['classes_taught']} ")
                # for taught_class in teacher["classes_taught"]:
                #     print(taught_class)

                teacher_found = True
                break

        if not teacher_found:
            print("Teacher not found!!!")

    def manage_homeroom_teacher(self):
        first_name = input("Enter Teacher's first name: ")
        last_name = input("Enter Teacher's last name: ")
        for teacher in self.user["homeroom_teacher"]:
            if teacher["first_name"] == first_name and teacher["last_name"] == last_name:
                print(f"\n{first_name} {last_name} leads the following class: ")
                led_class = teacher["class_led"]
                print(f"{led_class}")
                for student in self.user["students"]:
                    if led_class in student["class_name"]:
                        print(f"\nStudents in {led_class}:\n {student}")
                break
        else:
            print("Homeroom Teacher not found!!!")

    def run(self):

        while True:
            print("\n Main Menu:\n 1. Create\n 2. Manage\n 3. End\n")
            option = input("Select one option: ")
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
        while True:
            print(60 * "-")
            create_in = input("\nUser Creation Menu: \n1. Student\n2. Teacher entry\n"
                              "3. Homeroom Teacher\n4. End: ")
            if create_in == "4":
                print("Returning to main menu...")
                print(60 * "-")
                break
            elif create_in == "1":
                self.create_student()
            elif create_in == "2":
                self.create_teacher()
            elif create_in == "3":
                self.create_homeroom_teacher()
            else:
                print("Invalid option selected.")

    def manage_menu(self):
        print(60 * "-")

        while True:
            manage_in = input("\nManagement Menu:\n 1. Class\n 2. Student\n "
                              "3. Teacher\n 4. Homeroom\n 5. main menu:")
            if manage_in == "5":
                print("Returning to main menu...")
                print(60 * "-")
                break
            elif manage_in == "1":
                self.manage_class()
            elif manage_in == "2":
                self.manage_student()
            elif manage_in == "3":
                self.manage_teacher()
            elif manage_in == "4":
                self.manage_homeroom_teacher()
            else:
                print("Invalid option selected")


if __name__ == "__main__":
    SchoolManagement = SchoolManagementSystem()
    SchoolManagement.run()
