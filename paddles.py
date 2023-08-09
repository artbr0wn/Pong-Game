import turtle
from turtle import Turtle



PADDLE_SHAPE = ((20.0, -100.0), (20.0, 100.0), (-20.0, 100.0), (-20.0, -100.0))
PADDLE_1_POSITION = (350,0)
PADDLE_2_POSITION = (-360,0)
UP = 90
DOWN = 270
#now making a compound shape to use for both paddles
turtle.register_shape('paddle', PADDLE_SHAPE)

#test
# screen = Screen()
# screen.bgcolor('black')
# screen.tracer(n=1)

# # paddle setup
# paddle_a = Turtle()
# paddle_a.seth(90)
# paddle_a.shape('square')
# paddle_a.shapesize(stretch_wid=5,stretch_len=1)
# paddle_a.color('white')
# paddle_a.penup()
# paddle_a.goto(350,0)
#
# # paddle movement
# new_y = paddle_a.ycor()+20
# paddle_a.goto(x=paddle_a.xcor(),y=new_y)

#creating the paddle class

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.paddle1(position)

    def paddle1(self,position):
        self.shape('paddle')
        self.color('white')
        self.seth(90)
        self.penup()
        self.goto(position)

    def go_up(self):
        up_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=up_y)

    def go_down(self):
        down_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=down_y)








