from flask import Flask, render_template, request
import requests
from datetime import date, timedelta
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "jstew613@gmail.com"
PASSWORD = "ioylffhmzmwwrmnq"

app = Flask(__name__)

blog_data = requests.get("https://api.npoint.io/0f66887cfe209d777703").json()

def send_email(form_data):
    text = f"Name: {form_data[0]} \nEmail: {form_data[1]} \nPhone: {form_data[2]} \nMessage: {form_data[3]}"
    message = MIMEText(text)  # take random quote of the day
    message["subject"] = "New Message"
    message["from"] = form_data[1]
    message["To"] = MY_EMAIL

    with smtplib.SMTP(
        "smtp.gmail.com", 587
    ) as connection:  # 587 - port number to successfully connect for email
        connection.starttls()  # tls (transport layer security-secure connection to email server)
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.as_string())

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
        form_data = [name, email, phone, message]
        send_email(form_data)
        return render_template("contact.html", sent=True)
        

if __name__ == "__main__":
    app.run(debug=True)