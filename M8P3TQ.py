# Tamer Quran
# 8/26/2021
# Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together.
# Continue asking for a number until the sum of the list of numbers is greater than 100.

numList = []
sum = 0

while sum < 100:
    n = int(input("Enter a number: "))
    numList.append(n)
    sum += n # sum = sum + n

print(numList)
print(sum)
