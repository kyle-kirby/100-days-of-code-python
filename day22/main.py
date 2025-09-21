from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")

screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    #Detect collision with paddles
    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.hit_back()

    #Detect missed collision with paddle and score
    if ball.xcor() > 380:
        score.p1_point()
        ball.reset()

    if ball.xcor() < -380:
        score.p2_point()
        ball.reset()


screen.exitonclick()