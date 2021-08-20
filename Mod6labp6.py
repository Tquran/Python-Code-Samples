# Tamer Quran
# 8/12/2021
# This turtle function is my attempt to create a picture similar to the one that was provided to us.
import turtle

def drawHexagon(t, sz):
    for i in range(6):
        t.forward(sz)
        t.left(300)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("magenta")
# drawSquare(alex, 50)

x = 50
# The image has 10 hexagons so to get the image you just take 360/10 to get 36 for the degrees needed to turn.
for i in range(10):
    drawHexagon(alex, x)
    alex.left(36)
wn.exitonclick()
