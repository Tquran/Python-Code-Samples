# Tamer Quran
# 7/29/2021
# This gives a list from 1 to 50. The numbers that aren't divisible by 3,5,or both they are left alone.
# if they are divisible then it replaces the number and says what it is divisible by.
for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        print("Divisible by three")
    if i % 5 == 0 and i % 3 != 0:
        print("Divisible by five")
    if i % 5 == 0 and i % 3 == 0:
        print("Divisible by both")
    if i % 3 != 0 and i % 5 != 0:
        print(i)
# The and statements are needed to tell the program that if the number is divisible by both then it only needs
# to print the last satement.
# Another thing to remember is that Modulus is % and stands for divisible.
