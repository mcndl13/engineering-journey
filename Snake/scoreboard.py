from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 18, "normal"))
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        self.score = 0
        self.clear()
        self.goto(0, 265)
        self.update_score()

    def hide(self):
        self.clear()
