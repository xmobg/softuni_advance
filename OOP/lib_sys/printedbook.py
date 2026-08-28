from book import Book


class PrintedBook(Book):
    def __init__(self,title,author,isbn,price,publisher,cover_type):
        super().__init__(title,author,isbn,price,publisher)
        self.cover_type = cover_type


    def __str__(self):
        return f"{super().__str__()} {self.cover_type}"