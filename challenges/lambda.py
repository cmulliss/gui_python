# lambda fns dont have a name and only used to return values.


print((lambda x, y: x + y)(5, 7))


# def double(x):
#     return x * 2


# list comprehensions
sequence = [1, 2, 3, 4, 5]
# doubled = [double(x) for x in sequence]
doubled = [(lambda x: x * 2)(x) for x in sequence]

print(doubled)

# if you want to use lambda fns, use map
# doubled = map(double, sequence)
# need to convert to list as map doesn't return a list, but returns a map object
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
