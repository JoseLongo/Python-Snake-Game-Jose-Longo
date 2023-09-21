import turtle
from turtle import Turtle
import random
turtle.colormode(255)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.set_color()
        self.set_position()

    def set_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_color = (r, g, b)
        self.color(new_color)

    def set_position(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 250)
        self.goto((x, y))

    def reset(self):
        self.set_color()
        self.set_position()