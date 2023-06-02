from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Top-10-movies.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Bootstrap(app)

class RateMovieform(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()
    if not Movie.query.first():
        new_movie = Movie(title="Phone Booth", year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating = 7.3, ranking=10, review="My favourite character was the caller",
        img_url = "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
        db.session.add(new_movie)
        db.session.commit()
    else:
        print(Movie.query.first())

@app.route("/")
def home():
    top_movies = Movie.query.all()
    return render_template("index.html", movies = top_movies)

@app.route("/edit/id=<int:id>", methods=["GET", "POST"])
def edit(id):
    # movie_id = id
    form = RateMovieform()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(id)
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form)

if __name__ == '__main__':
    
    app.run(debug=True)
