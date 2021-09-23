week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

for day in week:
    print(day)

# if and in
user_input = input("which day of the week is it today? ").capitalize()

if user_input in week:
    # print("It is %s" % (user_input))
    print(f"It is {user_input}")
else:
    print(("try again"))
