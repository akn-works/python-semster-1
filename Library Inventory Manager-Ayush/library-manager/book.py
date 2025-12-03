class Book:
    def __init__(self, title, author, isbn):
        # Setting up the book details
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "available"  # By default, a new book is available

    def __str__(self):
        # This makes printing the book object look nice
        return f"[Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}]"

    def to_dict(self):
        # We need this to save data to the JSON file easily
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def is_available(self):
        if self.status == "available":
            return True
        return False

    def issue_book(self):
        if self.is_available():
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False