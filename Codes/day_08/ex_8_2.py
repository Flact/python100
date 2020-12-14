

# Write your code below this line 👇
# this code is worng
""" def prime_checker(number):
    for i in range(2, number - 1):
        is_prime = True
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

    # Write your code above this line 👆
    # Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number = n) """


def prime_checker(number):
    if number > 1:
        if number == 2:
            print("It's a prime number.")
        else:
            for i in range(2, 10):
                if number % i == 0:
                    print(f"{number} is not a prime number.")
                    print(f"{i} is a factor of {number}")
                    break
                else:
                    print(f"{number} is a prime number.")
                    break
    else:
        print("Enter a valid number, greater than 1.")


    # Write your code above this line 👆
    # Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
