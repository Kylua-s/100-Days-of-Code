# Project 19 - Pong
"""
Steps:
1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collission with a wall and bounce
6. Detecet collission with paddle
7. Detect when paddle misses
8. Keep score.
"""

import turtle
import paddle
import ball
import score

# Screen settings
screen = turtle.Screen()
screen.setup(800, 600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

# Create everything else
l_paddle = paddle.Paddle(-350)
r_paddle = paddle.Paddle(350)
ball = ball.Ball()
score = score.Score()
screen.tracer(1)

# Movment for the paddles
screen.listen()
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

game = True
while game:
    ball.move()

    # Colission with top and bottom wall
    if ball.ycor() < -285 or ball.ycor() > 290:
        ball.bounce_wall()

    # Colission with a paddle or side wall
    if ball.xcor() > 330 or ball.xcor() < -330:

        # Detect when right paddle misses
        if ball.xcor() > 333:
            ball.reset()
            score.l_point()

        # Detect when left paddle misses
        elif ball.xcor() < -333:
            ball.reset()
            score.r_point()

        # Detect paddle hit
        elif ball.distance(l_paddle) < 58 or ball.distance(r_paddle) < 58:
            ball.bounce_paddle()


screen.exitonclick()
