from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        # Setup paddle
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=15)
        self.penup()
        self.goto(coordinates[0], coordinates[1])

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())