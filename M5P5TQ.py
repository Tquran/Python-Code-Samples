# Tamer Quran
# 8/5/2021
# This program converts radians to degrees
radian_int = int(input("What is the number of radians?"))
# Using this allows for the user to get the answer that they desire.


def convert(radian):
    pi = 3.14159
    degree = radian * (180 / pi)
    return degree
# This algorithm converts radians to degrees


radian = radian_int
print("degree =", (convert(radian)))
