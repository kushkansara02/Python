print("Hello User!")
print("This is a program that will perform basic math")


k = int(input("What operation would you like to use? 1-Add 2-Sub 3-Mult 4-Div"))

if k > 4:
    print("Sorry, the number is too high. Please re-enter the number")

else:        
    j = int(input("Please give me a number: "))
    y = int(input("Please give me another number: "))

if k == 1:
    z = j+y

elif k == 2:
    z = j-y

elif k == 3:
    z = j*y

else:
    z = j/y

        
print("Your result is", z)
