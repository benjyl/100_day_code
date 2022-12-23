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

initial_pos = [0, -20, -40]

segments = []

sk = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(sk.up, "Up") # go up when click up arrow
screen.onkey(sk.down,"Down")
screen.onkey(sk.left, "Left")
screen.onkey(sk.right, "Right")
score = 0
# screen.textinput(f"Score: {score}")
game_on = True

while game_on:
    screen.update() # only updates once all segments have moved
    time.sleep(0.1)
    sk.move()
    
    
    # detect food collision
    if food.distance((sk.head.pos())) <15:
        print("nom nom")
        print(food.distance((sk.head.pos())))
        food.move_pos() # move food to new position if eaten
        
    
screen.exitonclick()