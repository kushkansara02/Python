#Kush Kansara
#April 10, 2018
#Duplicating Graphic Across Screen

import turtle

#startup settings
turtle.bgcolor("#29d0f2")
gif = "spongebob.gif"
turtle.register_shape(gif)

t = turtle.Turtle()
t.speed(0)

t.shape(gif)

t.penup()
t.goto(-450, 0)

for x in range(4):
#will clone the gif four times after moving it forward
    a = t.clone()
    a.penup()
    a.forward(x*350)
