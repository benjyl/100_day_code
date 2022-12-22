from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE!!!!!!!!")

screen.tracer(0) 

initial_pos = [0, -20, -40]

segments = []

sk = Snake()

screen.listen()
screen.onkey(sk.up, "Up") # go up when click up arrow
screen.onkey(sk.down,"Down")
screen.onkey(sk.left, "Left")
screen.onkey(sk.right, "Right")
screen.update()
game_on = True

while game_on:
    screen.update() # only updates once all segments have moved
    time.sleep(0.1)
    sk.move()
    
screen.exitonclick()