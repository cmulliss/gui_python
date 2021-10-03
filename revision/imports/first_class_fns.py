def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


# see uppacking args lecture
def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
# fns are variables
print(result)
