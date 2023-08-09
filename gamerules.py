from turtle import Turtle

class GameSetup(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=0, y=625)
        self.hideturtle()
        self.speed('fastest')
        for x in range(20):
            self.pensize(width=5)
            self.seth(270)
            self.pencolor('white')
            self.forward(25)
            self.penup()
            self.forward(20)
            self.pendown()

#