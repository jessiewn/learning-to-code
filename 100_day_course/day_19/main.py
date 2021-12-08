import random
from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()


screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="which turtle will win, type a color")



#red,orange,yellow,green,blue,purple
tim=Turtle(shape="turtle")
tim.color("red")
tim.penup()
tim.goto(x=-230,y=-100)


tim1=Turtle(shape="turtle")
tim1.color("orange")
tim1.penup()
tim1.goto(x=-230,y=-60)


tim2=Turtle(shape="turtle")
tim2.color("yellow")
tim2.penup()
tim2.goto(x=-230,y=-20)


tim3=Turtle(shape="turtle")
tim3.color("green")
tim3.penup()
tim3.goto(x=-230,y=20)


tim4=Turtle(shape="turtle")
tim4.color("blue")
tim4.penup()
tim4.goto(x=-230,y=60)


tim5=Turtle(shape="turtle")
tim5.color("purple")
tim5.penup()
tim5.goto(x=-230,y=100)

all_turtle=[tim,tim1,tim2,tim3,tim4,tim5]

is_race_on=False

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won!The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!The {winning_color} turtle is the winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
    



screen.exitonclick()