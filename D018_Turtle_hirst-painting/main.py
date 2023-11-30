import random
import turtle as t


def pick_new_color():
    color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
                  (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                  (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                  (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                  (176, 192, 208), (168, 99, 102)]
    rgb_tuple = random.choice(color_list)
    return rgb_tuple


carol = t.Turtle()
screen = t.Screen()
t.colormode(255)
carol.penup()
carol.ht()
x_coordinate = -230
y_coordinate = -225
carol.setpos((x_coordinate, y_coordinate))
carol.speed(0)
for _ in range(10):
    for _ in range(10):
        carol.dot(20, pick_new_color())
        carol.forward(50)
    y_coordinate += 50
    carol.setpos((x_coordinate, y_coordinate))

screen.exitonclick()
