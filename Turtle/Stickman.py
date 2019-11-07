#Kush Kansara
#April 6, 2018
#Stickman and Pet

#The purpose of this assignment was to create a stickman with his pet using turtle
#I created Timmy going towards his fish (his best friend) with his pet food as well

import turtle

#colour variables
brown = "#aa6c36"
green = "#587c2c"
bgc = "#53bced"
bg = turtle.Screen()

#two different turtles
a = turtle.Pen()
b = turtle.Pen()

#initial turtle sizes and speeds
a.pensize(7)
b.pensize(5)

a.speed(0)
b.speed(0)

#hides turtle from user
a.hideturtle()
b.hideturtle()

def setbackground():
#will set background colour
    bg.bgcolor(bgc)

def stickman():
#will draw the stickman
    a.penup()           #main body
    a.left(180)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(180)
    a.pendown()
    a.forward(200)

    a.right(90)         #head
    a.pendown()
    a.color("brown")
    a.begin_fill()
    a.circle(35, 360)
    a.end_fill()
    a.pencolor("black")
    a.right(90)
    a.forward(200)      #legs
    a.left(45)
    a.forward(100)
    a.left(90)
    a.forward(50)
    a.left(180)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(50)
    a.left(45)

    a.forward(500)      #ground
    a.left(180)
    a.forward(800)
    a.left(180)
    a.forward(300)
    a.left(180)
    a.right(45)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.left(45)

    a.penup()
    a.forward(230)
    a.left(45)
    a.forward(15)

    a.pendown()         #eyes
    a.pensize(8)
    a.forward(1)
    a.penup()
    a.left(180)
    a.forward(16)
    a.left(90)
    a.forward(15)
    a.pendown()
    a.forward(1)

    a.penup()
    a.pensize(5)
    a.right(135)
    a.forward(35)
    a.right(90)
    a.forward(11)
    a.left(90)
    a.left(180)

    a.forward(20)       #smile
    a.left(90)
    a.forward(9)
    a.left(90)
    a.pendown()
    a.circle(10, 180)
    a.penup()
    a.left(90)
    a.forward(11)
    a.left(90)
    a.forward(20)
    a.pendown()

    a.forward(106)      #hands
    a.right(90)
    a.forward(100)
    a.left(180)
    a.forward(200)
    a.left(180)
    a.forward(200)

    a.color("brown")
    b.color("brown")
    a.right(90)
    a.begin_fill()
    a.circle(15)
    a.end_fill()
    b.right(90)
    b.begin_fill()
    b.circle(15)
    b.end_fill()

def pet():
#will draw the fish as well as its tank and its table
    x = 0      #tank
    b.pencolor("black")
    b.pensize(10)
    b.penup()
    b.left(90)
    b.forward(100)
    b.left(90)
    b.forward(100)
    b.left(180)
    b.pendown()
    b.forward(200)
    b.left(90)
    b.forward(200)
    b.left(90)
    b.forward(200)
    b.pensize(5)

    b.color(brown)
    b.penup()
    b.left(180)
    b.forward(200)
    b.left(90)

    b.pendown()         #table
    b.begin_fill()
    b.forward(50)
    b.left(180)
    b.forward(300)
    b.left(90)
    b.forward(100)
    b.penup()
    b.left(90)
    b.forward(300)
    b.left(90)
    b.forward(100)
    b.end_fill()
    b.setpos(50, -200)
    b.left(180)

    b.left(90)
    b.forward(300)
    b.left(90)
    b.pendown()
    b.forward(100)
    b.color("black")

    b.penup()
    b.left(90)
    b.forward(50)
    b.right(90)
    b.forward(150)
    b.pensize(2)

    b.penup()           #tank
    b.begin_fill()
    b.setpos(100,50)
    b.left(180)
    b.forward(150)
    b.left(90)
    b.forward(200)
    b.left(90)
    b.forward(150)

    while x <= 4:       #waves
        b.pendown()
        b.color("blue")
        b.circle(10, 180)
        b.circle(-10,180)
        x += 1
        b.penup()

    b.end_fill()

    b.color("orange")
    b.penup()
    b.right(180)
    b.forward(75)
    b.left(90)
    b.forward(50)
    b.right(90)

    b.pendown()         #fish
    b.begin_fill()
    b.forward(50)
    b.left(120)
    b.forward(50)
    b.left(120)
    b.forward(50)
    b.left(180)
    b.forward(50)
    b.left(120)
    b.end_fill()
    b.right(180)
    b.begin_fill()
    b.setpos(170,-50)
    b.circle(25, 360)
    b.end_fill()
    b.setpos(205, -40)
    b.dot("black")      #fish's eye
    b.hideturtle()

def drawFishfood():
#will draw the fish food container
    a.penup()   #will draw container
    a.goto(-400, -200)
    a.setheading(90)
    a.fillcolor(green)
    a.pencolor("white")
    a.begin_fill()
    a.pendown()
    a.forward(150)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(150)
    a.right(90)
    a.forward(100)
    a.end_fill()

    a.penup()
    a.goto(-350, -125)
    a.color("blue")
    a.pendown()
    a.write("Fish Food", align="center", font=("arial", 20, "bold"))

#will draw stickman
stickman()

#will draw pet and its surroundings
pet()

#will set background at the end
setbackground()

#will draw fish food container
drawFishfood()

#will write the title
b.penup()
b.goto(0, 300)
b.color("black")
b.pendown()
b.write("Timmy and his Best Friend!", align="center", font=("arial", 40, "bold"))
