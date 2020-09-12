import pygame  # load pygame keywords
import sys  # let  python use your file system
import os  # help python identify your OS
import pygame
import sys
import os

'''
Variables
'''

world_x = 800
world_y = 600
fps = 40  # frame rate
ani = 4  # animation cycles
main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

'''
Objects
'''

# put Python classes and functions here


'''
Setup
'''

clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([world_x, world_y])
backdrop = pygame.image.load(os.path.join('assets', 'background-800x600.png'))
pygame.display.set_icon(pygame.image.load(os.path.join('assets', '001-ufo.png')))
pygame.display.set_caption("Invasores del Espacio")
backdropbox = world.get_rect()

'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    world.blit(backdrop, backdropbox)
    pygame.display.flip()
    clock.tick(fps)
