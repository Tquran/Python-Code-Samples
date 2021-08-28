# Tamer Quran
# 8/24/2021
# This program Takes an input of the year from the user and tells them if it is a leap year
# Also if it is divisible by 4 its is good, if divisible by 100 it is not good, but divisible by 400 is good.
year = int(input("What year would you like to check?"))
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                # True and False has to be capital to be used
            else:
                return False
        else:
            return True
    else:
        return False


print(leap(year))

