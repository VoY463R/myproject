import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create()
    car.move_car()
    for cars in car.all_cars:
        if player.distance(cars) < 30:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == player.finish:
        player.reset_position()
        car.increase_speed()
        scoreboard.level_up()
    screen.update()

    
screen.exitonclick()
