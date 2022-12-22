from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE!!!!!!!!")
initial_pos = [0, -20, -40]
for i in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.pu()
    new_segment.goto(x=initial_pos[i], y=0)




screen.exitonclick()