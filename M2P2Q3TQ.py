# Written by Tamer Quran
# 07/15/2021
# This program gives the area of a circle from the inputted radius
# (from math import pi) can also be used in place of pi = 3.14 but it is easier in this case
pi = 3.14
# I only used pi up to the hundredths place so the answers where only to the same place
r = float(input("What is the radius of the circle? : "))
print("The area of the circle with a radius of " + str(r) + " is: " + str(pi * r**2))
