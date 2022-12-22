from turtle import Turtle

INITIAL_POS = [0, -20, -40]

class Snake:
    def __init__(self):
       self.segments = []
       self.create_snake()
       
    def create_snake(self):

        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.pu() # keep pen up - otherwise draws
            new_segment.goto(x=INITIAL_POS[i], y=0)
            new_segment.speed("slowest")
            self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos()) # move segment to the position of the segment in front of it
        self.segments[0].fd(20)
        self.segments[0].left(90)