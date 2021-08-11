# Tamer Quran
# 8/5/2021
# This program outputs a random day of the week
import random
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# for weekDays each day has to have it's own "" marks or else it will just give you random letters and even commas.
a = random.choice(weekDays)
print(a)
