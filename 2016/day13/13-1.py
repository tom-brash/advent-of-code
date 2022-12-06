from collections import deque

def main():
    input_val = 1364
    target = (31, 39)

    maze = Maze(target, input_val)
    maze.find_target()

class Maze:
    def __init__(self, target, z):
        self.target = target
        self.z = z
        self.grid = {(0, 0): '.'}
        self.vectors = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

    def print_grid(self, n):
        for y in range(n):
            ps = ''
            for x in range(n):
                ps += self.grid.get((x, y), ' ')
            print(ps)

    def find_target(self):
        sq = deque()
        sq.append((0, 0, 0))  # format = x, y, d
        best_distances = {}
        while sq:
            x, y, d = sq.popleft()
            if (x, y) == self.target:
                print(f'Minimum steps required: {d}')
                break
            if (x, y) in self.grid:
                c = self.grid[(x, y)]
            else:
                c = self.check(x, y)
                self.grid[(x, y)] = c
            if c == '#':
                continue
            prev_best = best_distances.get((x, y), 1000000)
            if d >= prev_best:
                continue
            best_distances[(x, y)] = d
            sq.extend(self.get_moves(x, y, d))


    def check(self, x, y):
        ones = bin(x * x + 3 * x + 2 * x * y + y + y * y + self.z).count('1')
        if ones % 2 == 0:
            return '.'
        return '#'


    def get_moves(self, x, y, d):
        moves = []
        for i in range(4):
            v = self.vectors[i]
            move = (x + v[0], y + v[1], d + 1)
            if move[0] >= 0 and move[1] >= 0:
                moves.append(move)
        return moves




if __name__ == '__main__':
    main()
