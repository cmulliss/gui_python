n = int(input())

1 <= n >= 100
if (n % 2) == 1:
    print("Weird")
elif (n % 2) == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif (n % 2) == 0 and n >= 6 and n <= 20:
    print("Weird")
elif (n % 2) == 0 and n > 20:
    print("Not Weird")


# Python Program to Check if a Number is Odd or Even
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
# print("{0} is Even number". format(num))
# else:
# print("{0} is Odd number". format(num))
