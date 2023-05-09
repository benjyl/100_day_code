from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField, SubmitField
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "sdfsertsd452&"


class LoginForm(FlaskForm):
    email = StringField(label="Email")
    password = PasswordField(label="Password")
    terms = BooleanField(label="I agree to T&Cs")
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
