import uuid


class Book:
    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title
        self.uid = str(uuid.uuid4()) 

    def __str__(self):
        return f"'{self.title}' by {self.author} (ID: {self.uid})"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, uid: str):
        for book in self.books:
            if book.uid == uid:
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print(f"Book with ID {uid} not found")

    def show_books(self):
        if not self.books:
            print("There are no books in the library.")
        else:
            print(f"Books in the library '{self.name}':")
            for book in self.books:
                print(book)
