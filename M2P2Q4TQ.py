# Written by Tamer Quran
# 07/15/2021
# This Program converts Fahrenheit to Celsius
# (50°F - 32) x .5556 = 10°C (This is just an example I found on googled to use as a example equation)
Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
# At first I didn't add the round command to the equation and it was giving me lots of decimals after the answer
# I had to google how to round a python code and look at other problems to get it to work how I wanted
Celsius = round((Fahrenheit - 32) * .5556)
print(f"The temperature in celsius is {Celsius}")
