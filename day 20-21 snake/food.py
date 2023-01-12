from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

    def move_pos(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
