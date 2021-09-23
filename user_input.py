name = input("What is your name: ").capitalize()
print(name)

# input always gives a string, so need to convert strings to numbers
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8  # Make sure this is correct
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")
