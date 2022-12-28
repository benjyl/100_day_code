from turtle import Turtle
import random
import numpy as np

class Ball(Turtle):
    def __init__(self, screen_x, screen_y) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x = 0
        self.y = 0
        self.x_inc = 10 # movement increment in x dir
        self.y_inc = 10 # movement increment in y dir
        
        
    # #set heading to make ball go in random direction when start
        # self.setheading(random.randint(0, 355)) 
    # set heading to go to top right corner every time
        # self.direct = np.arctan2(screen_y, screen_x) * 180/np.pi
        # self.setheading(self.direct)
    
    def move(self,screen_x, screen_y, ):
        self.x += self.x_inc
        self.y += self.y_inc
        self.goto(self.x, self.y)
    

    def bounce(self):
        self.y_inc = - self.y_inc            
