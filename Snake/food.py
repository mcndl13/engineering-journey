import random
from turtle import Turtle

class Food (Turtle):
    size = 15

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        self.x_cord = 0
        self.y_cord = 0


    def refresh(self):
        self.showturtle()
        self.x_cord = random.randint(-250, 250)
        self.y_cord = random.randint(-250, 280)
        self.goto(self.x_cord, self.y_cord)

    def hide(self):
        self.hideturtle()