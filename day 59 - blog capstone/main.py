from flask import Flask, render_template
import requests
from datetime import date, timedelta

app = Flask(__name__)

def get_blog_data():
    response = requests.get("https://api.npoint.io/0f66887cfe209d777703")
    response.raise_for_status()
    data = response.json()
    return data

@app.route('/')
@app.route('/index.html')
def home():
    blog_data = get_blog_data()
    for i in range (len(blog_data)):
        blog_data[i]["date"] = str(date.today() - timedelta(days=i*7))
    return render_template("index.html", data=blog_data)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact_me():
    return render_template("contact.html")

if __name__ == "__main__":
    blog_data = get_blog_data()
    for i in range (len(blog_data)):
        blog_data[i]["date"] = str(date.today() - timedelta(days=i*7))
    print(blog_data)
    print(len(get_blog_data()))
    print(date.today())
    app.run(debug=True)