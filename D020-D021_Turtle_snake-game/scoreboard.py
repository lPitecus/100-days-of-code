from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Pontos: {self.score} Recorde: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Pontos: {self.score} Recorde: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
