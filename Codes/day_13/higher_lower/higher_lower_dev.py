

import random
from os import system
from time import sleep
from art import logo, vs
from game_data import data


# print(logo)
# print(vs)

# print(random.choice(data))


def persons_generator():
    end_of_range = len(data) - 1
    num1 = random.randint(0 , end_of_range)
    num2 = random.randint(0 , end_of_range)

    while num1 == num2:
        num2 = random.randint(0 , end_of_range)

    return [num1, num2]

# x, y = persons_generator()

# print(persons_generator())
# print(type(persons_generator()))

""" # Ternary Operators *****
# value_if_true if condition else value_if_false
**************
# condition = True
# print(2 if condition else 1/0) """


def winner(p1, p2):
    """
    docstring
    """
    return p1[1] if p1[0] > p2[0] else p2[1]



    

# print(f"\n{person1}\n\n{person2}")

# print(type(person1['follower_count']))

# print(f"Compare A {person1['name']}, {person1['description']}, from {person1['country']}\n{vs}\n"+
#     f"sdhfkjshfkhsdkjfhsdhk")

score = 0

while True:
    sleep(0.5)
    system("cls")

    elements = persons_generator()
    person1 = data[elements[0]]
    person2 = data[elements[1]]

    person1["tag"] = "a"
    person2["tag"] = "b"

    print(logo)
    print(f"You're right! Current score: {score}\n" if score > 0 else "")
    print(f"Compare A {person1['name']}, {person1['description']}, from {person1['country']}.\n{vs}\n"+
    f"Against B: {person2['name']}, {person2['description']}, from {person2['country']}.")
    answer = input("Who has more folloers? Type 'A' or 'B': ").lower()
    result = winner([person1["follower_count"], person1["tag"]], [person2["follower_count"], person2["tag"]])
    # print(result)
    if answer in ["a", "b"]:
        if answer == result:
            score += 1
        else:
            print(f"Sorry, Wrong answer. Final Score: {score}")
            break
    else:
        print(f"Sorry, Wrong input. Start Over")
        
    
# gaming_time()


# print(persons_generator()[0]['name']) # 0 is the first element of the return 





""" # Example
def multiple_returns(): 
    y = "Sample Text"
    x   = 20
    return y, x

value1, value2 = multiple_returns()
print(value1)
print(value2)
# End of Example """


