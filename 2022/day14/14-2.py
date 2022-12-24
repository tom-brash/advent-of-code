import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')
    
    grid = defaultdict(lambda: ' ')

    for x in input:
        points = x.split(' -> ')
        grid = draw_lines(grid, points)

    lowest_point = 0

    for l in grid:
        if l[1] > lowest_point:
            lowest_point = l[1]

    for x in range (-10000, 10000):
        grid[(x, lowest_point + 2)] = '#'
    
    total = 0
    while True:
        grid, status = drop_sand(grid, lowest_point)
        if status == "Resting":
            total += 1
        if grid[(500, 0)] == '.':
            break

    print(total)


def drop_sand(grid, lowest_point):
    loc = (500, 0)
    moved = True
    while moved:
        new_loc = attempt_move(loc, grid)
        if new_loc == loc:
            moved = False

        loc = new_loc
    
    grid[loc] = "."
    return grid, "Resting"

def attempt_move(loc, grid):
    x, y = loc
    y += 1
    if grid[(x, y)] == ' ':
        return (x, y)
    elif grid[(x - 1, y)] == ' ':
        return (x-1, y)
    elif grid[(x + 1, y)] == ' ':
        return (x + 1, y)
    else:
        return (x, y - 1)

def draw_lines(grid, points):
    for i in range(1, len(points)):
        start_point = p_map(points[i-1])
        end_point = p_map(points[i])
        if start_point[0] == end_point[0]:
            x = start_point[0]
            y_min = min(start_point[1], end_point[1])
            y_max = max(start_point[1], end_point[1])
            for y in range(y_min, y_max + 1):
                grid[(x, y)] = '#'
        else:
            y = start_point[1]
            x_min = min(start_point[0], end_point[0])
            x_max = max(start_point[0], end_point[0])
            for x in range(x_min, x_max + 1):
                grid[(x, y)] = '#'

    return grid

def p_map(s):
    points = [int(i) for i in s.split(',')]
    x = points[0]
    y = points[1]
    return (x, y)

if __name__ == "__main__":
    main()
