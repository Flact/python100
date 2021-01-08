
# from turtle import Turtle, Screen
#
# t = Turtle()
#
# print(t)
# t.shape("turtle")
# t.forward(100)
#
# s = Screen()
# s.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)