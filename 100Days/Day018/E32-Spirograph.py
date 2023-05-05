# Exercise 32 - Spirograph

# Exercise 32 - Solution
import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


circle = turtle.Turtle()
circle.speed('fastest')

# Necessary to be able to change the color with RGB
turtle.colormode(255)

# The range depends on the turning degree
# In this case: 360 / 5 = 72
for _ in range(72):
    circle.color(random_color())
    circle.circle(200)
    circle.right(5)


screen = turtle.Screen()
screen.exitonclick()