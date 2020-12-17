

from os import system
from time import sleep
from art import logo

# Calculaotr

# add
def add(n1, n2):
    """
    Add two numbers and return the total
    """
    return n1 + n2

# Subtract


def sub(n1, n2):
    """
    Subtract second number from first number and return the Subtraction
    """
    return n1 - n2

# Multiply


def mul(n1, n2):
    """
    Multiply two numbers and return the total
    """
    return n1 * n2

# Devide


def devi(n1, n2):
    """
    Devide first number by second and return the Devition
    """
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": devi,
}


def calculator():
    print(logo)
    num1 = float(input("What is your first number? "))

    for key in operations:
        print(key)

    end_of_calc = False

    while not end_of_calc:
        op_symble = input("Pick an operation symble: ")
        num2 = float(input("What is your next number? "))
        function_name = operations[op_symble]
        answer = function_name(num1, num2)
        print(f"{num1} {op_symble} {num2} = {answer}")
        if input(f"Type 'y' to continue with {answer} or type 'n' to start to new calculator: ").lower() == "y":
            num1 = answer
        else:
            end_of_calc = True
            sleep(1)
            system('cls')
            calculator()

calculator()



