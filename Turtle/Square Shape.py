#kush

import turtle
import random

turtle.bgcolor("black")
a = turtle.Pen()
w = turtle.Screen()
b = input("Enter your name: ")

for x in range(50):
    a.pencolor("blue")
    a.penup()
    a.forward(x * x + 15)
    a.write(b, font = ("Arial", int(15), "bold"))
    a.pendown()
    a.left(90)
