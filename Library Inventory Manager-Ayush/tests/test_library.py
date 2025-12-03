import unittest
import sys
sys.path.append('.')
from library_manager.book import Book

class TestBook(unittest.TestCase):
    
    def test_book_creation(self):
        b = Book("Python Basics", "John Doe", "12345")
        self.assertEqual(b.title, "Python Basics")
        self.assertEqual(b.status, "available")

    def test_issue_return(self):
        b = Book("Test Book", "Author", "999")
        
        # Test issuing
        b.issue_book()
        self.assertEqual(b.status, "issued")
        
        # Test returning
        b.return_book()
        self.assertEqual(b.status, "available")

if __name__ == '__main__':
    unittest.main()