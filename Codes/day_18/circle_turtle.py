import turtle as t
import random as r

s = t.Screen()
t.speed(11)


def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(r.random(), r.random(), r.random())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)  # or t.left(size_of_gap)


draw_circle(10)
s.exitonclick()
