#kush

count = 0

userinput = input("Please set your password: ")
print("After a while, you need to use your password.")

while True:
    a = input("\nEnter your password. ")

    if a == userinput:
        print("\nYou have successfully logged in.")
        break

    else:
        count += 1
        if count == 1:
            print("\nThat is the wrong password. You have",3-count,"tries left")
        if count == 2:
            print("\nThat is the wrong password. You have",3-count,"try left")
        elif count == 3:
            print("\nThat is the wrong password. You have run out of tries.")

    if count == 3:
        print("\nYou have been denied access")
        break
