'''
This version takes advantage of the fact that we are always working with a single empty cell, and recognizing
that any new moves will be directly connected to the empty cell. It generalizes to the case where multiple 
cells worth of data can fit in one cell, but the resultant passing of the node state and checking of sizes makes
it very slow to compute for the provided data (~10min)

'''

import re
from collections import deque
import copy

def main():
    with open('day22/22.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')[2:]

    nodes = {}
    max_x = 0
    for i in input_data:
        nums = [int(x) for x in re.findall(r'\d+', i)]
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
        sq.append((self.target, copy.deepcopy(self.nodes), self.empty, 0)) # format (target location, node data ,d)
        best_distances = {}
        i = 0
        while sq:
            loc, nodes, empty, d = sq.popleft()
            i += 1
            if i % 1000 == 0:
                print(i, d)
            if loc == (0, 0):
                print(f'Found best path, taking {d} steps')
                break
            previous_best = best_distances.get((loc, empty), 1000000)
            if d >= previous_best:
                continue
            best_distances[(loc, empty)] = d
            sq.extend(self.get_next_states(loc, nodes, empty, d))
            

    def get_next_states(self, loc, nodes, empty, d):
        adjacent = self.get_adjacent(*empty)
        available_space = nodes[empty][1]
        possible_states = []
        for a in adjacent:
            data_size = nodes[a][0]
            if data_size <= available_space:
                new_nodes = copy.deepcopy(nodes)
                new_nodes[empty][0] += data_size
                new_nodes[empty][1] -= data_size
                new_nodes[a][1] += data_size
                new_nodes[a][0] = 0
                new_loc = loc
                if a == loc:
                    new_loc = empty
                possible_states.append((new_loc, new_nodes, a, d + 1))
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
