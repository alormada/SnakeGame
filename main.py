from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

snake = Snake(screen)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # print(snake.head.position(), food.position())
    snake.move_forward()
    if snake.head.distance(food) <= 15:
        food.new_location()
        scoreboard.update_score()
        snake.create_segment(screen)

screen.exitonclick()