number = 7


# creates an infinite loop, so need break keyword
while True:
    user_input = input("Enter 'y' if you would like to play? (Y/n)")

    if user_input == "n":
        break
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print(f"Well done , you guessed {7}")

    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("try again")

    # or can do if user_input in ("y", "Y")
    # using in keyword
