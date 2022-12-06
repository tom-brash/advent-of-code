'''
DAY 18-1: Maze pathfinding

Here we need to find our way through a maze and pick up all the keys, which 
will immediately unlock doors in the maze. A breadth first search works here, 
creating a queue of positions to search and working our way around the maze.
A few tricks are employed to speed things up.

The 'state' that we are in needs to include not just the (x, y) location in the
maze, but also the number of keys reached. We keep a dictionary of states, and if 
we are reaching a given state in a longer amount of time than we previously used,
we can prune that branch from the search. (This prevents a start like W, E, W, E).

We store the keys using a bit string for faster comparison operations than a list 
or string. Each of the keys is represented as a single significant bit, and so we 
can keep track of all our keys using one integer. 26 0s represents no keys, 26 keys 
would be all the keys.

A deque is used instead of a list because we are only ever going to pop things off
the left and append to the right.
''' 
from collections import deque

def main():
    with open('day18/18-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    maze_lines = input_data.split('\n')

    # read in the input
    grid = {}
    traversable = {}  # only tiles that can be moved onto
    num_keys = 0
    origin = None
    rows = len(maze_lines)
    cols = len(maze_lines[0])
    for y, line in enumerate(maze_lines):
        for x, char in enumerate(line):
            if char == '@':
                origin = (x, y)
            elif is_key(char):
                num_keys += 1
            grid[(x, y)] = char
            if char != '#':
                traversable[(x, y)] = char

    print_grid(grid, rows, cols)
    print('\n')
    
    iterations = 0
    all_keys = (1 << num_keys) - 1  # create a bit string of 1s as long as the number of keys
    best_states = {}  # dictionary to store the best steps to reach any given state
    sq = deque()  # search queue
    sq.append(origin + (0, 0))  # format: (x, y, keys collected, distance traversed)
    while sq:
        iterations += 1  # track total work required
        x, y, keys, d = sq.popleft()
        char = grid[(x, y)]
        if is_key(char):            
            keys |= key_bit(char)  # add key to collection using bitwise OR
            if keys == all_keys:
                print('Finished!')
                print('All keys found! Took %d moves' %d)
                break
        elif is_door(char):
            if not have_key(char, keys):  # treat it like a wall if key is not possessed
                continue

        # check previous state - if it hasn't been reached then a value of 10m will be used to compare        
        previous_best = best_states.get((x, y, keys), 10000000)
        # discard search branch if it takes too many steps
        if d >= previous_best:
            continue
        best_states[(x, y, keys)] = d
        # add to RHS of queue all possible moves from current location
        sq.extend([move((x, y), i) + (keys, d + 1) for i in range(4) if move((x, y), i) in traversable]) 
    
    print(x, y, bin(keys), d)
         

# move in one direction
def move(loc, d):
    vector_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    x, y = loc
    return x + vector_dict[d][1], y + vector_dict[d][0]


# print the grid neatly
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


# return a bitstring with a 1 in place of the key
def key_bit(key):
    key_idx = ord(key) - 97
    return 1 << key_idx


# return a bitstring with a 1 in place of the door
def door_bit(door):
    door_idx = ord(door) - 65
    return 1 << door_idx


def have_key(door, keys):
    return door_bit(door) & keys


if __name__ == "__main__":
    main()