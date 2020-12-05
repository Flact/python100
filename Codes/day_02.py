
# it will print "H"
# print("Hello"[0])

# ---------------------------

# type checking
# num_char = len(input("What is your name? "))
# this print function will throw a erorr
# print("Your name has " + num_char + " Characters")

# -----------------------------------------------------

# print(type(num_char))
# the fix
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " Characters")

# -----------------------------------------------------------

# this will print 112
# print(1_2 + 100)

# -------------------------------------

# a = float(124)
# print(type(a))

# print(70 + float("100.12"))

# ---------------------------------

# entering two digits numer and add those two digits
# num  = input("Enter two digits number: ")
# print("\n" + str(int(num[0]) + int(num[1])))

# -----------------------------------------------------

# print(2 ** 3)
# print(type( 6 / 2))

# -------------------------------

# PEMDAS
# Parentheses ()
# Exponents **
# Multiplication/Division * /
# Addition/Subtraction + -

# print(3 * 3 + 3 / 3 - 3)

# ---------------------------------

# BMI Calculator
# weight = float(input("Input weight in kg: "))
# height = float(input("Enter hheight in m: "))
# print(int(weight / height ** 2))

# -----------------------------------------------

# ROUND
# print(round(8 / 3, 2))
# print(round(2.66666666, 2))

# ------------------------------------------

# floor division --***
# print(8 // 3)
# print(type(8 // 3))

# -----------------------------------

# f-string
# score = 100
# height = 1.8
# iswinning = True

# print(f"Your score is {score} and your height is {height} You are winng is {iswinning}")

# -------------------------------------------------------------------------------------------

# Years to live calculator(if you live 90yrs)

# age = int(input("Enter your age :"))
# years_remain = 90 - age
# print(f"You have {years_remain * 365} days, {years_remain * 52} weeks, {years_remain * 12} months")

# -------------------------------------------------------------------------------------------------------

# Tip calculator

total_bill = float(input("Welcome to tip claculator\nWhat was the total bill? $"))
precentage = int(input("What precentage whould you like to tip 10, 12 or 15: "))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay {round((total_bill / people) * (1 + precentage / 100) , 2)}")



