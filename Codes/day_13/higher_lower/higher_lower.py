

import random
from art import logo
from art import vs
from game_data import data


# print(logo)
# print(vs)

# print(random.choice(data))


def persons_generator():
    num1 = random.randint(0 , (len(data) - 1))
    num2 = random.randint(0 , (len(data) - 1))

    while num1 != num2:
        num2 = random.randint(0 , (len(data) - 1))

    return num1, num2

""" # Example
def multiple_returns(): 
    y = "Sample Text"
    x   = 20
    return y, x

value1, value2 = multiple_returns()
print(value1)
print(value2)
# End of Example """


