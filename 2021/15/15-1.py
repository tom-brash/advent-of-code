from collections import defaultdict
from collections import deque
import copy

def main():
    with open('15/15.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    grid = {}
    max_y = 0
    max_x = 0
    for i, y in enumerate(input_data):
        for j, c in enumerate(y):
            grid[(i, j)] = int(c)
            max_x = j
        max_y = i
    
    iterations = 0
    target = (max_x, max_y) # UPDATE to target state
    best_states = {}
    sq = deque()
    sq.append((0, 0, 0)) # UPDATE to origin
    while sq:
        iterations += 1
        x, y, d = sq.popleft()
        d += grid[(x, y)]
        if (x, y) == target:
            print('Finished!')
            print(f'Target found! Took {d} risk')

        previous_best = best_states.get((x, y), 1000000)
        if d >= previous_best:
            continue
        best_states[(x, y)] = d
        sq.extend([move((x, y), i) + (d,) for i in range(4) if move((x, y), i) in grid])

def move(loc, d):
    vector_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    x, y = loc
    return x + vector_dict[d][1], y + vector_dict[d][0]

class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()