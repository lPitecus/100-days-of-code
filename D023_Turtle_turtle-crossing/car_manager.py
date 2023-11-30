from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self, random_y):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(290, random_y)
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.setheading(180)
        self.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
