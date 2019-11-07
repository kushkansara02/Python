#Kush Kansara
#April 6, 2018
#Rainbow Activity Robot

#This was something that I did along with the rainbow assignment, as an extension and application of my knowledge
#This is a robot with rainbow spiral eyes and a rainbow mouth, who is named after anyone you want!

import turtle

#startup settings
turtle.tracer(0,0)          #to speed up the process of forming the picture, as it will take a long time to load otherwise
t = turtle.Turtle()
t.pensize(1.5)              #size of the pen while forming the rainbow
t.hideturtle()              #to hide the turtle from the user
turtle.colormode(255)       #to change colormode to rgb
screen = turtle.Screen()
screen.bgcolor("gray")      #to set background colour

def rainbowspiral():
#this will create a rainbow spiral, which is used for the robot's eyes
    for x in range(256):
        #this for loop creates colours from red to yellow
        t.pendown()
        t.pencolor(255, x, 0)
        t.forward(x/7)
        t.left(91)
        t.penup()

    for x in range(256):
        #this for loop creates colours from yellow to green
        t.pendown()             
        t.pencolor(255-x, 255, 0)
        t.forward((x+255)/7)
        t.left(91)
        t.penup()

    for x in range(256):
        #this for loop creates colours from green to turqoise
        t.pendown()
        t.pencolor(0, 255, x)
        t.forward((x+510)/7)
        t.left(91)
        t.penup()

    for x in range(256):
        #this for loop creates colours from turqoise to blue
        t.pendown()
        t.pencolor(0, 255-x, 255)
        t.forward((x+765)/7)
        t.left(91)
        t.penup()

    for x in range(256):
        #this for loop creates colours from blue to violet
        t.pendown()
        t.pencolor(x, 0, 255)
        t.forward((x+1020)/7)
        t.left(91)
        t.penup()

    for x in range(256):
        #this for loop creates colours from violet to red
        t.pendown()
        t.pencolor(255, 0, 255-x)
        t.forward((x+1275)/7)
        t.left(91)
        t.penup()

def rainbowline(y): #this parameter is to define the amount of distance that the line will go
#this will create a straight line in the colour of a rainbow
    for x in range(256):
        #this for loop creates colours from red to yellow
        t.pendown()
        t.pencolor(255, x, 0)
        t.forward(y/1530)
        t.penup()

    for x in range(256):
        #this for loop creates colours from yellow to green
        t.pendown()
        t.pencolor(255-x, 255, 0)
        t.forward(y/1530)
        t.penup()

    for x in range(256):
        #this for loop creates colours from green to turqoise
        t.pendown()
        t.pencolor(0, 255, x)
        t.forward(y/1530)
        t.penup()

    for x in range(256):
        #this for loop creates colours from turqoise to blue
        t.pendown()
        t.pencolor(0, 255-x, 255)
        t.forward(y/1530)
        t.penup()

    for x in range(256):
        #this for loop creates colours from blue to violet
        t.pendown()
        t.pencolor(x, 0, 255)
        t.forward(y/1530)
        t.penup()

    for x in range(256):
        #this for loop creates colours from violet to red
        t.pendown()
        t.pencolor(255, 0, 255-x)
        t.forward(y/1530)
        t.penup()

#eyes of robot
t.penup()
t.goto(-300,200)
t.pendown()
rainbowspiral()
t.penup()
t.goto(300,200)
t.pendown()
rainbowspiral()

#mouth of robot
t.penup()
t.goto(-300,-250)
t.setheading(360)
t.pensize(30)
t.pendown()
rainbowline(600)

t.left(90)
rainbowline(100)
t.left(90)
rainbowline(600)

t.left(90)
rainbowline(100)
t.pensize(5)
t.penup()

#radio lines in mouth
counter_1 = 0
t.goto(-280,-200)
t.setheading(360)
t.right(45)
rainbowline(20)
t.left(90)
rainbowline(50)
t.right(90)

while counter_1 < 7:    #this will create a zigzag pattern in the mouth 6 times
    rainbowline(50)
    t.left(90)
    rainbowline(50)
    t.right(90)
    counter_1 += 1

rainbowline(20)

#nose
t.goto(75,-50)          #makes a triangle as the nose
t.setheading(180)
rainbowline(150)
t.right(120)
rainbowline(150)
t.right(120)
rainbowline(150)

#the name input of the robot, which will underneath the robot
name = turtle.textinput("Robot Name", "What is its name?")
rname = name + " the robot"

t.goto(0,-350)
t.write(rname, align="center", font=("Arial", 40, "bold"))
