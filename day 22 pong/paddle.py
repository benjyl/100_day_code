from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DIST = 20

class Paddle(Turtle):
    def __init__(self, screenwidth, x_pos) -> None:
        super().__init__()
        self.color("white")
        self.pu()
        self.resizemode("user")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.goto(x=x_pos, y=0)
    
    def up(self):
        self.setheading(UP)
        self.fd(MOVE_DIST)
    
    def down(self):
        self.setheading(DOWN)
        self.fd(MOVE_DIST)