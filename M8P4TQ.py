# Tamer Quran
# 8/26/2021
# This program gives us the tens of a list from 0 to 50.
numList = []
counter = 0

while counter < 51:
    #  % 10 means that the number is divisible by 10
    if counter % 10 == 0:
        numList.append(counter)
    counter += 1
print(numList)
