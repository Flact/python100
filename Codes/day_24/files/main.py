# file = open("my_file.txt")
# content = file.read()
#
# print(content)
# file.close()

# "with" keyword don't have to close the file manually
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# # write into file: mode="w" (this will replace previous text)
# with open("my_file.txt", mode="w") as file:
#     file.write("Hello world!")


# append text into file: mode="a" (this will add text to previous text)
# with open("my_file.txt", mode="a") as file:
#     file.write("\nHello world!")

# if there is no file it'll create one (this will only works when "write" mode)
# with open("new_file.txt", mode="w") as file:
#     file.write("New Text into New File")
