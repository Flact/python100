import random
from os import system
from time import sleep
from art import logo, vs
from game_data import data


def winner(answer, p1, p2):
    return answer == "a" if p1["follower_count"] > p2["follower_count"] else answer == "b"


def formatter(person):
    return f"{person['name']}, {person['description']}, from {person['country']}."


def game():
    score = 0
    person1 = random.choice(data)
    person2 = random.choice(data)

    while True:
        sleep(1)
        system("cls")

        person1 = person2
        person2 = random.choice(data)

        while person1 == person2:
            person2 = random.choice(data)

        print(logo)
        print(f"You're right! Current score: {score}\n" if score > 0 else "")
        print(f"Compare A: {formatter(person1)}.\n{vs}\n"f"Against B: {formatter(person2)}")

        answer = input("Who has more folloers? Type 'A' or 'B': ").lower()
        result = winner(answer, person1, person2)
        
        if answer in ["a", "b"]:
            if result:
                score += 1
            else:
                print(f"Sorry, Wrong answer. Final Score: {score}")
                break
        else:
            print(f"Sorry, Wrong input. Start Over")
        
game()