from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app) # configure app for login

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
with app.app_context():
    db.create_all()

# user loader callback - reloads user object from user ID stored in session
# returns str ID of user and returns corresponding user object
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method=="POST":
        new_user = User(
            email = request.form.get("email"),
            password = request.form.get("password"),
            name=request.form.get("name")        
        )
        new_user.password = generate_password_hash(new_user.password, 
            method='pbkdf2:sha256', 
            salt_length=8
        )
        if User.query.filter_by(email=new_user.email):
            # Check whether email already exists in the database
            flash("Email already exists, login")
            return redirect(url_for("login"))
        else:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets", name=new_user.name, logged_in = current_user.is_authenticated))
        
    return render_template("register.html", logged_in = current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method=="POST":
        user =  User.query.filter_by(email=request.form.get("email")).first() # need to use the .first()
        print(f"User to login {user}")
        # Check if email exists in database and redirect user to register page if doesn't
        if not user: 
            flash("Email does not exist, please register")
            return redirect(url_for("register", logged_in = current_user.is_authenticated))
        
        else:
            given_password = request.form.get("password")
            
            if check_password_hash(user.password, given_password):
                login_user(user)
                return redirect(url_for("secrets", name=user.name, logged_in = current_user.is_authenticated))
            
            else:
                # return message if password wrong
                flash("Incorrect password, try again")
                return redirect(url_for("login", logged_in = current_user.is_authenticated))
            
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    # name=request.args.get("name") # get the argument after the URL ?, the parameter 
    return render_template("secrets.html", name=current_user.name, logged_in=True)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/download')
@login_required
def download():
    return send_from_directory(
        "static", "files/cheat_sheet.pdf" # first arg is folder, second arg is path within folder
    )


if __name__ == "__main__":
    app.run(debug=True)
