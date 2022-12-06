from collections import deque

def main():
    with open('day24/24.txt', 'r') as open_file:
        input_data = open_file.read()

    maze = Maze(input_data)
    maze.find_path()

class Maze:
    def __init__(self, input_data):
        self.targets = {}
        self.grid = set()
        for y, r in enumerate(input_data.split('\n')):
            for x, c in enumerate(r):
                if c == '#':
                    continue
                if c == '0':
                    self.pos = (x, y)
                elif c != '.':
                    self.targets[(x, y)] = int(c)
                self.grid.add((x, y))
        self.vectors = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

    def find_path(self):
        sq = deque()
        sq.append((*self.pos, 0, 0))
        goal = (1 << len(self.targets)) - 1
        best_distances = {}
        while sq:
            x, y, loc_string, d = sq.popleft()
            if loc_string == goal and (x, y) == self.pos:
                print(f'Fewest moves required: {d}')
                break
            best = best_distances.get((x, y, loc_string), 1000000)
            if d >= best:
                continue
            best_distances[(x, y, loc_string)] = d
            sq.extend(self.get_moves(x, y, loc_string, d))

    def get_moves(self, x, y, visited, d):
        possible = []
        for i in range(4):
            v = self.vectors[i]
            new_loc = (x + v[0], y + v[1])
            if new_loc not in self.grid:
                continue
            new_visited = visited
            if new_loc in self.targets:
                new_visited |= 1 << self.targets[new_loc] - 1
            possible.append((*new_loc, new_visited, d + 1))
        return possible


if __name__ == '__main__':
    main()