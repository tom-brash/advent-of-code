import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip()

    directions = [c for c in input]
    target_iterations = 1000000000000

    tetris = Tetris(directions)
    wind_length = len(directions)
    c_set = {}
    counter = 0
    cycle_start = None
    cycle_length = None
    cycle_size = None
    i = 0

    print(f'Searching for a cycle...')

    while counter < 30 and i < 90000000:
        c_set[(tetris.i % 5, tetris.wind_index)] = (tetris.i, tetris.height)
        if (tetris.i % 5, tetris.wind_index - wind_length) not in c_set:
            counter = 0
        else:
            if counter == 0:
                cycle_start = i
            counter += 1
            cycle_length = i - c_set[(tetris.i % 5, tetris.wind_index - wind_length)][0]
            cycle_size = tetris.height - c_set[(tetris.i % 5, tetris.wind_index - wind_length)][1]
        tetris.drop_shape()
        i += 1

    if counter != 30:
        print("No cycle found: terminating")
        return

    print(f"Cycle found! Cycle starts after {cycle_start} blocks have fallen, and repeats after {cycle_length} blocks. Each cycle adds {cycle_size} to tower height")

    num_cycles = (target_iterations - cycle_start) // cycle_length
    remaining = (target_iterations - cycle_start) % cycle_length

    print(f"Target iteration count contains {num_cycles} complete cycles. Simulating remaining tower...\n")

    tetris = Tetris(directions)
    for _ in range(cycle_start + remaining):
        tetris.drop_shape()

    print(f"Final answer: {tetris.height + num_cycles * cycle_size}") 


class Shape:
    def __init__(self, type, x, y):
        self.get_l_border(type)
        self.get_r_border(type)
        self.get_d_border(type)
        self.get_blocks(type)
        self.x = x
        self.y = y

        if type == "X":
            self.x += 1

    def get_l_border(self, type):
        if type == "F":
            self.l_border = [(0,0)]
        elif type == "X":
            self.l_border = [(0,0), (-1, 1), (0, 2)]
        elif type == "L":
            self.l_border = [(0,0), (2, 1), (2, 1)]
        elif type == "I":
            self.l_border = [(0,0), (0, 1), (0, 2), (0, 3)]
        elif type == "S":
            self.l_border = [(0,0), (0, 1)]

    def get_r_border(self, type):
        if type == "F":
            self.r_border = [(3,0)]
        elif type == "X":
            self.r_border = [(0,0), (1, 1), (0, 2)]
        elif type == "L":
            self.r_border = [(2,0), (2, 1), (2, 1)]
        elif type == "I":
            self.r_border = [(0,0), (0, 1), (0, 2), (0, 3)]
        elif type == "S":
            self.r_border = [(1,0), (1, 1)]

    def get_d_border(self, type):
        if type == "F":
            self.d_border = [(0,0), (1,0), (2,0), (3,0)]
        elif type == "X":
            self.d_border = [(0,0), (1, 1), (-1, 1)]
        elif type == "L":
            self.d_border = [(0,0), (1,0), (2, 0)]
        elif type == "I":
            self.d_border = [(0,0)]
        elif type == "S":
            self.d_border = [(0,0), (1, 0)]

    def get_blocks(self, type):
        if type == "F":
            self.blocks = [(0,0), (1,0), (2,0), (3,0)]
        elif type == "X":
            self.blocks = [(0,0), (1, 1), (-1, 1), (0, 1), (0, 2)]
        elif type == "L":
            self.blocks = [(0,0), (1,0), (2, 0), (2, 1), (2, 2)]
        elif type == "I":
            self.blocks = [(0,0), (0, 1), (0, 2), (0, 3)]
        elif type == "S":
            self.blocks = [(0,0), (1, 0), (0, 1), (1,1)]
class Tetris:
    def __init__(self, instructions):
        self.i = 0
        self.instructions = instructions
        self.grid = {}
        self.order = {0: "F", 1: "X", 2: "L", 3: "I", 4: "S"}
        for x in range(7):
            self.grid[(x, 0)] = '#'
        self.height = 0
        self.wind_index = 0
        self.d_length = len(instructions)

    def print_grid(self, shape=None):
        print_grid = self.grid.copy()

        if shape:
            for b in shape.blocks:
                x_pos = shape.x + b[0]
                y_pos = shape.y + b[1]
                print_grid[(x_pos, y_pos)] = '@'

        for r in range(self.height+29, -1, -1):
            print_row = "|"
            for c in range(7):
                print_row += print_grid.get((c, r), '.')
            print_row += "|"
            print(print_row)
        print('---------')


    def drop_shape(self):
        shape = Shape(self.order[self.i % 5], 2, self.height + 4)
        self.i += 1

        falling = True

        while falling:
            f = self.check_free(shape, self.instructions[self.wind_index % self.d_length])
            shape.x = shape.x + f
            self.wind_index += 1

            #self.print_grid(shape)

            f = self.check_free(shape, 'v')
            if f == 0:
                falling = False
                height_changed = False
                for b in shape.blocks:
                    x_pos = shape.x + b[0]
                    y_pos = shape.y + b[1]
                    if y_pos >= self.height:
                        height_changed = True
                        self.height = y_pos
                    self.grid[(x_pos, y_pos)] = '#'
                if height_changed:
                    level = True
                    for i in range(7):
                        if (i, self.height) not in self.grid:
                            level = False
                    if level:
                        print('Level!!!', self.i, self.wind_index % self.d_length)

            else:
                shape.y = shape.y + f
            

            #self.print_grid(shape)

    def check_free(self,shape, d):
        if d == "<":
            for b in shape.l_border:
                x_pos = shape.x - 1 + b[0]
                y_pos = shape.y + b[1]
                if (x_pos, y_pos) in self.grid or x_pos < 0:
                    return 0
            return - 1
        elif d == ">":
            for b in shape.r_border:
                x_pos = shape.x + 1 + b[0]
                y_pos = shape.y + b[1]
                if (x_pos, y_pos) in self.grid or x_pos > 6:
                    return 0
            return 1
        elif   d == "v":
            for b in shape.d_border:
                x_pos = shape.x + b[0]
                y_pos = shape.y - 1 + b[1]
                if (x_pos, y_pos) in self.grid:
                    return 0
            return -1
            

if __name__ == "__main__":
    main()
