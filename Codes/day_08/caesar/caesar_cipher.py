import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode":
        if shift_amount < 26:
            for letter in start_text:
                if (alphabet.index(letter) + shift_amount) < 26:
                    end_text += alphabet[(shift_amount + alphabet.index(letter))]
                else:
                    end_text += alphabet[(shift_amount - (26 - (alphabet.index(letter))))] # 26 because list index end at 25
            print(f"Here's the {cipher_direction}d result: {end_text}")
        else:
            print("Enter valid shift number, less than 26")
    elif cipher_direction == "decode":
        if shift_amount < 26:
            for letter in start_text:
                end_text += alphabet[(alphabet.index(letter)) - shift_amount]
            print(f"Here's the {cipher_direction}d result: {end_text}")
        else:
            print("Enter valid shift number, less than 26")
    else:
        print("Invalid input, Type 'encode' or 'decode'")
    
    

caesar(text, shift, direction)