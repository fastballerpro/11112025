import pytest
from app.oop.models import Book, Library


@pytest.fixture
def library():
    return Library("City Library")


@pytest.fixture
def book1():
    return Book("Taras Shevchenko", "Kobzar")


@pytest.fixture
def book2():
    return Book("Lesya Ukrainka", "Forest Song")



class TestBook:

    def test_create_book(self, book1):
        assert book1.author == "Taras Shevchenko"
        assert book1.title == "Kobzar"
        assert isinstance(book1.uid, str)


class TestLibrary:

    def test_library_creation(self, library):
        assert library.name == "City Library"
        assert library.books == []

    def test_add_book(self, library, book1):
        library.add_book(book1)

        assert len(library.books) == 1
        assert library.books[0] == book1

    def test_add_two_books(self, library, book1, book2):
        library.add_book(book1)
        library.add_book(book2)

        assert len(library.books) == 2

    def test_remove_book(self, library, book1):
        library.add_book(book1)
        library.remove_book(book1.uid)

        assert book1 not in library.books

    def test_remove_not_existing_book(self, library):
        library.remove_book("fake-id")

        assert library.books == []

    def test_show_books_empty(self, library):
        library.show_books()
        assert True

    def test_show_books_with_books(self, library, book1):
        library.add_book(book1)
        library.show_books()
        assert len(library.books) == 1
