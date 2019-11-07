#Kush Kansara
#heyYou

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("heyYou")

background = pygame.Surface(screen.get_size()).convert()
background.fill((0, 0, 0))

text_entry = pygame.Surface((500, 50)).convert()
text_entry.fill((255, 255, 255))

font = pygame.font.SysFont("arial", 25)
entry_value = ""
entry_text = font.render(entry_value, True, (0, 0, 0))

font2 = pygame.font.SysFont("times new roman", 50)
out_value = ""
out = font2.render(out_value, True, (255, 255, 255))

clock = pygame.time.Clock()

keep_going = True

while keep_going:
    clock.tick(30)

    for ev in pygame.event.get():

        if ev.type == QUIT:
            keep_going = False

        elif ev.type == KEYDOWN:
            
            if ev.key == K_BACKSPACE and len(entry_value) > 0:
                entry_value = entry_value[:-1]

            elif (ev.unicode.isalnum() or ev.key == K_SPACE) and len(entry_value) < 20:
                entry_value += ev.unicode

            elif ev.key == K_RETURN:
                out_value = entry_value

            entry_text = font.render(entry_value, True, (0, 0, 0))
            out = font2.render(out_value, True, (255, 255, 255))

    screen.blit(background, (0, 0))           
    screen.blit(text_entry, (0, 0))
    screen.blit(entry_text, (150, 0))
    screen.blit(out, (50, 200))
    
    pygame.display.flip()

pygame.quit()
