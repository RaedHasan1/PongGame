from turtle import Turtle

ZERO = 0.0000000001


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(ZERO)
        self.score = 0
        self.c_score = 0
        self.left(90)
        self.draw()

    def draw(self):
        self.penup()
        if self.score > self.c_score:
            self.pencolor("red")
        elif self.score < self.c_score:
            self.pencolor("blue")
        else:
            self.pencolor("white")
        self.goto(0, -300)
        for ycor in range(-300, 280, 20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.goto(0, ycor)
        self.write(f"{self.c_score}:{self.score}", align="center", font=("david", 30, "bold"))

    def score_update(self, point):
        self.clear()
        point == 1 ? self.score +=1 : self.c_score += 1
        self.draw()
