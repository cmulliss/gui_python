numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(doubled)

# usually all in one line
# build it with what you want to put in the new list, x * 2
# for the variable you are using in numbers
friends = ["Sue", "Steve", "Bob", "Sam"]

# starts_s = []

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

# print(starts_s)

# or can do as list comprehension
# 1st friend is the friends name, then the iteration, then if
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)
