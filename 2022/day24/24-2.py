import re
from collections import deque, defaultdict
import heapq

def main():
    print('\nElves forgot their snacks in the grove..........')
    print('Plotting most efficient route back...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    valley = Valley(input)
    start = valley.start
    target = valley.target

    possible_states = defaultdict(set)
    possible_states[0].add(start)
    t = 0
    targets_hit = 0
    targets = {0: target, 1: start, 2: target}

    while targets_hit < 3:
        positions = possible_states[t]
        proposals = set()
        for p in positions:
            proposals = proposals.union(set([(p[0] + v[0], p[1] + v[1]) for v in [(1, 0), (-1, 0), (0, 1), (0, -1)]]))
            proposals.add(p)
        clear = valley.clear[t+1]
        next_positions = clear.intersection(proposals)
        t += 1
        possible_states[t] = next_positions
        if targets[targets_hit] in next_positions:
            # print(f'Found a target! Switching target...')
            possible_states[t] = set()
            possible_states[t].add(targets[targets_hit])
            # print(possible_states[t])
            targets_hit += 1
            # print(t)
    
    print(f'\n(24-2) Minimum steps to get out, backtrack for snacks, and get out again: {t}')

class Valley:
    def __init__(self, input):
        self.h_blizzards = {0: defaultdict(list)}
        self.v_blizzards = {0: defaultdict(list)}
        self.clear = defaultdict(set)
        for r, row in enumerate(input, -1):
            for c, ch in enumerate(row, -1):
                if ch in '<>':
                    self.h_blizzards[0][ch].append((r, c))
                elif ch in '^v':
                    self.v_blizzards[0][ch].append((r,c))
                elif ch in 'E.':
                    self.clear[0].add((r, c))
        self.width = len(input[0]) - 2
        self.height = len(input) - 2
        self.move_dicts = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
        self.start = (-1, 0)
        self.target = (self.height, self.width - 1)
        for i in range(self.height):
            self.v_blizzards = self.update_blizzards(self.v_blizzards, i)

        for i in range(self.width):
            self.h_blizzards = self.update_blizzards(self.h_blizzards, i)

        for i in range(1, self.height * self.width):
            self.update_clear_space(i)

    def update_blizzards(self, b, i):
        b[i + 1] = defaultdict(list)
        for direction, positions in b[i].items():
            new_positions = self.move(direction, positions)
            b[i + 1][direction] = new_positions
        return b

    def move(self, direction, positions):
        vec = self.move_dicts[direction]
        new_positions = []
        for pos in positions:
            n_r = (pos[0] + vec[0]) % self.height
            n_c = (pos[1] + vec[1]) % self.width
            new_positions.append((n_r, n_c))
        return new_positions
    
    def update_clear_space(self, i):
        blizzards = self.get_blizzards(i) 
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) in blizzards:
                    continue
                self.clear[i].add((r, c))
        self.clear[i].add(self.start)
        self.clear[i].add(self.target)

    def get_blizzards(self,i):
        all_blizzards = set()
        for d in ['<', '>']:
            all_blizzards = all_blizzards.union(self.h_blizzards[i % self.width][d])
        for d in ['^', 'v']:
            all_blizzards = all_blizzards.union(self.v_blizzards[i % self.height][d])
        return all_blizzards

if __name__ == "__main__":
    main()
