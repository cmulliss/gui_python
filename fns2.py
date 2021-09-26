def add(x, y):
    result = x + y
    print(result)


add(5, 3)


# positional arguments
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")


name = input("enter your name: ")
surname = input("enter your surname: ")
say_hello(name, surname)
