'''
DAY 17-1: (Intcode) Reading in scaffolding pattern from camera input 

The first part simply takes in the input as intcode memory and runs it to get back
an ASCII representation of the outside of the ship. By transforming this into a grid
we can easily get the coordinates of the intersections (and print it off nicely)
''' 

import sys
import os
import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day17/17-1-input.txt','r') as input_file:
        input_contents = input_file.read()
    
    initial_memory = [int(x) for x in input_contents.split(',')]

    camera = Intcode_computer(initial_memory)
    camera.run()
    string_grid = print_camera_output(camera.output_queue)
    grid = [[c for c in x] for x in string_grid.split('\n')]
    grid = [x for x in grid if x != []]
    total = total_intersections(grid)
    print('Sum of alignment parameters:', total)

def print_camera_output(output):
    print_string = ''
    for i in output:
        if i != 'halt':
            print_string += chr(i)
    print(print_string)
    return print_string


def total_intersections(grid):
    total = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == '#' and grid[y - 1][x] == '#' and grid[y + 1][x] == '#' and grid[y][x - 1] == '#' and grid[y][x + 1] == '#':
                total += y * x
    return total

if __name__ == "__main__":
    main()