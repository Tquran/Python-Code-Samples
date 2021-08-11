# Tamer Quran
# 8/5/2021
# This program outputs pi with a algorithm and with the import function.
import math
k = 1
s = 0
# Range function is used to allow for the amount of numbers that pi uses
for i in range(1000000):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k
    k += 2
print(s)
print(math.pi)
