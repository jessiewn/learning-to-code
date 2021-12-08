from turtle import Turtle,Screen
screen=Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.writescore()

    def writescore(self):
        self.write(f"score={self.score}",align="center",font=("Arial",18,"normal"))
        
    
    def scoreboard(self):
        self.clear()
        self.score+=1
        self.writescore()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",25,"normal"))

    
