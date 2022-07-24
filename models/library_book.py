from models.books import *

book1 = Book("The Philosophers Stone", "J.K Rowling", "Fantasy", False,"16/11/1995")
book2= Book("Chamber of Secrets", "J.K Rowling", "Fantasy", True, "1/2/3")
book3= Book("Prisoner of Askaban", "J.K Rowling", "Fantasy", True, "1/2/13")
books = [book1, book2, book3]

def add_book(book):
    books.append(book)

def delete_book(book):
    books.remove(book)