from collections import defaultdict
from collections import deque
import math
import re
import copy


def main():
    with open('20/20.txt', 'r') as open_file:
        input_data = open_file.read()
    
    mask = '#..###.##....#.#.#...#.#.#...##...####......##.##..###...#.####..#..#..#####..#.##.....#..#.###.##...#.#.....#...##.##.##...#####.#.#.#.##.###.#.##..#.##.##.#..#...####.#.#.....#..#.....###.#..#.#.#.#...#.###..#.###..##.#..#...##...####.#.........###..#.##.#..#.#...##.#.#.##.####.###....#####..###...##..#####..###..##..#.#.#..###.##.###..#.#######.####..#....###.##...#.####..#.#######...###...##.##.###...##..#.....#.###....#..#.#..###.#...#######.#...##..#.#..##.#...##.#..##.##..#...#.#.##.####........#..#.'
    
    #mask = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
    grid = {}
    rows = input_data.split('\n')
    nrows = len(rows)
    ncols = len(rows[0])
    for i, r in enumerate(rows):
        for j, c in enumerate(r):
            if c == '#':
                grid[(i, j)] = '1'
            else:
                grid[(i, j)] = '0'
    
    for y in range(-60, ncols + 60):
        for x in range(-60, nrows + 60):
            if (y, x) not in grid:
                grid[(y, x)] = '0'

    
    leftmost = -60
    rightmost = ncols + 60
    topmost = -60
    bottommost = nrows + 60
    z = '0'
    for i in range(50):
        print(i)
        new_grid = copy.deepcopy(grid)
        for r in range(topmost, bottommost):
            for c in range(leftmost, rightmost):
                m = ''
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        m += grid.get((r + i, c + j), z)
                m = int(m, base=2)
                new_char = mask[m]
                if new_char == '#':
                    new_char = '1'
                else:
                    new_char = '0'
                new_grid[(r, c)] = new_char
        grid = copy.copy(new_grid)
        leftmost -=1
        rightmost += 1
        topmost -= 1
        bottommost += 1
        if z == '0':
            z = '1'
        else:
            z = '0'
    
    total = 0
    for x in grid.values():
        if x == '1':
            total += 1
    print(total)

def print_grid(grid):
    y_min = 0
    y_max = 0
    x_min = 0
    x_max = 0
    for p in grid.keys():
        if p[0] < y_min:
            y_min = p[0]
        if p[0] > y_max:
            y_max = p[0]
        if p[1] < x_min:
            x_min = p[0]
        if p[1] > x_max:
            x_max = p[0]
        
    for y in range(y_min, y_max + 1):
        row = ''
        for x in range(x_min, x_max + 1):
            row += grid[(y, x)]
        print(row)



    
    
class Thing:
    def __init__(self):
        pass

if __name__ == '__main__':
    main()