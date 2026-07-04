class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def remove(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return product
        return None

    def __repr__(self):
        lines = []
        for product in self.products:
            lines.append(f'{product.name}: {product.quantity}')
        return '\n'.join(lines)