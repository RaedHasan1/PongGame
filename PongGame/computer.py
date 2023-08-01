from paddle import Paddle


class Computer(Paddle):
    def __init__(self):
        super().__init__()
        self.color("blue")
    @overriding
    def move_update(self):
        if self.ycor() >= 0 and ball.ycor() < 0:
            self.goto(self.xcor(), self.ycor() - 10)
        elif self.ycor() <= 0 and ball.ycor() > 0:
            self.goto(self.xcor(), self.ycor() + 10)
        elif self.ycor() > 0 and ball.ycor() > 0:
            self.ycor() - ball.ycor() < 0 ? self.goto(self.xcor(), self.ycor() + 10) : self.goto(self.xcor(), self.ycor() - 10)
        elif self.ycor() < 0 and ball.ycor() < 0:
            abs(self.ycor()) - abs(ball.ycor()) < 0 ? self.goto(self.xcor(), self.ycor() - 10) : self.goto(self.xcor(), self.ycor() + 10)
        else:
            pass
