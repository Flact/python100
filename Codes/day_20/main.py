from turtle import Screen
from snake import Snake
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.3)
    snake.move()

screen.exitonclick()
