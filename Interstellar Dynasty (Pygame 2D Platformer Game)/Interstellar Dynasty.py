#Kush Kansara
#June 15th, 2018
#Pygame Summative: Interstellar Dynasty

#The purpose of this code is to create a beautiful game using pygame, and use
#knowledge and skills that have been acquired during this course in order to
#make an efficient, fun game.

### RESOURCES ###
#https://www.youtube.com/watch?v=UdsNBIzsmlI - for understanding animation
#http://programarcadegames.com/python_examples/show_file.php?file=platform_jumper.py - for understanding gravity

import pygame
from pygame.locals import *
import sys

class Sprite(pygame.sprite.Sprite):
    #will create a sprite for game levels, depending on x-coordinates, y-coordinates, and image and updates it

    def __init__(self, xcor, ycor, image):      #parameters: x-coordinate, y-coordinate, image of sprite
        #initialize the sprite
        
        pygame.sprite.Sprite.__init__(self)     #initialize sprites

        self.image = pygame.image.load(image)   #loaded image

        self.rect = self.image.get_rect()       #set reference to the image's rect
        self.rect.left = xcor                   #set x-coordinate of the sprite
        self.rect.top = ycor                    #set y-coordinate of the sprite

        self.velocity_x = 0                     #speed of player
        self.velocity_y = 0                     #initial gravity speed

    def update(self):
        #update the sprite and check for collisions

        #global variables referenced elsewhere in the code
        global score_count, movementx
        global level
        global high_score_var

        self.gravity()                              #call gravity function when updating

        self.rect.left += self.velocity_x           #move sprite left or right

        platform_hits = pygame.sprite.groupcollide(plat_group, character_group, False, False, False) #see if platform is hit
        
        for platform in platform_hits:                  #for each collision
            
            if self.velocity_x > 0:                     #if sprite was moving left
                self.rect.right = platform.rect.left    #set platform's left to sprite's right
                
            elif self.velocity_x < 0:                   #if sprite was moving right
                self.rect.left = platform.rect.right    #set platform's right to sprite's left

        self.rect.top += self.velocity_y            #move sprite up or down

        if self.rect.top < 0:                       #if sprite's coordinates further than the top of screen
            self.rect.top = 0                       #keep sprite at top of screen

        elif self.rect.top > screen.get_height():   #if sprite's coordinates further than the bottom of screen
            score_count = 0                         #set player's score to 0
            Died()                                  #player dies, call Die function

        if self.rect.left < 0:                      #if sprite's coordinates further than the left edge of screen
            self.rect.left = 0                      #keep the sprite at the left edge of the screen

        elif self.rect.left > screen.get_width() - 300: #if sprite's coordinates are further than right edge of the screen
            self.rect.left = screen.get_width() - 300   #keep sprite at right edge of the screen

        platform_hits = pygame.sprite.groupcollide(plat_group, character_group, False, False, False) #see if platform is hit
        
        for platform in platform_hits:                  #for each collision
 
            if self.velocity_y > 0:                     #if moving up
                self.rect.bottom = platform.rect.top    #set image's top to block's bottom
                
            elif self.velocity_y < 0:                   #if moving down
                self.rect.top = platform.rect.bottom    #set image's bottom to block's top

        platform_hits = pygame.sprite.groupcollide(plat_group, enemy_group, False, False, False) #see if enemies hit platform
        
        for platform in platform_hits:                  #for each collision
 
            if self.velocity_y > 0:                     #if moving up
                self.rect.bottom = platform.rect.top    #set platform's top to enemy's bottom
                
            elif self.velocity_y < 0:                   #if moving down
                self.rect.top = platform.rect.bottom    #set platform's bottom to enemy's top

        if pygame.sprite.groupcollide(ship_group, character_group, False, True, False): #see if character touches the rocketship

            pygame.mixer.Channel(0).stop()                                  #stop previously playing music
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("rocket.ogg"))  #start rocketship sound on another channel
            
            if level == 1:      #if it is level 1
                level += 1      #level variable increments
                nextLevel()     #call the function for next level

            else:                               #if it is level 2
                high_score_var = score_count    #make player's current score a high score variable
                score_count = 0                 #reset the player's score to 0
                Win()                           #call the win function

        elif pygame.sprite.groupcollide(fuel_group, character_group, True, False, False): #see if character touches fuel

            pygame.mixer.Channel(2).play(pygame.mixer.Sound("fuel.ogg"))        #play fuel sound effect
            
            if level == 1:                          #if it is level 1
                movementx += 5                      #increment movement speed

            else:
                movementx += 10                     #if it is level 2
                score_count = score_count * 1.2     #imcrement movement speed and multiply score

        elif pygame.sprite.groupcollide(spike_group, character_group, False, True, False) or pygame.sprite.groupcollide(enemy_group, character_group, False, True, False):
            #see if character touches spikes
            pygame.mixer.Channel(0).stop()                                  #stop previously playing music
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("death.ogg"))   #start death sound effect on another channel
            score_count = 0                                                 #reset player score to 0
            Died()                                                          #call the Died function

        elif pygame.sprite.groupcollide(star_group, character_group, True, False, False): #see if character touches a star

            pygame.mixer.Channel(4).play(pygame.mixer.Sound("point.ogg"))   #play point sound effect

            if level == 1:          #if it is level 1
                score_count += 50   #increment score

            else:                   #if it is level 2
                score_count += 100  #increment score more steeply

        if level != 1: #if it isn't level 1 (black holes are first introduced in level 2)     
            
            if pygame.sprite.groupcollide(hole_group, character_group, False, False, False): #see if character touches black hole
                pygame.mixer.Channel(5).play(pygame.mixer.Sound("teleport.ogg")) #play teleport sound effect               
                character.rect.left = 300           #change character's rect coordinates to teleport him
                character.rect.top = 625

    def gravity(self):
        #apply the effect of gravity

        if self.velocity_y == 0:        #if there is no effect of gravity
            self.velocity_y = 1         #configure the effect of gravity

        else:                           #if there is an effect of gravity
            self.velocity_y += 2        #increment the effect of gravity

        if pygame.sprite.groupcollide(plat_group, character_group, False, False, False):    #if collision occurs
            self.velocity_y = 0                                                             #gravity is now 0

    def jump(self, distance):       #parameter: distance traveled in one jump
        #sprite will jump

        if self == alien1 or self == alien2 or (level != 1 and self == alien3): #if the sprite jumping is an alien
            own_group = enemy_group                                             #enemy_group will be checked for collisions

        else:
            own_group = character_group                                     #if sprite jumping is the character
            pygame.mixer.Channel(6).play(pygame.mixer.Sound("jump.ogg"))    #character_group will be checked for collisions

        walkCount = 0           #set as 0 as jumping resets animation
 
        #moving down a bit and see if there is a platform below
        self.rect.y += 2
        platformhit = pygame.sprite.groupcollide(plat_group, own_group, False, False, False)
        self.rect.y -= 2

        #if there was a platform below
        if len(platformhit) > 0 or self.rect.bottom >= screen.get_height():  #if is on ground
            self.velocity_y = -distance                 #jump upwards depending on given paramter

    def move_player(self, action, distance):
        #move the sprite

        #global variables referenced elsewhere in the code
        global movementx

        movementx = 20          #define variable for movement

        if action == "left":            #if character is going left
            self.velocity_x = -distance #x-cor has a negative change

        elif action == "right":         #if character is going right
            self.velocity_x = distance  #x-cor has a positive change

        else:                           #if character is doing neither
            self.velocity_x = 0         #x-cor has no change

        self.animations()

    def animations(self):
        #change sprite's image depending on walkCount

        #global variable referenced elsewhere in the code
        global walkCount

        #lists that contain images of each position
        Right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
        Left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

        if left:        #if character is going left
            character.image = Left[walkCount%9]     #change picture depending on walkCount
            walkCount += 1                          #walkCount increments

        elif right:     #if character is going right
            character.image = Right[walkCount%9]    #change picture depending on walkCount
            walkCount += 1                          #walkCount increments

        else:           #if neither
            character.image = pygame.image.load("standing.png") #change picture to stationary
            walkCount = 0

