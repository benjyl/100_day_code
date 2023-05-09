from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = "sdfsertsd452&"


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), validators.Email(message="Invalid email")])
    password = PasswordField(label="Password", validators=[validators.Length(min=8, message="Password must be at least %(min)d characters long"), DataRequired()])
    terms = BooleanField(label="I agree to T&Cs", validators=[validators.input_required()])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
