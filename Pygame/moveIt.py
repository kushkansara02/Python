#Kush Kansara
#moveIt

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("moveIt")

background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))
screen.blit(background, (0, 0))

x_pos = 200
y_pos = 200
movement = 50

rectangle = pygame.draw.rect(screen, (0, 0, 0), [x_pos, y_pos, 500, 500], 2)
screen.fill(Color("black"), rectangle)

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(30)

    for ev in pygame.event.get():

        if ev.type == QUIT:
            done = True

        elif ev.type == KEYDOWN:

            if ev.key == K_DOWN:
                y_pos += movement

            elif ev.key == K_UP:
                y_pos -= movement

            elif ev.key == K_LEFT:
                x_pos -= movement

            elif ev.key == K_RIGHT:
                x_pos += movement

        screen.blit(background, (0, 0))
        rectangle = pygame.draw.rect(screen, (0, 0, 0), [x_pos, y_pos, 500, 500], 2)
        screen.fill(Color("black"), rectangle)            

    pygame.display.flip()

pygame.quit()
