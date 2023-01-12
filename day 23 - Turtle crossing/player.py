from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)  # face north

    def move(self):
        """move player forward when up button hit
        Check whether reached top of screen
        """
        self.fd(MOVE_DISTANCE)

    def new_level(self):
        """reset player position when get to top"""
        self.goto(STARTING_POSITION)
