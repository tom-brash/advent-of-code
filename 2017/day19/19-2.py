import string

def main():
    with open('day19/19.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    router = Router(input_data)
    router.packet_run()
    print(router.collected)
    print(f'Steps taken: {router.steps + 1}')


class Router():
    def __init__(self, input_data):
        self.grid = {}
        for y, row in enumerate(input_data):
            for x, c in enumerate(row):
                if c != ' ':
                    self.grid[(x, y)] = c
        
        self.pos = [k for k in self.grid.keys() if k[1] == 0][0]
        self.d = 2
        self.vecs = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
        self.collected = ''
        self.complete = False
        self.steps = 0

    def packet_run(self):
        while True:
            if self.grid[self.pos] != '+':
                self.pos = (self.pos[0] + self.vecs[self.d][0], self.pos[1] + self.vecs[self.d][1])
                if self.pos not in self.grid:
                    self.complete = True
                    break
                self.steps += 1
                if self.grid[self.pos] in string.ascii_uppercase:
                    self.collected += self.grid[self.pos]
                    
            else:
                found = False
                for i in [-1, 1]:
                    possible_d = (self.d + i) % 4
                    possible_move = (self.pos[0] + self.vecs[possible_d][0], self.pos[1] + self.vecs[possible_d][1])
                    if possible_move in self.grid:
                        found = True
                        self.pos = possible_move
                        self.d = possible_d
                        break
                if not found:
                    self.complete = True
                    break

                self.steps += 1
                if self.grid[self.pos] in string.ascii_uppercase:
                    self.collected += self.grid[self.pos]


if __name__ == '__main__':
    main()