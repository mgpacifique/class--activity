from deescript import Book, User, Borrow, BorrowLibrary


def run_tests():
    user = User(1, "Alice", 23)
    book = Book(10, "1984", "George Orwell", 1949, False)

    borrow = Borrow(user, book, "2026-05-11")

    assert borrow.userId == 1
    assert borrow.bookId == 10
    assert borrow.name == "Alice"
    assert borrow.title == "1984"
    assert borrow.isBorrowed is True
    assert borrow.broughtBack is False

    borrow.mark_returned()

    assert borrow.broughtBack is True
    assert borrow.isBorrowed is False

    print("All tests passed.")


def demo_display():
    # Create a library
    library = BorrowLibrary()

    # Add some borrow records
    user1 = User(1, "Alice", 23)
    book1 = Book(10, "1984", "George Orwell", 1949, False)
    borrow1 = Borrow(user1, book1, "2026-05-11")
    library.add_record(borrow1)

    user2 = User(2, "Bob", 30)
    book2 = Book(20, "To Kill a Mockingbird", "Harper Lee", 1960, False)
    borrow2 = Borrow(user2, book2, "2026-05-10")
    borrow2.mark_returned()  # This one is returned
    library.add_record(borrow2)

    user3 = User(3, "Charlie", 25)
    book3 = Book(30, "The Great Gatsby", "F. Scott Fitzgerald", 1925, False)
    borrow3 = Borrow(user3, book3, "2026-05-09")
    library.add_record(borrow3)

    # Display all records
    library.display_all()

    # Display only active (not returned) records
    library.display_active()


if __name__ == "__main__":
    run_tests()
    print("\n" + "="*50)
    print("DEMO: Displaying Borrow Records")
    print("="*50)
    demo_display()

