number = 7

user_input = input("Enter 'y' if you would like to play.").lower()

if user_input == "y":
    # all these following lines are within the above if statement, so following only run if first if is true
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print(f"Well done , you guessed {7}")
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("try again")

        # or can do if user_input in ("y", "Y")
        # using in keyword
