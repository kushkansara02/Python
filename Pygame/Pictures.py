#Kush Kansara
#pictures

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode()
pygame.display.set_caption("pictures")

background = pygame.Surface(screen.get_size()).convert()

m1 = pygame.image.load("meme1.jpg").convert()
m2 = pygame.image.load("meme2.jpg").convert()
m3 = pygame.image.load("meme3.jpg").convert()
m4 = pygame.image.load("meme4.jpg").convert()

meme_list = ("m1", "m2", "m3", "m4")

counter = 1

screen.blit(m1, (0, 0))
pygame.display.flip()

keep_going = True
clock = pygame.time.Clock()

while keep_going:
    clock.tick(15)

    for ev in pygame.event.get():

        if ev.type == QUIT:
            keep_going = False

        elif ev.type == KEYDOWN:

            if ev.key == K_RIGHT:
                screen.blit(background, (0, 0))
                exec("screen.blit(" + meme_list[counter%4] + ", (0, 0))")
                counter += 1

    pygame.display.flip()

pygame.quit()
