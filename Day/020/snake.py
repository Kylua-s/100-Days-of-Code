import turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.new_seqment(0, 0)
        self.new_seqment(-20, 0)
        self.new_seqment(-40, 0)
        self.head = self.segments[0]

    # Create a new seqment at the given coordinates
    def new_seqment(self, x, y):
        seg = turtle.Turtle('square')
        seg.color('white')
        seg.penup()
        seg.goto(x, y)
        self.segments.append(seg)

    # Moves the last to part to the position of the second last part ... until the firt part moves forward
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.head.forward(20)

    # For changing the movement direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
