import turtle


class State(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def write_state(self, state_name, state_coordinate):
        self.goto(state_coordinate)
        self.write(f"{state_name}", align="center", font=("Arial", 10, "normal"))
