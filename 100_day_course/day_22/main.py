from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

ball=Ball()
scoreboard=Scoreboard()




game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with r_paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()
        scoreboard.r_points()
    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        scoreboard.l_points()
    #detect r_paddle failure
    if ball.xcor()>380:
        ball.reset_position()
    #detect l_paddle failure
    if ball.xcor()<-380:
        ball.reset_position()


    



screen.exitonclick()