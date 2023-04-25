from flask import Flask, render_template
import requests
from post import Post

blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
blog_instances = []
# separate data into object instances
for blog in blog_data:
    blog_inst = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    blog_instances.append(blog_inst)
app = Flask(__name__)

@app.route('/')
def home():
    api_url= "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(api_url)
    blog_data = response.json()
    print(blog_data)
    return render_template("index.html", data = blog_instances)

@app.route('/post/<int:index>')
def get_blog_post(index):
    blog_data = blog_instances[index-1]
    return render_template("post.html", blog=blog_data)
if __name__ == "__main__":
    app.run(debug=True)
