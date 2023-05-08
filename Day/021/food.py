import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    # Spawns new food
    def refresh(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))
