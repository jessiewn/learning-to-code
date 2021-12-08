import random
from turtle import Turtle,Screen
import turtle

screen=Screen()
tim=Turtle()
turtle.colormode(255)


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color



color_list = ['red', 'orange', 'yellow', 'green', 'blue',
  'purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro', 'gray',
  'dimgray', 'LightSlateGray','AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']

direction=[0,90,180,270]

tim.pensize(8)
tim.speed(10)

for i in range(300):
    tim.pencolor(random_color())
    tim.forward(20)
    tim.right(random.choice(direction))



screen.exitonclick()

