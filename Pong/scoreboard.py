from turtle import Turtle
from settings import HEIGHT, WIDTH

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-WIDTH//4 , HEIGHT//2 - 50)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-WIDTH//4 , HEIGHT//2 - 80)
        self.write(f"{self.l_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(WIDTH//4, HEIGHT//2 - 80)
        self.write(f"{self.r_score}", align="center", font=("Arial", 50, "normal"))
    

    def point(self, player):
        if player == "left":
            self.l_score += 1
        elif player == "right":
            self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over\nWinner: {'P1' if self.l_score > self.r_score else 'P2'}", align="center", font=("Arial", 20, "normal"))