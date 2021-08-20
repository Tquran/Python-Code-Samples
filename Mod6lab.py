# Tamer Quran
# 8/12/2021
# Module 6 Problem 1 - This program gives the area of a circle using the radius chosen by the user. It also uses functions and math.
import math
r = int(input("What is the radius?"))
def findArea(r):
# math.pi can be shortened by using pi = math.pi but this is not needed
    return math.pi * (r*r);
print("Area of circle = " + str(findArea(r)));
# Remember to place r in the findArea() or it will not work