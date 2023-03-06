import numpy as np

test_map = [
        [0 , 0 , 0 , 0 , 0],
        [1 , 1 , 0 , 0 , 0],
        [0 , 1 , 0 , 0 , 0],
        [1 , 1 , 0 , 0 , 0],
        [0 , 0 , 0 , 0 , 0],
        ]

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
        # map_state[-1][i]
        black_counter = 0
        for di in [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]:
            if map_state[i + di[0] ][ -1 + di[1]  ] == 0:
                black_counter += 1


    # Then we check the top and bottom

    # Then we check everything else
    return next_frame

print(np.matrix ( next_cell_frame(test_map) ) )

