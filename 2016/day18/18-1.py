def main():
    with open('day18/18.txt', 'r') as open_file:
        seed_row = open_file.read()
        trap_floor = TrapFloor(seed_row, 40)
        trap_floor.propagate()
        trap_floor.print_floor()
        print(f'Number of safe tiles: {trap_floor.count_safe()}')

class TrapFloor:
    def __init__(self, seed, h):
        self.h = h
        self.grid = [seed]
        self.w = len(seed)
        self.trapconfigs = ['^^.', '.^^', '^..', '..^']

    def propagate(self):
        for i in range(1, self.h):
            new_row = ''
            prev_row = self.grid[i - 1]
            for j in range(self.w):
                if j == 0:
                    check = '.' + prev_row[j: j+ 2]
                elif j == self.w - 1:
                    check = prev_row[j - 1: j + 1] + '.'
                else:
                    check = prev_row[j - 1: j + 2]
                if check in self.trapconfigs:
                    new_row += '^'
                else:
                    new_row += '.'
            self.grid.append(new_row)

    def count_safe(self):
        count = 0
        for i in range(self.h):
            count += self.grid[i].count('.')
        return count

    def print_floor(self):
        for i in range(self.h):
            print(self.grid[i])

if __name__ == '__main__':
    main()
