import numpy as np
import funcs

test_map = [
        [0 , 0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0 , 0],
        ]

print(np.matrix ( funcs.next_cell_frame(test_map) ) )

