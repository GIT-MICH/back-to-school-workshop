import csv

class Student:
    def __init__(self, name, surname, class_name, year_of_birth, grade_average):
        self.name = name
        self.surname = surname
        self.class_name = class_name
        self.year_of_birth = year_of_birth
        self.grade_average = float(grade_average)

    def __str__(self):
        return f"""
        UCZEŃ --> 
        imię: {self.name}, 
        nazwisko: {self.surname}, 
        klasa: {self.class_name},
        średnia: {self.grade_average}"""

    @classmethod
    def from_file(cls, file, class_school=None):
        with open(file) as students_file:
            students = []
            for row in csv.reader(students_file):
                if class_school is None or class_school == row[2]:
                    students.append(cls(row[0], row[1], row[2], int(row[3]), float(row[4])))
                else:
                    print(f"Student name {row[1]} isn't in class {class_school}")
        return students


george = Student('George', 'Swim', '1A', 2000, 4.2)
print(george)
john = Student('John', 'Colt', '5B', 1999, 3.8)
print(john)
print(30*'-')

students = Student.from_file("students.csv", None)
for student in students:
    print(student)
