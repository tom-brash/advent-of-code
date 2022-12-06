'''
DAY 24-2: Conway's Game of Life with hexagons

This extends the hexagonal  grid into nother variant on Conway's Game of Life, 
this time using hexagons. The pattern used in 24-1 is used as the starting state.
Again, offsetting odd numbered rows is used as the coordinate convention:
https://www.redblobgames.com/grids/hexagons/

This is the third version of the functioning code. As the active tiles expand,
more and more tiles need to be checked against their neighbors. The first version
jsut checked every cell within the outer boundaries of where the active cells are,
but it took ~20min to run. In particular, even though the number of active cells did 
not explode upwards, they got further apart, and the search space grows with the square
of the dimensions.

This version does not consider all of the tiles within the boundaries, but instead
iterates over the active cells only, putting the neighbors of these cells in a dictionary
and using that to upate at each step. The code still takes ~20s to run, but is ~60x faster
than the previous iterations.

To further save time, since the find_neighbors function is reasonably expensive, the neighbors
are stored in a dictionary for rapid retrieval to prevent looking for the same neighbors
twice
'''

import numpy as np
import copy
from collections import defaultdict

def main():
    with open('day24/24-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    instructions = [parse_instruction(x) for x in input_data.split('\n')]

    active_tiles = []

    d_dict = {'ne': [np.array([0, -1]), np.array([1, -1])],
                'nw': [np.array([-1, -1]), np.array([0, -1])],
                'se': [np.array([0, 1]), np.array([1, 1])],
                'sw': [np.array([-1, 1]), np.array([0, 1])],
                'e': [np.array([1, 0]), np.array([1, 0])],                
                'w': [np.array([-1, 0]), np.array([-1, 0])] ,
                }

    for instruction in instructions:
        referenced_tile = go_to_instruction(instruction, d_dict)
        if referenced_tile in active_tiles:
            active_tiles.remove(referenced_tile)
        else:
            active_tiles.append(referenced_tile)
    
    print('initial active tiles: ', str(len(active_tiles)))

    neighbor_dict = {}

    for i in range(100):
        active_dict = defaultdict(int)
        new_active = []
        for tile in active_tiles:
            if tile not in neighbor_dict:
                neighbor_dict[tile] = get_neighbors(tile, d_dict)
            for neighbor in neighbor_dict[tile]:
                active_dict[neighbor] += 1
        
        for tile, active in active_dict.items():
            if tile in active_tiles:
                if active == 1 or active == 2:
                    new_active.append(tile)
            else:
                if active == 2:
                    new_active.append(tile)
        
        active_tiles = copy.deepcopy(new_active)
        print('active tiles after ', i + 1, 'day(s): ', str(len(active_tiles)))
    print('hi')

# get directions as list from input without delimiters
def parse_instruction(instruction):
    directions = []
    while instruction != '':
        if instruction[0] == 'n' or instruction[0] == 's':
            directions.append(instruction[:2])
            instruction = instruction[2:]
        else:
            directions.append(instruction[0])
            instruction = instruction[1:]
    return directions


def go_to_instruction(instruction, d_dict):
    current_tile = np.array([0, 0])
    for direction in instruction:
        if current_tile[1] % 2 == 0:
            current_tile = current_tile + d_dict[direction][0]
        else:
            current_tile = current_tile + d_dict[direction][1]
    return(tuple(current_tile))


def get_neighbors(tile, d_dict):
    neighbors = []
    tile = np.array(tile)
    if tile[1] % 2 == 0:  # if in an even row
        for key in d_dict.keys():
            neighbors.append(tuple(tile + d_dict[key][0]))
    else:
        for key in d_dict.keys():
            neighbors.append(tuple(tile + d_dict[key][1]))
    return neighbors


def find_boundaries(active_tiles):
    cols = [x[1] for x in active_tiles]
    rows = [x[0] for x in active_tiles]
    print(min(rows) - 1, max(rows) + 1, min(cols) - 1, max(cols) + 1)
    return(min(rows) - 1, max(rows) + 1, min(cols) - 1, max(cols) + 1)


if __name__ == "__main__":
    main()
