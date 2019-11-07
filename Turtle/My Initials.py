#Kush Kansara
#April 6, 2018
#My Initials

#The purpose of this assignment was to create my initials using turtle
#I created my initials with a box around them, as well as a spiral to encover them

import turtle

screen = turtle.Screen()

turtle.bgcolor("orange")    #sets background colour
a = turtle.Pen()
a.pencolor("blue")          #sets the colour of the initial pen
a.pensize(15)               #size of the pen
a.speed(0)                  #fastest possible speed for the turtle
a.hideturtle()              #hides turtle from user's view

def drawK(x,y): #parameters: x & y = coordinates on the screen
#this function will draw a "K" at a specific coordinate
    a.penup()
    a.goto(x,y)
    a.setheading(90)
    a.pendown()
    a.forward(200)
    a.right(180)
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

def drawDot(x, y): #parameters: x & y = coordinates on the screen
#this function will draw a dot at a specific coordinate
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.forward(2)
    a.penup()

def drawBorders():
#this function will draw borders around the initials
    a.goto(250, 150)
    a.setheading(90)
    a.forward(80)
    a.right(90)
    a.forward(100)
    a.left(180)
    a.pencolor("purple")
    a.pensize(10)
    a.pendown()
    a.forward(700)
    a.left(90)
    a.forward(560)
    a.left(90)
    a.forward(700)
    a.left(90)
    a.forward(560)
    a.left(180)
    a.forward(500)
    a.pencolor("red")
    a.right(90)
    a.penup()
    a.forward(50)
    a.pendown()
    a.forward(600)

def drawSpiral():
#this will draw a spiral around the initials
    a.penup()
    a.goto(400, 350)
    a.right(1)
    a.pendown()
    for x in range(100):
        a.color("gray")
        a.forward(800+x)
        a.left(91)

#first k will be drawn
drawK(-300, -50)

#dot between k's will be drawn
drawDot(0, -250)

#second k will be drawn
drawK(100, -50)

#border around k's will be drawn
drawBorders()

#spiral around the initials
drawSpiral()
