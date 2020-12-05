
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

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("this is a Leap Year")
        else:
            print("this is not a Leap Year")
    else:
        print("this is a Leap Year")
else:
    print("this is not a Leap Year")


