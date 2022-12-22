from turtle import Turtle

# constants are in capitals - stored up here to make easier to find if want to change
INITIAL_POS = [0, -20, -40]
MOVE_DIST = 20

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
        self.segments[0].fd(MOVE_DIST)
    
    # The next 4 methods only refer to first block, telling it to change heading depending on arrow click
    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)