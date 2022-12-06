import re

def main():
    with open('day8/8.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')
    
    screen = Screen(6, 50)
    
    for i in instructions:
        parameters = [int(x) for x in re.findall(r'\d+', i)]
        if i[:4] == 'rect':
            screen.rec(parameters[0], parameters[1])
        elif i[:10] == 'rotate row':
            screen.rot_row(parameters[0], parameters[1])
        elif i[:10] == 'rotate col':
            screen.rot_col(parameters[0], parameters[1])

    screen.print_screen()
    print(screen.count_on())
    

class Screen:
    def __init__(self, r, c):
        self.matrix = []
        self.n = r
        for i in range(r):
            self.matrix.append([' '] * c)
    
    def rec(self, x, y):
        for i in range(x):
            for j in range(y):
                self.matrix[j][i] = '#'

    def rot_row(self, r, n):
        self.matrix[r] = [self.matrix[r][(i - n) % len(self.matrix[r])] for i, x in enumerate(self.matrix[r])]

    def rot_col(self, c, n):
        col = [self.matrix[i][c] for i in range(self.n)]
        col = [col[(i - n) % len(col)] for i, x in enumerate(col)]
        for i, x in enumerate(col):
            self.matrix[i][c] = x

    def print_screen(self):
        for i in range(self.n):
            print(''.join(self.matrix[i]))
    
    def count_on(self):
        total = 0
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                if self.matrix[r][c] == '#':
                    total += 1
        return total


if __name__ == '__main__':
    main()