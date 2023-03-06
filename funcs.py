
# Helper functions for the program

def generate_noise_map(noise_density : int, window_size : tuple) -> list:

    noise_map = []

    # Generate Rows
    for j in range(0,window_size[1]//2):

        noise_map.append([])
        
        # Generate Columns
        for i in range(0,window_size[0]//2):
            if random.randrange(0,100) < noise_density:
                noise_map[-1].append(1)
            else:
                noise_map[-1].append(0)

    return noise_map

def next_cell_frame(map_state : list) -> list:

    next_frame = map_state

    # We will change to black if there are 4 squares that are black
    # Else we will change to white.
    # Black therefore will get slight preference 

    # We don't need to check the corners cause they only have 3 squares touching them 
    # and can therefore never change.

    # Then we check the sides

    # For the corners since we only check 5 squares
    # We will change to black if there are 3 squares that are black

    # Left side
    for i in range(1,len(map_state) - 1):
        # map_state[i][0]
        black_counter = 0
        for di in [(1,0), (1,1), (0,1), (-1,1), (-1,0)]:
            if map_state[i + di[0] ][ 0 + di[1]  ] == 0:
                black_counter += 1

        if black_counter >= 3:
            next_frame[i][0] = 0
        else:
            next_frame[i][0] = 1

    # Right side
    for i in range(1, len(map_state) - 1):
        # map_state[i][-1]
        black_counter = 0
        for di in [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]:
            if map_state[ i + di[0] ][ -1 + di[1] ] == 0:
                black_counter += 1

        if black_counter >= 3:
            next_frame[i][-1] = 0
        else:
            next_frame[i][-1] = 1


    # Then we check the top and bottom

    # Top 
    for j in range(1, len(map_state[0]) - 1):
        # map_state[0][j]
        black_counter = 0
        for di in [(0,-1), (1, -1), (1,0), (1,1), (0,1)]:
            if map_state[ 0 + di[0] ][ j + di[1] ] == 0:
                black_counter += 1

        if black_counter >= 3:
            next_frame[0][j] = 0
        else:
            next_frame[0][j] = 1

    # Bottom
    for j in range(1, len(map_state[-1]) - 1):
        # map_state[-1][j]
        black_counter = 0
        for di in [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1)]:
            if map_state[ -1 + di[0] ][ j + di[1] ] == 0:
                black_counter += 1

        if black_counter >= 3:
            next_frame[-1][j] = 0
        else:
            next_frame[-1][j] = 1

    # Then we check everything else
    return next_frame

