

from data import MENU, resources, coins, logo
from time import sleep

# print(MENU['cappuccino']['ingredients']['water'])


inpt_choies = ["espresso", "latte", "cappuccino", "report", "off"]
profit = 0.0


print(f"{logo}\n-------------MENU-------------")

for key in MENU:
    print(f"\n{key}: ${MENU[key]['cost']}")


def resource_modifire(ing):
    """
    docstring
    """
    for itm in ing:
        resources[itm] -= ing[itm]


def coins_collector(ch, drink):
    t = 0.0
    cost = drink['cost']  # Menu item cost(cost)
    print(f"\n{ch.title()} price is ${cost}, Please insert coins")
    for coin in coins:
        x = (input(f"\nHow many {coin}s: "))
        # print(t)
        if int(x) in range(101):
            t += float(x) * coins[coin]
        elif t > 0:
            print(
                "\nWrong input, Here's your money refunded ${t}\nPlease come back later")
        else:
            print("\nWrong input, Please come back later")
    if t > cost:
        print(f"Here's your {ch}. and Here's Your Change: ${t - cost}")
        global profit
        profit += cost
        resource_modifire(drink["ingredients"])
    elif t == cost:
        print(f"Here's your {ch}")
        resource_modifire(drink["ingredients"])
    else:
        print(
            f"\nNot enuogh money\nHere's your money refunded ${t}\nPlease come back later")
    # return t


def is_resources(ing):
    """
    docstring
    """
    for item in ing:
        if resources[item] < ing[item]:
            print(f"\nInsufficient {item}, Please come back")
            return False
    return True


while True:
    choise = input("\nWhat would you like ('Espresso'/'Latte'/'Cappuccino'): ").lower()
    if choise in inpt_choies:
        if choise == "report":
            for res in resources:
                print(f"\n{res}:\t{resources[res]}")
            print(f"Proffit: ${profit}")
        elif choise == "off":
            break
        else:
            if not is_resources(MENU[choise]["ingredients"]):
                break
            drink = MENU[choise]
            coins_collector(choise, drink)

    elif input("Wrong input, Do you want to start again? (y/n)").lower() == "y":
        continue
    else:
        print("Wrong input, Exiting Program...")
        sleep(1)
        break
