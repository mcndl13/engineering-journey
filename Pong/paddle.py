from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.color("white")
        self.speed(10)
        self.goto(position)
        self.player = "left" if position[0] < 0 else "right"

        self.moving_up = False
        self.moving_down = False

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.moving_up = True

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.moving_down = True

    def release_up(self):
        self.moving_up = False

    def release_down(self):
        self.moving_down = False