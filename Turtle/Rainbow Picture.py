#Kush Kansara
#April 6, 2018
#Rainbow Activity Picture

#The purpose of this assignment was to create a picture that involved a rainbow
#I created a beautiful setting with a rainbow, grass, birds, and rain

import turtle

#initial variables(these are all counters for future use)
counter = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0

#startup settings
turtle.tracer(0, 0)                 #to speed up the process of forming the rainbow

t = turtle.Turtle()
t.pensize(1.5)                      #to make the colours of the rainbow look well blended together
t.hideturtle()                      #to hide the turtle from the user

turtle.colormode(255)               #to switch colour mode to rgb

scr = turtle.Screen()
scr.bgcolor(12, 214, 255)           #to set backgorund colour

def Rainbow():
#will create a rainbow
    for x in range(256):
        #will create colours from red to yellow
        t.pencolor(255, x, 0)
        if x%2 == 0:                #this will create an alternating pattern within the circles' direction
            t.circle(500-(x/3), 180)
        else:
            t.circle(-(500-(x/3)), 180)
        t.setheading(90)

    for x in range(256):
        #will create colours from yellow to green
        t.pencolor(255-x, 255, 0)
        if x%2 == 0:
            t.circle(415-(x/3), 180)
        else:
            t.circle(-(415-(x/3)), 180)
        t.setheading(90)

    for x in range(256):
        #will create colours from green to turqoise
        t.pencolor(0, 255, x)
        if x%2 == 0:
            t.circle(330-(x/3), 180)
        else:
            t.circle(-(330-(x/3)), 180)
        t.setheading(90)

    for x in range(256):
        #will create colours from turqoise to blue
        t.pencolor(0, 255-x, 255)
        if x%2 == 0:
            t.circle(245-(x/3), 180)
        else:
            t.circle(-(245-(x/3)), 180)
        t.setheading(90)

    for x in range(256):
        #will create colours from blue to violet
        t.pencolor(x, 0, 255)
        if x%2 == 0:
            t.circle(160-(x/3), 180)
        else:
            t.circle(-(160-(x/3)), 180)
        t.setheading(90)

def Grass(x, y, z): #parameters: x & y = coordinates of starting point, z = size of grass
#will make grass in given coordinates
    t.penup()
    t.pensize(10)
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.circle(z, 90)
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.forward(z)
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.circle(-z, 90)
    t.penup()
    t.pensize(1.5)

def Sun(x, y): #parameters: x & y = coordinates of starting point
#will make a sun in given coordinates
    t.penup()
    t.goto(x, y)
    t.color(255, 239, 1)
    t.setheading(90)
    t.begin_fill()
    t.pendown()
    t.circle(75)
    t.penup()
    t.end_fill()

def Bird(x, y): #parameters: x & y = coordinates of the bird
#this function will draw a bird at the given coordinates
    t.penup()
    t.color("black")
    t.pensize(7.5)
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.circle(40, 90)
    
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.circle(-40, 90)
    t.penup()

def Raindrop(x, y): #parameters: x & y = coordinates of the raindrop
#this function will create a raindrop
    t.penup()
    t.pensize(5)
    t.goto(x, y)
    t.setheading(270)
    t.color("blue")
    t.pendown()
    t.forward(25)
    t.penup()

#ground
t.penup()
t.goto(800, -300)
t.setheading(180)
t.color(20, 172, 30)
t.begin_fill()
t.pendown()
t.forward(1600)
t.penup()
t.left(90)
t.forward(1600)
t.left(90)
t.forward(1600)
t.left(90)
t.forward(200)
t.end_fill()
t.penup()

#rainbow
t.penup()
t.goto(500, -325)
t.setheading(90)
t.pendown()
Rainbow()

#grass
t.pencolor(20, 172, 30)
Grass(-600, -300, 50)
Grass(600, -300, 50)

#sun in the sky
Sun(-500, 300)

#cloud in the sky
for x in range(4):
    t.penup()
    t.goto(400-counter_2, 300)
    t.color("white")
    t.begin_fill()
    t.pensize(10)
    t.pendown()
    t.circle(50)
    t.end_fill()
    counter_2 += 60

#birds in the sky
Bird(-300, 200)
Bird(-100, 300)
Bird(450, 350)

#raindrops
while counter_3 < 6:                #creates raindrops all over the cloud
    Raindrop(140, 180-counter_4)
    Raindrop(205, 190-counter_4)
    Raindrop(270, 180-counter_4)
    Raindrop(335, 200-counter_4)
    Raindrop(400, 180-counter_4)
    counter_3 += 1
    counter_4 += 100
