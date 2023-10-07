class SchoolClass:
    def __init__(self, class_name, homeroom_teacher):
        self.class_name = class_name
        self.homeroom_teacher = homeroom_teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return self.class_name

    def manage_class(self):
        class_name = input("Please enter the class name you wish to check (e.g., 3C): ")

        # Check if the class_name exists in the students
        if class_name in self.user["students"]:
            print(f"Students in class {class_name}:")
            for student in self.user["students"][class_name]:
                print(f"Student name: {student['first_name']} {student['last_name']}")

        # Check if the class_name exists in the homeroom_teacher
        if class_name in self.user["homeroom_teacher"]:
            homeroom_teacher = self.user["homeroom_teacher"][class_name]
            print(f"Homeroom Teacher: {homeroom_teacher['first_name']} {homeroom_teacher['last_name']}")
        else:
            print(f"Class {class_name} not found")
