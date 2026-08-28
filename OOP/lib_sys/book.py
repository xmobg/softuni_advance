class Book:
    def __init__(self,title,author,isbn,price,publisher):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.publisher = publisher

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self._price = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if len(value.strip()) == 0:
            raise ValueError('Title cannot be empty')
        self._title = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self,value):
        if  10 ==  len(value.strip()) or len(value.strip()) == 13 :
            self._isbn = value
        else:
            raise ValueError('ISBN must be 10 or 13 characters')

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Publisher: {self.publisher}"
