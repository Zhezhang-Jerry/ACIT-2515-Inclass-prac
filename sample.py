class Point:
    def __init__(self, x, y):
        print("I am creating a Point object")
        self.x = 0
        self.y = 0

    def print(self):
        print("I am Point", self.x, self.y)

class Student:
    def __init__(self, name, student_number):
        self._name = name
        self.student_number = "A" + student_number
        self.grades = list()

    @property
    def name(self):
        return self._name

    def add_grade(self, grade):
        self.grades.append(grade)

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise UserWarning("Name cannot be empty")

        self._name = new_name

    def gpa(self):
        return sum(self.grades)/len(self.grades)

    def print(self):
        print("I am student", self._name, "with number", self.student_number)
        print("GPA", self.gpa())
