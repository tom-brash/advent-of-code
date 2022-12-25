import re
from collections import deque, defaultdict

def main():
    print('====Day 12====')
    print('Attempting contact with elves....')
    print('No signal')
    print('Plotting path up nearby mountain to get signal...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    grid = {}

    for y, row in enumerate(input):
        row_dict = {}
        for x, c in enumerate(row):
            if c == "S":
                grid[(x, y)] = ord('a')
                start = (x, y)
            elif c == "E":
                grid[(x, y)] = ord('z')
                target = (x, y)
            else:
                grid[(x, y)] = ord(c)

    sq = deque()
    best_states = {}

    sq.append(start + (0,))
    
    while sq:
        x, y, d = sq.popleft()
        if (x, y) == target:
            print(f'\n(12-1) Best route found up the mountain in {d} moves')

        previous_best = best_states.get((x, y), 1000000000)
        if d >= previous_best:
            continue
        best_states[(x, y)] = d
        sq.extend(get_valid_moves(x, y, d, grid))


def get_valid_moves(x, y, d, grid):
    vector_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    current = (x, y)
    possible_outcomes = []
    current_height = grid[current]
    for i in range(4):
        new = (x + vector_dict[i][0], y + vector_dict[i][1])
        if new not in grid:
            continue
        if grid[new] - grid[current] > 1:
            continue
        possible_outcomes.append(new + (d + 1,))
    return possible_outcomes

if __name__ == "__main__":
    main()
