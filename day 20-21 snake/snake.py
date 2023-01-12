from turtle import Turtle

# constants are in capitals - stored up here to make easier to find if want to change
INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_POS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(
                self.segments[seg_num - 1].pos()
            )  # move segment to the position of the segment in front of it
        self.head.fd(MOVE_DIST)

    def reset(self):
        """
        resets snake to start and changes removes previous snakes from screen
        """
        for segment in self.segments:
            segment.ht()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        # add new segment to end of snake
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()  # keep pen up - otherwise draws
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # extend snake when want more food
        self.add_segment(self.segments[-1].position())

    # The next 4 methods only refer to first block, telling it to change heading depending on arrow click
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