class CloseApp():
    #close the game and window

    def __init__(self):

        pygame.quit()   #exit pygame
        sys.exit()      #close window

class beginningScreen():
    #beginning menu of options within the game

    def __init__(self):
        #initialize items

        #global variables referenced elsewhere in the code
        global font, font2, font3, font4, font5
        global screen
        global clock
        global black, white
        global high_score_list

        screen = pygame.display.set_mode((1000, 668))       #set window dimensions
        pygame.display.set_caption("Interstellar Dynasty")  #set window caption

        background = pygame.image.load("start_screen.jpg").convert()    #load background image
        screen.blit(background, (0, 0))                                 #blit image onto screen

        #standard fonts for use throughout the whole game
        font = pygame.font.Font("mainfont.ttf", 100)
        font2 = pygame.font.Font("mainfont.ttf", 65)
        font3 = pygame.font.Font("mainfont.ttf", 20)
        font4 = pygame.font.Font("mainfont.ttf", 45)
        font5 = pygame.font.Font("mainfont.ttf", 30)

        #standard colours for use throughout the whole game
        black = (0, 0, 0)
        white = (255, 255, 255)

        #list of high scores
        high_score_list = [[2900, "Ashwin"],[3500, "Kush"],[2950, "Joshua"],[2750, "Anush"],[2500, "Devrshi"],[2030, "Paul"],[2010, "Raghu"],[2560, "Vader"],[2765, "Michael"],[2764, "Scott"]]

        #title of game and blitting it onto the screen
        title = font.render("Interstellar Dynasty", True, (255, 255, 255))
        screen.blit(title, (100, 100))

        clock = pygame.time.Clock() #defining clock variable

        self.mainloop()             #calling mainloop function

    def mainloop(self):
        #main loop for beginning menu
        global music_started

        #global variable referenced elsewhere in the code

        done = False                #variable for while loop

        if not music_started:       #if it has not started
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("startmusic.ogg"))  #initial music
            music_started = True

        while not done:         #main loop for screen
            clock.tick(30)      #set FPS
            
            for ev in pygame.event.get():   #for each event occurring

                if ev.type == QUIT:         #if the event is quit, end the loop
                    done = True                   

            #main buttons in the main screen for use
            button(650, 250, 285, 75, "Play Game", level1_gameScreen, black, white)
            button(650, 325, 300, 75, "Game Story", GameStory, black, white)
            button(650, 400, 310, 75, "High Scores", Highscore, black, white)
            button(650, 475, 200, 75, "Controls", Controls, black, white)
            button(650, 550, 100, 75, "Quit", CloseApp, black, white)

            #update the screen
            pygame.display.flip()

        #when loop ends, close window
        CloseApp()

