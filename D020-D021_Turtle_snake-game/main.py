from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("Cobra Cabulosa")
screen.bgcolor("black")
screen.setup(width=600, height=600)
# Comando que faz a tela atualizar apenas quando for dado o comando screen.update()
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)


# Loop que faz a cobra se movimentar.
game_is_on = True
velocity = 0.01
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(velocity)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        if scoreboard.score % 10 == 0:
            velocity *= 0.9
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        velocity = 0.1

    # Detect collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset()
            velocity = 0.1

screen.exitonclick()
