# Exercise 31 - Random Walk

# Exercise 31 - Solution
import turtle
import random

colors = ['cornflower blue', 'coral', 'sea green', 'indian red', 'gold', 'deep pink', 'cyan', 'dark orchid']

line = turtle.Turtle()
line.pensize(10)
line.speed('fastest')

direction = [-90, 0, 90]
for _ in range(100):
    line.forward(25)
    line.color(random.choice(colors))
    line.right(random.choice(direction))

screen = turtle.Screen()
screen.exitonclick()