class button():
    #will create a "button" on screen for use by the player

    def __init__(self, ixcor, iycor, width, height, text, function, colour1, colour2):#parameters for basic qualities of button
        #initializing the button

        #mouse variables
        mouse = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        #if mouse's coordinates are in range of the button's rect
        if (ixcor + width > mouse[0] > ixcor) and (iycor + height > mouse[1] > iycor):
            label = font2.render(text, True, colour2)       #set a label
            if mouse_press[0] == 1:     #if mouse is clicked while in the range
                function()              #call function defined in parameters

        #if mouse's coordinates are elsewhere                           
        else:
            label = font2.render(text, True, colour1)   #set label to different colour

        screen.blit(label, (ixcor, iycor))      #bilt the label

class level1_gameScreen():
    #class for first level of game

    def __init__(self):
        #initializing the level

        #global variables referenced elsewhere in the code
        global plat_group, character_group, ship_group, fuel_group, spike_group, star_group, enemy_group
        global score_count, level, background
        global screen_locations, fuel_locations, spike_locations, star_locations

        pygame.mixer.music.stop()                                           #stop previously playing music
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("gamemusic.ogg"))   #play level music
        
        pygame.display.set_mode((1050, 750))    #set window dimensions

        background = pygame.image.load("space_background.png").convert()    #initialize background

        #essential sprite groups for the level
        plat_group = pygame.sprite.Group()
        character_group = pygame.sprite.Group()
        ship_group = pygame.sprite.Group()
        fuel_group = pygame.sprite.Group()
        spike_group = pygame.sprite.Group()
        star_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()

        level = 1           #variable to hold the information of what level it is
        score_count = 0     #variable to hold player's score

        #variable for platform and rocket locations
        screen_locations = [
        "       R",
        "   PPPPP",
        "",
        "PPPPPP",
        "",
        "  PPPPPP",
        "        ",
        "PPPPPPPP",
        ]

        #variable for fuel locations
        fuel_locations = [
        "   F",
        "   F",
        "    F",
        " F",
        ]

        #variable for spike locations
        spike_locations = [
        "",
        "     S",
        "  S",
        "   S",
        "  S",
        ]

        #variable for star loctions
        star_locations = [
        "",
        " TTT",
        " TT TT",
        " TTT T",
        "   TTT",
        ]

        self.gameObjects()  #call next function to create sprites

    def gameObjects(self):
        #will call Sprite class to actually create the sprites on the level

        #global variables referenced elsewhere in the code
        global character, alien1, alien2

        #coordinates for platform and rocket locations
        mainx = mainy = 0

        for row in screen_locations:
            
            for char in row:
                
                if char == "P":                                     #for every letter "P"
                    platform = Sprite(mainx, mainy, "platform.png") #create platform sprite
                    plat_group.add(platform)                        #add it to its respective group

                elif char == "R":                                   #for every letter "R"
                    ship = Sprite(mainx, mainy, "rocketship.png")   #create rocketship sprite
                    ship_group.add(ship)                            #add it to its respective group

            #increment coordinates to keep the array going
                mainx += 100
            mainy += 100
            mainx = 0

        #coordinates for fuel locations
        fuelx = fuely = 25

        for row in fuel_locations:
            
            for char in row:
                
                if char == "F":                                         #for every letter "F"
                    fuel = Sprite(fuelx, fuely, "rocketship_fuel.png")  #create a fuel sprite
                    fuel_group.add(fuel)                                #add it to its respective group

            #increment x-coordinate to keep the array going
                fuelx += 100    
            fuely += 200
            fuelx = 0

        #coordinates for spike locations
        spikex = 0
        spikey = -115
        
        for row in spike_locations:
            
            for char in row:
                
                if char == "S":                                     #for every letter "S"
                    spike = Sprite(spikex, spikey, "spikes.png")    #create spike sprite
                    spike_group.add(spike)                          #add it to its respective group

            #increment x-coordinate to keep the array going
                spikex += 100
            spikey += 200
            spikex = 0

        #coordinates for star locations
        starx = stary = -170

        for row in star_locations:
            
            for char in row:
                
                if char == "T":                             #for every letter "T"
                    star = Sprite(starx, stary, "star.png") #create star sprite
                    star_group.add(star)                    #add it to its respective group

            #increment x-coordinate to keep the array going
                starx += 100
            stary += 200
            starx = 0

        #introduce alien sprites as enemies
        alien1 = Sprite(725, 400, "alien.png")
        alien2 = Sprite(0, 200, "alien.png")
        enemy_group.add(alien1, alien2)         #add these sprites to the enemy_group

        #introduce the main character's sprite
        character = Sprite(650, 625, "standing.png")
        character_group.add(character)          #add this sprite to the character_group

        self.mainloop()         #call mainloop function

    def mainloop(self):
        #main loop for level 1

        #global variables referenced elsewhere in the code
        global left, right

        #basic essential variables
        done = False            #for while loop
        left = False            #for character position
        right = False           #for character position
        alien_alternate = True  #for aliens going back and forth

        counter = 0  #counter to regulate alien movements

        level_display = font4.render("Level 1", True, white)    #display level  

        while not done:
            clock.tick(27)      #set FPS to match character animations

            #regulate alien movements in each loop
            #regularly go left and right as well as jump
            if alien_alternate:

                if counter <= 10:
                    alien1.move_player("left", 5)
                    alien2.move_player("right", 5)
                    counter += 1

                else:
                    alien1.jump(30)
                    alien2.jump(30)
                    alien_alternate = False
                    counter = 0

            else:

                if counter <= 10:
                    alien1.move_player("right", 5)
                    alien2.move_player("left", 5)
                    counter += 1

                else:
                    alien1.jump(30)
                    alien2.jump(30)
                    alien_alternate = True
                    counter = 0

            for ev in pygame.event.get():   #for each event during the game

                if ev.type == QUIT:         #if event is quit, end loop
                    done = True

                if ev.type == KEYDOWN:      #if key is pressed

                    key = pygame.key.get_pressed()  #set variable
                    
                    if key[K_LEFT]:     #if left key is pressed

                        #set position variables
                        left = True
                        right = False

                        #move player
                        character.move_player("left", movementx)

                    if key[K_RIGHT]:    #if right key is pressed

                        #set position variables
                        left = False
                        right = True

                        #move player
                        character.move_player("right", movementx)

                    if key[K_UP]:       #if up key is pressed

                        #set position variables
                        left = False
                        right = False

                        #make player jump
                        character.jump(30)
                        
                elif ev.type == KEYUP:      #if key is let go
                    
                    #set position variables
                    left = False
                    right = False

                    #make player stationary if left or right keys are not being pressed
                    if (ev.key == K_LEFT and character.velocity_x < 0) or (ev.key == K_RIGHT and character.velocity_x > 0):
                        character.move_player("stay", movementx)

            #defining surfaces and labels for the level
            score_label = font4.render(" Score: " + str(int(score_count)), True, white)
            display_surface = pygame.Surface((250, 750))
            display_surface.fill((244, 152, 66))

            #blitting the essential labels and surfaces
            screen.blit(background, (0, 0))

            screen.blit(display_surface, (815, 0))
            screen.blit(score_label, (825, 375))
            screen.blit(level_display, (825, 300))
            
            #drawing sprite groups that do not need to be updated
            plat_group.draw(screen)
            ship_group.draw(screen)
            fuel_group.draw(screen)
            spike_group.draw(screen)
            star_group.draw(screen)

            #drawing sprite groups that need to be updated
            enemy_group.clear(screen, background)       #clears current sprites on screen
            enemy_group.update()                        #updates the group
            enemy_group.draw(screen)

            character_group.clear(screen, background)   #clears current sprites on screen
            character_group.update()                    #updates the group
            character_group.draw(screen)

            pygame.display.flip()       #update screen
            
        CloseApp()      #close window if loop is exited

