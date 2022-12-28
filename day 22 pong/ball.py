from turtle import Turtle
import random
import numpy as np

class Ball(Turtle):
    def __init__(self, screen_x, screen_y) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        # 
        # self.setheading(random.randint(0, 355)) # if want to move randomly
        # self.setheading
        self.direct = np.arctan2(screen_y, screen_x) * 180/np.pi
        self.setheading(self.direct)
    def move(self):
        self.fd(20)