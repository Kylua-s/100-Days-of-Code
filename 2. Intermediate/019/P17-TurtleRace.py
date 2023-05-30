# Project 17 - Turtle Race
# Create a turtle race

import turtle
import random

# Screen settings
screen = turtle.Screen()
screen.setup(600, 400)
screen.title("Welcome to the turtle race!")


def create_turtle(color, x, y):
    t = turtle.Turtle('turtle')
    t.color(color)
    t.penup()
    t.goto(x, y)
    return t


# Creates all turtles
black = create_turtle('black', -250, 150)
red = create_turtle('red', -250, 100)
orange = create_turtle('orange', -250, 50)
yellow = create_turtle('yellow', -250, 0)
green = create_turtle('green', -250, -50)
blue = create_turtle('blue', -250, -100)
purple = create_turtle('purple', -250, -150)
turtles = [black, red, orange, yellow, green, blue, purple]

guess = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
winner = 'It will be ...'

# The race
race = True
while race:
    for t in turtles:
        # Moves each turtle by a random amount forward
        t.forward(random.randint(1, 10))
        # If the right screen border is crossed
        if t.xcor() >= 280:
            race = False
            winner = t.pencolor()
            print(winner)
            break

# Info message at the end
text = turtle.Turtle()
text.hideturtle()
if guess == winner:
    text.write(f"You won! The {winner} turtle is the winner.", False, 'center')
else:
    text.write(f"You lost! The {winner} turtle is the winner.", False, 'center')

screen.exitonclick()
