# try:
#     file = open("a_file.txt")
#     d = {"key": "Value"}
#     print(d["aaaa"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as err_message:
#     print(f"That {err_message} not found")
# else:
#     file = open("a_file.txt", "r")
#     cont = file.read()
#     print(cont)
# finally:
#     # file.close()
#     # print("File Closed")
#     raise TypeError("This is a custom err message")


# def divide_else(a, b):
#     try:
#         print(a / b)
#     except ZeroDivisionError as e:
#         print('catch ZeroDivisionError:', e)
#     else:
#         print('finish (no error)')
#
#
# divide_else(1, 0)


# h = float(input("Height: "))
# w = int(input("Weight: "))
#
# if h > 3:
#     raise ValueError("Human height should not over 3m")
#
# bmi = h / w ** 2
#
# print(bmi)
