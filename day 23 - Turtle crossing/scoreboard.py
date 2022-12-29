from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.ht() # hide turtle
        
        
    def update_scoreboard(self, level):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Level {level}", align="center", font=FONT)
        
    
