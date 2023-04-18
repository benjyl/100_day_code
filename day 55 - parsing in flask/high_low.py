from flask import Flask
from random import randint

NUMBER = randint(0,9)

app = Flask(__name__)

@app.route("/")
def start_game():
    return "<h1>Guess a number between 0 and 9</h1>\
        <img src=https://media1.giphy.com/media/NAy2FD8xWrH4jUIBrq/giphy.gif?cid=ecf05e47p6uffyl6qf941amjapl0ywm05tqwuamt721i1jht&rid=giphy.gif&ct=g>"

@app.route("/<int:number>")
def user_gues(number):
    if number == NUMBER:
        return f"<h1 style='color:green'>You guessed {number}: Correct</h1>\
            <img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
    elif number > NUMBER:
        return f"<h1 style='color:purple'>You guessed {number}: Too high, try again</h1>\
            <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    elif number < NUMBER:
         return f"<h1 style='color:red'>You guessed {number}: Too low, try again</h1>\
            <img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"

if __name__ == "__main__":
    app.run(debug=True) # debugger will allow changes to be updated without having to reload server