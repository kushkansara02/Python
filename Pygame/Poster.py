#Kush Kansara
#poster

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 316))
pygame.display.set_caption("poster")

background = pygame.Surface(screen.get_size()).convert()
screen.blit(background, (0, 0))

kingsman = pygame.image.load("kingsman.jpg").convert()
screen.blit(kingsman, (0, 0))

kingsman_font = pygame.font.Font("texgyreschola-bold.otf", 40)
main_label = kingsman_font.render("Kingsman", False, ((244, 215, 66)))
screen.blit(main_label, (200, 0))

pygame.display.flip()

keep_going = True

clock = pygame.time.Clock()

while keep_going:
    clock.tick(10)

    for ev in pygame.event.get():
        
        if ev.type == QUIT:
            keep_going = False

pygame.quit()
