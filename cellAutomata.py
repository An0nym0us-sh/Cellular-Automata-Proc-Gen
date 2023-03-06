import pygame
import random
import sys

import funcs


clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("Cellular Automata")

# Each of the squares will be 2x2
WINDOW_SIZE = (400,200)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # The actual Size of the window

def main():
    running = True

    world_map = funcs.generate_noise_map(60, WINDOW_SIZE)

    while running:
        for j in range(0, len(world_map)):
            for i in range(0, len(world_map[0])):
                if world_map[j][i] == 0:
                    pygame.draw.rect(screen, "black", pygame.Rect(2*i,2*j,2,2))
                else:
                    pygame.draw.rect(screen, "white", pygame.Rect(2*i,2*j,2,2))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    world_map = funcs.next_cell_frame(world_map)
                if event.key == K_DOWN:
                    world_map = funcs.generate_noise_map(60, WINDOW_SIZE)


        pygame.display.update()
        clock.tick(60)

main()
