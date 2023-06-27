from turtle import Screen, Turtle
from score import ScoreBoard
from paddle import Paddle
from computer import Computer
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

startScreen = Turtle()
user = Paddle()
computer = Computer()
ball = Ball()

user.position_paddle(350)
computer.position_paddle(-350)

screen.listen()
screen.onkeypress(user.up, "Up")
screen.onkeypress(user.down, "Down")

startScreen.shapesize(0.0000000001)
startScreen.goto(0, 0)
startScreen.penup()
startScreen.color("white")
startScreen.write("Press space to start", align="center", font=("david", 24, "normal"))
scoreB = ScoreBoard()


def game():

    startScreen.clear()
    startScreen.goto(1000, 1000)
    screen.update()
    game_on = True
    while game_on:

        time.sleep(0.1)
        screen.update()
        ball.move_update()
        computer.computer_moving(ball)

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()
        if ball.distance(user) < 60 and ball.xcor() > 320:
            ball.x_move *= -1
            ball.color("red")
        if ball.distance(computer) < 60 and ball.xcor() < -320:
            ball.x_move *= -1
            ball.color("blue")

        if ball.xcor() > 380 or ball.xcor() < -380:
            if ball.xcor() < 0:
                scoreB.score_update(1)
                ball.color("white")
            if ball.xcor() > 0:
                scoreB.score_update(-1)
                ball.color("white")
            ball.x_bounce()


screen.onkeypress(game, "space")
screen.exitonclick()
