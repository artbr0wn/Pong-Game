from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.game_ball()
        self.movement_x = 12
        self.movement_y = 12

    def game_ball(self):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)

    def ball_start(self):
        self.penup()
        new_x = self.xcor() + self.movement_x
        new_y = self.ycor() + self.movement_y
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.movement_y *= -1

    def bounce_x(self):
        self.movement_x *= -1

    def ball_reset(self):
        self.goto(x=0, y=0)
        self.bounce_x()
        self.ball_speed_decrease()

    def ball_speed_increase(self):
        self.movement_x *= 1.1

    def ball_speed_decrease(self):
        self.movement_x *= 0.5