from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

def create_snake(x_position):
    name = Turtle()
    name.penup()
    name.setx(x_position)
    name.shape("square")
    name.color("white")
    screen.tracer(0)
    name.shapesize()
    return name

def turn_left():
    snake1.left(90)
    turn_location = snake1.position()
    for j in range(len(snake)):
        screen.update()
        time.sleep(0.1)
        for i in range(1, len(snake)):
            # print(snake[i].position(), snake[i-1].position())
            if snake[i].position() != turn_location:
                snake[i].forward(20)
            else:
                snake[i].left(90)
                snake[i].forward(20)
        snake1.forward(20)

def turn_right():
    snake1.right(90)
    turn_location = snake1.position()
    for j in range(len(snake)):
        screen.update()
        time.sleep(0.1)
        for i in range(1, len(snake)):
            # print(snake[i].position(), snake[i-1].position())
            if snake[i].position() != turn_location:
                snake[i].forward(20)
            else:
                snake[i].right(90)
                snake[i].forward(20)
        snake1.forward(20)


snake1 = create_snake(0)
snake2 = create_snake(-20)
snake3 = create_snake(-40)

snake = [snake1, snake2, snake3]

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(fun=turn_left, key="a")
    screen.onkey(fun=turn_right, key="d")
    for seg in snake:
        seg.forward(20)


screen.exitonclick()