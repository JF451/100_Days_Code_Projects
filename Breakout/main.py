from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from block import Block

#Screen setup
screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.title("Breakout")

screen.tracer(0)

paddle = Paddle((40,-300))
ball = Ball()

blocks = []
for i in range(15):
    blocks.append(Block("red"))

for index, block in enumerate(blocks):
    block.goto(-index * 30, 20)

for index, block in enumerate(blocks):
    block.goto(index * 30, 20)


screen.listen()

screen.onkey(paddle.right,"Right")
screen.onkey(paddle.left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 300:
        ball.bounce_y()

    for block in blocks:
        if ball.distance(block) < 20:
            ball.bounce_y()
            block.reset()

    if ball.distance(paddle) < 20:
        print("SUCCCESS")


    if ball.distance(paddle) < 20:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() < -350:
        ball.reset_position()

screen.exitonclick()

