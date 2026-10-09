
from time import sleep
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
        self.write("PONG", align="center", font=("Arial", 48, "bold"))
        self.goto(0, 20)
        self.write("W / S  -  Move left paddle (Player 1)", align="center", font=("Arial", 16, "normal"))
        self.goto(0, -20)
        self.write("Up / Down  -  Move right paddle (Player 2)", align="center", font=("Arial", 16, "normal"))
        self.goto(0, -100)
        prompt = "Press SPACE to play again" if replay else "Press SPACE to start"
        self.write(prompt, align="center", font=("Arial", 20, "bold"))
        self.screen.update()

    def wait_for_start(self):
        game_started = False

        def start_game():
            nonlocal game_started
            game_started = True

        self.screen.onkeypress(start_game, key="space")
        self.screen.listen()
        while not game_started:
            self.screen.update()
            sleep(0.05)

        self.clear()

    def countdown(self):
        for number in ("3", "2", "1", "GO!"):
            self.clear()
            self.goto(0, 0)
            self.write(number, align="center", font=("Arial", 48, "bold"))
            self.screen.update()
            sleep(1)
        self.clear()