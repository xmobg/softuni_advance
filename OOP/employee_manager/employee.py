from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,name,employee_id,base_salary,social_security_number,department):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.social_security_number = social_security_number
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.name} {self.department} {self.employee_id}"
