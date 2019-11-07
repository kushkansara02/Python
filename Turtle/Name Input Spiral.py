#kush

import turtle
import random

turtle.bgcolor("black")
a = turtle.Pen()
w = turtle.Screen()

print("Welcome!")
print("Note: the number of colors you enter must be the same as the number of people to enter>")
f = input("Enter your colors, seperated by spaces: ")
g = input("Enter your people, seperated by spaces: ")
h = f.split()
i = g.split()

for x in range(50):
    a.pencolor(h[x%len(h)])
    a.penup()
    a.forward(x * x)
    a.write(i[x%len(i)], font = ("Arial", int(x), "bold"))
    a.pendown()
    a.left(360/len(i))
