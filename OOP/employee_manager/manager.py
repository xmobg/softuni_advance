from employee import Employee


class Manager(Employee):
    def __init__(self,name,employee_id,base_salary,social_security_number,department,bonus_percentage,department_budget):
        super().__init__(name,employee_id,base_salary,social_security_number,department)
        self.bonus_percentage = bonus_percentage
        self.department_budget = department_budget
        self.team_members = list()

    def calculate_salary(self):
        return self.base_salary + (self.base_salary * self.bonus_percentage / 100)

    def add_team_member(self,employee):
        if employee not in self.team_members:
            self.team_members.append(employee)
        else:
            raise ValueError("Team member already exists")

    def team_size(self):
        return len(self.team_members)


    def give_bonus_to_team(self,amount):
        for employee in self.team_members:
            employee.base_salary += amount

    def can_afford(self, expense):
        return self.department_budget >= expense