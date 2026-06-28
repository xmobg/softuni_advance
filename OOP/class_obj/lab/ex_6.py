class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def age (self):
        return 2026 - self.year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def is_vintage(self):
        if self.age() >= 30:
            return True
        return False

car = Car("BMW", "E30", 1987)
print(car)              # BMW E30 (1987)
print(car.age())        # 39
print(car.is_vintage())