class level2_gameScreen():
    #class for level 2 of the game

    def __init__(self):
        #initializing the level

        #global variables referenced elsewhere in the code
        global hole_group
        global screen_locations, fuel_and_hole_locations, spike_locations, star_locations

        pygame.mixer.music.stop()                                           #stop previous music
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("gamemusic.ogg"))   #play level music

        screen = pygame.display.set_mode((1050, 750))           #set screen dimensions

        hole_group = pygame.sprite.Group()      #introduce new group for new item (black hole)

        #empty sprite groups from previous level
        plat_group.empty()
        character_group.empty()
        ship_group.empty()
        fuel_group.empty()
        spike_group.empty()
        star_group.empty()
        enemy_group.empty()

        #locations for platform and rocketship
        screen_locations = [
        "R",
        "PPPPP",
        "",
        "PPPPP",
        "",
        "PPPPP",
        "",
        "PPPPP",
        ]

        #locations for fuel and black holes
        fuel_and_hole_locations = [
        "   F",
        " F H",
        " H F",
        "FH",
        ]

        #locations for spikes
        spike_locations = [
        "",
        "   S",
        "  S",
        " S",
        "S",
        ]

        #locations for stars
        star_locations = [
        "",
        "TTT",
        "T TT",
        "TTT ",
        "TTT",
        ]

        self.gameObjects()      #call function which will create objects for the game

    def gameObjects(self):
        #creates essential sprites and objects for level

        #global variables referenced elsewhere in the code
        global character, alien1, alien2, alien3

        #coordinates for platform and rocketship locations
        mainx = mainy = 0

        for row in screen_locations:
            
            for char in row:
                
                if char == "P":                                     #for every letter "P"
                    platform = Sprite(mainx, mainy, "platform.png") #create platform sprite
                    plat_group.add(platform)                        #add it to its respective group

                elif char == "R":                                   #for every letter "R"
                    ship = Sprite(mainx, mainy, "rocketship.png")   #create rocketship sprite
                    ship_group.add(ship)                            #add it to its respective group

            #increment coordinate variables to keep array going on the screen
                mainx += 100
            mainy += 100
            mainx = 0

        #coordinates for fuel and black hole locations
        objectx = objecty = 25

        for row in fuel_and_hole_locations:
            
            for char in row:
                
                if char == "F":                                             #for every letter "F"                                    
                    fuel = Sprite(objectx, objecty, "rocketship_fuel.png")  #create fuel sprite
                    fuel_group.add(fuel)                                    #add it to its respective group

                elif char == "H":                                           #for every letter "H"
                    hole = Sprite(objectx, objecty, "black_hole.png")       #create black hole sprite
                    hole_group.add(hole)                                    #add it to its respective group

            #increment coordinate variables to keep array going on the screen
                objectx += 100
            objecty += 200
            objectx = 0

        #coordinates for spike locations
        spikex = 0
        spikey = 80
        
        for row in spike_locations:
            
            for char in row:
                
                if char == "S":                                     #for every letter "S"
                    spike = Sprite(spikex, spikey, "spikes.png")    #create spike sprite
                    spike_group.add(spike)                          #add it to its respective group

            #increment coordinate variables to keep array going on the screen
                spikex += 100
            spikey += 200
            spikex = 0

        #coordinates for star locations
        starx = stary = -175

        for row in star_locations:
            
            for char in row:
                
                if char == "T":                             #for every letter "T"
                    star = Sprite(starx, stary, "star.png") #create star sprite
                    star_group.add(star)                    #add it to its respective group

            #increment coordinate variables to keep array going on the screen
                starx += 100
            stary += 200
            starx = 0

        #creating the character sprite
        character = Sprite(250, 625, "standing.png")
        character_group.add(character)          #adding it to its respective group

        #creating the enemy sprites
        alien1 = Sprite(400, 625, "alien2.png")
        alien2 = Sprite(400, 425, "alien2.png")
        alien3 = Sprite(400, 225, "alien2.png")
        enemy_group.add(alien1, alien2, alien3) #adding them to their respective group

        self.mainloop()     #call mainloop function

    def mainloop(self):
        #mainloop for level 2

        #global variables referenced elsewhere in the code
        global left, right

        #positional variables
        left = False
        right = False

        done = False    #variable for while loop

        while not done:
            clock.tick(27)      #set FPS according to character's animation

            #for every loop, make the enemies jump
            alien1.jump(50)
            alien2.jump(50)
            alien3.jump(50)

            for ev in pygame.event.get():       #for an event in the level

                if ev.type == QUIT:             #if the event is quit, end the loop
                    done = True

                elif ev.type == KEYDOWN:        #if the event is a key being pressed
        
                    key = pygame.key.get_pressed()  #key variable
                    
                    if key[K_LEFT]:     #if key being pressed is left

                        #set positional variables
                        left = True
                        right = False

                        #move player
                        character.move_player("left", movementx)

                    if key[K_RIGHT]:    #if key being pressed is right

                        #set positional variables
                        left = False
                        right = True

                        #move player
                        character.move_player("right", movementx)

                    if key[K_UP]:       #if key being pressed is up
    
                        #set positional variables
                        left = False
                        right = False

                        #make the character jump
                        character.jump(30)
                        
                elif ev.type == KEYUP:      #if key is not being pressed

                    #set positional variables
                    left = False
                    right = False

                    #if key not being pressed is left or right, make the player stay
                    if (ev.key == K_LEFT and character.velocity_x < 0) or (ev.key == K_RIGHT and character.velocity_x > 0):
                        character.move_player("stay", movementx)

            #essential labels and surfaces for the level
            score_label = font4.render(" Score: " + str(int(score_count)), True, white)
            display_surface = pygame.Surface((250, 750))
            display_surface.fill((244, 152, 66))

            #blitting the surfaces and labels of the level
            screen.blit(background, (0, 0))

            screen.blit(display_surface, (800, 0))
            screen.blit(score_label, (800, 375))

            #drawing the sprite groups that don't need to be updated
            plat_group.draw(screen)
            ship_group.draw(screen)
            fuel_group.draw(screen)
            spike_group.draw(screen)
            star_group.draw(screen)
            hole_group.draw(screen)

            #drawing the sprite groups that need to be updated
            enemy_group.clear(screen, background)       #clear the sprites on the screen
            enemy_group.update()                        #update the group
            enemy_group.draw(screen)

            character_group.clear(screen, background)  #clear the sprites on the screen 
            character_group.update()                    #update the group
            character_group.draw(screen)

            pygame.display.flip()       #update the screen
            
        CloseApp()      #close game and window when loop is ended

