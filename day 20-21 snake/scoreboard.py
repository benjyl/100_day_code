from turtle import Turtle
ALIGN = "center"
FONT =("arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.ht() # hide turtle
        self.setpos(x=0, y=270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
    
    def update_score(self):
        self.score += 1
        self.clear() # clear writing every time score updates
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
    
    def game_over(self):
        self.setpos(x=0, y=0)
        self.write(f"GAME OVER!", align=ALIGN, font=FONT)