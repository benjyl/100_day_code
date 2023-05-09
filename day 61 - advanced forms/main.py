from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "sdfsertsd452&"


class LoginForm(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
