from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    
    def __init__(self):
        self.starting_positions = STARTING_POSITIONS
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        
    def create_snake(self):
        for position in self.starting_positions:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.goto(position)
            new_segment.shape("square")
            new_segment.color("white")
            self.snake_segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.goto([self.snake_segments[-1].xcor() - 20, self.snake_segments[-1].ycor()])
        new_segment.shape("square")
        new_segment.color("white")
        self.snake_segments.append(new_segment)
        

    def collide_with_self(self):
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for seg in range(len(self.snake_segments) -1, 0, -1):
            new_x = self.snake_segments[seg-1].xcor()
            new_y = self.snake_segments[seg-1].ycor()
            self.snake_segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.snake_segments:
            segment.hideturtle()
            segment.clear()
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def hide(self):
        for segment in self.snake_segments:
            segment.hideturtle()