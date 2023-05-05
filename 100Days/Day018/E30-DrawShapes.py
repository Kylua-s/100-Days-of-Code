# Exercise 30 - Draw Shapes
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon and each shape should have a different color

# Exercise 30 - Solution
import turtle

# Creates the line
line = turtle.Turtle()

colors = ['', '', 'cornflower blue', 'coral', 'sea green', 'indian red', 'gold', 'deep pink', 'cyan', 'dark orchid']


for i in range(3, 11):
    for _ in range(i):
        line.color(colors[i])
        line.forward(100)
        # Calculates the degree of each shape
        line.right(360/i)