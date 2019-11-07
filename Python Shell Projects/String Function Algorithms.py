#kush

def stringfunction():
    userinput = input("Enter a string: ")
    uppercounter = 0
    lowercounter = 0
    numbercounter = 0
    spacecounter = 0

    for letters in userinput:
        if letters.isupper():
            uppercounter += 1
        elif letters.islower():
            lowercounter += 1
        elif letters.isdigit():
            numbercounter += 1
        elif letters.isspace():
            spacecounter += 1

    x = print("You have",uppercounter,"uppercase letter(s),",lowercounter,"lowercase letter(s),",numbercounter,"number(s), and",spacecounter,"space(s).")

stringfunction()
