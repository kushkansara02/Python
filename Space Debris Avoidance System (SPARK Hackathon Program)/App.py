import pygame
from pygame.locals import *
import sys

class CloseApp():

    def __init__(self):

        pygame.quit()
        sys.exit()

class MainMenu():

    def __init__(self):
        global font, font2, font3
        global black, white, red
        global clock, screen

        screen = pygame.display.set_mode((1000, 668))
        pygame.display.set_caption("Space Debris Avoidance System")

        background = pygame.image.load("mainmenu.jpg").convert()
        screen.blit(background, (0, 0))

        font = pygame.font.Font("mainfont.ttf", 65)
        font2 = pygame.font.Font("mainfont.ttf", 50)
        font3 = pygame.font.Font("mainfont.ttf", 25)

        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 50, 50)

        back1 = pygame.surface.Surface((925, 75))
        back1.fill(black)
        screen.blit(back1, (25, 50))

        title = font.render("Space Debris Avoidance System", True, (white))
        screen.blit(title, (50, 50))

        clock = pygame.time.Clock()
        self.mainloop()

    def mainloop(self):

        done = False

        while not done:
            clock.tick(30)

            for ev in pygame.event.get():

                if ev.type == QUIT:
                    done = True

            button(750, 250, 100, 75, "Info", infoScreen, white, red, black)
            button(750, 400, 100, 75, "Calculate", PathwayQuestion, white, red, black)
            button(750, 550, 100, 75, "Quit", CloseApp, white, black, red)

            pygame.display.flip()

        CloseApp()


class button():
    #will create a "button" on screen for use by the player

    def __init__(self, ixcor, iycor, width, height, text, function, colour1, colour2, colour3):#parameters for basic qualities of button
        #initializing the button

        #mouse variables
        mouse = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        box = pygame.surface.Surface((width + 100, height - (0.33*height/len(text))))
        box.fill(colour3)

        #if mouse's coordinates are in range of the button's rect
        if (ixcor + width > mouse[0] > ixcor) and (iycor + height > mouse[1] > iycor):
            label = font2.render(text, True, colour2)       #set a label
            if mouse_press[0] == 1:     #if mouse is clicked while in the range
                function()              #call function defined in parameters

        #if mouse's coordinates are elsewhere                           
        else:
            label = font2.render(text, True, colour1)   #set label to different colour

        screen.blit(box, (ixcor - 12, iycor - 12))
        screen.blit(label, (ixcor, iycor))              #blit the label

class infoScreen():

    def __init__(self):

        background = pygame.image.load("space debris.jpg").convert()

        box = pygame.surface.Surface((500, 75))
        box.fill(white)
        box2 = pygame.surface.Surface((550, 500))
        box2.fill(white)

        title = font.render("What do we do?", True, (black))
        text = font3.render("Space exploration, although very complicated, is", True, (black))
        text2 = font3.render("at the forefront of human innovation. And,", True, (black))
        text3 = font3.render("although it can be very rewarding when done", True, (black))
        text4 = font3.render("right, the complications that can occur are", True, (black))
        text5 = font3.render("very dire - often death. One of the main issues", True, (black))
        text6 = font3.render("in this area is the presence of space debris", True, (black))
        text7 = font3.render("We  recognized this problem, so in this software", True, (black))
        text8 = font3.render("application, you will find the technology", True, (black))
        text9 = font3.render("needed in order to greatly reduce the chance", True, (black))
        text10 = font3.render("of your space shuttle being punctured by junk!", True, (black))
        
        done = False
        
        while not done:
            clock.tick(30)

            for ev in pygame.event.get():

                if ev.type == QUIT:
                    done = True

            screen.blit(background, (0, 0))
            screen.blit(box, (265, 50))
            screen.blit(title, (300, 50))
            screen.blit(box2, (225, 150))

            z = 250
            y = 165
            x = 50
            screen.blit(text, (z, y))
            screen.blit(text2, (z, y+x))
            screen.blit(text3, (z, y+2*x))
            screen.blit(text4, (z, y+3*x))
            screen.blit(text5, (z, y+4*x))
            screen.blit(text6, (z, y+5*x))
            screen.blit(text7, (z, y+6*x))
            screen.blit(text8, (z, y+7*x))
            screen.blit(text9, (z, y+8*x))
            screen.blit(text10, (z, y+9*x))

            button(850, 550, 100, 75, "Back", MainMenu, black, white, red)
            
            pygame.display.flip()

        CloseApp()

