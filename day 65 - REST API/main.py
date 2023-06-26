from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all() # create database

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"]) # "GET" not strictly necessary as allowed by default 
def random_cafe():
    cafe_choice = db.session.query(Cafe).order_by(func.random()).first()
    # cafe_choice = db.session.query(Cafe).all()
    # random_cafe = random.choice(cafe_choice)
    return jsonify(can_take_calls = cafe_choice.can_take_calls,
                   coffee_price = cafe_choice.coffee_price,
                   has_sockets = cafe_choice.has_sockets,
                   has_toilet = cafe_choice.has_sockets,
                   has_wifi = cafe_choice.has_wifi,
                   id= cafe_choice.id,
                   img_url = cafe_choice.img_url,
                   location = cafe_choice.location,
                   map_url = cafe_choice.map_url,
                   name = cafe_choice.name,
                   seats = cafe_choice.seats)

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
