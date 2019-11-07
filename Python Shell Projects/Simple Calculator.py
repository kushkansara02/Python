#simplecalculator

def prime():
    print("\nThis function will show you all of the prime numbers in a range you specify")
    a = input("Please enter two numbers. They should be seperated by spaces (Smaller number should be first): ")
    b = a.split(" ")
    i = 2
    x = int(b[0])
    y = int(b[1])
    
    for num in range(x,y):
        if all(num%i != 0 for i in range(x+1,num)):
            print(num)

def factor():
    print("\nThis function will show you all of the factors of a number you specify.")
    a = int(input("\nPlease enter the number you would like to know the factors of: "))
    i = 2
    
    for num in range(2,a):
        if a%i == 0:
            print(i)
            i += 1
        elif a%i != 0:
            i += 1

def commonfactor():
    print("\nThis function will show you the common factors of two numbers you specify.")
    a = input("\nPlease enter the numbers you would like to know the common factors of.\n(Please seperate these two numbers with a space) ")
    i = 1
    b = a.split(" ")
    x = int(b[0])
    y = int(b[1])

    for num in range (1, x+1 or y+1):
        
        if x%i == 0 and y%i == 0:
            if i == 1:
                i += 1
            else:
                print(i)
                i += 1
                
        elif x%i != 0 or y%i != 0:
            i += 1

print ("Welcome!")
print ("\nThis is a simple functions calculator! Select any of these functions to continue!")

while True:

    x = int(input("\n1-Addition,\n2-Subraction,\n3-Multiplication,\n4-Division,\n5-Percentage,\n6-Exponents,\n7-Find all prime numbers between a range,\n8-Find all factors of a number,\n9-Find the common factors of two numbers\n\n"))

    if x > 9 or x < 0:
        print ("\nSorry, this is not a defined function!")
        print ("\nPlease try again!")
    x = str(x)
    if x.isalpha():
        print ("\nSorry, this is not a defined function!")
        print ("\nPlease try again!")
    x = int(x)

    if x == 1:

        y = int(input("\nYou have chosen addition! Enter your first number! "))
        z = int(input("\nNow enter your second number! "))      
        a=y+z
        print ("\nYour answer is",a)

    elif x == 2:

        y = int(input("\nYou have chosen subraction! Enter your first number! "))
        z = int(input("\nNow enter your second number! "))      
        a=y-z
        print ("\nYour answer is",a)

    elif x == 3:

        y = int(input("\nYou have chosen multiplication! Enter your first number! "))
        z = int(input("\nNow enter your second number! "))      
        a=y*z
        print ("\nYour answer is",a)

    elif x == 4:

        y = int(input("\nYou have chosen addition! Enter your first number! "))
        z = int(input("\nNow enter your second number! "))      
        a=y/z
        print ("\nYour answer is",a)

    elif x == 5:

        y = int(input("\nYou have chosen percentages! Enter your first number! "))
        z = int(input("\nNow enter your second number! "))      
        a=y/z*100
        print ("\nYour answer is",a,"percent")

    elif x == 6:

        y = int(input("\nYou have chosen exponents! Enter your base! "))
        z = int(input("\nNow enter your exponent! "))      
        a=y**z
        print ("\nYour answer is",a)

    elif x == 7:
        prime()

    elif x == 8:
        factor()

    elif x == 9:
        commonfactor()

    playagain = input("\nWould you like to do another calculation? ")

    if playagain == "Yes" or playagain == "yes":
            continue

    else:
        print ("\nGoodbye")
        break
