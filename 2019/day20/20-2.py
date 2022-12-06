'''
DAY 20-2: Navigating recursive mazes with portals

Now when you go through an inner portal, the explorer goes to the next level down. 
Going through an outer portal takes the explorer back up a level. 

The BFS logic works almost identically, except the state now includes what level
the explorer is at. To enable this, the connected tile list is modified slightly.
Instead of adding 2 value tuples (x, y), we use 3 value tuples (x, y, z) where z
represents the change in level. If not using a portal, this will be zero.
'''

import pprint
from collections import defaultdict
from collections import deque

def main():
    with open('day20/20-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    maze_rows = input_data.split('\n')
    w = len(maze_rows[0])
    h = len(maze_rows)
    grid = {}
    traversable = {}
    portals = defaultdict(list)
    # read in grid
    for y in range(h):
        for x in range(w):
            char = maze_rows[y][x]
            grid[(x, y)] = char
            if char == '.':
                traversable[(x, y)] = [] # empty list for connected tiles
            if char >= 'A' and char <= 'Z':
                if y > 0 and x > 0 and y < (h - 1) and x < (w - 1):
                    if maze_rows[y + 1][x] == '.':
                        portals[''.join([maze_rows[y - 1][x], char])].append((x, y + 1))
                    elif maze_rows[y - 1][x] == '.':
                        portals[''.join([char, maze_rows[y + 1][x]])].append((x, y - 1))
                    elif maze_rows[y][x + 1] == '.':
                        portals[''.join([maze_rows[y][x - 1], char])].append((x + 1, y))
                    elif maze_rows[y][x - 1] == '.':
                        portals[''.join([char, maze_rows[y][x + 1]])].append((x - 1, y))

    # add 3 value tuples (x, y, change in level) to connected tile list
    for loc in traversable:
        traversable[(loc)].extend([move(loc, d) + (0,) for d in range(4) if move(loc, d) in traversable])
    
    # add 3 value tuples (x, y, change in level) to connected tile list for locations reachable by portal
    for key, value in portals.items():
        if len(value) == 1:
            continue
        for i, loc in enumerate(value):
            x, y = loc
            if x == 2 or x == 120 or y == 2 or y == 118:
                traversable[(x, y)].append([(loc) + (-1,) for j, loc in enumerate(value) if j != i][0])
            else:
                traversable[(x, y)].append([(loc) + (1,) for j, loc in enumerate(value) if j !=i][0])

    # set start and finish tiles (including level required)
    origin = portals['AA'][0] + (0,)
    destination = portals['ZZ'][0] + (0,)
    
    sq = deque()
    sq.append(origin + (0,))  # format (x, y, z, d)
    best_states = {}
    while sq:
        x, y, z, d = sq.popleft()
        if z < 0:  # can't go below level 0
            continue
        if (x, y, z) == destination:
            print('Final destination reached in %d steps' %d)
            break
        previous_best = best_states.get((x, y, z), 1000000)
        if d >= previous_best:
            continue
        best_states[(x, y, z)] = d
        sq.extend([x[:2] + (z + x[2], d + 1) for x in traversable[(x, y)]])  # add possible next steps to queue, including change in level and distance


def move(loc, d):
    vector_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    x, y = loc
    return x + vector_dict[d][1], y + vector_dict[d][0]


def print_grid(grid, rows, cols):
    for y in range(rows):
        p_row = ''
        for x in range(cols):
            p_row += grid[(x, y)]
        print(p_row)


if __name__ == "__main__":
    main()