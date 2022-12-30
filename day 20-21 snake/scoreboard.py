from turtle import Turtle
ALIGN = "center"
FONT = ("arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.pu()
        self.ht()  # hide turtle
        self.setpos(x=0, y=270)
        self.write(
            f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()  # clear writing every time score updates
        self.write(
            f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        with open("data.txt", mode='w') as data:
            data.write(str(self.highscore))

    # def game_over(self):
    #     self.setpos(x=0, y=0)
    #     self.write(f"GAME OVER!", align=ALIGN, font=FONT)
