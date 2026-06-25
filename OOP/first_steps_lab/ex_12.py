class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def is_square(self):
        return self.width  == self.height


rect = Rectangle(4, 6)
print(rect.area())       # 24
print(rect.perimeter())  # 20
print(rect.is_square())  # False