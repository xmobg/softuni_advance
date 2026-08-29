from employee import Employee

class Developer(Employee):
    def __init__(self,programing_language,year_of_experience,name,employee_id,base_salary,social_security_number,department):
        super().__init__(name,employee_id,base_salary,social_security_number,department)
        self.programing_language = programing_language
        self.year_of_experience = year_of_experience


    def calculate_salary(self):
        return self.base_salary + (self.year_of_experience * 200)