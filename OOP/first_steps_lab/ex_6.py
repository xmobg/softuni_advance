# Създай клас Dog който приема name и breed (порода)
# Да има метод bark() който връща "Woof! My name is {name}!"
class Dog:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"Woof! My name is {self.name}"
dog = Dog("Rex", "Labrador")
print(dog.bark())  # Woof! My name is Rex!