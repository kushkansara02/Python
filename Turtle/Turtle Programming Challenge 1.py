#Kush Kansara
#My Initials
#March 23rd, 2018

import turtle

screen = turtle.Screen()

turtle.bgcolor("orange")
a = turtle.Pen()
a.pencolor("blue")
a.pensize(15)
a.speed(0)
a.hideturtle()

def drawK(x,y):
##    a.penup()
##    a.left(90)
##    a.forward(400)
##    a.left(90)
##    a.forward(250)
##    a.left(90)
    a.goto(x,y)
    a.setheading(90)
    a.forward(200)
    a.right(90)
    a.pendown()
    a.left(90)
    a.forward(400)
    a.penup()
    a.right(180)
    a.forward(200)
    a.right(45)
    a.pendown()
    a.forward(280)
    a.right(180)
    a.forward(280)
    a.left(90)
    a.forward(280)
    a.penup()
    a.left(45)

def drawDot():
    a.forward(49)
    a.pendown()
    a.forward(2)
    a.penup()
    a.forward(49)

#k
drawK()

#dot
drawDot()

#k
##drawK()

#k
##a.left(180)
##a.pendown()
##a.right(90)
##a.forward(400)
##a.penup()
##a.left(180)
##a.forward(200)
##a.left(45)
##a.pendown()
##a.forward(280)
##a.left(180)
##a.forward(280)
##a.right(90)
##a.forward(280)
##a.penup()

#border
##a.left(90)
##a.forward(80)
##a.right(90)
##a.forward(100)
##a.left(180)
##a.pencolor("purple")
##a.pensize(10)
##a.pendown()
##a.forward(700)
##a.left(90)
##a.forward(560)
##a.left(90)
##a.forward(700)
##a.left(90)
##a.forward(560)
##a.left(180)
##a.forward(500)
##a.pencolor("red")
##a.right(90)
##a.penup()
##a.forward(50)
##a.pendown()
##a.forward(600)
