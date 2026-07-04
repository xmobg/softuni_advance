from project.product import Product


class Drink(Product):
    def __init__(self, name):
        Product.__init__(self, name,10)
        