'''
DAY 20-1: Navigating mazes with portals

Here we need to navigate a maze that has portals all around it.

The more annoying part of this may be the parsing. Since the portals are two character names, 
it is a little clunky to parse the file line by line and get the portal names.

We do a couple of loops here. First we loop through the input file and keep track of a grid 
dictionary (solely for printing purposes) and a traversable dictionary (the spaces that can
be moved on). We also keep track of where the portals are and the cells they're touching.

We then loop through the traversable dictionary. For each location, we make a list of 
locations that are reachable using traditional movement (no portals). Finally, we add
the portal destinations to those lists in the traversable dictionary.

The actual maze pathfinding itself is a simple breadth first search using very similar
logic to day 18, checking all locations and seeing if the destination has previously
been reached faster.
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
                traversable[(x, y)] = []  # empty list for connected tiiles
            if char >= 'A' and char <= 'Z':  # make list of portals
                if y > 0 and x > 0 and y < (h - 1) and x < (w - 1):
                    if maze_rows[y + 1][x] == '.':
                        portals[''.join([maze_rows[y - 1][x], char])].append((x, y + 1))
                    elif maze_rows[y - 1][x] == '.':
                        portals[''.join([char, maze_rows[y + 1][x]])].append((x, y - 1))
                    elif maze_rows[y][x + 1] == '.':
                        portals[''.join([maze_rows[y][x - 1], char])].append((x + 1, y))
                    elif maze_rows[y][x - 1] == '.':
                        portals[''.join([char, maze_rows[y][x + 1]])].append((x - 1, y))

    # create list of connected tiles
    for loc in traversable:
        traversable[(loc)].extend([move(loc, d) for d in range(4) if move(loc, d) in traversable])
    
    # add to connected tiles list the tiles reachable by portals
    for key, value in portals.items():
        if len(value) == 1:
            continue
        traversable[value[0]].append(value[1])
        traversable[value[1]].append(value[0])
    
    # set start and end locations
    origin = portals['AA'][0]
    destination = portals['ZZ'][0]
    
    # breadth first search of the space
    sq = deque()
    sq.append(origin + (0,))  # format (x, y, d)
    best_states = {}
    while sq:
        x, y, d = sq.popleft()
        if (x, y) == destination:
            print('Final destination reached in %d steps' %d)
            break
        previous_best = best_states.get((x, y), 1000000)
        if d >= previous_best:
            continue
        best_states[(x, y)] = d
        sq.extend([x + (d + 1,) for x in traversable[(x, y)]])


# get result of a move in some direction
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