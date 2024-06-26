import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.bounce_x()
        ball.setx(320)

    if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        ball.setx(-320)

    if ball.xcor() > 380:
        ball.reset_score()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_score()
        scoreboard.r_point()

screen.exitonclick()
