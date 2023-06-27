from paddle import Paddle


class Computer(Paddle):
    def __init__(self):
        super().__init__()
        self.color("blue")

    def computer_moving(self, ball):
        if self.ycor() >= 0 and ball.ycor() < 0:
            self.goto(self.xcor(), self.ycor() - 10)
        elif self.ycor() <= 0 and ball.ycor() > 0:
            self.goto(self.xcor(), self.ycor() + 10)
        elif self.ycor() > 0 and ball.ycor() > 0:
            if self.ycor() - ball.ycor() < 0:
                self.goto(self.xcor(), self.ycor() + 10)
            else:
                self.goto(self.xcor(), self.ycor() - 10)
        elif self.ycor() < 0 and ball.ycor() < 0:
            if abs(self.ycor()) - abs(ball.ycor()) < 0:
                self.goto(self.xcor(), self.ycor() - 10)
            else:
                self.goto(self.xcor(), self.ycor() + 10)
        else:
            pass
