#RESOURCES
#ftp://ftp.borg.moe/yarr/Gentoomen%20Library/Programming/Python/Python%20and%20Tkinter%20Programming%20(2000).pdf
#https://en.wikipedia.org/wiki/Tkinter
#https://docs.python.org/2/library/tkinter.html#the-window-manager
#http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
#https://www.python-course.eu/tkinter_layout_management.php
#http://www.sable.mcgill.ca/~bdufou1/files/docs/python/Sep01/TkIntroSlides.pdf

#Strategies Defined & Designed by Ms. A. Gorski in Java
#Adapted from Java by Ms. K. Willis


import random
from tkinter import *   #import the entire tkinter library
import tkinter as tk    #defines the imported content from the library as tk for faster typing

class ZombieApplication(tk.Frame): 

    def __init__(self, master=None):
        
        tk.Frame.__init__(self, master)
        self.grid()

        global pictureLabel
        global playButton
        global quitButton

        logo = tk.PhotoImage(file="logo.gif")   #access the image
        pictureLabel = tk.Label(self,image = logo)  #attach the image
        pictureLabel.pack(side=tk.LEFT) #define label location; must be split to avoid attribution error
        pictureLabel.image = logo   #saves from the garbage collector
        
        play = tk.PhotoImage(file="play.gif")
        playButton = tk.Button(self,image =play,command=self.beginGame)
        playButton.pack(side=tk.LEFT, padx=10 ) # action can be activated
        playButton.image = play     #saves from the garbage collector
        
        stop = tk.PhotoImage(file="quit.gif")
        quitButton = tk.Button(self,image =stop,justify=tk.LEFT,command=self.ending)
        quitButton.pack(side=tk.RIGHT,padx=20)
        quitButton.image = stop  #saves from the garbage collector


    def ending(self):
        #ending part of Zombie Dice
        #current master app screen and remaining resources are purged from memory
        app.destroy()

    def activateGameButtons(self):
        #presents active buttons on the screen for the initialization of the first play
        global b1
        global b2
        global b3
        
        go = tk.PhotoImage(file="keepGoing.gif")
        b1 = tk.Button(self,image=go,command=self.keepGoing)
        b1.grid(row=3,column=0)
        b1.image = go    
        
        stop = tk.PhotoImage(file="stopAndScore.gif")
        b2 = tk.Button(self,image=stop,command=self.stop_Score) # button visible but not accessible
        b2.grid(row=3,column=1) # action can be activated
        b2.image = stop 
                
        nextP = tk.PhotoImage(file="nextPlayer.gif")        
        b3 = tk.Button(self,image=nextP, justify=tk.LEFT,command=self.nextPlayer, state=DISABLED) # button visible but not accessible
        b3.grid(row=3,column=2)
        b3.image = nextP

        
    def setButtons(self, keepButton, stopScoreButton, nextPlayerButton):
        #Set the Buttons for action or disable action
        #Boolean variables must be passed when True button DISABLED

        #THIS SECTION OF CODE IS INEFFICIENT AND MUST BE CORRECTED
        
        if keepButton:
            b1.configure(state=DISABLED) # button visible but not accessible        
        else:
            b1.configure(state=NORMAL) # button visible and accessible
            
        if stopScoreButton:     
            b2.configure(state=DISABLED) # button visible but not accessible
        else:
            b2.configure(state=NORMAL) # button visible and accessible
            
        if nextPlayerButton:                 
            b3.configure(state=DISABLED) # button visible but not accessible
        else:       
            b3.configure(state=NORMAL) 


    def rollDie(self):
        #Rolling Dice
##        print("Rolling Dice code!")
        
        count = IntVar()    #variable used for counting the number of gunshots received during the rolling of the dice
        count.set(0)
        
        
        ##     A Green die has 3 brains, 2 footprints, 1 shotgun (6 green dice)
        ##     A Yellow die has 2 brains, 2 footprints, 2 shotguns (4 yellow dice)
        ##     A Red die has 1 brain, 2 footprints, 3 shotguns (3 red dice)
        ##      
        ##     The total number of faces on the 13 dice are 78
        ##     A random number between 1 and 78 (inclusive) is generated and divided as follows:
        ##     between 1 and 18 (inclusive): green brain
        ##     between 19 and 30 (inclusive): green footprints
        ##     between 31 and 36 (inclusive): green shotgun
        ##     between 37 and 44 (inclusive): yellow brains
        ##     between 45 and 52 (inclusive): yellow footprints
        ##     between 53 and 60 (inclusive): yellow shotgun
        ##     between 61 and 63 (inclusive): red brains
        ##     between 64 and 69 (inclusive): red footprints
        ##     between 70 and 78 (inclusive): red shotgun

        for i in range(1,4):
            #loop to ensure each dice has a random new face
            num = random.randint(1,78)
            #assigning the face of the dice for the number generated
            if (num <= 18):
                logo = tk.PhotoImage(file= "greenBrain.gif")
                tempScore.set(tempScore.get()+1)
            elif (num <= 30):
                logo = tk.PhotoImage(file="greenFootPrints.gif")
            elif (num <= 36):
                logo = tk.PhotoImage(file="greenShotGun.gif")
                shot.set(shot.get()+1)
                count.set(count.get()+1)
            elif (num <= 44):
                logo = tk.PhotoImage(file="yellowBrain.gif")
                tempScore.set(tempScore.get()+1)
            elif (num <= 52):
                logo = tk.PhotoImage(file="yellowFootPrints.gif")
            elif (num <= 60):
                logo = tk.PhotoImage(file="yellowShotGun.gif")
                shot.set(shot.get()+1)
                count.set(count.get()+1)
            elif (num <= 63):
                logo = tk.PhotoImage(file="redBrain.gif")
                tempScore.set(tempScore.get()+1)
            elif (num <= 69):
                logo = tk.PhotoImage(file="redFootPrints.gif")
            else:
                logo = tk.PhotoImage(file="redShotGun.gif")
                shot.set(shot.get()+1)
                count.set(count.get()+1)
            
            #putting the face on the dice that was assigned
            if i == 1:
                l1.configure(image=logo)
                l1.image = logo

            elif i == 2:        
                l2.configure(image=logo)
                l2.image = logo

            else:
                l3.configure(image=logo)
                l3.image = logo


            #Updating the text display on the game screen for brains and shots received 
            shotScoreLabel.configure(text = "Shotguns: "+ str(shot.get()), font="Chiller 30 bold")
            brainScoreLabel.configure(text = "Braaaiinss: "+ str(tempScore.get()), font="Chiller 30 bold")
            
        if count.get() > 2:
            shot.set(0)
            tempScore.set(0)
            self.setButtons(True, True, False)           
        else:
            count.set(0)

    
    def stop_Score(self):
        #Clicking Stop & Score