class Died():
    #screen being called when character dies

    def __init__(self):
        #initializing screen

        pygame.mixer.Channel(0).stop()       #stop previously playing music

        background = pygame.image.load("transition.jpg").convert()  #initialize background

        pygame.display.set_mode((960, 541))     #set window dimensions

        youWin = font2.render("You Failed... Please Try Again.", True, (0, 0, 0))   #main label

        win_pic = pygame.image.load("died.jpg").convert()       #loading the main image on screen

        #blitting everything on to the screen
        screen.blit(background, (0, 0))
        screen.blit(win_pic, (275, 150))
        screen.blit(youWin, (85, 0))

        self.mainLoop() #calling the mainloop function

    def mainLoop(self):
        #the mainloop for the death screen

        done = False        #variable for while loop

        while not done:
            clock.tick(30)      #set FPS

            for ev in pygame.event.get():       #for each event in the game

                if ev.type == QUIT:     #if the event is quit
                    done = True         #end loop

            if level == 1:      #if it was level 1, create button that restarts level 1
                button(350, 450, 300, 75, "Try Again", level1_gameScreen, black, white)

            else:               #if it was level 2, create button that restarts level 2
                button(350, 450, 300, 75, "Try Again", level2_gameScreen, black, white)
            
            pygame.display.flip()       #update the screen
                    
        CloseApp()      #close the window and game if the loop is ended

