from turtle import Turtle

MOVING_DISTANCE = 20


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        start_x = 0
        for _ in range(4):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.goto(start_x, 0)
            self.segments.append(new_segment)
            start_x -= 20

    def add_segment(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        last_segment = self.segments[len(self.segments) - 1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)

    def move(self):
        #Move each single segment to the position of the one in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        #Move the first segment forward so the rest will follow along
        self.segments[0].forward(MOVING_DISTANCE)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

