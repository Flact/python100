""" 
Bug = ""

programming_dictionary = {Bug: "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again",
                          }

print(programming_dictionary[Bug]) """



""" programming_dictionary = {123: "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again",
                          }

print(programming_dictionary[123]) """

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          }

programming_dictionary["Loop"] = "The action of doing something over and over again"

# print(programming_dictionary)

# Create an empty dictionary
# empty_dictionary = {}

# wipe a dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in dictionry
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

