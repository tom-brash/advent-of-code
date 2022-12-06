from collections import deque

# move in one direction
def move(loc, d):
    vector_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    x, y = loc
    return x + vector_dict[d][1], y + vector_dict[d][0]

grid = {}
traversable = {}

iterations = 0
target = 1000 # UPDATE to target state
best_states = {}
sq = deque()
sq.append((0, 0, 0)) # UPDATE to origin
while sq:
    iterations += 1
    x, y, d = sq.popleft()
    char = grid[(x, y)]
    if (x, y) == target:
        print('Finished!')
        print(f'Target found! Took {d} moves')
        break

    previous_best = best_states.get((x, y), 1000000)
    if d >= previous_best:
        continue
    best_states[(x, y)] = d
    sq.extend([move((x, y), i) + (d + 1,) for i in range(4) if move((x, y), i) in traversable])

