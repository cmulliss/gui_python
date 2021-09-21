day_of_week = input("what day is it? ").lower()
if day_of_week == "monday":
    print(f"Have a good start to your week. ")
elif day_of_week == "saturday" or "sunday":
    print("Have a good weekend")
else:
    print("Have a good day whatever day it is")
