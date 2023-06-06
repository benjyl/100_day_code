from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import desc, asc

API_KEY = "fb403c26144ea4ee4afd01bfa8444db6"
API_READ_ACCESS = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjQwM2MyNjE0NGVhNGVlNGFmZDAxYmZhODQ0NGRiNiIsInN1YiI6IjY0N2RjZTdjY2Y0YjhiMDEyMjc3MTZiYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bK2-S6cVizWGpO8BCO_EAp238OGIy06Tii-4QZQJIzM"

MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Top-10-movies.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Bootstrap(app)

# WTForm for editing movie rating and review
class RateMovieform(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

class AddMovieForm(FlaskForm):
    title = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")
    
# SQLAlchemy database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all() # create database
    # if no entries to database then add first entry
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
    top_movies = Movie.query.all() # get all movies
    movies = db.session.query(Movie).order_by(asc(Movie.rating)).all()
    print(movies)
    num_movies = len(movies)
    for i in range(num_movies):
        movies[i].ranking = num_movies - i
    db.session.commit()
    return render_template("index.html", movies = movies) # show all movies 

# Edit rating and review for given movie when press update
@app.route("/edit/id=<int:id>", methods=["GET", "POST"])
def edit(id):
    
    # Get WTForm data
    form = RateMovieform()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(id)
        # Update SQL database
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form)

@app.route("/delete/id=<int:id>")
def delete(id):
    book_to_delete = Movie.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    
@app.route("/add", methods = ["GET", "POST"]) # can't use requests without these methods
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_to_add = form.title.data
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {API_READ_ACCESS}"
        }
        params = {"query": movie_to_add}
        response = requests.get(MOVIE_URL, headers=headers, params=params)
        movies = response.json()["results"]
        # print(movies)
        return render_template("select.html", movies=movies)

        # Update SQL database
        
        # movie_to_add.rating = form.rating.data
        # movie_to_add.review = form.review.data
        # db.session.commit()
        # return redirect("/")
    return render_template("add.html", form=form)

@app.route("/select", methods=["GET", "POST"])
def select_movie():
    # print("movie id", id)
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {API_READ_ACCESS}"
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_api_id}", headers=headers)
    response.raise_for_status()
    data = response.json()
    print(data)
    base_url_data = requests.get(url=f"https://api.themoviedb.org/3/configuration?api_key={API_KEY}").json()
    base_url = base_url_data["images"]["secure_base_url"]
    backdrop_size = base_url_data["images"]["backdrop_sizes"][1]
    MOVIE_DB_IMAGE_URL = f"{base_url}/{backdrop_size}"
    
    print(base_url)
    
    # return redirect(url_for(edit)))
    new_movie = Movie(
            title=data["original_title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
    db.session.add(new_movie)
    db.session.commit()
    movie_id = new_movie.id
    return redirect(url_for("edit", id=movie_id))


if __name__ == '__main__':
    app.run(debug=True)
