

from data import MENU, resources, coins, logo

# print(MENU['cappuccino']['ingredients']['water'])


inpt_choies = ["espresso", "latte", "cappuccino", "report"]
# print(inpt_choies)

# print(type(calculator()))
# print(calculator())

# while True:
print(f"{logo}\n-------------MENU-------------")

for key in MENU:
    print(f"\n{key}: ${MENU[key]['cost']}")


def resource_modifire(wtr, milk, cof):
    """
    docstring
    """
    pass

def get_resource(parameter_list):
    """
    docstring
    """
    pass

def coins_collector(ch):
    t = 0.0
    mc = MENU[ch]['cost'] # Menu item cost(mc)
    for coin in coins:
        t += float(input(f"How many {coin}s: ")) * coins[coin]
        # print(t)
    if t > mc:
        pass
    elif t == mc:
        print(f"Here's your {ch}")
    else:
        print("Not enuogh money")
    return t


choise = input("What would you like (espresso/latte/cappuccino): ").lower()
if choise in inpt_choies:
    if choise == "report":
        pass
    else:
        print("Please insert coins")
        coins_collector(choise)
    
else:
    input("Wrong input, Do you want to start again? (y/n)").lower() in ["y", "n"]