class nextLevel():
    #screen called when player passes a level

    def __init__(self):
        #initializing the screen

        background = pygame.image.load("transition.jpg").convert()  #initializing the background

        pygame.display.set_mode((960, 541))     #set window dimensions

        youWin = font2.render("Good Job! On to the next level!", True, (0, 0, 0))   #main label

        win_pic = pygame.image.load("win.jpg").convert()        #loading the main image on screen

        #blitting everything on to the screen
        screen.blit(background, (0, 0))
        screen.blit(win_pic, (275, 150))
        screen.blit(youWin, (75, 0))
        
        self.mainLoop()     #call the mainloop function

    def mainLoop(self):
        #mainloop for the next level screen

        done = False        #variable for while loop

        while not done:
            clock.tick(30)      #set FPS

            for ev in pygame.event.get():       #for every event

                if ev.type == QUIT:         #if event is quit, end loop
                    done = True

            #create button to go on to the next level
            button(350, 450, 300, 75, "Next Level", level2_gameScreen, black, white)
            
            pygame.display.flip()       #update the screen
                    
        CloseApp()      #close window and game if loop is ended

class Win():
    #screen being called when player beats both levels

    def __init__(self):
        #initializing the screen

        background = pygame.image.load("winback.jpg").convert()     #initializing the background

        pygame.display.set_mode((960, 541)) #set the window dimensions

        #main variables for the end screen
        youWin = font2.render("You have beaten the game!", True, black)
        theScore = font4.render("Your score was:" + str(int(high_score_var)), True, black)

        #main image
        win_pic = pygame.image.load("win.jpg").convert()

        #blitting everything on to the screen
        screen.blit(background, (0, 0))
        screen.blit(win_pic, (275, 150))
        screen.blit(youWin, (75, 0))
        screen.blit(theScore, (75, 50))
        
        self.mainloop()     #calling the mainloop for the screen

    def mainloop(self):
        #the mainloop for the end screen

        done = False        #variable for while loop

        while not done:
            clock.tick(30)      #set FPS

            for ev in pygame.event.get():       #for each event in the game

                if ev.type == QUIT:         #if the event is quit
                    done = True             #end the loop

            #create a button to go to the next screen
            button(425, 450, 150, 75, "Next", enterHighscore, black, (200, 0, 0))

            pygame.display.flip()   #update the game screen
                    
        CloseApp()      #close window and game if loop is ended

