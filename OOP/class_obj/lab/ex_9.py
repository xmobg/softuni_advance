class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self,grade):
        if 2 <= grade <= 6:
            self.grades.append(grade)
            return f"Grade {grade} added"
        return "Invalid grade"

    def average(self):
        if len(self.grades) == 0:
            return "No grades yet"
        return f"{sum(self.grades)/len(self.grades):.2f}"

    def is_passing(self):
        if not self.grades:
            return False
        return sum(self.grades) / len(self.grades) >= 3

    def __str__(self):
        return f"Student {self.name}, age {self.age}, average grade: {self.average()}"


s = Student("Иван", 18)
print(s.add_grade(5))    # Grade 5 added
print(s.add_grade(3))    # Grade 3 added
print(s.add_grade(7))    # Invalid grade
print(s.average())       # 4.0
print(s.is_passing())    # True
print(s)                 # Student Иван, age 18, average grade: 4.0