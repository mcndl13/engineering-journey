from time import sleep
from turtle import Screen
from ball import Ball
from scoreboard import ScoreBoard
from paddle import Paddle

WIDTH = 600
HEIGHT = 600
STARTING_POSITIONS = [((-WIDTH//2) + 25, 0), ((WIDTH//2) - 25, 0)]

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

l_paddle = Paddle(STARTING_POSITIONS[0])
r_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball(WIDTH, HEIGHT)


screen.listen()

screen.onkeypress(l_paddle.up, key="w")
screen.onkeyrelease(l_paddle.release_up, key="w")

screen.onkeypress(l_paddle.down, key="s")    
screen.onkeyrelease(l_paddle.release_down, key="s")

screen.onkeypress(r_paddle.up, key="Up")
screen.onkeyrelease(r_paddle.release_up, key="Up")

screen.onkeypress(r_paddle.down, key="Down")
screen.onkeyrelease(r_paddle.release_down, key="Down")


def end_game():
    global game_is_on
    game_is_on = False

scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move()

    if l_paddle.moving_up:
        l_paddle.up()

    if l_paddle.moving_down:
        l_paddle.down()

    if r_paddle.moving_up:
        r_paddle.up()

    if r_paddle.moving_down:
        r_paddle.down()

    if (ball.ycor() + 15 >= HEIGHT//2 or ball.ycor() - 15 <= -HEIGHT//2):
        print("bounce")
        ball.bounce_y()

    if ball.distance(l_paddle) < 10 and ball.xcor() < -WIDTH//2 - 50:
        print("bounce l_paddle")
        ball.bounce_x()

    if ball.distance(r_paddle) < 10 and ball.xcor() > WIDTH//2 + 50:
        print("bounce r_paddle")
        ball.bounce_x()

screen.exitonclick()

