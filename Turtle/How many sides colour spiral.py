#kush

import turtle

t = turtle.Pen()

turtle.bgcolor("black")

sides = eval(input("Enter a number of sides between 2 and 6: "))

colors = ["red", "yellow", "green", "orange", "green", "purple"]

for x in range(360):
    t.speed(0)
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
