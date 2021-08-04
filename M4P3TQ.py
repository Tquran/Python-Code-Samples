# Tamer Quran
# 7/29/2021
# This program is meant to allow a user to create a simple shape and color it in.

number_of_sides_int = int(input("How many sides does it have?"))
length_int = int(input("What is the length of the side?"))
line_color = input("What color is the line?")
fill_color = input("What color is the inside?")
import turtle
wn = turtle.Screen()
# wn.bgcolor(fill_color) This line can be added to color in the background.
tamer = turtle.Turtle()
tamer.color(line_color)
tamer.fillcolor(fill_color)
tamer.begin_fill()
for i in range(number_of_sides_int):
    tamer.forward(length_int)
    tamer.left(360 / number_of_sides_int)
tamer.end_fill()
wn.exitonclick()
# The numbers and colors inputted can be changed around to create different stuff.
