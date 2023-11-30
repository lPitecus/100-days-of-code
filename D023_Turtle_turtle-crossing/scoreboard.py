from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score = 0
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over!", align="center", font=FONT)
