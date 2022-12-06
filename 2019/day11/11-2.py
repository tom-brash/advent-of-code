'''
DAY 11-2: (Intcode) Getting the painted cell pattern 

Now we need to actually draw the pattern. In the first part of the code, we already track
which cells are turned white. Turning the starting cell white and leaving the code alone
gives us the right cells to track.

From here we just need to create a new function to create the grid. Somewhat disingenously,
the grid here is labelled in conventional fashion, rather than counting down from the top
left corner. This means the grid function needs to start at max_y, min_x and create the grid
one row at a time. As there are only two colors, the function just checks if each cell is 
white, and otherwise prints a blank space for easier reading
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
    white_cells = [[0, 0]]
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
        
        t_current_location = tuple(current_location)
        if instruction == 0:
            if t_current_location in white_cells:
                white_cells.remove(t_current_location)
        elif instruction == 1:
            if t_current_location not in white_cells:
                white_cells.append(t_current_location)
        
        if direction == 1:
            current_direction = (current_direction + 1) % 4
        elif direction == 0:
            current_direction = (current_direction - 1) % 4

        
        vector = vector_dict[current_direction]
        current_location[0] += vector[0]
        current_location[1] += vector[1]

    print_grid(white_cells)


def print_grid(white_cells):
    min_x = min_y = 1000
    max_x = max_y = -1000
    for cell in white_cells:
        if cell[0] > max_x:
            max_x = cell[0]
        if cell[0] < min_x:
            min_x = cell[0]
        if cell[1] > max_y:
            max_y = cell[1]
        if cell[1] < min_y:
            min_y = cell[1]
    
    for y in list(range(min_y, max_y + 1))[::-1]:   
        row = ''
        for x in list(range(min_x, max_x + 1)):            
            if tuple([x, y]) in white_cells:
                row += '#'
            else:
                row += ' '
        print(row)




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