#Kush Kansara
#BallMovement

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("BallMovement")

background = pygame.Surface(screen.get_size()).convert()

ball = pygame.image.load("ball.png")
x_pos = 0
y_pos = 0
movement = 10

keep_going = True
clock = pygame.time.Clock()

while keep_going:
    clock.tick(30)

    for ev in pygame.event.get():

        if ev.type == QUIT:
            keep_going = False

        elif ev.type == KEYDOWN:

            if ev.key == K_UP:
                y_pos -= movement

            elif ev.key == K_DOWN:
                y_pos += movement

            elif ev.key == K_LEFT:
                x_pos -= movement

            elif ev.key == K_RIGHT:
                x_pos += movement

    screen.blit(background, (0, 0))
    screen.blit(ball, (x_pos, y_pos))
    pygame.display.flip()

pygame.quit()
