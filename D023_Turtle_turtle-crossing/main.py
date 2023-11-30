import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def should_create_car(answer, level):
    """Receives a number, and if this number is 1, generate a car object in the car list"""
    if answer == 1:
        new_car = CarManager(random.randint(-240, 280))
        # match the car speed with the corresponding level
        if level > 0:
            new_car.move_distance = (level*10) + 5
        list_of_cars.append(new_car)
    else:
        pass


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(fun=player.move_up, key="w")
screen.onkeypress(fun=player.move_down, key="s")

list_of_cars = []
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    # randomly creates a car
    # the lower the value of b, the higher the chance of a car spawning in the while loop
    car_spawn_chance = random.randint(0, 6)
    should_create_car(car_spawn_chance, scoreboard.score)
    # loops through every car on the screen for them to move
    for car in list_of_cars:
        car.move()

    # Detect if player has reached the finish line and puts them in the starting position.
    if player.ycor() >= 280:
        player.goto(x=0, y=-280)
        scoreboard.level_up()
        for car in list_of_cars:
            car.level_up()

    # Detect if player has hit a car
    for car in list_of_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
