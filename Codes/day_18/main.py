import turtle as tur
import random

t = tur.Turtle()
screen = tur.Screen()

t.shape("turtle")
tur.colormode(255.0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# t.forward(100)
# t.right(90)

# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# t.setx(100)
# t.sety(0)
# t.dot(10)
# print(t.position())
# for i in range(10):
#     t.forward(15)
#     t.penup()
#     t.forward(5)
#     t.pendown()

# for i in range(3, 10):
#     t.pencolor(random(), random(), random())
#     for x in range(i):
#         # angle = 360 / i
#         t.right(360 / i)
#         t.forward(100)

angles = [0.0, 90.0, 180.0, 270.0]
# colors = ["blue", "mint cream", "yellow", "dark turquoise", "hot pink", "gold",
#           "black", "sienna", "green yellow", "rosy brown", "tomato", "dark orchid"]
t.pensize(10)
t.speed(6)
for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(angles))

screen.exitonclick()
