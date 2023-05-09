import turtle
import random


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(0.75, 0.75)
        self.penup()
        self.x_speed = 2
        self.y_speed = 2

    # Movement for the ball
    def move(self):
        x = self.xcor() + self.x_speed
        y = self.ycor() + self.y_speed
        self.goto(x, y)

    # For top and bottom wall
    def bounce_wall(self):
        self.y_speed *= -1

    # For paddle
    def bounce_paddle(self):
        self.x_speed *= -1

    # Resets the ball and randomize the y-coordiante movement
    def reset(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.y_speed = random.uniform(0.1, 5)
