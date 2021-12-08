
import random
from typing import List

from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_POSITIONS=[(300,-250),(300,-200),(300,-150),(300,-100),(300,-50),(300,0),(300,50),(300,100),(300,150),(300,200),(300,250)]


class CarManager():
    def __init__(self):
        self.cars : List[Turtle] =[]
        self.create_cars()
        self.s_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        car_number=random.randint(0,3)
        for i in range(car_number):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(random.choice(STARTING_POSITIONS))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.s_speed)

    def increase_speed(self):
        self.s_speed+=MOVE_INCREMENT

