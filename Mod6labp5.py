# Tamer Quran
# 8/12/2021
# This turtle function is used to create 5 squares within each other
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
# drawSquare(alex, 50)

x = 240
for i in range(6):
    x = x - 40
    drawSquare(alex, x)
    alex.up()
# alex.up and alex.down are like when you take the pen off of a surface to start a new drawing elsewhere.
# If alex.up/down is not used the line will continue and the drawing will be done incorrectly.
    alex.forward(20)
    alex.left(90)
    alex.forward(20)
    alex.down()
    alex.right(90)
    # x = x - 20
wn.exitonclick()
