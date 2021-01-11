# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)

import turtle as t
import random

t.colormode(255.0)

color_list = [(26, 109, 164), (194, 38, 81), (237, 161, 51), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (142, 109, 57),
              (101, 197, 219), (205, 166, 29), (21, 58, 132), (212, 74, 91), (238, 89, 52), (141, 208, 226),
              (119, 192, 140),
              (7, 157, 88), (5, 186, 179), (106, 108, 198), (137, 29, 72), (98, 51, 36), (24, 154, 211),
              (228, 169, 188),
              (152, 213, 194), (174, 187, 221), (232, 174, 164), (31, 91, 94), (85, 46, 33), (35, 46, 83)]
t.speed(10)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100
# t.dot(20, (26, 109, 164))
#
# t.forward(50)
# # t.pendown()
# t.dot(20, (26, 109, 164))
# # t.penup()
# t.forward(50)
# t.dot(20, (26, 109, 164))
# t.home()
# t.setheading(90)
# t.forward(50)
# t.setheading(0)
for r in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if r % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = t.Screen()
screen.exitonclick()
