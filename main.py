from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def endgame():
    choice = screen.textinput(title="Game over", prompt="Do you want to play again? (yes/no): ")
    if choice != "no":
        screen.listen()
        return True
    else:
        return False

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
snake = Snake()
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
    snake.move_forward()
    # print(snake.head.position(), food.position())

    # Detect collision with food
    if snake.head.distance(food) <= 20:
        scoreboard.update_score()
        snake.create_segment()
        food.new_location()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = endgame()
        scoreboard.reset()
        snake.reset_snake()

    # Detect collision with tail
    for seg in snake.tail:
        if snake.head.distance(seg) < 10:
            game_on = endgame()
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()