from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

def end_game():
    global game_is_on
    game_is_on = False

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")   
screen.onkey(fun=end_game, key="Escape")
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if(snake.head.distance(food) < 15):
        snake.add_segment()
        food.refresh()
        scoreboard.increase_score()

    if(snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295 or snake.collide_with_self()):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
