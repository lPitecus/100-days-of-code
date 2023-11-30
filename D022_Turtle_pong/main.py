from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.change_position()
    screen.update()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.setx(320)
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.setx(-320)
        ball.bounce_x()

    # detect r_paddle out of bounds
    if ball.xcor() > 385:
        ball.restart_position()
        scoreboard.l_point()

    # detect l_paddle out of bounds
    if ball.xcor() < -385:
        ball.restart_position()
        scoreboard.r_point()


screen.exitonclick()
