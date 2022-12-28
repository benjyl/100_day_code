from turtle import Turtle, Screen
from paddle import Paddle
import time

def create_centre(height):
    centre.color("white")
    centre.pu()
    centre.hideturtle()
    centre.pensize(8)
    centre.goto(x=0, y=height)
    screen.tracer(0) # turns off animation for moving objects to position, manual screen update required
    while centre.position()[1]> -height:
        centre.pd()
        centre.setheading(270)
        centre.forward(20)
        centre.pu()
        centre.forward(20)
        
screen = Screen()
screen.setup(width=1.0, height=1.0) # float takes up whole screen
s_h = screen.window_height()
s_w = screen.window_width()
screen.bgcolor("black")
screen.title("Pong")
centre = Turtle()
create_centre(s_h/2)

screen.listen()


right_paddle = Paddle(s_w/2-50)
left_paddle = Paddle(-s_w/2 + 50)

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
