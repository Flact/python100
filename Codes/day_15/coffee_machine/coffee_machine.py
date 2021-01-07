

from data import MENU, resources, coins, logo
from time import sleep


inpt_choies = ["espresso", "latte", "cappuccino", "report", "off"]
profit = 0.0


def resource_modifire(ing):
    """
    Manage resources afetr odering a drink
    """
    for itm in ing:
        resources[itm] -= ing[itm]


def coins_collector(ch, drink):
    t = 0.0
    cost = drink['cost']  # Menu item cost(cost)
    print(f"\n{ch.title()} price is ${cost}, Please insert coins")
    for coin in coins:
        x = (input(f"\nHow many {coin}s: "))
        if x.isdigit() and int(x) in range(0, 301):
            t += float(x) * coins[coin]
            if t == cost or t > cost:
                break

        elif t > 0:  # In middel of the loop if enter wrong characters
            print(f"\nWrong input, Here's your money refunded ${t}\nPlease come back later")
        else:
            print("\nWrong input 🤭, Start again..")
            sleep(1)
            break
    if not t == 0 and t > cost:
        print(f"Here's your {ch} ☕. and Here's Your Change:💸 ${round((t - cost), 2)}")
        global profit
        profit += cost
        resource_modifire(drink["ingredients"])
    elif t == cost:
        print(f"Here's your {ch} ☕ Have a good one 👻")
        resource_modifire(drink["ingredients"])
    elif t > 0:
        print(f"\nNot enuogh money\nHere's your money refunded ${t}\nPlease come back later")


def is_resources(ing):
    """
    Chech if resourses is enough and return if good
    """
    for item in ing:
        if resources[item] < ing[item]:
            print(f"\nInsufficient {item}, Please come back")
            return False
    return True


while True:
    print(f"{logo}\n-------------MENU-------------")
    for key in MENU:
        print(f"\n{key}: ${MENU[key]['cost']}")
    choise = input(
        "\nWhat would you like ('Espresso'/'Latte'/'Cappuccino'): ").lower()
    if choise in inpt_choies:
        if choise == "report":
            for res in resources:
                print(f"\n{res}:\t{resources[res]}")
            print(f"\nProffit: ${profit}")
        elif choise == "off":
            break
        else:
            if not is_resources(MENU[choise]["ingredients"]):
                sleep(1)
                break
            drink = MENU[choise]
            coins_collector(choise, drink)

    elif input("\nWrong input, Do you want to start again? (y/n): ").lower() == "y": continue
    else:
        print("\nWrong input 😜, Exiting Program... 👋")
        sleep(1)
        break
