class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return f"{book} was added"
        return f"{book} is already in the library"

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"{book} was removed"
        return f"{book} is not in the library"

    def __str__(self):
        return f"Library {self.name} has {len(self.books)} books"

