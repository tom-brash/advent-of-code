'''
DAY 11-1: (Intcode) Counting painted cells 

Here we just need to keep track of the number of cells that have been painted at least once.
We create an intcode object that runs the code, and then just need to keep track of a set of 
cells that have been switched colors at least once.

We start on a black panel, and all panels begin as black.
''' 

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day11/11-1-input.txt','r') as input_file:
        input_contents = input_file.read()

    init_memory = [int(i) for i in input_contents.split(',')]
    painting_robot = Intcode_computer(init_memory, input_queue=[])
    white_cells = []
    painted_cells = set()
    current_location = [0, 0]
    current_direction = 0
    vector_dict = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1 , 0)}
    while True:
        if current_location in white_cells:
            current_color = 1
        else:
            current_color = 0
        painting_robot.add_to_input_queue(current_color)
        instruction, direction = move_painter_robot(painting_robot)
        
        if instruction == 'halt':
            break
        
        if instruction == 0:
            if current_location in white_cells:
                white_cells.remove(current_location)
                painted_cells.add(tuple(current_location))
        elif instruction == 1:
            if current_location not in white_cells:
                white_cells.append(current_location.copy())
                painted_cells.add(tuple(current_location))
        
        if direction == 1:
            current_direction = (current_direction + 1) % 4
        elif direction == 0:
            current_direction = (current_direction - 1) % 4

        
        vector = vector_dict[current_direction]
        current_location[0] += vector[0]
        current_location[1] += vector[1]

    print(len(painted_cells))


def move_painter_robot(painting_robot):
    painting_robot.run(pause_at_output=True)
    instruction = painting_robot.get_last_output()
    if instruction == 'halt':
        print('Program ended')
        return 'halt', ''
    painting_robot.run(pause_at_output=True)
    direction = painting_robot.get_last_output()
    return instruction, direction


if __name__ == '__main__':
    main()