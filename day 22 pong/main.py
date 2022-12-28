from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball

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
s_h = screen.window_height()/2
s_w = screen.window_width()/2
screen.bgcolor("black")
screen.title("Pong")


# create pong pieces
centre = Turtle()
create_centre(s_h)

ball = Ball(s_w, s_h) 

right_paddle = Paddle(s_w-50)
left_paddle = Paddle(-s_w + 50)
screen.listen()



screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move(s_w, s_h)
    #detect wall collision
    if abs(ball.ycor()) > s_h - 40:
        ball.hit_wall()
    
    # detect paddle collision
    if abs(ball.xcor()) > s_w - 70 and (ball.distance(left_paddle) < 70 or ball.distance(right_paddle)<70):
        ball.hit_paddle()
    
    
        
screen.exitonclick()
