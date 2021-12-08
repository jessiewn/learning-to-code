FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level=0
        self.update_scorebard()


    def update_scorebard(self):
        self.clear()
        self.goto(-240,270)
        self.write(f"Level:{self.level}",align="center",font=FONT)
    def increase_level(self):
        self.level+=1
        self.update_scorebard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

        
