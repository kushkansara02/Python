#prime numbers

def prime():
    print("This function will show you all of the prime numbers in a range you specify")
    a = input("Please enter two numbers. They should be seperated by spaces (Smaller number should be first): ")
    b = a.split(" ")
    i = 2
    x = int(b[0])
    y = int(b[1])
    
    for num in range(x,y):
        if all(num%i != 0 for i in range(x+1,num)):
            print(num)

prime()
