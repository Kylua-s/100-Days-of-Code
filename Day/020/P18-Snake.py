# Project 18 - Snake Part 1
"""
This is a two-day project.

Steps for the first day:
- Create a snake body.
- Move the snake
- Control the snake
"""

# Project 18 - Solution
import turtle
import time
from snake import Snake

# Screen settings
screen = turtle.Screen()
screen.setup(600, 600)
screen.title('Snake')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()

# Snake movement
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
