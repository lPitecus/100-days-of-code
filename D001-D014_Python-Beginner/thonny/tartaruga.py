from turtle import Turtle, Screen
import random

kleber = Turtle()
kleber.shape("turtle")
number_of_sides = [4, 5, 6, 7, 8, 9, 10]
angle = 0
for shape in number_of_sides:
    while angle < 360:
        kleber.forward(100)
        kleber.right(360/shape)
        angle += 360/shape