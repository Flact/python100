# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# f = open("Input/Names/invited_names.txt", "r")
# print(f.readlines())
# x = f.readlines()
# y = x.strip()
#
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("Input/Letters/starting_letter.docx", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        # print(new_letter)
        # print(stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", "w") as completed_letter:
            completed_letter.write(new_letter)

