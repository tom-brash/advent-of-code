'''
DAY 24-2: Conway's recursive bugs

This version extends recursively - the 5x5 grid given is the 0th layer, but the
middle cell is replaced by another 5x5 grid. Similarly, the starting grid is the
middle cell of another, larger grid, extending infinitely up or down.

Here the simple vector search doesn't quite do it, but a slightly modified approach
is fine. Each cell will always be next to the same combination of cells, relative to
their current position. We can calculate this first as a dictionary (including a z
vector of +/- 1) and then extend the grids as we need to. Each move will never require
adding more than 1 grid up and 1 grid down.
''' 

import copy
from collections import defaultdict
import pprint

def main():
    with open('day24/24-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    bugs = RecursiveGrid()
    bugs.add_grid(0, [[c for c in x] for x in input_data.split('\n')])
    for _ in range(200):
        bugs.run_round()
    print('Total bugs in recursive grid after 200 rounds:', bugs.get_total_bugs())

# series of 5x5 grids
class RecursiveGrid:
    def __init__(self):
        self.grids = {}
        self.c = 5
        self.r = 5
        self.max_level = 0
        self.min_level = 0
        self.vector_map = self.create_vector_map()  # create map of which cells connect to which


    # add new grid to the system at specified level
    def add_grid(self, level, rows=None):
        if rows == None:
            rows = [['.' for x in range(self.c)] for y in range(self.r)]
        rows[2][2] = '?'  # middle cell should not be a bug or blank
        self.grids[level] = rows
    

    # print all the grids
    def print_grids(self):
        for z in range(self.min_level, self.max_level + 1):
            self.print_level(z)


    # print a single grid at specified level
    def print_level(self, level):
        print('Level %d:' %level)
        for row in self.grids[level]:
            print(row)
        print()
    

    # run a single round
    def run_round(self):
        self.expand_grid()  # expand grid in both directions        
        copy_grids = copy.deepcopy(self.grids)
        for z in range(self.min_level, self.max_level + 1):  # for each level
            for x in range(self.c):  # for each column
                for y in range(self.r):  # for each row
                    neighbor_bugs = self.get_neighbors(x, y, z)
                    if self.grids[z][y][x] == '#':
                        if neighbor_bugs == 1:
                            copy_grids[z][y][x] = '#'
                        else:
                            copy_grids[z][y][x] = '.'
                    else:
                        if neighbor_bugs == 1 or neighbor_bugs == 2:
                            copy_grids[z][y][x] = '#'
                        else:
                            copy_grids[z][y][x] = '.'
                    if y == 2 and x == 2:  # make sure the center value stays as '?'
                        copy_grids[z][y][x] = '?'
        self.grids = copy.deepcopy(copy_grids)
        self.condense_grid()  # condense the grid back down if an outer layer is not necessary
    

    # determine current neighbors, using predetermined vector dictionary
    def get_neighbors(self, x, y, z):
        total = 0
        for neighbor in self.vector_map[(x, y)]:
            z_move, check_x, check_y = neighbor
            # as new outer levels have been created, will never need to go outside these bounds and risk an index error
            target_level = z + z_move 
            if target_level >= self.min_level and target_level <= self.max_level:
                if self.grids[target_level][check_y][check_x] == '#':
                    total += 1
        return total


    # add a grid above and below the current bounds
    def expand_grid(self):
        self.add_grid(self.max_level + 1)
        self.add_grid(self.min_level - 1)
        self.max_level += 1
        self.min_level -= 1
    

    # remove outer grids if not being used
    def condense_grid(self):
        if self.count_bugs(self.min_level) == 0:
            del self.grids[self.min_level]
            self.min_level += 1
        if self.count_bugs(self.max_level) == 0:
            del self.grids[self.max_level]
            self.max_level -= 1


    # count the bugs in a single layer
    def count_bugs(self, level):
        grid = self.grids[level]
        total = 0
        for row in grid:
            for col in row:
                if col == '#':
                    total += 1
        return total


    # count bugs in all layers
    def get_total_bugs(self):
        total = 0
        for z in range(self.min_level, self.max_level + 1):
            total += self.count_bugs(z)
        return total


    # create map of which cells are connected to each cell as a 3D vector (relative z position, x, y)
    def create_vector_map(self):
        vector_map = {}
        for x in range(self.c):
            for y in range(self.r): 
                neighbors = set()
                for vector in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    check_x = x + vector[0]
                    check_y = y + vector[1]
                    # add connected cells within same grid
                    if check_x >= 0 and check_y >= 0 and check_x < self.c and check_y < self.r and (check_x, check_y) != (2, 2):
                        neighbors.add((0, check_x, check_y))
                    # add connected cells 
                    elif check_x < 0:
                        neighbors.add((1, 1, 2))
                    elif check_x >= self.c:
                        neighbors.add((1, 3, 2))
                    elif check_y < 0:
                        neighbors.add((1, 2, 1))
                    elif check_y >= self.r:
                        neighbors.add((1, 2, 3))
                    # add connected cells in lower level grid
                    elif (check_x, check_y) == (2, 2):
                        if x == 1:
                            for i in range(5):
                                neighbors.add((-1, 0, i))
                        elif x == 3:
                            for i in range(5):
                                neighbors.add((-1, 4, i))
                        elif y == 1:
                            for i in range(5):
                                neighbors.add((-1, i, 0))
                        elif y == 3:
                            for i in range(5):
                                neighbors.add((-1, i, 4))
                vector_map[(x, y)] = list(neighbors)
        return vector_map


if __name__ == "__main__":
    main()