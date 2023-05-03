from flask import Flask, render_template
import requests
from datetime import date, timedelta

app = Flask(__name__)

blog_data = requests.get("https://api.npoint.io/0f66887cfe209d777703").json()

@app.route('/')
# @app.route('/index.html')
def home():
    for i in range (len(blog_data)):
        blog_data[i]["date"] = str(date.today() - timedelta(days=i*7))
    return render_template("index.html", data=blog_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact_me():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def post(num):
    # blog_post = 
    return render_template('post.html', post_data=blog_data[num-1])

if __name__ == "__main__":
    app.run(debug=True)