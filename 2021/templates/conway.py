import copy

class ConwayGrid:
    def __init__(self, config):
        self.grid = {}
        self.h = len(config)
        self.w = len(config[0])
        for y, row in enumerate(config):
            for x, c in enumerate(y):
                self.grid[(x, y)] = c
    
    def update(self):
        new_grid = copy.deepcopy(self.grid)
        for y in range(self.h):
            for x in range(self.w):
                current = self.grid[(x, y)]
                on = self.get_on(x, y)
                # if current == 'opt_1':    # UPDATE BLOCK
                #     if cond1 or cond2:
                #         new_grid[(x, y)] = opt_1
                # elif current == 'opt2':
                #     if cond1 or cond2:
                #         new_grid[(x, y)] = opt_1
        self.grid = new_grid

    def get_on(self, x, y):
        t = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if self.grid.get((x + i, y + j), '.') == '#':  # UPDATE 
                    t += 1
        return t

    def count_on(self):
        t = 0
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[(x, y)] == '#':
                    t += 1
        return t
    
    def print_out(self):
        for y in range(self.h):
            row = ''
            for x in range(self.w):
                row += self.grid[(x, y)]
            print(row)
    