from turtle import Turtle, Screen

import paddles
from gamerules import GameSetup
from paddles import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
# turtle = Turtle()

PADDLE_SHAPE = ((20.0, -100.0), (20.0, 100.0), (-20.0, 100.0), (-20.0, -100.0))
screen.register_shape('paddle', PADDLE_SHAPE)

# screen size + color
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Art's Pong game")

# game background
screen.tracer(n=0)
game_is_on = True
game_background = GameSetup()



# created 2 paddle classes
right_user_paddle = Paddle((350, 0))
left_user_paddle = Paddle((-360, 0))

#movement for both paddles

screen.listen()
screen.onkey(key='o', fun=right_user_paddle.go_up)
screen.onkey(key='l', fun=right_user_paddle.go_down)

screen.onkey(key='w', fun=left_user_paddle.go_up)
screen.onkey(key='s', fun=left_user_paddle.go_down)



# ball class
pong_ball = Ball()

#score
scoreboard = Score()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong_ball.ball_start()

    #detect collision with wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    #detect collision with paddle
    if pong_ball.distance(right_user_paddle) < 85 and pong_ball.xcor() > 320 or \
            pong_ball.distance(left_user_paddle) < 85 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()
        if pong_ball.movement_x <= -12 or pong_ball.movement_x >= 12:
            pong_ball.ball_speed_increase()
        elif pong_ball.movement_x <= -18 or pong_ball.movement_x >= 18:
            pong_ball.ball_speed_decrease()

    #detect collision w/ wall for right paddle
    if pong_ball.xcor() > 380:
        pong_ball.ball_reset()
        #scoreboard update
        scoreboard.l_point()

    #detect collision w/ wall for left paddle
    if pong_ball.xcor() < -380:
        pong_ball.ball_reset()
        scoreboard.r_point()



screen.exitonclick()