class enterHighscore():
    #screen called when user enters high score

    def __init__(self):
        #initializing the screen

        #global variables referenced in other areas of code
        global high_score_list
        global score1, score2, score3, score4, score5, score6, score7, score8, score9, score10

        pygame.display.set_mode((950, 600))     #setting the window dimensions

        background = pygame.image.load("highscores.png").convert()  #initializing the background
        screen.blit(background, (0, 0))     #blitting the background

        #main labels and surfaces created and blitted
        title = font5.render("Your score was: " + str(int(high_score_var)) + ", type your name and press enter", True, black)
        screen.blit(title, (100, 25))
        text_entry = pygame.Surface((500, 50))
        text_entry.fill((255, 255, 255))
        entry_value = ""                    #main text variable
        entry_text = font.render(entry_value, True, black)

        done = False        #variable for while loop

        while not done:
            clock.tick(30)  #set FPS

            for ev in pygame.event.get():       #for each event in the game

                if ev.type == QUIT:             #if the event is quit
                    done = True                 #end the loop

                elif ev.type == KEYDOWN:        #if the event is a key being pressed
                    
                    if ev.key == K_BACKSPACE and len(entry_value) > 0:  #if key is backspace
                        entry_value = entry_value[:-1]                  #shorten length of the variable by 1

                    elif (ev.unicode.isalnum() or ev.key == K_SPACE) and len(entry_value) < 20: #if a letter is pressed
                        entry_value += ev.unicode           #add the unicode onto the string (letter)

                    elif ev.key == K_RETURN:                #if return is pressed
                        next_entry = [int(high_score_var), entry_value]    #list with player's score and name
                        high_score_list.append(next_entry)                      #add this list into another nested list
                        high_score_list.sort(reverse = True)                    #sort the list to make higher numbers first

                        #update top 10 scores as text (using different indices of the nested list)
                        score1 = font4.render(str(high_score_list[0]), True, black)
                        score2 = font4.render(str(high_score_list[1]), True, black)
                        score3 = font4.render(str(high_score_list[2]), True, black)
                        score4 = font4.render(str(high_score_list[3]), True, black)
                        score5 = font4.render(str(high_score_list[4]), True, black)
                        score6 = font4.render(str(high_score_list[5]), True, black)
                        score7 = font4.render(str(high_score_list[6]), True, black)
                        score8 = font4.render(str(high_score_list[7]), True, black)
                        score9 = font4.render(str(high_score_list[8]), True, black)
                        score10 = font4.render(str(high_score_list[9]), True, black)

                        music_started = False       #restart the starting music
                       
                        beginningScreen()                                       #call the beginning screen

                #update the entry text
                entry_text = font4.render(entry_value, True, (0, 0, 0))

                #blit everything on tp the screen
                screen.blit(text_entry, (225, 275))
                screen.blit(entry_text, (225, 275))
            
            pygame.display.flip()       #update the game screen

        CloseApp()          #close window and game if loop is ended

class Highscore():
    #screen to show all high scores

    def __init__(self):
        #initializing the screen

        pygame.display.set_mode((950, 600))     #set screen dimensions

        background = pygame.image.load("highscores.png").convert()      #initialize background
        screen.blit(background, (0, 0))

        title = font.render("High Scores!", True, black)        #create title text
        screen.blit(title, (250, 0))                            #blit title

        self.mainloop()         #call mainloop function

    def mainloop(self):
        #mainloop for the high score screen

        #global variable referenced elsewhere in the code
        global high_score_list

        done = False        #variable for while loop

        while not done:
            clock.tick(30) #set FPS

            for ev in pygame.event.get():       #for each event in the game

                if ev.type == QUIT:             #if event is quit, end the loop
                    done = True

                try:        #try blitting these labels onto the screen
                    #blitting the updated high scores onto the screen
                    screen.blit(score1, (350, 100))
                    screen.blit(score2, (350, 150))
                    screen.blit(score3, (350, 200))
                    screen.blit(score4, (350, 250))
                    screen.blit(score5, (350, 300))
                    screen.blit(score6, (350, 350))
                    screen.blit(score7, (350, 400))
                    screen.blit(score8, (350, 450))
                    screen.blit(score9, (350, 500))
                    screen.blit(score10, (350, 550))

                except: #if an error occurs, it means that the user has not completed the game, release non-updated scores
                    #blitting a statement for the player
                    sorry = font4.render("No Scores have been updated. Beat the Game!", True, black)
                    screen.blit(sorry, (25, 300))

            #create button to go back to the main menu
            button(0, 0, 150, 75, "Back", beginningScreen, black, white)

            pygame.display.flip()       #update the game screen

        CloseApp()      #close window and game if the loop has ended
        
