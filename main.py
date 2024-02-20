from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scorecard=Scorecard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detct collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle)< 50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
       ball.bounce_x()
    #detect r_paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scorecard.l_point()
    #detect l_paddle misees
    if ball.ycor()<-380:
        ball.reset_position()
        scorecard.r_point()


screen.exitonclick()