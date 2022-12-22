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

snake = Snake()

screen.update()
game_on = True

while game_on:
    screen.update() # only updates once all segments have moved
    time.sleep(0.1)
    snake.move()
    
screen.exitonclick()