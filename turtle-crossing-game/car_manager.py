from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.starting_move = STARTING_MOVE_DISTANCE
        self.create()

    def create(self):
        random_create = random.randint(1,6)
        if random_create == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(x=310, y=random.randint(-250,250))
            car.color(random.choice(COLORS))
            self.all_cars.append(car)
        
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.starting_move)
            
    def increase_speed(self):
        self.starting_move += MOVE_INCREMENT
            
                