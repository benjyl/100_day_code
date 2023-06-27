from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random

######## Notes ##########
# request.args vs request.form 
    # Use request.args.get when retrieving data passed in URL e.g. for GET & PATCH methods
    # Use request.form.get when posting data to a form e.g. for POST method
    # If try request.form.get for a patch, code doesn't fail, it returns a None

# Use postman to test API - can generate documentation from it for all the different calls
#########################

API_KEY = "TopSecretAPIKey" # test API key that cafe deletion must match 

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
@app.route("/add", methods=["POST"])
def add_cafe():
    # if request.method == "POST":
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        has_sockets = bool(request.form.get("has_sockets")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"})
    
## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["POST", "PATCH"])
def update_coffee_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    print(cafe_to_update)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price") 
        db.session.commit()
        return jsonify(success = "Successfully updated the price")
    else:
        return jsonify(error = {"Not Found": "Sorry a cafe with that id was not found in the database"})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == API_KEY:
        cafe_closed = Cafe.query.get(cafe_id)
        if cafe_closed:
            db.session.delete(cafe_closed)
            return jsonify(success = "Cafe shutdown and has been successfully removed from the database")
        else:
            return jsonify(error = {"Not found": "Cafe queried does not exist in this database"})
    else:
        return jsonify(error = "Invalid API-key used, operation not allowed")
    


if __name__ == '__main__':
    app.run(debug=True)
