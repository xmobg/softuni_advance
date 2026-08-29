from employee import Employee


class Intern(Employee):
    def __init__(self,name,employee_id,base_salary,social_security_number,department,mentor,stipend_duration_months):
        super().__init__(name,employee_id,base_salary,social_security_number,department)
        self.mentor = mentor
        self.stipend_duration_months = stipend_duration_months

    def calculate_salary(self):
        return self.base_salary * 0.5