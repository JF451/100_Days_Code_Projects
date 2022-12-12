from turtle import Turtle

class Block(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("square")
        self.color(color)

        self.turtlesize(stretch_wid=2, stretch_len=2)
        self.penup()

