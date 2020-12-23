

from art import logo
import random
from os import system
from time import sleep

attempts = 0
random_number = random.randint(1, 100)
guss_number = 0


# too low -> 0% - 25%
# more than that -> 25% - 50%
# little more than that -> 50% - 75%
# very close -> 75% - 100%


# too High -> 0% - 25%
# Less than that -> 25% - 50%
# little less than that -> 50% - 75%
# very close -> 75% - 100%

def cal_percentage(guss_n, rand_n):
    """
    docstring
    """
    return 100 - (rand_n - guss_n)
    


def do_the_thing(chances):
    """
    docstring
    """
    differnce = random_number - guss_number

    if differnce < 0:
        pass
    else:
        pass

    while chances != 0 and random_number != guss_number:
        # the fuction to be done
        chances -= 1
        if chances == 0:
            print("\nYou lose")
        pass


def start_fuction():
    sleep(0.5)
    system("cls")
    print(f"{logo} \nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        do_the_thing(10)
    elif difficulty == "hard":
        do_the_thing(5)
    elif input("Wrong input, To start over type 'y' or not type 'n'").lower() == "y":
        start_fuction()


start_fuction()



