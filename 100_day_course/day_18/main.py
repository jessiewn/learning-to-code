import turtle as t
import random
from turtle import Screen, Turtle


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

t.colormode(255)
tim = t.Turtle()

tim.speed("fastest")

for i in range(36):
    tim.pencolor(random_color())
    tim.circle(80,steps=100)
    tim.setheading(tim.heading()+10)





































screen = Screen()
screen.exitonclick()
