'''
This version of the code takes advantage of the data provided. Notably, there are two types of data cell: large and small.
The large cells (~500B) cannot move into any adjacent cell at any time. The smaller cells, though they vary somewhat in data
size and capacity, are entirely interchangable: the largest small data fits within the smallest container. Further, the data
are all of size such that no two data can fit within one cell.

Given this, we don't need to keep track of the entire memory state as we use breadth first search. As we are essentially just
doing a sliding block puzzle with multiple blockers (the large cells) we can just keep track of the target and the current
empty space: it makes no difference how the other small blocks are interchanged. 
'''


import re
from collections import deque

def main():
    with open('day22/22.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')[2:]

    nodes = {}
    max_x = 0
    for i in input_data:
        nums = [int(x) for x in re.findall(r'\d+', i)]
        if nums[3] > 300:
            continue
        nodes[(nums[0], nums[1])] = [nums[3], nums[4]]
        if nums[0] > max_x:
            max_x = nums[0]
        if nums[3] == 0:
            empty = (nums[0], nums[1])

    cluster = MemoryCluster(nodes, max_x, empty)
    cluster.find_best_path()

class MemoryCluster:
    def __init__(self, node_data, max_x, empty):
        self.nodes = node_data
        self.vectors = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
        self.viable_pairs = set()
        self.target = (max_x, 0)
        self.empty = empty

    def find_best_path(self):
        sq = deque()
        sq.append((self.target, self.empty, 0)) # format (target location, empty ,d)
        best_distances = {}
        while sq:
            loc, empty, d = sq.popleft()
            if loc == (0, 0):
                print(f'Found best path, taking {d} steps')
                break
            previous_best = best_distances.get((loc, empty), 1000000)
            if d >= previous_best:
                continue
            best_distances[(loc, empty)] = d
            sq.extend(self.get_next_states(loc, empty, d))
            

    def get_next_states(self, loc, empty, d):
        adjacent = self.get_adjacent(*empty)
        possible_states = []
        for a in adjacent:
            new_loc = loc
            if a == loc:
                new_loc = empty
            possible_states.append((new_loc, a, d + 1))
        return possible_states


    def get_adjacent(self, x, y):
        adjacent = []
        for i in range(4):
            v = self.vectors[i]
            loc = (x + v[0], y + v[1])
            adjacent.append(loc)
        adjacent = [loc for loc in adjacent if loc in self.nodes]
        return adjacent


if __name__ == '__main__':
    main()
