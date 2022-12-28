from turtle import Turtle, Screen

def create_centre():
    centre.color("white")
    height = screen.window_height()
    centre.pu()
    centre.hideturtle()
    centre.pensize(8)
    centre.goto(x=0, y=height/2)
    screen.tracer(0) 
    while centre.position()[1]> -height/2:
        centre.pd()
        centre.setheading(270)
        centre.forward(20)
        centre.pu()
        centre.forward(20)
        
screen = Screen()
screen.setup(width=1.0, height=1.0) # float takes up whole screen
screen.bgcolor("black")
centre = Turtle()
create_centre()
    

screen.exitonclick()
