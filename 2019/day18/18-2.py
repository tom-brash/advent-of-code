'''
DAY 18-2: Maze pathfinding with four explorers

Here the grid is modified slightly (this has been done manually in the input data)
to split it into four grids, each with its own explorer. A simplification is done here
to assume that, given that waiting has no penalty, the correct instructions can always
be interspersed in such a way that doors with keys in other quartiles can essentially
be ignored. If it is necessary to go through one, the explorer can just pause outside
until the key is collected elsewhere. 

In practice this works on the input, but it is not fully generalizable. It is possible
that in edge cases it will not be possible for the explorer to 'wait' at the optimum moment,
instead needing to take more steps in another direction. 

The only meaningful difference from the code in 18-1 is that instead of starting with no
keys, each explorer is presumed to start with all the keys not from that region.
''' 

from collections import deque

def traverse_grid(maze_lines):
    grid = {}
    traversable = {}
    all_keys = (1 << 26) - 1
    starting_keys = all_keys
    origin = None
    rows = len(maze_lines)
    cols = len(maze_lines[0])
    for y, line in enumerate(maze_lines):
        for x, char in enumerate(line):
            if char == '@':
                origin = (x, y)
            elif is_key(char):
                starting_keys ^= key_bit(char)  # bitwise exclusive OR used to make the key possession 0 instead of 1
            grid[(x, y)] = char
            if char != '#':
                traversable[(x, y)] = char

    print_grid(grid, rows, cols)
    print('\n')
    
    iterations = 0
    best_states = {}
    sq = deque()
    sq.append(origin + (starting_keys, 0))  # format: (x, y, keys collected, distance traversed)
    while sq:
        iterations += 1  # track total work required
        x, y, keys, d = sq.popleft()
        char = grid[(x, y)]
        if is_key(char):
            
            keys |= key_bit(char)  # add key to collection
            if keys == all_keys:
                print('Finished!')
                print('All keys found! Took %d moves' %d)
                break
        elif is_door(char):
            if not have_key(char, keys):
                continue

        previous_best = best_states.get((x, y, keys), 10000000)
        if d >= previous_best:
            continue
        best_states[(x, y, keys)] = d
        sq.extend([move((x, y), i) + (keys, d + 1) for i in range(4) if move((x, y), i) in traversable]) 
    
    return d
         

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


def is_key(char):
    return char >= 'a' and char <= 'z'


def is_door(char):
    return char >= 'A' and char <= 'Z'


def key_bit(key):
    key_idx = ord(key) - 97
    return 1 << key_idx


def door_bit(door):
    door_idx = ord(door) - 65
    return 1 << door_idx


def have_key(door, keys):
    return door_bit(door) & keys


if __name__ == "__main__":
    with open('day18/18-2-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    maze_lines = input_data.split('\n')    
    # create four separate quartiles
    q1 = [x[:40] for x in maze_lines[:40]]
    q2 = [x[41:] for x in maze_lines[:40]]
    q3 = [x[:40] for x in maze_lines[41:]]
    q4 = [x[41:] for x in maze_lines[41:]]
    
    total = 0
    for q in [q1, q2, q3, q4]:
        total += traverse_grid(q)
    
    print('Total:', total)
    
