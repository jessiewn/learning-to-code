import turtle

class Scoreboard(turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
    
    def score_caculator(self):
        self.score+=1