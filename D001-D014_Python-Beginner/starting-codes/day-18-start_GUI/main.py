from turtle import Turtle, Screen
import random


def pick_random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_color = (r, g, b)
    return random_color


kleber = Turtle()
kleber.shape("turtle")
tela = Screen()
tela.colormode(255)

# desafio 5
# kleber.speed(0)
# angle = 0
# while angle != 360:
#     kleber.pencolor(pick_random_color())
#     kleber.circle(100)
#     kleber.left(8)
#     angle += 8


# desafio 4
# kleber.speed(0)
# kleber.pensize(10)
# while True:
#     kleber.pencolor(pick_random_color())
#     kleber.forward(30)
#     direction = random.randint(0, 4)
#     kleber.setheading(90*direction)


# desafio 3
# number_of_sides = [4, 5, 6, 7, 8, 9, 10]
# angle = 0
#
# for shape in number_of_sides:
#     kleber.pencolor(pick_random_color())
#     angle = 0
#     while angle < 360:
#         kleber.forward(100)
#         kleber.right(360/shape)
#         angle += 360/shape


# desafio 2
# kleber.penup()
# kleber.setx(-250)
# kleber.pendown()
# for _ in range(20):
#     kleber.forward(10)
#     kleber.penup()
#     kleber.forward(10)
#     kleber.pendown()

tela.exitonclick()
