import turtle


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.speed('fastest')
        self.l_score = 0
        self.r_score = 0
        self.update()

    # Updates the score
    def update(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align='center', font=('Courier', 25, 'normal'))

    # Increases the left score by 1 and updates
    def l_point(self):
        self.l_score += 1
        self.update()

    # Increases the right score by 1 and updates
    def r_point(self):
        self.r_score += 1
        self.update()
