from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

positions = [(0, 0), (-20, 0), (-40, 0)]

for position in positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()
