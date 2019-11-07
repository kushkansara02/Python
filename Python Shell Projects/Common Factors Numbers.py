#commonfactorsofnumbers

def commonfactor():
    print("This function will show you the common factors of two numbers you specify.")
    a = input("\nPlease enter the numbers you would like to know the common factors of.\n(Please seperate these two numbers with a space) ")
    i = 1
    b = a.split(" ")
    x = int(b[0])
    y = int(b[1])

    for num in range (1, x or y):
        
        if x%i == 0 and y%i == 0:
            print(i)
            i += 1
                
        elif x%i != 0 or y%i != 0:
            i += 1
            
commonfactor()
