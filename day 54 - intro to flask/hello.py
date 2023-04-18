from flask import Flask

app = Flask(__name__) # Flask class

print(__name__)

#decorator adds additional functionality to existing function

@app.route("/") # when user navigates to our URL with just / show how page
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
# flask --app hello run - run this in command line to get flask to work

# Python decorator function

