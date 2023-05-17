import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor() # cursor to control/modify database, e.g. add data row or edit/delete data

# .execute - tells cursor to execute an action
# CREATE TABLE - creates new database table - table name comes after keyword
# () - parts inside parentheses are table fields (column headings)
# id INTEGER PRIMARY KEY - first field called "id", datatype = integer, primary key for this table
# Primary key - unique identifier for record in table
# title varchar(250) NOT NULL UNIQUE - second field called title - accepts variable-length string of characters (max length 250 characters)
# NOTNULL - must have a value (can't be empty) UNIQUE - no 2 records can have the same title
# author varchar(250) NOT NULL - field accept string up to 250 chars, cannot be empty
# rating FLOAT NOT NULL- field accepts float cannot be empty

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
# db.commit() # add the entry

# Using Flask alchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
with app.app_context():
    db.create_all()
    new_book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
    all_books = db.session.query(Book).all
    print(all_books())
    
    book = Book.query.filter_by(title="Harry Potter").first()
    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()
    book_id = 1
    print(book_to_update)
    
    book_to_delete = db.session.get(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    
    