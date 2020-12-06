
# if else condition

# print("Welcome to the rollercoaster")
# height = int(input("Enter your height in cm: "))

# if height >= 120:
#     print("\nYou can ride rolllercoaster")
# else:
#     print("\nSorry, you have to graw taller")

# --------------------------------------------------------

# odd even numbers

# num = int(input("Enter decimal number: "))
# if (num % 2 == 0):
#     print("this number is an Even")
# else:
#     print("this number is an Odd")

# ----------------------------------------------

# Rollercoaster with differnt pricese for differnt ages (elif)

# print("Welcome to the rollercoaster")
# height = int(input("Enter your height in cm: "))

# if height >= 120:
#     print("\nYou can ride rolllercoaster")
#     age  = int(input("Enter your age: "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("\nSorry, you have to graw taller")

# -----------------------------------------------------

# Leap year

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("this is a Leap Year")
#         else:
#             print("this is not a Leap Year")
#     else:
#         print("this is a Leap Year")
# else:
#     print("this is not a Leap Year")


# --------------------------------------------------------

# Rollercoaster photo


# print("Welcome to the rollercoaster")
# height = int(input("Enter your height in cm: "))

# bill = 0

# if height >= 120:
#     print("\nYou can ride rolllercoaster")
#     age  = int(input("Enter your age: "))
#     if age <= 12:
#         bill = 5
#         print("Please pay for Child ticket $5.")
#     elif age <= 18:
#         bill = 7
#         print("Please pay for Youth ticket $7")
#     else:
#         bill = 12
#         print("Please pay for Adult ticket $12")

#     photo = input("\nDo you want a photo \"Y\" or \"N\" ")
#     if photo == "Y":
#         # add $3 to their bill
#         bill += 3
#     print(f"Please pay ${bill}")

# else:
#     print("\nSorry, you have to graw taller")


# Automatic pizza order program

print("\nWelcome to Python Pizza Deliveries!")
size = input("\nWhat size pizza do you want? S, M, or L ")
add_pepperoni = input("\nDo you want pepperoni? Y or N ")
extra_cheese = input("\nDo you want extra cheese? Y or N ")

total = 0

if size == "S":
    total = 15
elif size == "M":
    total = 20
else:
    total = 25

if add_pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}.")
