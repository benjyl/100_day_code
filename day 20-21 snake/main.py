from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE!!!!!!!!")

screen.tracer(0) 

segments = []

sk = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(sk.up, "Up") # go up when click up arrow
screen.onkey(sk.down,"Down")
screen.onkey(sk.left, "Left")
screen.onkey(sk.right, "Right")

# screen.textinput(f"Score: {score}")
game_on = True

while game_on:
    screen.update() # only updates once all segments have moved
    time.sleep(0.1)
    sk.move()
    
    
    # detect food collision
    if food.distance((sk.head.pos())) <15:
        food.move_pos() # move food to new position if eaten
        sk.extend()
        scoreboard.increase_score()
        scoreboard.update_score()
        
    #Detect wall collision
    if abs(sk.head.xcor()) >290 or abs(sk.head.ycor()) >290:
        scoreboard.reset()
        sk.reset()
        # game_on=False
    for segment in sk.segments[1:]:
        if sk.head.distance(segment)<10:
            scoreboard.reset()
            sk.reset()
        
    
screen.exitonclick()