def main():
    with open('day21/21.txt', 'r') as open_file:
        input_data = open_file.read()

    fractal = Fractal(input_data.split('\n'))
    for i in range(18):
        fractal.iteration()
        fractal.count_pixels()
        

class Fractal():
    def __init__(self, input_data):
        self.grid = {}
        
        # read in instructions
        self.instructions = {}
        for i in input_data:
            ip = tuple(i.split(' => ')[0].split('/'))
            op = i.split(' => ')[1].split('/')
            self.instructions[ip] = op

        # initialize grid
        for y, row in enumerate(['.#.', '..#', '###']):
            for x, c in enumerate(row):
                self.grid[(x, y)] = c
        
        self.size = 3
    
    def iteration(self):
        new_grid = {}
        if self.size % 2 == 0:
            for i in range(self.size // 2):
                for j in range(self.size // 2):
                    block = [''.join([self.grid[(i * 2, j * 2)], self.grid[(i * 2 + 1, j * 2)]]),
                        ''.join([self.grid[(i * 2, j * 2 + 1)], self.grid[(i * 2 + 1, j * 2 + 1)]])]
                    
                    new_block = self.find_match(block)
                    for y, row in enumerate(new_block):
                        for x, c in enumerate(row):
                            new_grid[(i * 3 + x, j * 3 + y)] = c
            self.size = self.size // 2 * 3

        else:
            for i in range(self.size // 3):
                for j in range(self.size // 3):
                    block = [''.join([self.grid[(i * 3, j * 3)], self.grid[(i * 3 + 1, j * 3)], self.grid[(i * 3 + 2, j * 3)]]),
                        ''.join([self.grid[(i * 3, j * 3 + 1)], self.grid[(i * 3 + 1, j * 3 + 1)], self.grid[(i * 3 + 2, j * 3 + 1)]]),
                        ''.join([self.grid[(i * 3, j * 3 + 2)], self.grid[(i * 3 + 1, j * 3 + 2)], self.grid[(i * 3 + 2, j * 3 + 2)]])]
                    
                    new_block = self.find_match(block)
                    for y, row in enumerate(new_block):
                        for x, c in enumerate(row):
                            new_grid[(i * 4 + x, j * 4 + y)] = c
            self.size = self.size // 3 * 4
        
        self.grid = new_grid

    def count_pixels(self):
        print(f"Total pixels in image: {sum([1 for p in self.grid.values() if p == '#'])}")

    def find_match(self, block):
        found = False
        while True:
            for i in range(4):
                check_block = tuple([''.join(x) for x in block])
                if check_block in self.instructions:
                    return self.instructions[check_block]
                block = list(zip(*reversed(block)))
            block = [list(reversed(a)) for a in block]
    
    def print_grid(self):
        for y in range(self.size):
            print(''.join([self.grid[(i, y)] for i in range(self.size)]))
    

if __name__ == '__main__':
    main()