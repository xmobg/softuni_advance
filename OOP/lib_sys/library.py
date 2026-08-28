class Library:
    def __init__(self):
        self.books = {}


    def add_book(self,book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
        else:
            raise ValueError(f"Book with ISBN {book.isbn} already exists")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
        else:
            raise ValueError(f"Book with ISBN {isbn} does not exist")

    def find_book(self,isbn):
        if isbn in self.books:
            return self.books[isbn]
        else:
            raise ValueError(f"Book with ISBN {isbn} does not exist")

    def list_all_books(self):
            for book in self.books.values():
                print(f"-{book}-")

    def find_book_by_author(self, author):
        matching_book = []
        for book in self.books.values():
            if book.author == author:
                matching_book.append(book)
        if not matching_book:
            raise ValueError(f"Author {author} does not exist")
        return matching_book