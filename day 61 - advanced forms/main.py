from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from werkzeug.utils import secure_filename

app = Flask(__name__)


class LoginForm(FlaskForm):
    pass


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = FlaskForm()
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
