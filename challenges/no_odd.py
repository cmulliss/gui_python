list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in list1:
    if num % 2 == 0:
        print(num)

# using list comprehensions

list2 = [10, 21, 4, 45, 66, 93]
evens = [num for num in list2 if num % 2 == 0]
print(evens)
