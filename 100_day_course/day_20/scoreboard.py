from turtle import Turtle,Screen
screen=Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("/Users/nan/coding/learning-to-code/100_day_course/day_20/data.txt",mode="r")as file:
            high_test=int(file.read())
        self.high_score=high_test
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.writescore()

    def writescore(self):
        self.write(f"Score:{self.score} High score:{self.high_score}",align="center",font=("Arial",18,"normal"))
        
    
    def scoreboard(self):
        self.clear()
        self.score+=1
        self.writescore()


    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("/Users/nan/coding/learning-to-code/100_day_course/day_20/data.txt",mode="w")as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}",align="center",font=("Arial",18,"normal"))
    
