import time
from turtle import Turtle


class HomeScreen(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.hideturtle()
        self.color("white")
        self.penup()

    def display(self, replay=False):
        self.clear()
        self.goto(0, 100)
        self.write("SNAKE", align="center", font=("Arial", 48, "bold"))
        self.goto(0, 20)
        self.write("Use the arrow keys to move", align="center",
                   font=("Arial", 18, "normal"))
        self.goto(0, -80)
        prompt = "Press SPACE to play again" if replay else "Press SPACE to start"
        self.write(prompt, align="center", font=("Arial", 20, "bold"))
        self.screen.update()

    def wait_for_start(self):
        started = False

        def start():
            nonlocal started
            started = True

        self.screen.onkeypress(start, key="space")
        self.screen.listen()
        while not started:
            self.screen.update()
            time.sleep(0.05)
        self.clear()

    def display_game_over(self):
        self.clear()
        self.goto(0, 80)
        self.write("GAME OVER", align="center", font=("Arial", 42, "bold"))
        self.goto(0, 0)
        self.write("Play again?", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -60)
        self.write("Y = Yes    N = No", align="center",
                   font=("Arial", 20, "bold"))
        self.screen.update()

    def wait_for_replay(self):
        replay = None

        def play_again():
            nonlocal replay
            replay = True

        def quit_game():
            nonlocal replay
            replay = False

        self.screen.onkeypress(play_again, key="y")
        self.screen.onkeypress(quit_game, key="n")
        self.screen.listen()
        while replay is None:
            self.screen.update()
            time.sleep(0.05)
        self.clear()
        return replay

    def countdown(self):
        for number in ("3", "2", "1", "GO!"):
            self.clear()
            self.goto(0, 0)
            self.write(number, align="center", font=("Arial", 48, "bold"))
            self.screen.update()
            time.sleep(1)
        self.clear()
