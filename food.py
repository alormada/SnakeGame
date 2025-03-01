from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.new_location()

    def new_location(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        location = (x, y)
        self.goto(location)