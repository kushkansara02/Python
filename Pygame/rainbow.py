#Kush Kansara
#Rainbow

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("rainbow")

background = pygame.Surface(screen.get_size()).convert()

clock = pygame.time.Clock()

keep_going = True

while keep_going:
    clock.tick(30)

    for ev in pygame.event.get():

        if ev.type == QUIT:
            keep_going = False

        elif ev.type == KEYDOWN:
            
            if ev.key == K_1:
                background.fill((255, 0, 0))

            elif ev.key == K_2:
                background.fill((255,127,0))

            elif ev.key == K_3:
                background.fill((255,255,0))

            elif ev.key == K_4:
                background.fill((0, 255, 0))

            elif ev.key == K_5:
                background.fill((0, 0, 255))

    screen.blit(background, (0,0))
    pygame.display.flip()

pygame.quit()
