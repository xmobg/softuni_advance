class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    def average_grade(self):
        return round(sum(self.grades)/len(self.grades), 2)

    def is_passing(self):
        return self.average_grade() >= 3

student = Student("Ivan", 18, [5, 4, 3, 6, 5])
print(student.average_grade())  # 4.6
print(student.is_passing())     # True