from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")
        self.penup()
        self.x_move = 15
        self.y_move = 15

    def move_update(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):
        if self.ycor() > 0:
            self.y_move *= -1
        else:
            self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.y_move *= -1
        self.goto(0, 0)
