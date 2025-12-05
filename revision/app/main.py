from oop.models import Book, Library


def main():

    library = Library("City Library")

    book1 = Book("Taras Shevchenko", "Kobzar")
    book2 = Book("Lesya Ukrainka", "Forest Song")

    library.add_book(book1)
    library.add_book(book2)

    library.show_books()

    library.remove_book(book1.uid)

    library.show_books()


if __name__ == "__main__":
    main()
