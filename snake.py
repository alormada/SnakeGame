from turtle import Turtle

class Snake:
    def __init__(self, screen):
        self.last_seg_pos = (0, 0)
        self.segments = []
        x_pos = [0, -20, -40, -60, -80, -100]
        for i in range(3):
            self.create_segment(screen)
            self.head = self.segments[0]
            self.move_forward()

    def create_segment(self, screen):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(self.last_seg_pos)
        tim.shapesize()
        screen.tracer(0)
        self.segments.append(tim)

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
        self.last_seg_pos = (self.segments[-1].xcor(), self.segments[-1].ycor())