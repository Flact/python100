from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    # t.setheading(0)
    t.forward(10)


def move_backward():
    # t.setheading(0)
    t.backward(10)


def move_left():
    # if t.heading() == 90.0:
    #     t.forward(10)
    # else:
    #     t.setheading(0)
    #     t.left(90)
    #     t.forward(10)
    t.left(10)


def move_right():
    # if t.heading() == 270.0:
    #     t.forward(10)
    # else:
    #     t.setheading(0)
    #     t.right(90)
    #     t.forward(10)
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
print(screen.listen())
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
