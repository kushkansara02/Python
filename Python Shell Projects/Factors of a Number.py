#factorsofnumbers

def factor():
    print("This function will show you all of the factors of a number you specify.")
    a = int(input("Please enter the number you would like to know the factors of: "))
    i = 2
    
    for num in range(2,a):
        if a%i == 0:
            print(i)
            i += 1
        elif a%i != 0:
            i += 1
        
factor()
