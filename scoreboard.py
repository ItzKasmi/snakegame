from turtle import Turtle

ALIGNMENT = "center"
FONT = ("verdana", 15, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode='r') as self.data:
            self.high_score = int(self.data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt", mode='w') as self.data:
                self.data.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
