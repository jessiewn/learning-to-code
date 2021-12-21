import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboad=Scoreboard()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboad.scoreboard()
        snake.extend()

  
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboad.reset()
        snake.reset()


    # detect collision with tail
    #if head collide with any segment of the tail: trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboad.reset()
            snake.reset()


screen.exitonclick()








