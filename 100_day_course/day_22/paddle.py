from turtle import Turtle, Screen, position



screen= Screen()
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.showturtle()
    


    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)



        

