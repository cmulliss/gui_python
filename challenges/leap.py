year = int(input("Enter the year you want to check: "))
year = 1900 <= year <= 10 ** 5


def leap_year(year):

    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


print(year)

# 2000	2004

# return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
