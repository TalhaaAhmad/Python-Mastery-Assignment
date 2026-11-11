# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 9 - OOP: classes and objects


# ---------- Warm-up: Student class ----------
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"


# ---------- Build: Bank account ----------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be more than 0")
        self.balance = self.balance + amount
        self.history.append("Deposit " + str(amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be more than 0")
        if amount > self.balance:
            raise ValueError("Not enough balance")
        self.balance = self.balance - amount
        self.history.append("Withdraw " + str(amount))

    def print_history(self):
        for line in self.history:
            print(line)


# ---------- Challenge: Library system ----------
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size, available=True):
        super().__init__(title, author, available)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} (eBook, {self.file_size} MB)"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print("You borrowed", title)
                else:
                    print(title, "is already borrowed")
                return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("You returned", title)
                return
        print("Book not found")

    def available_books(self):
        result = []
        for book in self.books:
            if book.available:
                result.append(book)
        return result


# the demo only runs when this file is run directly (so tests can import it)
if __name__ == "__main__":
    print("--- Warm-up: Student ---")
    s = Student("Ali", 12)
    s.add_mark(80)
    s.add_mark(72)
    s.add_mark(91)
    print(s)

    print("\n--- Build: Bank account ---")
    account = BankAccount("Ali", 1000)
    account.deposit(500)
    account.withdraw(200)
    try:
        account.withdraw(5000)
    except ValueError as error:
        print("Error:", error)
    try:
        account.deposit(-10)
    except ValueError as error:
        print("Error:", error)
    print("Balance:", account.balance)
    account.print_history()

    print("\n--- Challenge: Library ---")
    library = Library()
    library.add_book(Book("Python Basics", "Ahmed"))
    library.add_book(Book("Data Structures", "Sara"))
    library.add_book(EBook("Learn Git", "Hina", 5))
    library.borrow("Python Basics")
    library.borrow("Python Basics")
    print("Available books:")
    for book in library.available_books():
        print(" -", book)
    library.return_book("Python Basics")
    print("After returning:", len(library.available_books()), "books available")
