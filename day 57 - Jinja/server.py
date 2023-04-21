from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route("/")
def home():
    curr_year = date.today().year
    # for every python variable want to include in the html, add another keyword argument
    # Each one needs name and value specified, can't just hand in the variable
    return render_template("index.html", year=curr_year)


if __name__ == "__main__":
    app.run(debug=True)
