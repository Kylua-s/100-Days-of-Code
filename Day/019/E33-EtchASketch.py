# Exercise 33 - Etch A Sketch
"""
Idea:
Make an 'etch a sketch'-app.

Key bindings:
w = forwards
a = left
s = backwards
d = right
c = clear drawing
"""

# Exercise 33 - Solution
import turtle


def move_forwards():
    pen.forward(10)


def move_backwards():
    pen.forward(-10)


def turn_right():
    pen.right(10)


def turn_left():
    pen.left(10)


def clear_screen():
    pen.clear()


pen = turtle.Turtle()
screen = turtle.Screen()

screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_right, 'd')
screen.onkey(turn_left, 'a')
screen.onkey(clear_screen, 'c')
screen.exitonclick()
