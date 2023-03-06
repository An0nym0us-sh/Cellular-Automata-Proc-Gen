import pygame
import logging as log
import random

log.basicConfig(level=log.DEBUG)

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("Cellular Automata")

# Each of the squares will be 2x2
WINDOW_SIZE = (1200,800)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # The actual Size of the window

def main():
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

