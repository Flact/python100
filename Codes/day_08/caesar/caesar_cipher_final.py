import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # double the list because to remove complexcity alphabet[(shift_amount - (26 - (alphabet.index(letter))))]

print(art.logo)

def caesar(start_text, shift_amount, cipher_direction):
    if shift_amount < 26:
        if cipher_direction == "encode":
            loop_through(start_text, shift_amount, cipher_direction)
        elif cipher_direction == "decode":
            loop_through(start_text, shift_amount * -1, cipher_direction)
        else:
            print("Invalid input, Type 'encode' or 'decode'")
    else:
        print("Enter valid shift number, less than 26")


def loop_through(text, amount, direction):
    end_text = ""
    for char in text:
        if char in alphabet:
            end_text += alphabet[(alphabet.index(char) + amount)]
        else:
            end_text += char
    print(f"Here's the {direction}d result: {end_text}")


should_end = True
while should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = False
        print("Goodbye")
    elif restart == "yes":
        should_end = True
    else:
        print("Invalid Input")
        break
