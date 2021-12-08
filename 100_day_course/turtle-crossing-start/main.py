FINISH_LINE_Y = 280

import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player=Player()
    carmanager=CarManager()
    scoreboard=Scoreboard()

    screen.listen()
    screen.onkey(player.move,"Up")

    game_is_on = True
    game_loop=0
    while game_is_on:
        game_loop+=1
        time.sleep(0.1)
        screen.update()
        carmanager.move()
        if game_loop%6==0:
            carmanager.create_cars()
        
        #detect player collide with a car
        for car in carmanager.cars:
            if player.distance(car)<22:
                scoreboard.game_over()
                game_is_on=False
        #Detect when the turtle player has reached the top edge
        if player.ycor()>=FINISH_LINE_Y:
            player.reset()
            carmanager.increase_speed()
            scoreboard.increase_level()


    screen.exitonclick()
main()