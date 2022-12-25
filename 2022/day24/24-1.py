import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    valley = Valley(input)

class Valley:
    def __init__(self, input):
        self.blizzards = {0: defaultdict(list)}
        self.clear_spaces = defaultdict(set)
        self.current = 0
        for r, row in enumerate(input, -1):
            for c, ch in enumerate(row, -1):
                if ch in '<>^v':
                    self.blizzards[self.current][ch].append((r, c))
                elif ch == '.':
                    self.clear_spaces[0].add((r, c))
        self.left_c = 0
        self.right_c = len(input[0]) - 3
        self.up_r = 0
        self.bottom_r = len(input) - 3
        self.width = self.right_c + 1
        self.height = self.bottom_r + 1
        self.cycle = self.width * self.height
        self.starting_clear = self.clear_spaces[0]
        # print(self.width, self.height)
        # print(self.left_c, self.right_c, self.up_r, self.bottom_r)
        # print(self.blizzards)
        # print(self.clear_spaces)
        self.move_dicts = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

        for i in range(self.cycle):
            print(i)
            self.update_blizzards()
        
        print(self.clear_spaces[self.current] == self.clear_spaces[0])
        # print(self.starting_clear)
        # print(self.clear_spaces[self.current - 1])
        

    def update_blizzards(self):
        self.blizzards[self.current + 1] = defaultdict(list)
        for k, v in self.blizzards[self.current].items():
            n_positions = self.move(k, v)
            self.blizzards[self.current + 1][k] = n_positions
        self.current += 1
        self.find_open_ground()
        # print(f'At time {self.current}')
        # print(f'Current blizzards: {self.blizzards[self.current]}')
        # print(f'Equals starting state: {self.clear_spaces[self.current] == self.starting_clear}')

    def move(self, d, positions):
        vec = self.move_dicts[d]
        new_positions = []
        for pos in positions:
            n_r = (pos[0] + vec[0] ) % self.height
            n_c = (pos[1] + vec[1] ) % self.width
            new_positions.append((n_r , n_c ))
        return new_positions

    def find_open_ground(self):
        all_blizzards = []
        for d in ['<', '^', 'v', '>']:
            all_blizzards.extend(self.blizzards[self.current][d])
        for r in range(self.up_r, self.bottom_r + 1):
            for c in range(self.left_c, self.right_c + 1):
                if (r, c) in all_blizzards:
                    continue
                self.clear_spaces[self.current].add((r, c))
        self.clear_spaces[self.current].add((-1, 0))
        self.clear_spaces[self.current].add((self.bottom_r + 1, self.right_c))
        # print(f'CLEAR: {len(self.clear_spaces[self.current])}')
            

if __name__ == "__main__":
    main()
