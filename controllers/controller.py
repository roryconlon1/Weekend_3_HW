from crypt import methods
from flask import redirect, render_template, request
from app import app
from models.library_book import add_book, books, delete_book
from models.books import Book

@app.route('/bookstore')
def index():
    return render_template('/bookstore/index.html', title='Home', books=books)

@app.route('/bookstore/<index>')
def bookstore(index):
    individual_book= int(index)
    return render_template('/bookstore/individual.html', title='Individual Book', book=books[individual_book])

@app.route('/bookstore/new')
def new():
    return render_template('bookstore/new.html', title='New Book')

@app.route('/bookstore', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = request.form['checked_out']
    date = request.form['date']
    new_book = Book(title, author, genre, checked_out, date)
    add_book(new_book)
    return redirect('/bookstore')

@app.route('/bookstore/delete/<title>', methods=['POST'])
def books_delete(title):
    delete_book(title)
    return redirect('/bookstore')








