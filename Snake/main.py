from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from homescreen import HomeScreen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

home_screen = HomeScreen(screen)

screen.listen()

home_screen.display()
home_screen.wait_for_start()
home_screen.countdown()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_is_on = True
START_DELAY = 0.1
MIN_DELAY = 0.03
SPEED_INCREMENT = 0.005


def end_game():
    global game_is_on
    game_is_on = False


def play_round():
    global game_is_on
    game_is_on = True

    while game_is_on:
        screen.update()
        delay = max(MIN_DELAY, START_DELAY - scoreboard.score * SPEED_INCREMENT)
        time.sleep(delay)
        snake.move()

        if snake.head.distance(food) < 15:
            snake.add_segment()
            food.refresh()
            scoreboard.increase_score()

        hit_wall = (
            snake.head.xcor() > 295
            or snake.head.xcor() < -295
            or snake.head.ycor() > 295
            or snake.head.ycor() < -295
        )
        if hit_wall or snake.collide_with_self():
            scoreboard.game_over()
            game_is_on = False


screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=end_game, key="Escape")

while True:
    play_round()
    snake.hide()
    food.hide()
    scoreboard.hide()
    screen.update()
    home_screen.display_game_over()
    if not home_screen.wait_for_replay():
        screen.bye()
        break
    snake.reset()
    food.refresh()
    scoreboard.reset()
    screen.update()
    home_screen.countdown()

screen.exitonclick()
