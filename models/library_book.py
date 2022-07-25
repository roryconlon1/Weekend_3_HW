from models.books import *

book1 = Book("The Philosophers Stone", "J.K Rowling", "Fantasy", False,"16/11/1995")
book2= Book("Chamber of Secrets", "J.K Rowling", "Fantasy", True, "1/2/3")
book3= Book("Prisoner of Askaban", "J.K Rowling", "Fantasy", True, "1/2/13")
books = [book1, book2, book3]

def add_book(book):
    books.append(book)

def delete_book(title):
    book_to_remove = None
    for book in books:
        if book.title == title:
            book_to_remove = book
            break

    books.remove(book_to_remove)