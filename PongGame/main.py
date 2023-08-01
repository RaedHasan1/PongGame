from turtle import Screen, Turtle
from score import ScoreBoard
from paddle import Paddle
from computer import Computer
from ball import Ball
import time
RED = 1
BLUE = -1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle = Paddle()
computer = Computer()
ball = Ball()

screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

start_screen = Turtle()
start_screen.hideturtle()
start_screen.penup()
start_screen.goto(0, 0)
start_screen.color("white")
start_screen.write("Press space to start", align="center", font=("david", 24, "normal"))

score_b = ScoreBoard()


def game():

    start_screen.clear()
    game_on = True
    while game_on:

        time.sleep(0.1)
        screen.update()
        ball.move_update()
        computer.move_update(ball)

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()
        if ball.distance(paddle) < 60 and ball.xcor() > 320:
            ball.x_move *= -1
            ball.color("red")
        if ball.distance(computer) < 60 and ball.xcor() < -320:
            ball.x_move *= -1
            ball.color("blue")

        if ball.xcor() > 380 or ball.xcor() < -380:
            if ball.xcor() < 0:
                score_b.score_update(RED)
                ball.color("white")
            if ball.xcor() > 0:
                score_b.score_update(BLUE)
                ball.color("white")
            ball.x_bounce()


screen.onkeypress(game, "space")
screen.exitonclick()
