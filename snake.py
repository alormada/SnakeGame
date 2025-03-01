from turtle import Turtle

class Snake:
    def __init__(self, screen):
        self.segments = []
        x_pos = [0, -20, -40, -60, -80, -100]
        for i in range(3):
            tim = Turtle()
            tim.penup()
            tim.shape("square")
            tim.color("white")
            tim.setx(x_pos[i])
            tim.shapesize()
            screen.tracer(0)
            self.segments.append(tim)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move_forward(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        self.segments[0].forward(20)