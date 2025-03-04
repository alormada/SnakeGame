from turtle import Turtle

class Snake:
    def __init__(self):
        self.last_seg_pos = (0, 0)
        self.count = 0
        self.segments = []
        self.create_snake()
        self.tail = []


    def create_snake(self):
        self.last_seg_pos = 0, 0
        for i in range(3):
            self.create_segment()
            self.segments[i].goto(-i * 20, 0)
            self.last_seg_pos = (-i * 20, 0)
            print(self.segments[i].position())
        self.head = self.segments[0]
        self.tail = self.segments[1:]

    def create_segment(self):
        new_seg = Turtle()
        new_seg.penup()
        new_seg.shape("square")
        new_seg.color("red")
        new_seg.goto(self.last_seg_pos)
        self.segments.append(new_seg)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

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
        # if self.count != 2:
        # print(self.segments)
        # print(f"{self.count}")
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
            # print(f"SEG i {i} POSITION: {self.segments[i].xcor()} {self.segments[i].ycor()}")
            # print(f"SEG i - 1 {i - 1} POSITION: {self.segments[i - 1].xcor()} {self.segments[i - 1].ycor()}")
        self.head = self.segments[0]
        self.head.forward(20)
        # print(f"HEAD POSITION: {self.head.xcor()} {self.head.ycor()}")
        self.last_seg_pos = (self.segments[-1].xcor(), self.segments[-1].ycor())
        # else:
        #     for seg in self.segments:
        #         seg.forward(2)
        #     self.count += 1
        #     self.last_seg_pos = (self.segments[-1].xcor(), self.segments[-1].ycor())