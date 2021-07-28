# Written by Tamer Quran
# 07/15/2021
# This Program will calculate a persons BMI by asking their height and weight
# Imperial equation used for BMI [(lbs x 703)/ inches^2] Height is calculated in inches
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in lbs: "))
# After putting in the
BMI = (weight * 703) / height**2
print(f"Your BMI is {BMI}")
