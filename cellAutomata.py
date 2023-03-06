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

def generate_noise_map(noise_density : int) -> list:

    noise_map = []

    # Generate Rows
    for j in range(0,WINDOW_SIZE[1]//2):

        noise_map.append([])
        
        # Generate Columns
        for i in range(0,WINDOW_SIZE[0]//2):
            if random.randrange(0,100) < noise_density:
                noise_map[-1].append(1)
            else:
                noise_map[-1].append(0)

    # Log out the stuff
    log.info("Noise Map")
    log.info(f"Height : {len(noise_map)}")
    log.info(f"Width : {len(noise_map[0])}")

    return noise_map

def next_cell_frame(map_state : list) -> list:

    next_frame = map_state

    # We will change to black if there are 4 squares that are black
    # Else we will change to white.
    # Black therefore will get slight preference 

    # We don't need to check the corners cause they only have 3 squares touching them 
    # and can therefore never change.

    # Then we check the sides

    # Right side
    for i in range(1,len(map_state) - 1):
        # map_state[i][0]
        black_counter = 0
        for di in [(1,0), (1,1), (0,1), (-1,1), (-1,0)]:
            if map_state[i + di[0] ][ 0 + di[1]  ] == 0:
                black_counter += 1

        if black_counter >= 4:
            next_frame[i][0] = 0
        else:
            next_frame[i][0] = 1

    # Left side
    for j in range(1, len(map_state) - 1):
        # map_state[i][-1]
        black_counter = 0
        for di in [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]:
            if map_state[i + di[0] ][ -1 + di[1]  ] == 0:
                black_counter += 1

        if black_counter >= 4:
            next_frame[i][-1] = 0
        else:
            next_frame[i][-1] = 1


    # Then we check the top and bottom

    # Then we check everything else



def main():
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

generate_noise_map(50)
