

import random

# Rock Paper Scissors ASCII Art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# print(rock + "\n" + paper)

my_choies = int(input("What do you choose type 0 for Rock, 1 for Paper, 2 for Scissors: "))
arts = [rock, paper, scissors]
if my_choies < 3:
    print(f"\nYour Choise:\n{arts[my_choies]}")
    computer_choies = random.randint(0 ,2)
    print(f"\nComputer Choise:\n{arts[computer_choies]}")

    if my_choies == 0 and computer_choies == 2:
        print("You win")
    elif my_choies == 2 and computer_choies == 1:
        print("You win")
    elif my_choies == 1 and computer_choies == 0:
        print("You win")
    elif my_choies == computer_choies:
        print("Try Again") 
    else:
        print("You Lose")
else:
    print("\nInvalid number try again!")





    

