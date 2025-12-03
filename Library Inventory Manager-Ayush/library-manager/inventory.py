import json
import os
import logging
from library_manager.book import Book

# Setting up basic logging to track errors
logging.basicConfig(filename='library.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class LibraryInventory:
    def __init__(self):
        self.books = []
        self.filename = "books.json"
        self.load_books() # Load data when program starts

    def add_book(self, title, author, isbn):
        # Check if ISBN already exists
        for book in self.books:
            if book.isbn == isbn:
                print("Error: A book with this ISBN already exists.")
                return
        
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' added successfully!")
        logging.info(f"Added book: {title}")

    def display_all(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- All Books ---")
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        found = False
        print(f"\n--- Search Results for '{title}' ---")
        for book in self.books:
            # lower() makes it case-insensitive
            if title.lower() in book.title.lower():
                print(book)
                found = True
        
        if not found:
            print("No matching books found.")

    def find_book_by_isbn(self, isbn):
        # Helper function to get a book object
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def save_books(self):
        # Task 3: Saving to JSON
        try:
            data = []
            for book in self.books:
                data.append(book.to_dict())
            
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving file: {e}")
            logging.error(f"Error saving file: {e}")

    def load_books(self):
        # Task 3: Loading from JSON with try-except
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        # Re-creating Book objects from data
                        book = Book(item['title'], item['author'], item['isbn'])
                        book.status = item['status']
                        self.books.append(book)
                logging.info("Books loaded successfully.")
            else:
                # If file doesn't exist, we just start with empty list
                self.books = []
        except Exception as e:
            print("Error loading data. Starting with empty library.")
            logging.error(f"Error loading file: {e}")
            self.books = []