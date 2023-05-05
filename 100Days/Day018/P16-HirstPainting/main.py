# Project 16 - Hirst Painting
# Recreate a Hirst dot painting

# Project 16 - Solution
import turtle
import colorgram
import random

# Extracting colors from an image
rgb_colors = []
colors = colorgram.extract("100-Days-of-Code---Documentation/100Days/Day018/P16-HirstPainting/ellipticine.png", 101)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Settings
turtle.colormode(255)
circle = turtle.Turtle()
circle.speed('fastest')
circle.hideturtle()
circle.up()

# Positions the circle at the top right
circle.left(45)
circle.forward(400)
circle.left(-45)


for _ in range(10):
    # Positions the circle for each new row
    circle.left(180)
    circle.forward(500)
    circle.left(90)
    circle.forward(50)
    circle.left(90)
    for _ in range(10):
        # Draws each row
        circle.dot(25, random.choice(rgb_colors))
        circle.forward(50)
    

screen = turtle.Screen()
screen.exitonclick()

