from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import URLField
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv 

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location = URLField("Location", validators=[DataRequired(), URL()])
    open_time = StringField("Opening time (e.g. 7 A.M.)", validators=[DataRequired()])
    close_time = StringField("Closing time (e.g. 9 P.M.)", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=[(i*'☕️', i*'☕️') for i in range(1, 6)], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength", choices=[(i*'💪', i*'💪') if i > 0 else ('✘', '✘') for i in range(6)], validators=[DataRequired()])
    power_rating = SelectField("Power outlet availability", choices=[(i*'🔌', i*'🔌') if i > 0 else ('✘', '✘') for i in range(6)], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

        data_dict = form.data
        data_list = []
        print(form.coffee_rating.data)
        for val in data_dict.values():
            data_list.append(val)
        data_list = data_list[:7]
        with open('cafe-data.csv', 'r+', newline='', encoding='utf-8') as csv_file:
            if any(data_list[0] in s for s in csv_file):
                print("already in")
            # row_list = []
            # for row in csv_file:
            #     row_list.append(row)
            # print(row_list)
            # if data_list[0] in csv_file:
            #     print("already added")
            else:
                writer_object = csv.writer(csv_file)
                writer_object.writerow(data_list)
                
        
        
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file: # add encoding else emojis cause error
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        # print(list_of_rows)
        list_of_rows = list_of_rows[1:len(list_of_rows)]
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
