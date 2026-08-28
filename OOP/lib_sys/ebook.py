from book import Book


class Ebook(Book):
    def __init__(self,title,author,isbn,price,publisher,file_size_mb):
        super().__init__(title,author,isbn,price,publisher)
        self.file_size_mb = file_size_mb



    def __str__(self):
        return f"{super().__str__()} {self.file_size_mb} MB"


