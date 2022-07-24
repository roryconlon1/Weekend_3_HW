import unittest
from models.books import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("The Bible", "The Disciples", "Adventure", False)

    def test_book_has_name(self):
        self.assertEqual("The Bible", self.book1.title)