##        print("Stop & Score code!")

        if cTurn.get() == 1:
            cScore.set(cScore.get() + tempScore.get())
            
            compScoreLabel.configure(text = "Player 2 Ate: "+ str(cScore.get())+ " Braaiinss", font="Chiller 35 bold")
      
        else:
            uScore.set(uScore.get() + tempScore.get())    
            
            userScoreLabel.configure(text = "Player 1 Ate: "+ str(uScore.get())+ " Braaiinss", font="Chiller 35 bold")

            
        shot.set(0)
        tempScore.set(0)
        
        self.setButtons(True, True, False)
                    
            
    def keepGoing(self):
        #Keep Going
##        print("Keep Going code!")
        self.rollDie()
      

    def nextPlayer(self):
        #After getting shotgunned
##        print("Next Player code!")

        #Updating the text display on the game screen for brains and shots received            
        shotScoreLabel.configure(text = "Shotguns: "+ str(shot.get()), font="Chiller 30 bold")
        brainScoreLabel.configure(text = "Braaaiinss: "+ str(tempScore.get()), font="Chiller 30 bold")

        
        self.resetDice()
        self.setButtons(False, False, True)       

    def beginGame(self):
        #beginning a new game screen
        
        #Clear all startup widgets
        pictureLabel.pack_forget()
        playButton.pack_forget()
        quitButton.pack_forget()

        #call the player's screen
        self.playersTurn()

    def resetDice(self):
        #Inital setting of the dice on the screen to all zombies or when the player is being changed
        global l1
        global l2
        global l3
         
        logo = tk.PhotoImage(file="zombie.gif")


        l1 = tk.Label(self, image=logo)
        l1.grid(row=2,column=0)
        l1.image = logo

 
        l2 = tk.Label(self, image=logo)
        l2.grid(row=2,column=1)
        l2.image = logo


        l3 = tk.Label(self, image=logo)
        l3.grid(row=2,column=2)
        l3.image = logo


    def playersTurn(self):
        #Player's Turn

        global shotScoreLabel  #Label locations require updating during interation of the game
        global brainScoreLabel #Each label can be updated without taking extra memory locations and will remain for program execution
        global userScoreLabel
        global compScoreLabel
        
        
        turnLabel = tk.Label(self, text="Player 1", font="Ravie 40")
        turnLabel.grid(row=0,column=0)

        shotScoreLabel = tk.Label(self, text = "Shotguns: "+ str(shot.get()), font="Chiller 30 bold")
        shotScoreLabel.grid(row=0,column=1)

        brainScoreLabel = tk.Label(self, text = "Braaaiinss: "+ str(tempScore.get()), font="Chiller 30 bold")
        brainScoreLabel.grid(row=0,column=2)
         
        userScoreLabel = tk.Label(self, text = "Player 1 Ate: "+ str(uScore.get())+ " Braaiinss", font="Chiller 35 bold")
        userScoreLabel.grid(row=1,column=0)

        compScoreLabel = tk.Label(self, text = "Player 2 Ate: "+ str(cScore.get())+ " Braaiinss", font="Chiller 35 bold")
        compScoreLabel.grid(row=1,column=2)
        
        self.resetDice()    #Zombie Logo for each dice location       
        self.activateGameButtons()  #Game buttons are set for input response from the player
            

#### MAIN BODY OF CODE ####
          
app = ZombieApplication()   #calls the initialization of the application's screen
app.master.title("Zombie Dice") #sets the title of the application's screen
app.master.maxsize(1100,410)
app.master.config(background="red")

 ###    DEFINING VARIABLES THAT ARE NECESSARY FOR THE GAME'S PROGRESS   ###

shot = IntVar()
tempScore = IntVar()
uScore = IntVar()
cScore = IntVar()
cTurn = BooleanVar()
 ###    INITIALIZING VARIABLES THAT ARE NECESSARY FOR THE GAME'S PROGRESS   ###
shot.set(0)
tempScore.set(0)
uScore.set(0)
cScore.set(0)
cTurn.set(False)


app.mainloop()