class PathwayQuestion():

    def __init__(self):
        global picked_planet
        picked_planet = ""
        
        background = pygame.surface.Surface((1000, 668))  #initializing the background
        background.fill((66, 155, 244))
        screen.blit(background, (0, 0))     #blitting the background

        #main labels and surfaces created and blitted
        title = font2.render("Please select which planet you want to go to", True, black)
        xtra = font3.render("Select a major planet where you wish to go", True, black)
        xtra2 = font3.render("and our systems will opticmize your route", True, black)
        xtra3 = font3.render("to make sure you avoid space debris!", True, black)

        x = 300
        y = 100
        z = 25
        screen.blit(title, (50, 25))
        screen.blit(xtra, (x, y + z))
        screen.blit(xtra2, (x, y + 2*z))
        screen.blit(xtra3, (x, y + 3*z))
        
        text_entry = pygame.Surface((500, 50))
        text_entry.fill((255, 255, 255))
        entry_value = ""                    #main text variable
        entry_text = font.render(entry_value, True, black)
       
        done = False
        
        while not done:
            clock.tick(30)

            for ev in pygame.event.get():
                entry_text = font.render(entry_value, True, black)

                if ev.type == QUIT:
                    done = True

                elif ev.type == KEYDOWN:

                    if ev.key == K_BACKSPACE and len(entry_value) > 0:
                        entry_value = entry_value[:-1]

                    elif (ev.unicode.isalnum() or ev.key == K_SPACE) and len(entry_value) < 20:
                        entry_value += ev.unicode

                    elif ev.key == K_RETURN:
                        picked_planet = entry_value
                        Pathway(picked_planet)
                        
                screen.blit(text_entry, (275, 300))
                screen.blit(entry_text, (275, 300))

            button(850, 550, 100, 75, "Back", MainMenu, black, white, red)            
            pygame.display.flip()

        CloseApp()

class Pathway():

    def __init__(self, planet):
        
        if planet == "uranus":
            planet = "U"
        elif planet == "venus":
            planet = "V"
        elif planet == "mercury":
            planet = "M"
        elif planet == "jupiter":
            planet = "J"
        elif planet == "saturn":
            planet = "R"
        else:
            print("Invalid Syntax, Please try Again.")
            PathwayQuestion()

        stars = pygame.image.load("solar.jpg")
        screen.blit(stars, (0, 0))

        helio = [
                "     D   ",
                "  D     U",
                "D    E   ",
                "   V  M  ",
                "    S D  ",
                "   D     ",
                "         ",
                " J  D    ",
                "     R   ",
]
        mainx = mainy = 0

        screen.blit(stars, (0, 0))
        pygame.display.flip()

        for row in helio:
            
            for char in row:
                
                if char == "U":                                     
                    uranus = pygame.image.load("uranus.jpg").convert()
                    screen.blit(uranus, (mainx, mainy))

                elif char == "E":                                     
                    earth = pygame.image.load("earth.png").convert()
                    screen.blit(earth, (mainx, mainy))

                elif char == "V":                                     
                    venus = pygame.image.load("venus.jpg").convert()
                    screen.blit(venus, (mainx, mainy))

                elif char == "M":                                     
                    mercury = pygame.image.load("mercury.jpg").convert()
                    screen.blit(mercury, (mainx, mainy))

                elif char == "J":                                     
                    jupiter = pygame.image.load("jupiter.jpg").convert()
                    screen.blit(jupiter, (mainx, mainy))

                elif char == "R":                                     
                    saturn = pygame.image.load("saturn.jpg").convert()
                    screen.blit(saturn, (mainx, mainy))

                elif char == "D":                                     
                    debris = pygame.image.load("debris.png").convert()
                    screen.blit(debris, (mainx, mainy))

                pygame.display.flip()
            
            #increment coordinates to keep the array going
                mainx += 100
            mainy += 61
            mainx = 0

        done = False

        while not done:
            clock.tick(30)

            for ev in pygame.event.get():

                if ev.type == QUIT:
                    done = True
        
        CloseApp()

pygame.init()

MainMenu()
