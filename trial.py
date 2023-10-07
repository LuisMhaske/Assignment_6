class SchoolClass:
    def __init__(self, class_name, homeroom_teacher):
        self.class_name = class_name
        self.homeroom_teacher = homeroom_teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return self.class_name