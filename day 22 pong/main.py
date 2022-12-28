from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
        
screen = Screen()
screen.setup(width=1.0, height=1.0) # float takes up whole screen
s_h = screen.window_height()/2
s_w = screen.window_width()/2
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
scoreboard.create_centre(s_h)


# create pong pieces
centre = Turtle()
# create_centre(s_h)

ball = Ball(s_w, s_h) 

right_paddle = Paddle(s_w-50)
left_paddle = Paddle(-s_w + 50)
screen.listen()



screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.update()

game_on = True


while game_on:
    screen.update()
    time.sleep(ball.sleep)
    ball.move(s_w, s_h)
    #detect wall collision
    if abs(ball.ycor()) > s_h - 40:
        ball.hit_wall()
    
    # detect paddle collision
    if abs(ball.xcor()) > s_w - 70 and (ball.distance(left_paddle) < 50 or ball.distance(right_paddle)<50):
        ball.hit_paddle()

    
    # right paddle misses
    if ball.xcor() > s_w - 30:
        scoreboard.update_score(left=True)
        ball.reset_pos()

    # left paddle misses
    elif ball.xcor() < -(s_w-30):
        scoreboard.update_score() 
        ball.reset_pos()

    
    
screen.exitonclick()
