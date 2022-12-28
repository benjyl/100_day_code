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
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.y = 0 # y position of paddle
        self.x = x_pos
        self.goto(x=self.x, y=self.y)

    
    def up(self):
        self.y +=20
        self.goto(self.x, self.y)
    
    def down(self):
        self.y -=20
        self.goto(self.x, self.y)