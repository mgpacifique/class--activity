# Class Activity — Library Borrow System

A Python class-activity project that models a simple **library borrowing system** using object-oriented programming (OOP). The activity covers class design, inheritance, and sequence diagramming.

---

## 📐 Sequence Diagram

The diagram below was created on [diagrams.net](https://app.diagrams.net) and illustrates the **Sequence Diagram of Borrowed operations** — showing how a `User` borrows a `Book` (1:N) and how `History` stores borrowed books from users (N:1).

![Sequence Diagram of Borrowed operations](https://github.com/user-attachments/assets/33c69ed8-df51-44a8-96ef-2cbe756ecb93)

---

## 🗂️ Project Structure

```
class--activity/
├── deescript.py        # Core classes: Book, User, Borrow, BorrowLibrary
├── deescript_test.py   # Unit tests and demo runner
└── README.md
```

---

## 🧱 Class Design

### `Book`
Represents a library book.

| Attribute    | Type    | Description                  |
|-------------|---------|------------------------------|
| `id`        | int     | Unique book identifier        |
| `title`     | str     | Title of the book             |
| `author`    | str     | Author name                   |
| `year`      | int     | Publication year              |
| `isBorrowed`| bool    | Whether the book is borrowed  |

### `User`
Represents a library user.

| Attribute | Type | Description              |
|----------|------|--------------------------|
| `id`     | int  | Unique user identifier    |
| `name`   | str  | User's full name          |
| `age`    | int  | User's age                |

### `Borrow` (inherits `User` + `Book`)
Represents a borrow record, linking a user to a book.

| Attribute     | Type | Description                        |
|--------------|------|------------------------------------|
| `userId`     | int  | ID of the borrowing user            |
| `bookId`     | int  | ID of the borrowed book             |
| `date`       | str  | Date the book was borrowed          |
| `broughtBack`| bool | Whether the book has been returned  |

Key methods:
- `mark_returned()` — marks the book as returned
- `get_info()` — returns a dictionary of the borrow record
- `display()` — returns a formatted string summary

### `BorrowLibrary`
A collection that manages multiple `Borrow` records.

Key methods:
- `add_record(borrow)` — adds a borrow record
- `display_all()` — prints all borrow records
- `display_active()` — prints only unreturned records

---

## ▶️ Usage

```python
from deescript import Book, User, Borrow, BorrowLibrary

user = User(1, "Alice", 23)
book = Book(10, "1984", "George Orwell", 1949, False)

borrow = Borrow(user, book, "2026-05-11")
print(borrow.display())

borrow.mark_returned()
print(borrow.get_info())
```

---

## ✅ Running Tests

```bash
python deescript_test.py
```

Expected output:
```
All tests passed.

==================================================
DEMO: Displaying Borrow Records
==================================================
...
```

---

## 🔗 Relationships

- **User → Borrow**: 1 user can have many borrow records (1:N)
- **Borrow → History**: N borrow records are stored per user (N:1)
