from collections import defaultdict
from queue import PriorityQueue
import numpy as np
import time

def main():
    with open('15/15.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    # create main grid from input
    grid = np.array([[int(i) for i in line] for line in input_data])
    
    # create expanded grid
    big_grid = np.block([[grid + i + j for i in range(5)] for j in range(5)])
    big_grid[big_grid > 9] -= 9

    start_time = time.time()
    print(shortest_path(grid, (0, 0)))
    print(shortest_path(big_grid, (0, 0)))
    print(time.time() - start_time)
    start_time = time.time()


def shortest_path(grid, start):
    n = len(grid) - 1
    visited = set()
    dist = defaultdict(lambda: np.inf, {start: 0})
    vecs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = PriorityQueue()
    q.put((0, start))
    while q:
        d, node = q.get()
        if node in visited: continue
        visited.add(node)
        if node == (n, n):
            return d
        y, x = node
        for vi, vj in vecs:
            new_y, new_x = y + vi, x + vj
            if new_y in (-1, n + 1) or new_x in (-1, n + 1):
                continue
            new_node = (new_y, new_x)
            if new_node in visited:
                continue
            new_d = d + grid[new_y][new_x]
            if new_d < dist[new_node]:
                dist[new_node] = new_d
                q.put((new_d, new_node))
    
    return None
        

if __name__ == '__main__':
    main()