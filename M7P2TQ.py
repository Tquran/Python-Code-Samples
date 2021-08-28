# Tamer Quran
# 8/24/2021
# This program takes two inputs from a user and tells us if they are greater than, less than, or equal to 10.
x = 10
def evaluateInput1():
    input1 = int(input("what is your first value:"))
    input2 = int(input("what is your second value:"))
    sum = input1 + input2
    if sum == x:
        print("The sum of these values is equal to 10")
    elif sum < x:
        print("The sum of these values is less than 10")
    else:
        print("The sum of these values is greater than 10")


evaluateInput1()
