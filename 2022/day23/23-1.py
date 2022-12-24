import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    es = Elves()
    for r, row in enumerate(input):
        for c, ch in enumerate(row):
            if ch == "#":
                es.elves.append(Elf(r,c))

    for i in range(10):
        es.run_round()

    es.get_answer()

class Elves:
    def __init__(self):
        self.elves = []
        self.order = deque(['N', 'S', 'W', 'E'])
        self.current_positions = None

    def get_positions(self):
        positions = set()
        for e in self.elves:
            positions.add(e.pos)
        self.current_positions = positions
        self.d_dict = {
                'N': ((-1, -1), (-1, 0), (-1, 1)),
                'S': ((1, -1), (1, 0), (1, 1)),
                'W': ((-1, -1), (0, -1), (1, -1)),
                'E': ((-1, 1), (0, 1), (1, 1))
                }

    def run_round(self):
        current_positions = self.get_positions()
        # get proposed
        proposed_moves = defaultdict(int)
        for e in self.elves:
            proposed = e.pos
            # check for empty
            if not self.check_pos(e.pos, 'all'):
                # check directions
                for d in self.order:
                    if self.check_pos(e.pos, d):
                        move = self.d_dict[d][1]
                        proposed = (e.pos[0] + move[0], e.pos[1]+ move[1])
                        break
            proposed_moves[proposed] += 1
            e.proposed = proposed

        for e in self.elves:
            if proposed_moves[e.proposed] > 1:
                continue
            e.pos = e.proposed
        
        self.order.rotate(-1)

    def print_grid(self):
        self.get_positions()
        min_r, max_r, min_c, max_c = self.get_boundaries()
        for r in range(min_r, max_r + 1):
            print_str = ''
            for c in range(min_c, max_c + 1):
                if (r,c) in self.current_positions:
                    print_str += '#'
                else:
                    print_str += '.'
            print_str += str(r)
            print(print_str)

    def get_answer(self):
        min_r, max_r, min_c, max_c = self.get_boundaries()
        width = (max_c - min_c) + 1
        height = (max_r - min_r) + 1
        print(f'Free spaces after 10 movement cycles: {width * height  - len(self.current_positions)}')

    def get_boundaries(self):
        self.get_positions()
        min_r = 1000
        min_c = 1000
        max_r = 0
        max_c = 0
        
        for p in self.current_positions:
            if p[0] < min_r:
                min_r = p[0]
            if p[0] > max_r:
                max_r = p[0]
            if p[1] < min_c:
                min_c = p[1]
            if p[1] > max_c:
                max_c = p[1]

        return (min_r, max_r, min_c, max_c)

                
    def check_pos(self, pos, d):
        if d == "all":
            for i in ['N', 'S', 'W', 'E']:
                for p in self.d_dict[i]:
                    if (pos[0] + p[0], pos[1] + p[1]) in self.current_positions:
                        return False
            return True

        for p in self.d_dict[d]:
            if (pos[0] + p[0], pos[1] + p[1]) in self.current_positions:
                return False
        return True

class Elf:
    def __init__(self, r, c):
        self.pos = (r, c)
        self.proposed = None


if __name__ == "__main__":
    main()
