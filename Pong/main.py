from turtle import Screen

from game import Game
from homescreen import HomeScreen
from settings import HEIGHT, WIDTH


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

home_screen = HomeScreen(screen)
home_screen.display()
home_screen.wait_for_start()
home_screen.countdown()
game = Game(screen)

while True:
    game.run()
    home_screen.display(replay=True)
    home_screen.wait_for_start()
    game.reset()
    home_screen.countdown()
