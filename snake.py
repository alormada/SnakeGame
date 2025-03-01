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
        self.head = self.segments[0]

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_forward(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        self.head.forward(20)