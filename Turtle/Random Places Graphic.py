#Kush Kansara
#April 11th, 2018
#This is a program where a graphic will disappear and reappear on the screen

import turtle
from random import randint as r
from time import sleep as s

#initialization
t = turtle.Turtle()
t.speed(0)
t.penup()

k = turtle.Pen()
k.hideturtle()
k.speed(0)
k.penup()

sc = turtle.Screen()

gif = "spongebob.gif"
turtle.bgcolor("#29d0f2")

phrase = "Spongebob was here"

#dimensions of gif
hgif = 450
wgif = 185

#dimensions of screen
a = turtle.window_width()
b = turtle.window_height()

turtle.register_shape(gif)                                       #registers shape

t.shape(gif)

def write():
#this function will print a phrase wherever the spongebob gif is
    xc = t.xcor()
    yc = t.ycor()
    k.goto(xc, yc)
    k.pendown()
    k.color("yellow")
    k.write(phrase, align = "center", font = ("Arial", 25, "bold"))
    k.penup()

def randomplaces():
#this function will make the turtle appear in different, random places
    while True:
        sc.listen()
        sc.onkey(write, "space")                                #will print words when the space key is pressed
        t.hideturtle()                                          #hides turtle to make it flash
        s(0.75)                                                 #adds a delay to the flash
        t.goto(r(-b+wgif, b-wgif), r(-a+hgif, a-hgif))          #random places, and accounts for size of gif
        t.showturtle()                                          #shows turtle on screen for flash
        s(0.75)                                                 #keeps turtle on screen

#top of screen text
t.penup()
t.goto(0, (b/2))
t.pendown()
t.write("Press space at any time to mark where spongebob has been!", align = "center", font = ("Arial", 25, "bold"))
t.penup()

#flashing of gif at random places
randomplaces()
