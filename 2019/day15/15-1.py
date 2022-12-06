'''
DAY 15-1: (Intcode) Pathfinding through a maze 

Not an elegant solution, but it works.

Here the goal is to find the oxygen generator in an unknown maze. The way that we can
access the maze and understand it is by moving around an intcode rover, which can move around
but not easily 'reverse' (at least not without understanding intcode better than I do).

Given that mapping the surrounds requires a number of moves, here we map the entire space 
first by moving randomly, prioritizing moves with an unknown outcome. Fortunately the input
provided is short enough that this is a relatively quick process (~15 - 200s, depending on the seed).
A seed is provided that makes short work of this.

Then we can start filling out the grid from the home space, filling in all adjacent cells until
the reactor is found. (This is the same logic applied to 15-2)
''' 

import sys
import os
import tkinter as tk
import copy
import random
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    global current_location
    with open('day15/15-1-input.txt','r') as input_file:
        input_contents = input_file.read()
    
    # read in the input as the starting intcode memory
    starting_memory = [int(x) for x in input_contents.split(',')]
    random.seed(7)  # not required, but performed the best of 10 random seeds

    # create the tkinter variables
    window = tk.Tk()
    lbl_text = tk.StringVar()
    lbl = tk.Label(window, textvariable=lbl_text, font='TkFixedFont')
    lbl.pack()

    # create the repair droid and the grid variables
    repair_droid = Intcode_computer(starting_memory.copy(), input_queue=[])
    grid = create_starting_grid(41, 41)
    printable = printable_grid(copy.deepcopy(grid))    
    current_location = [21, 21]
    vector_dict = {1: [0, -1], 2: [0, 1], 3: [-1, 0], 4: [1, 0]}
    lbl_text.set(printable)
    
    # determine how a movement works, defining locally to make use of vector dictionary and repair droid
    def move(direction):        
        global current_location
        repair_droid.add_to_input_queue(direction)
        repair_droid.run(pause_at_output=True)
        outcome = repair_droid.get_last_output()
        vector = vector_dict[direction]
                
        if grid[current_location[1]][current_location[0]] != 2:
            grid[current_location[1]][current_location[0]] = 1
        
        test_location = [current_location[0] + vector[0], current_location[1] + vector[1]]
        if outcome == 0:
            grid[test_location[1]][test_location[0]] = 0
        elif outcome == 1:
            grid[test_location[1]][test_location[0]] = 1
            current_location = test_location
        elif outcome == 2:
            grid[test_location[1]][test_location[0]] = 2
            current_location = test_location
        
        if grid[current_location[1]][current_location[0]] != 2:
            grid[current_location[1]][current_location[0]] = 3
    
    # map out the grid
    i = 0
    while any(4 in sublist for sublist in grid) == True:
        if grid[current_location[1]][current_location[0] - 1] == 4:
            direction = 3
        elif grid[current_location[1]][current_location[0] + 1] == 4:
            direction = 4
        elif grid[current_location[1] - 1][current_location[0]] == 4:
            direction = 1
        elif grid[current_location[1] + 1][current_location[0]] == 4:
            direction = 2
        else:
            direction = random.randint(1,4)
        move(direction)
        i += 1
        if i % 10000 == 0:
            grid = fill_in_blanks(grid)
            printable = printable_grid(copy.deepcopy(grid))
            lbl_text.set(printable)
            window.update()
    
    
    grid = [[i if i != 3 else 1 for i in x] for x in grid]
    grid[21][21] = 5
    printable = printable_grid(copy.deepcopy(grid))
    lbl_text.set(printable)
    
    lbl_time = tk.StringVar()
    lbl2 = tk.Label(window, textvariable=lbl_time, font='TkFixedFont')
    lbl2.pack()

    window.update()
    time.sleep(2)

    # fill in the grid with oxygen

    oxygen_start_location = find_cell(grid, 5)
    grid[oxygen_start_location[0]][oxygen_start_location[1]] = 6
    minutes = 0
    printable = printable_grid(copy.deepcopy(grid))
    lbl_text.set(printable)
    lbl_time.set('Minutes passed: ' + str(minutes))
    window.update()
    while any(2 in sublist for sublist in grid) == True:
        minutes += 1
        grid = propogate_oxygen(grid)
        printable = printable_grid(copy.deepcopy(grid))
        lbl_text.set(printable)
        lbl_time.set('Minutes passed: ' + str(minutes))
        window.update()
        time.sleep(0.05)
    print('Minimum time to reach oxygen reactor:',minutes)
    window.mainloop()


# find a given cell type in the grid
def find_cell(grid, search):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == search:
                return [y, x]


# fill in any cells of the pattern that could not otherwise be reached:
#   #
#  #A#
#   #

def fill_in_blanks(grid):
    for y in range(1, len(grid) -1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y - 1][x] == 0:
                if grid[y + 1][x] == 0:
                    if grid[y][x-1] == 0:
                        if grid[y][x+1] == 0:
                            grid[y][x] = 0
    return grid


# spread oxygen to connected cells (not including walls)
def propogate_oxygen(grid):
    new_grid = copy.deepcopy(grid) # copy required so that only one step is made each time this function is invoked
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 0 or grid[y][x] == 6:
                continue
            elif grid[y - 1][x] == 6 or grid[y + 1][x] == 6 or grid[y][x-1] == 6 or grid[y][x+1] == 6:
                new_grid[y][x] = 6
    return new_grid


# create a starting grid of arbitrary size, with walls around the edges
def create_starting_grid(x, y):
    grid = []
    for i in range(y):
        row = []
        if i == 0 or i == (y-1):
            for j in range(x):
                row.append(0)
        else:
            for j in range(x):
                if j == 0 or j == (x-1):
                    row.append(0)
                else:
                    row.append(4)
        grid.append(row)

    return grid


# create a visible text version of the grid to print to tkinter
def printable_grid(grid):
    print_chars = {0: '0', 1: ' ', 2: 'X', 3: 'R', 4: '?', 5: 'H', 6: '~'}
    printable_grid = ''
    for row in grid:
        for i, pixel in enumerate(row):
            row[i] = print_chars[pixel]
        printable_grid += (''.join(row))
        printable_grid += '\n'
    return printable_grid


if __name__ == "__main__":
    main()