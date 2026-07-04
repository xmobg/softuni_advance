from project.person import Person
from project.employee import Employee



class Teacher(Person, ):
    def teach(self):
        return "teaching..."
