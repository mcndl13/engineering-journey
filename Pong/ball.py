
from turtle import Turtle
import random

VELOCITY = 1.3

class Ball (Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("circle")
        self.turtlesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 0)
        self.move_x = (10 * random.choice([-1, 1])) * VELOCITY
        self.move_y = 10 * random.choice([-1, 1]) * VELOCITY

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1