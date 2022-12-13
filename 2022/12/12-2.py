import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    grid = {}
    possible_starts = []

    for y, row in enumerate(input):
        row_dict = {}
        for x, c in enumerate(row):
            if c in ['S', 'a']:
                grid[(x, y)] = ord('a')
                possible_starts.append((x, y))
            elif c == "E":
                grid[(x, y)] = ord('z')
                target = (x, y)
            else:
                grid[(x, y)] = ord(c)

    impossible_locations = 0
    worst_found = 0
    best_found = 100000000
    for start in possible_starts:
        best_route = map_path(start, target, grid)
        if not best_route:
            impossible_locations += 1
            continue
        if best_route < best_found:
            best_found = best_route
        if best_route > worst_found:
            worst_found = best_route

    print(f'{len(possible_starts)} different routes attempted')
    print(f'{impossible_locations} of those starts were deemed impossible')
    print(f'Longest viable route was {worst_found} steps')
    print(f'\nBest possible route was {best_found} steps')

def map_path(start, target, grid):
    sq = deque()
    best_states = {}

    sq.append(start + (0,))

    while sq:
        x, y, d = sq.popleft()
        if (x, y) == target:
            return d
        previous_best = best_states.get((x, y), 1000000000)
        if d >= previous_best:
            continue
        best_states[(x, y)] = d
        sq.extend(get_valid_moves(x, y, d, grid))
    return None


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
