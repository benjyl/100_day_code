from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all() # get all books in session
    return render_template("index.html",  books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/id<int:id>",  methods=["GET", "POST"])
def edit_rating(id):
    if request.method == "POST":
        book_update = Book.query.get(id)
        book_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=db.session.query(Book).get(id))

@app.route("/delete/id=<int:id>")
def del_book(id):
    book_delete = Book.query.get(id)
    db.session.delete(book_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

