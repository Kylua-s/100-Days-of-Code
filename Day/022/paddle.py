import turtle


class Paddle(turtle.Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, 0)

    def move_up(self):
        y = self.ycor() + 20
        self.sety(y)

    def move_down(self):
        y = self.ycor() - 20
        self.sety(y)
