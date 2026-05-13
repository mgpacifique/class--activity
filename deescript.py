# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:29:16 2026

@author: ovouz
"""

# defining the class user
class Book:
    def __init__ (self, id, title, author, year, isBorrowed):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.isBorrowed = bool(isBorrowed)
        
# defining the class user 
class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

# defining the borrow logic
class Borrow(User, Book):
    def __init__(self, user, book, date, broughtBack=False):

        # Keep user and book state through inherited base classes.
        User.__init__(self, user.id, user.name, user.age)
        Book.__init__(self, book.id, book.title, book.author, book.year, True)

        self.userId = user.id
        self.bookId = book.id
        self.date = date
        self.broughtBack = bool(broughtBack)

    def mark_returned(self):
        self.broughtBack = True
        self.isBorrowed = False

    def get_info(self):
        # returning the asserted values.
        return {
            "user_id": self.userId,
            "user_name": self.name,
            "book_id": self.bookId,
            "book_title": self.title,
            "author": self.author,
            "borrow_date": self.date,
            "brought_back": self.broughtBack,
            "is_borrowed": self.isBorrowed
        }

    def display(self):
        # display a single borrow record in formatted text
        status = "Returned" if self.broughtBack else "Not Returned"
        return f"""
--- Borrow Record ---
User: {self.name} (ID: {self.userId})
Book: {self.title} by {self.author} (ID: {self.bookId})
Borrow Date: {self.date}
Status: {status}
        """


class BorrowLibrary:
    def __init__(self):
        self.records = []

    def add_record(self, borrow):
        self.records.append(borrow)

    def display_all(self):
        if not self.records:
            print("No borrow records found.")
            return
        print("\n" + "="*50)
        print("BORROW LIBRARY RECORDS")
        print("="*50)
        for i, record in enumerate(self.records, 1):
            print(f"\n[Record {i}]{record.display()}")
        print("="*50 + "\n")

    def display_active(self):
        active = [r for r in self.records if not r.broughtBack]
        if not active:
            print("No active borrow records.")
            return
        print("\n" + "="*50)
        print("ACTIVE BORROW RECORDS")
        print("="*50)
        for i, record in enumerate(active, 1):
            print(f"\n[Record {i}]{record.display()}")
        print("="*50 + "\n")