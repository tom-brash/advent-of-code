'''
DAY 24-1: Identifying black tiles

Another variant on Conway's Game of Life, this time using hexagons. The main
thing here is just working out an acceptable coordinate system for hexagons,
such that we can refer to a particular grid hexagon easily and uniquely.

Here I've used offset coordinates, shifting odd numbered rows to the right, using
the convention described here: https://www.redblobgames.com/grids/hexagons/

After that we just parse the instructions. It is always unique as there are no
'N' and 'S' directions, only 'NW', 'NE', 'SW' and 'SE'. Then we just fill out the 
grid, adding tiles to the list of black tiles if they aren't already in it, and removing
them from the list if they are already there
'''

import numpy as np

def main():
    with open('day24/24-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    instructions = [parse_instruction(x) for x in input_data.split('\n')]

    black_tiles = []

    for instruction in instructions:
        referenced_tile = go_to_instruction(instruction)
        if referenced_tile in black_tiles:
            black_tiles.remove(referenced_tile)
        else:
            black_tiles.append(referenced_tile)
    
    print(len(black_tiles))


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


def go_to_instruction(instruction):
    current_tile = np.array([0, 0])
    # storing possible moves as [even row, odd row]
    d_dict = {'ne': [np.array([0, -1]), np.array([1, -1])],
                'nw': [np.array([-1, -1]), np.array([0, -1])],
                'se': [np.array([0, 1]), np.array([1, 1])],
                'sw': [np.array([-1, 1]), np.array([0, 1])],
                'e': [np.array([1, 0]), np.array([1, 0])],                
                'w': [np.array([-1, 0]), np.array([-1, 0])]}

    for direction in instruction:
        if current_tile[1] % 2 == 0:
            current_tile = current_tile + d_dict[direction][0]
        else:
            current_tile = current_tile + d_dict[direction][1]
    return(list(current_tile))


if __name__ == "__main__":
    main()
