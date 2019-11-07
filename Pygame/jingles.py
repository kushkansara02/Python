#Kush Kansara
#jingles

import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("jingles")

clock = pygame.time.Clock()
keep_going = True

while keep_going:
    clock.tick(15)

    for ev in pygame.event.get():

        if ev.type == QUIT:
            keep_going = False

        elif ev.type == KEYDOWN:

            if ev.key == K_RETURN:
                pygame.mixer.music.load("jingle.ogg")
                pygame.mixer.music.play(-1)

    pygame.display.flip()

pygame.quit()
