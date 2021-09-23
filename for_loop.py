friends = ["Sue", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend!")

# calculate average grades
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

# loops
for grade in grades:
    total = total + grade

print(total / amount)

# total = total + grade is the same as total += grade

# or don't really need loop, can use sum
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)
