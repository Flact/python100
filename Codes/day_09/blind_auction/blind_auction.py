from os import system
from time import sleep
from art import logo
# sleep(2)
# system('cls')


print(logo)

def heigest_bid(bid_list):
    h_bid = 0
    winner = ""
    for bid in bid_list:
        if h_bid < bid_list[bid]:
            h_bid = bid_list[bid]
            winner = bid
    print(f"\nThe winner is {winner} with a bid of ${h_bid}")


bid_again = True
one_bid = {}

while bid_again:
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    value = int(input("What's your bid? $"))
    one_bid[name] = value
    responce = input("Are there any other bidders ? Type 'yes' or 'no'. ").lower()
    if responce == 'no':
        bid_again = False
        heigest_bid(one_bid)
    elif responce == 'yes':
        sleep(2)
        system('cls')
    else:
        print("Wrong input, type 'yes' or 'no'")
        sleep(2)
        system('cls')


