from flask import Flask

app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello World</h1>\
        <p>This is a paragraph</p>\
            <iframe src='https://giphy.com/embed/3oriO0OEd9QIDdllqo' width='480' height='477' frameBorder='0' class='giphy-embed' allowFullScreen></iframe><p><a href='https://giphy.com/gifs/jerseydemic-3oriO0OEd9QIDdllqo'>via GIPHY</a></p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"

# Variable_name for function added to URL in <> so when user URL shown function writes hello username
# Function takes in decorator value
# <int:number> uses a converter to specify argument type, useful for a path which accepts / in its variable unlike a string
@app.route("/username/<name>/<int:number>")
def hello_user(name, number):
    return f"Hello {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True) # debugger will allow changes to be updated without having to reload server