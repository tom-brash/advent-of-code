'''
DAY 24-1: Conway's bugs

Here we have a modified version of Conway's Game of Life. A bit of extra
code is included in the below for neatness (and in anticipation of extensions) but
the premise is straightforward. Active cells with exactly one active neighbor stay
active, while inactive cells become active with 1-2 active neighbors.

We run until we see a repeated state (simple is simplistic enough we can just keep track
of a list of visited states) and then print out the 'biodiversity' value, calculated
as escalating powers of 2 multipled by whether there is a bug in the cell (reading left
to right, top to bottom)
''' 
import copy

def main():
    with open('day24/24-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    bugs = Grid([[c for c in x] for x in input_data.split('\n')])
    bugs.run()
    bugs.print_grid()
    print('Biodiversity score of repeated grid: ', bugs.calculate_biodiversity())

class Grid:
    def __init__(self, rows):
        self.rows = rows
        self.previous_states = [copy.deepcopy(self.rows)]
        self.r = len(self.rows)
        self.c = len(self.rows[0])


    def print_grid(self):
        for row in self.rows:
            print(row)


    def run(self):
        iterations = 0
        while True:
            self.run_round()
            if self.rows in self.previous_states:
                print('Repeat state found!! It took %d iterations' %iterations)
                return 1
            self.previous_states.append(copy.deepcopy(self.rows))
            iterations += 1


    def run_round(self):
        rows_copy = [['.' for x in range(self.c)] for y in range(self.r)]
        for x in range(self.c):
            for y in range(self.r):
                bug_neighbors = self.get_neighbors(x, y)
                if self.rows[y][x] == '#':
                    if bug_neighbors == 1:
                        rows_copy[y][x] = '#'
                else:
                    if bug_neighbors == 1 or bug_neighbors == 2:
                        rows_copy[y][x] = '#'
        
        self.rows = copy.deepcopy(rows_copy)


    def get_neighbors(self, x, y):
        n = 0
        for vector in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            check_x = x + vector[0]
            check_y = y + vector[1]
            if check_x >= 0 and check_y >= 0 and check_x < self.c and check_y < self.r:
                if self.rows[check_y][check_x] == '#':
                    n += 1
        return n

    def calculate_biodiversity(self):
        multiple = 1
        biodiversity = 0
        for y in range(self.r):
            for x in range(self.c):
                if self.rows[y][x] == '#':
                    val = 1
                else:
                    val = 0
                biodiversity += multiple * val
                multiple *= 2
        return biodiversity

if __name__ == "__main__":
    main()