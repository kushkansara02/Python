#kush

studentcount = 0
g = []

print("Hello! This program will take in your students and their marks!\n\n(Note: When inputting, the name of the student and their mark should be seperated by a space)")

howmanystudents = int(input("\nHow many students do you want to input?\n\n"))

while howmanystudents > studentcount:
    a = input("\nPlease enter the name of the student and his/her mark: ")
    b = a.split(" ")
    g.append(b)
    studentcount += 1

print("\nThis is your list:\n",g)

while True:
    print("\nWhat would you like to do with your string now?")
    h = int(input("\n1. Sort the list alphabetically and numerically\n2. Add a student to the list\n3. Delete a student from the list\n4. Find a student's mark from the list\n5. Create a new list with only the student names\n6. Exit the program\n\n"))

    if h == 1:
        i = int(input("\nWould you like to:\n1. Sort it alphabetically and numerically\n2. Sort it alphabetically and numerically reversed\n\n"))
        
        if i == 1:
            g.sort(reverse = False)
            print("\nThis is your new list:\n",g)

        elif i == 2:
            g.sort(reverse = True)
            print("\nThis is your new list:\n",g)

        else:
            print("\nThis was not defined. Please try again")

    elif h == 2:
        j = input("\nEnter the student name and mark that you would like to add. (Note: These should also be seperated by a space\n\n")

        k = j.split(" ")
        g.append(k)
        print("\nThis is your new list:\n",g)

    elif h == 3:
        l = input("\nWhat is the name of the student would you like to delete?\nNote: If the student name you input is not within the list, you will be returned to the initial option\n\n")

        for students in g:
            for mark in students:
                if mark == l:
                    g.remove(students)
                    print("\nThis is your new list:\n",g)

    elif h == 4:
        m = input("\nWhich student's mark would you like to find?(Input the name, and his/her position will be returned for you)\nNote: If the student name you input is not within the list, you will be returned to the initial options\n\n")

        for students in g:
            for mark in students:
                if mark == m:
                    print("\nYour student's mark is:",students[1])

    elif h == 5:
        for students in g:
            students.pop(1)

        print("\nHere is your student list:\n",g)
            
        
    elif h == 6:
        break

    else:
        print("\nThis was not defined. Please try again")
        continue
