from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE!!!!!!!!")

screen.tracer(0) 

initial_pos = [0, -20, -40]

segments = []

for i in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.pu()
    new_segment.goto(x=initial_pos[i], y=0)
    new_segment.speed("slowest")
    segments.append(new_segment)

screen.update()
game_on = True

while game_on:
    screen.update() # only updates once all segments have moved
    time.sleep(0.1)
    
    for seg_num in range(len(segments)-1, 0, -1):
        segments[seg_num].goto(segments[seg_num-1].pos()) # move segment to the position of the segment in front of it
    segments[0].fd(20)
    segments[0].left(90)
screen.exitonclick()