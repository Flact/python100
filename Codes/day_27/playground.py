def add(*args):
    t = 0
    for n in args:
        # print(n)
        t += n
    return t


# print(add(10, 10, 10, 10))

def calculate(n, **kwargs):
    # print(type(kwargs))  #kwargs is dictionary
    # print(kwargs)

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

    n += kwargs["add"]
    # print(f"Add: {n}")
    n *= kwargs["multiply"]
    # print(f"Multiply: {n}")


calculate(2, add=10, multiply=20)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")  # kw is a dict, so 'get' method can access value by key
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# my_car = Car(make="honda", model="accord")
# print(my_car.make)
# print(my_car.model)

my_car = Car(make="honda")
print(my_car.make)
print(my_car.model)
