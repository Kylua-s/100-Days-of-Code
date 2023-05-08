import turtle


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.speed('fastest')
        self.score = -1
        self.increase()

    # Increases the score by 1
    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=('Courier', 20, 'normal'))

    # Game over screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=('Courier', 25, 'normal'))

