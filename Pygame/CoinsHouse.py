#Kush Kansara
#CoinsHouse

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("CoinsHouse")

coin1 = pygame.image.load("coin.png").convert()
coin2 = pygame.image.load("coin.png").convert()
coin3 = pygame.image.load("coin.png").convert()
coin4 = pygame.image.load("coin.png").convert()
coin5 = pygame.image.load("coin.png").convert()

screen.blit(coin1, (150, 200))
screen.blit(coin2, (350, 200))
screen.blit(coin3, (150, 400))
screen.blit(coin4, (350, 400))
screen.blit(coin5, (250, 50))


pygame.display.flip()

keep_going = True
clock = pygame.time.Clock()



while keep_going:
    clock.tick(30)

    for ev in pygame.event.get():

        if ev.type == QUIT:
            keep_going = False

pygame.quit()
