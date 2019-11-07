#kush kansara

#this is the function that takes an American spelled word and turns it into Canadian spelling!
def spelling(str):
    while True:
        y = 1
        a = input("\nPlease enter your word in American spelling: ")

        if len(a) <= 4:
            print("\nYour word was already in Canadian spelling! The Canadian spelling is:",a)

        #if the input is longer than 64 characters, then the user will be asked to enter again
        if len(a) >= 64:
            print("\nThis word is too long! Please try again!")

        #if the user inputs "quit!", then the program will break
        if a == "quit!":
            print("\nThank you for using this program!")
            break

        #user input must be under 64 letters, and four letter words are already in Canadian spelling
        while len(a) > 4 and len(a) <= 64 and a != "quit!":

            #this code ensures that if no "or" is found within the spelling, the word is printed again, as it is already in Canadian spelling
            if y == len(a):
                print("\nYour word was already in Canadian spelling! The Canadian spelling is:",a)
                break

            else:
                #this will search for an "o" within the word
                if a[y] == "o":
                    if y < len(a):
                        y += 1


                        #if the "o" is followed by a an "r", then the spelling will be changed from "or" to "our"
                        if a[y] == "r":
                            print("\nThe Canadian spelling is:",a.replace("or","our"))
                            break

                elif a[y] != "o":
                    if y < len(a):
                        y += 1

print("Welcome to the Kush's program of changing American spelling to Canadian spelling!\n\nEnter: 'quit!' as your input at any time to exit the program")

#calls the function above after the beginning of the code
spelling(str)
