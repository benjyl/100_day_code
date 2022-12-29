from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.ht() # hide turtle
        self.level = 1
    
    def update_level(self):
        self.level += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Level {self.level}", align="center", font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
    
