# Exercise 28 - Square
# Draw a square

# Exercise 28 - Solution
import turtle

# Creates the turtle
michelangelo = turtle.Turtle()
michelangelo.shape("turtle")

# Draws the square
for _ in range(4):
    michelangelo.forward(100)
    michelangelo.right(90)

