from flask import Flask, render_template, request
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


@app.route('/post/<int:num>')
def post(num):
    # blog_post = 
    return render_template('post.html', post_data=blog_data[num-1])

@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    # If click on contact button / type url /contact
    if request.method == "GET":
        return render_template("contact.html")
    # If press submit button on form
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        return render_template("contact.html", sent=True)
        
        
        return f"<h1>Name: {name} <br/> email: {email} <br/> phone: {phone} <br/> message: {message} <br/>Successfully sent your message"

if __name__ == "__main__":
    app.run(debug=True)