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
    
    def to_dict(self):
        # getattr - retuns value of named attribute of object. E.g. for id returns the id value
        # print(f"table={self.__table__}", f"table columns: {self.__table__.columns}")
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


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
    return jsonify(cafe_choice.to_dict())

@app.route("/all", methods=["GET"]) # "GET" not strictly necessary as allowed by default 
def all_cafes():
    all_cafes = db.session.query(Cafe).all()
    # return jsonify({cafe.name: cafe.to_dict() for cafe in all_cafes}) # dict of dicts
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes]) # list of dicts

@app.route("/search", methods=["GET"])
def search_cafe_at_location():
    location = request.args.get("loc") # requested location
# Can achieve required search by 2 methods, 
#   1: call class within the session class - only works within the configured session
#   2: directly call the class 
    # cafes_at_location = db.session.query(Cafe).filter_by(location = f"{location}").all()
    cafes_at_location = Cafe.query.filter_by(location=f"{location}").all()
    if cafes_at_location:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes_at_location])
    else:
        return jsonify(error={"Not found": "Sorry, we do not have a cafe at that location"})
    
## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
