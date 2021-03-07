fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as e:
        print(f"Fruit pie, Err is: '{e}'")
    else:
        print(fruit + " pie")


make_pie(4)