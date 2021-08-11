# Tamer Quran
# 8/5/2021
# This program uses a for statement to find the factorial of a user inputted number
import math
Num = int(input("What number would you like the factorial for?"))

answer = 1
for i in range(Num):
    answer = (i + 1) * answer
print(answer)
# Outputs can be labeled if needed by adding a line of string with where the code came from
print(math.factorial(Num))
