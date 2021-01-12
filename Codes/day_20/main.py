from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.3)
    for seg_num in range(len(segments) - 1, 0, -1):  # move segments by second to last segment
        # move last segment to next segment position
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
