from flask import Flask, render_template
from datetime import date
from random import randint
import requests

app = Flask(__name__)


def guess_age(name):
    age_params = {"name": name}
    response = requests.get("https://api.agify.io", params=age_params)
    response.raise_for_status()
    data = response.json()
    age = data["age"]
    return age


def guess_gender(name):
    params = {"name": name}
    response = requests.get("https://api.genderize.io", params=params)
    response.raise_for_status()
    data = response.json()
    gender = data["gender"]
    return gender


@app.route("/")
def home():
    curr_year = date.today().year
    # for every python variable want to include in the html, add another keyword argument
    # Each one needs name and value specified, can't just hand in the variable
    return render_template("index.html", year=curr_year, num=randint(1,10))


@app.route("/guess/<name>")
def guess(name):
    # Get guess from API of user age
    name = name.capitalize()
    age = guess_age(name)
    gender = guess_gender(name)

    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
