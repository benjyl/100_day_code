from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    api_url= "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(api_url)
    blog_data = response.json()
    print(blog_data)
    return render_template("index.html", data = blog_data)

@app.route('/post/<num>')
def get_blog_post(num):
    api_url= "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(api_url)
    blog_data = response.json()[int(num)-1]
    return render_template("post.html", blog = blog_data)
if __name__ == "__main__":
    app.run(debug=True)
