from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
# waiting for space key before calling move_forward()
screen.onkey(fun=move_forward, key="space") # higher order function, using function as input to another

screen.exitonclick()