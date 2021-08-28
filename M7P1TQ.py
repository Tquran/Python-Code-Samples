# Tamer Quran
# 8/24/2021
# This program takes two inputs from a user and tells us if it is equal or not.

x = input("What number to you want x to be?")
y = input("What number to you want y to be?")


def evaluateInput1(x, y):
    if x == y:
        print('These values are equal')
    else:
        print('These values are not equal')

evaluateInput1(x, y)