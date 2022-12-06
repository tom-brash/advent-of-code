import hashlib
from collections import deque

def main():
    passcode = 'pslxynzg'
    vault = Vault(passcode)
    vault.find_best_path()

class Vault:
    def __init__(self, passcode):
        self.passcode = passcode
        self.target = (3, 3)
        self.vectors = {0: (0, -1, 'U'), 3: (1, 0, 'R'), 1: (0, 1, 'D'), 2: (-1, 0, 'L')}

    def find_best_path(self):
        sq = deque()
        sq.append((0, 0, '', 0)) # format x, y, path, d
        best_distances = {}
        while sq:
            x, y, path, d = sq.popleft()
            if (x, y) == self.target:
                print(f'Made it to the vault in {d} steps')
                print(f'Path: {path}')
                break
            sq.extend(self.get_paths(x, y, path, d))

    def get_paths(self, x, y, path, d):
        path_string = self.passcode + path
        open_doors = hashlib.md5(path_string.encode()).hexdigest()[:4]
        moves = []
        for i in range(4):
            if open_doors[i] in 'bcdef':
                v = self.vectors[i]
                move = (x + v[0], y + v[1], path + v[2], d + 1)
                if move[0] >= 0 and move[0] < 4 and move[1] >= 0 and move[1] < 4:
                    moves.append(move)
        return moves


if __name__ == '__main__':
    main()
