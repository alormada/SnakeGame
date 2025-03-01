from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

snake = Snake(screen)

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    # snake.turn_left(screen)
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    # screen.update()
    snake.move_forward()

screen.exitonclick()