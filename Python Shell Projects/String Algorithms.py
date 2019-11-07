#String Manipulation

import time

while True:
    
    userinput = str(input("\nPlease Enter a Word: "))

    b = input('''\nWhich of the following would you like to do?
1. Change the whole word to either uppercase or lowercase
2. Check how many numbers and how many letters there are
3. Count the number of characters in the word
4. Search for a letter within the word and return its position\n\n''')

    if b == "1":
        hello = input("\nWould you like to change to uppercase or lowercase? ")

        if hello == "Uppercase" or hello == "uppercase":
            print("\nObtaining your new word\n")
            time.sleep(3)
            print(userinput.upper())

        elif hello == "Lowercase" or hello == "lowercase":
            print("\nObtaining your new word\n")
            time.sleep(3)
            print(userinput.lower())

        else:
            print("Sorry, what you entered was not defined.")

    elif b == "2":
        a1 = userinput.count("1")
        a2 = userinput.count("2")
        a3 = userinput.count("3")
        a4 = userinput.count("4")
        a5 = userinput.count("5")
        a6 = userinput.count("6")
        a7 = userinput.count("7")
        a8 = userinput.count("8")
        a9 = userinput.count("9")
        a0 = userinput.count("0")
        k = userinput.replace(" ","")
        j = k.isalpha()
        print("\nChecking...")
        
        if j == True:
            print("\nThis word does not have any numbers!")
            
        elif j == False:
            total = int(a1+a2+a3+a4+a5+a6+a7+a8+a9+a0)
            chars = len(k)-total
            print("\nYour word has",total,"numbers!")
            print("\nYour word has",chars,"letters!")
            print("\nYour word has",c,"spaces")


    elif b == "3":
        print("\nCounting the characters...")
        time.sleep(3)
        c = len(userinput)
        print("\nYour word has",c,"characters")

    elif b == "4":
        d = str(input("\nWhich character would you like to look for? "))
        print("\nSearching...")
        time.sleep(3)
        kush = int (userinput.find(d))
        
        if kush>=0:
            print("\nIf you are a coder, the first position your character appears in is:\n")
            print(userinput.find(d))
            print("\nIf you are a non-coder, the first position your character appears in is:\n")
            print(userinput.find(d)+1)
            
        else:
            print("\nSorry, this character is not in your word")

    else:
        print("\nThis is not a defined operation. Please try again")

    again = input("\nWould you like to input another word? Yes or No? ")

    if again == "Yes" or again == "yes":
        continue
    
    else:
        break
