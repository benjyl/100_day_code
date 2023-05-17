import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor() # cursor to control/modify database, e.g. add data row or edit/delete data

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

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
db.commit() # add the entry