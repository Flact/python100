from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_guess)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
is_race_on = False

# creating multiple instances of turtles
for index in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[index])
    t.penup()
    t.goto(x=-230, y=y_positions[index])
    all_turtles.append(t)

print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:  # this loop maintain each turtle move by
        # random pixels on one iteration of while loop
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've win {wining_color} turtle is the winner.")
            else:
                print(f"You've lose {wining_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
