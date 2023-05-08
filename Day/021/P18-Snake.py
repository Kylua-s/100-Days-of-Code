# Project 18 - Snake Part 2
"""
This is a two-day project.

Steps for the second day:
- Create a scoreboard
- Extend the snake
- Detect colission with food
- Detect colission with walls
- Detect collision with tail
"""

# Project 18 - Solution
import turtle
import time
from snake import Snake
from food import Food
from score import Score

# Screen settings
screen = turtle.Screen()
screen.setup(600, 600)
screen.title('Snake')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

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

    # Colission with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend_snake()

    # Colission with walls
    x, y = snake.head.pos()
    if x < - 280 or x > 280 or y < - 280 or y > 280:
        score.game_over()
        game = False

    # Collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game = False

screen.exitonclick()
