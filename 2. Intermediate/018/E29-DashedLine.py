# Exercise 29 - Dashed Line
# Draw a dashed line

# Exercise 29 - Solution
import turtle

# Creates the line
line = turtle.Turtle()

# Draws the dashed line
for _ in range(10):
    line.down()
    line.forward(10)
    line.up()
    line.forward(10)
