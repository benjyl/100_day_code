from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.ra
        self.color("white")
        self.pu()
        self.setheading(random.randint(0, 355))
        self.width()
    def move(self):
        self.fd(20)