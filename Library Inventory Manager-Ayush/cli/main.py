import sys
# This line is needed to find the library_manager folder
sys.path.append('.') 

from library_manager.inventory import LibraryInventory

def main():
    library = LibraryInventory()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == '2':
            library.display_all()

        elif choice == '3':
            search_term = input("Enter title to search: ")
            library.search_by_title(search_term)

        elif choice == '4':
            isbn = input("Enter ISBN of book to issue: ")
            book = library.find_book_by_isbn(isbn)
            if book:
                if book.issue_book():
                    print("Book issued successfully.")
                    library.save_books() # Save the new status
                else:
                    print("Could not issue book. It might already be issued.")
            else:
                print("Book not found.")

        elif choice == '5':
            isbn = input("Enter ISBN of book to return: ")
            book = library.find_book_by_isbn(isbn)
            if book:
                if book.return_book():
                    print("Book returned successfully.")
                    library.save_books() # Save the new status
                else:
                    print("Book was not issued.")
            else:
                print("Book not found.")

        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()