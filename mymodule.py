def divide(dividend, divisor):
    return dividend / divisor


print("mymodule.py:", __name__)


# __name__, referred to as 'dunder main', is a global variable in python, which changes depending on which file you are in. Enables you to differentiate between the file you are in, and the file you import.