class GameStory():
    #screen to display the game's story

    def __init__(self):
        #initialization of the screen

        pygame.display.set_mode((750, 750))     #set window dimensions

        background = pygame.image.load("GameStory.png").convert()       #initializing background
        screen.blit(background, (0, 0))                                 #blitting background

        #instruction labels for the story
        instr1 = font3.render("Hello, challenger! You have come to test your skills, I see. You think", True, white)
        instr2 = font3.render("you can make it in space? Very well. In this story, you are General Solomon", True, white)
        instr3 = font3.render("Crox, an outcast from the planet Klorg. Your friends don't seem to want", True, white)
        instr4 = font3.render("you anymore, and that's fine. You are more than determined to survive.", True, white)
        instr5 = font3.render("The only problem? Actually doing so. Along the way to freedom, you", True, white)
        instr6 = font3.render("will face many obstacles, and will have to make many sacrifices. But,", True, white)
        instr7 = font3.render("in the end, you will come out victorious. The point of this game is", True, white)
        instr8 = font3.render("to survive through Solomon's journey. Get through all of the platform", True, white)
        instr9 = font3.render("levels successfully, while dodging all of your enemies' attempts of", True, white)
        instr9 = font3.render("                          levels without anyone stopping you.", True, white)
        instr10 = font5.render("Do not stay in the same spot for more than two seconds", True, (255, 0, 0))
        instr11 = font5.render("The interstellar equilibrium will shake, and you will die", True, (255, 0, 0))

        #blitting the instruction labels
        screen.blit(instr1, (125, 25))
        screen.blit(instr2, (125, 75))
        screen.blit(instr3, (125, 125))
        screen.blit(instr4, (125, 175))
        screen.blit(instr5, (125, 225))
        screen.blit(instr6, (125, 275))
        screen.blit(instr7, (125, 325))
        screen.blit(instr8, (125, 375))
        screen.blit(instr9, (125, 425))
        screen.blit(instr10, (25, 500))
        screen.blit(instr11, (25, 550))

        self.mainLoop()     #calling the mainloop function

    def mainLoop(self):
        #mainloop for the game story screen

        done = False        #variable for the while loop

        while not done:
            clock.tick(30)  #set FPS

            for ev in pygame.event.get():       #for each event in the game

                if ev.type == QUIT:             #if the event is quit
                    done = True                 #end the loop

            #create button to go back to the game menu
            button(375, 650, 130, 50, "Back", beginningScreen, white, black)

            pygame.display.flip()       #update game screen

        CloseApp()      #close window and game if loop is ended

class Controls():
    #screen to show controls to player

    def __init__(self):
        #initializing screen

        pygame.display.set_mode((950, 600))     #set window dimensions

        background = pygame.image.load("Controls.jpg").convert()        #initializing the background
        screen.blit(background, (0, 0))

        #creating instruction labels for the controls
        instr1 = font4.render("The controls of this game are simple.", True, black)
        instr2 = font4.render("Use the left and right arrow keys to move.", True, black)
        instr3 = font4.render("Use the up arrow key to jump.", True, black)
        instr4 = font4.render("Avoid the enemies and dangerous obstacles,", True, black)
        instr5 = font4.render("And get to your shuttle in order to win.", True, black)
        instr6 = font3.render("Collect these for a movement speed boost", True, black)
        instr7 = font3.render("Collect these for points", True, black)
        instr8 = font3.render("Avoid these, they will kill you", True, black)
        instr9 = font3.render("These will transport you elsewhere", True, black)

        #loading images for items
        fuel = pygame.image.load("rocketship_fuel.png").convert()
        star = pygame.image.load("star.png").convert()
        spikes = pygame.image.load("spikes.png").convert()
        black_hole = pygame.image.load("black_hole.png").convert()

        #blitting everything on to the screen
        screen.blit(background, (0, 0))
        
        screen.blit(instr1, (50 , 25))
        screen.blit(instr2, (50, 75))
        screen.blit(instr3, (50, 125))
        screen.blit(instr4, (50, 175))
        screen.blit(instr5, (50, 225))
        screen.blit(instr6, (150, 300))
        screen.blit(instr7, (150, 350))
        screen.blit(instr8, (150, 400))
        screen.blit(instr9, (150, 450))

        screen.blit(fuel, (525, 275))
        screen.blit(star, (350, 340))
        screen.blit(spikes, (400, 400))
        screen.blit(black_hole, (475, 425))

        self.mainLoop()     #calling the mainloop function

    def mainLoop(self):
        #mainloop for controls creen

        done = False        #variable for while loop

        while not done:
            clock.tick(30)  #set FPS

            for ev in pygame.event.get():       #for each event in the game

                if ev.type == QUIT:         #if the event is quit
                    done = True             #end the loop

            #create button to go back to game menu
            button(475, 500, 150, 50, "Back", beginningScreen, black, white)

            pygame.display.flip()       #update game screen

        CloseApp()      #close window and game if loop is ended

pygame.init()       #initialize pygame
pygame.mixer.init() #initialize pygame.mixer

music_started = False       #variable to hold if the beginning music has started (to ensure it doesn't restart
                            #when coming back from other screens)

walkCount = 0           #define variable for animations

beginningScreen()   #call first screen
