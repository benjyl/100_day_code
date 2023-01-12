from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_on = False
bet = screen.textinput(
    title="Make your Bet", prompt="Which colour turtle do you think will win"
)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list = []
y_pos = -100
for colour in colours:
    new_turt = Turtle(shape="turtle")
    new_turt.color(colour)
    new_turt.pu()
    new_turt.goto(x=-230, y=y_pos)
    y_pos += 40
    turtle_list.append(new_turt)
# print(turtle_list)

if bet:
    race_on = True

while race_on:

    for turtle in turtle_list:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            if winner == bet.lower():
                print(f"You won! The winner was the {winner} turtle ")
            else:
                print(f"You lost! The winner was the {winner} turtle ")
            race_on = False


screen.exitonclick()
