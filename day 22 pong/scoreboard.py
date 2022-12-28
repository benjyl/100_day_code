from turtle import Turtle
ALIGN = "center"
FONT =("arial", 80, "bold")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        
        self.color("white")
        self.pu()
        self.ht() # hide turtle
        
        self.lscore = 0 # left player score
        self.rscore = 0 # right player score
        
        self.update_scoreboard()
        
        #self.setpos(x=0, y=270)
        #self.write(f"{self.lscore}      {self.rscore}", align=ALIGN, font=FONT)
    def create_centre(self, height):
        self.color("white")
        self.pu()
        self.hideturtle()
        self.pensize(8)
        self.goto(x=0, y=height)
         # turns off animation for moving objects to position, manual screen update required
        while self.position()[1]> -height:
            self.pd()
            self.setheading(270)
            self.forward(20)
            self.pu()
            self.forward(20)
    
    def update_scoreboard(self):
        self.goto(-150, 300)
        self.write(f"{self.lscore}", align=ALIGN, font=FONT)
        self.goto(150, 300)
        self.write(f"{self.rscore}", align=ALIGN, font=FONT)
    
    def update_score(self, left=False):
        if left:
            self.lscore += 1
        else:
            self.rscore +=1
        self.clear() # clear writing every time score updates
        self.update_scoreboard()
        self.create_centre()