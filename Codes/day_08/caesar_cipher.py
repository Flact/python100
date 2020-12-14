
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(plain_text, shift_amount):
    cipher_plain_text = ''
    if shift_amount < 26:
        for letter in plain_text:
            if (alphabet.index(letter) + shift_amount) < 26:
                cipher_plain_text += alphabet[(shift_amount + alphabet.index(letter))]
            else:
                cipher_plain_text += alphabet[(shift_amount - (26 - (alphabet.index(letter))))]
        print(str(cipher_plain_text))
    else:
        print("Enter valid shift number, less than 26")
    

encrypt(text, shift)

# for l in text:
#     print(alphabet.index(l))

# print(shift)


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 