#chooseyourownadventure
#labels such as 'c1a2' are simply to categorize the user's choices for organizational purposes

import time
while True:
    print("Welcome, challenger! Before entering, be warned...you may not leave alive")
    time.sleep(1)
    x = str(input("\nWould you still like to continue? Yes or No? "))
    time.sleep(2)

    if x == "Yes" or x == "yes":
        print("\nVery well. Your adventure first starts at the moment you receive a package outside your door")
        print("at 1am in the morning. At first, you make no sense of it. It is a blue envelope with the words")
        print("'open if you wish to escape the world.'Then you notice something glistening")
        y = str(input("within the envelope. Do you open it or not? Yes or No? "))  
        time.sleep(2)

        #c1 - done (z)
        if y == "Yes" or y == "yes":
            print("\nYou chose...poorly. Your life has forever changed for the worse. As you open the envelope,")
            print("you hear a knock on the door.")
            print("You find a man standing at your door, covered in mud. He sees the envelope in your hand,")
            print("squeaks in excitement, and starts telling you his story")
            print("He explains the blue stone that you have in your hand, that it's the most powerful")
            print("object to ever exist. It can either be the bane of your existence or create your empire")
            print("You feel like he's hiding something from you, but you choose not to investigate.")
            z = str(input("He asks you to accompany him to his 'headquarters'. What do you say, yes or no? "))
            time.sleep(2)

            #c1a - done (b)
            if z == "Yes" or z == "yes":
                print("\nHe takes you in his car, but you notice something off about it. You check,")
                print("and there is a gun within the glove compartment. You can either:")
                b = int(input("1.Take the gun and shoot him \n2.Stay with him\n "))
                time.sleep(2)

                #c1a1 - done
                if b == 1:
                    print("\nYou take the gun and shoot him with it. You pull the hand brake, and run as far")
                    print("away as you can from the car. You take a taxi home, and live happily ever after...")
                    print("Until three years after the incident. You get another envelope at your door, only")
                    print("this time it's red...Good job! You survived! For now...To be continued...")

                #c1a2 - done
                elif b == 2:
                    print("\nYour choice seemed like the correct one...only at first. He suddenly stops,")
                    print("and as you look around, you are deep inside a forest. He reaches for the glove")
                    print("compartment and takes the gun out. As he points it at your head, you")
                    print("see everything clearly. He only wants the jewel for himself. It is too late now...")
                    print("You accept it, close your eyes, and accept your fate")
                    time.sleep(2)
                    print("Game Over...Atleast you tried...")
   
                else:
                    print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
                    print("a computer turning off... Next time, choose a valid option")
            
            #c1b - done (c)
            elif z == "No" or z == "no":
                print("\nHe seems a little annoyed at you, with his left eye twitching. He starts to let out a")
                print("scream, but suddenly stifles it. He says in a monotone voice:")
                print("'Very well sir. We will see you soon.' Before you can say anything, he suddenly")
                print("disappears. Then, as you try to go back inside, you see a flash of blue light")
                print("surrounding you. Next thing you know, you are in a poorly lit prison cell without")
                print("the blue gem. There is a person sleeping in the corner...")
                c = str(input("Do you wake him up? Yes or No? "))
                time.sleep(2)

                #c1b1 - done
                if c == "Yes" or c == "yes":
                    print("\nWhen you tap his shoulder, he jerks around, ready to defend himself. 'Y-you...")
                    print("You're the one with the blue... I heard about you, but didn't believe it...")
                    print("You need to get out of here...they will be watching...you can't let them get their")
                    print("hands on your gift...your gems...' He gets up, and says:")
                    print("'I need to get you out of here...WE need to get you out of here..' A few days pass,")
                    print("and within those days you plan to get out of prison...On the big day, the plan is")
                    print("successful, and you get out of prison and live happily ever after...Until you")
                    print("realize that the blue gem wasn't the only one...")
                    print("Good job! You survived! For now...To be continued...")

                #c1b2 - done
                elif c == "No" or c == "no":
                    print("\nWho was lying in the bed will forever remain a mystery to you...A good decision or")
                    print("not? You are about to find out. The prison seems to run as a normal prison would,")
                    print("however you do not get any indication as to why you are here or how. A week passes")
                    print(", and you notice each day you slowly get less and less freedom. No showers, no")
                    print("privacy, and eventually no food. Everyone still seems to ignore you. As your life")
                    print("fades before your eyes, you realize; you are literally invisible. You die a lonely")
                    print("death, filled with regrets. When the time comes, you close your eyes and accept it")
                    print("Game Over...Atleast you tried...")

                else:
                    print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
                    print("a computer turning off... Next time, choose a valid option")

            else:
                print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
                print("a computer turning off... Next time, choose a valid option")
        
        #c2 - done (a)
        elif y == "No" or y == "no":
            print("\nYou chose...wisely. You go throw it in the trash can, and get a good night's sleep.")
            print("In the morning, when you wake up, you have breakfast quietly, but notice something strange")
            print("in your cereal. Did you win something? You see a strange blue jewel in the milk.")
            a = str(input("Maybe it's one of the prizes! Do you want to go and cash the prize in? Yes or No? "))
            time.sleep(2)

            #c2a - done (e)
            if a == "Yes" or a == "yes":
                print("\nYou look at the address on the cereal. '144 Kzombez Lane.' Did this exist before?")
                print("You go to the location and find out it exists...but on what you can swear was farmland")
                print("yesterday. You don't think much of it and continue inside. It seems like a headquarters")
                print("of some sort. You meet with a strange man who keeps staring at your prize. When you get")
                print("to the counter, you see something bizarre. A floating head as a receptionist!")
                e = str(input("Do you talk to it, or not? Yes or No? "))
                time.sleep(2)

                #c2a1 - done
                if e == "Yes" or e == "yes":
                    print("\nYou approach the floating head, and show it the blue jewel, you hear sirens.")
                    print("You see military grade soldiers line up around you. Guns cocked. 'Drop the weapon")
                    print("and slowly lift your hands!' You are faced with a tough decision. After much")
                    print("consideration, you realize you have to obey the command. As you drop the gem,")
                    print("however, you see a sudden blue light all around you. Then you survey your")
                    print("surroundings. You are at home! After the incident, you live happily ever after")
                    print("That is, until you realize the blue gem wasn't the only existant one.")
                    print("Good job! You survived! For now...To be continued...")

                #c2a2 - done
                elif e == "No" or e == "no":
                    print("\nYou decide to just get out of this suspicious place. You head for the doors when")
                    print("suddenly, the sirens go off. There is a trapdoor right underneath you, and you")
                    print("fall into it. It closes right after you. It is a dark passage with no light and")
                    print("very little space. As you are about to find out, this is the end of your life.")
                    print("No one comes for you and you don't get any human interaction as well as food")
                    print("As you are breathing your final breaths, you die in confusion. What was it about?")
                    print("You will never find out. Game Over...Atleast you tried...")

                else:
                    print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
                    print("a computer turning off... Next time, choose a valid option")                

            #c2b - done (f)
            elif a == "No" or a == "no":
                print("\nThe rest of your day is otherwise ordinary. However, throughout the day, you constantly")
                print("feel like someone is watching. You see glimpses of a shadow, but never catch it in time")
                print("As your day progresses, the shadows seem to get closer and closer. As you realize you're")
                print("in trouble, you only have two options")
                print("1.Take your knife made of special rubies and hide in the closet")
                print("2.Get your limited edition titanium bullets shotgun and take the shadow on")
                f = int(input(""))
                time.sleep(2)

                #c2b1 - done
                if f == 1:
                    print("\nYou quickly swipe your knife from the bottom of your sofa and go to the upper floor")
                    print("There, you go inside a closet with a small space to see and breathe. You wait for")
                    print("what seems like days. Finally, you hear the door open. Someone ruffles through your")
                    print("things in the bottom floor, and starts to come upstairs. He starts to come towards")
                    print("your closet, looking directly at you. He opens it, but acts as if nothing is in")
                    print("the closet itself. Are you invisible? He leaves your house immediately after that")
                    print("and that is the last you see of him. You live happily ever after...that is, until")
                    print("you find out that this shadow has friends...lots of them...after this, your life")
                    print("will be forever changed...But for now, good job! You survived! To be continued...")

                #c2b2 - done
                elif f == 2:
                    print("\nYou wait in your chair by the door for what seems like days. Finally, however, you")
                    print("hear knocking on your door. Suddenly, the door breaks, with wooden shrapnel flying")
                    print("all over the place. You see the shadow, and it is quite literally that. A shadow")
                    print("You let loose with your gun, but all of the bullets seem to go through the shadow")
                    print("The shadow takes one look at you and you evaporate into thin air. A painless death")
                    print("Game Over...Atleast you tried...")

                else:
                    print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
                    print("a computer turning off... Next time, choose a valid option")

            else:
                print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
                print("a computer turning off... Next time, choose a valid option")

        else:
            print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
            print("a computer turning off... Next time, choose a valid option")

    elif x == "No" or x == "no":
        print("\nVery well then...go live your boring, adventureless life..")

    else:
        print("\nHmm...This choice is invalid...quite literally. All around you, the world ends like")
        print("a computer turning off... Next time, choose a valid option")

    again = str(input("\nWould you like to play again? Yes or No? "))

    if again == "Yes" or again == "yes":
            time.sleep(2)
            print("\nThis game will replay in 5 seconds")
            time.sleep(1)
            print("5")
            time.sleep(1)
            print("4")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            
    else:
        break
