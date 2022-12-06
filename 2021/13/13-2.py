from collections import defaultdict
from collections import deque
import copy

def main():
    with open('13/13.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')

    grid = set()

    for i in input_data[0].split('\n'):
        x, y = [int(x) for x in i.split(',')]
        
        grid.add((x, y))

    for f in input_data[1].split('\n'):        
        d = f.split('=')[0][-1]
        n = int(f.split('=')[1])
        grid = fold_along(grid, d, n)
        
    for r in range(max(grid, key=lambda x: x[1])[1] + 1):
        out = ''
        for c in range(max(grid, key=lambda x: x[0])[0] + 1):
            if (c, r) in grid:
                out += '@'
            else:
                out += ' '
        print(out)


def fold_along(grid, d, n):
    if d == 'x':
        part_grid = {p for p in grid if p[0] > n}
        for p in part_grid:
            x, y = p
            x = n - (x -n)
            grid.add((x, y))
        grid = {p for p in grid if p[0] < n}
    
    if d == 'y':
        part_grid = {p for p in grid if p[1] > n}
        for p in part_grid:
            x, y = p
            y = n - (y - n)
            grid.add((x, y))
        grid = {p for p in grid if p[1] < n}
    return grid

class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()