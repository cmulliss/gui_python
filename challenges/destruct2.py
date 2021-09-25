people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# separate into elements
# 1st value is head, others are tail
head, *tail = [1, 2, 3, 4, 5]
# gives 1 [2, 3, 4, 5]
print(head, tail)

# or can do:
*head, tail = [1, 2, 3, 4, 5]
print(head, tail)
# gives [1, 2, 3, 4] 5
