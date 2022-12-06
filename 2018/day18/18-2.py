'''
Day 18-2: Conway's lumberyard over the millenia

Another problem in the vein of "now do it more times" - instead of 10x we are running it 1,000,000,000x.
This is too many times for even an efficient implementation - which mine is not. 

By observation, however, the pattern stabilizes neatly after ~500 iterations, at which point the lumberyards
and forests continue to flow down the screen (southeast, roughly) in waves that repeat themselves every 28 
iterations. Knowing this, we don't need to run 1b iterations, but instead just 500 times for the pattern to 
stabilize, and then to the first iteration on the same 'cylce' as 1b.
'''

import copy

def main():
    with open('day18/18-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    rows = input_data.split('\n')
    landscape = Landscape(rows)

    x = (1000000000 - 500) // 28
    n = 1000000000 - x * 28
    for i in range(n):
        landscape.update()
    landscape.get_resources()

    
class Landscape:
    def __init__(self, data):
        self.grid = {}
        self.width = len(data[0])
        self.height = len(data)
        # self.visited = []
        self.steps = 0
        for y, row in enumerate(data):
            for x, c in enumerate(row):
                self.grid[(x, y)] = c
    
    def update(self):
        self.steps += 1
        updated = copy.deepcopy(self.grid)
        for x in range(self.width):
            for y in range(self.height):
                o, t, l = self.check(x, y)
                if self.grid[(x, y)] == '.':
                    if t >= 3:
                        updated[(x, y)] = '|'
                elif self.grid[(x, y)] == '|':
                    if l >= 3:
                        updated[(x, y)] = '#'
                else:
                    if l == 0 or t == 0:
                        updated[(x, y)] = '.'
        self.grid = updated
        # if self.grid in self.visited:
        #     print(f'Repeat!! After {self.steps} updates')
        # else:
        #     self.visited.append(self.grid)
        
    
    def check(self, x, y):
        o = 0
        t = 0
        l = 0
        for x_delta in [-1, 0, 1]:
            for y_delta in [-1, 0, 1]:
                if x_delta != 0 or y_delta != 0:
                    c = self.grid.get((x + x_delta, y + y_delta), '!')
                    if c == '.':
                        o += 1
                    elif c == '|':
                        t += 1
                    elif c == '#':
                        l += 1        
        return o,t, l
    
    def get_resources(self):
        t = 0
        l = 0
        for x in range(self.width):
            for y in range(self.height):
                c = self.grid[(x, y)]
                if c == '|':
                    t += 1
                elif c == '#':
                    l += 1
        print(l * t)     

    def printout(self):
        print_string = ''
        for y in range(self.height):
            for x in range(self.width):
                print_string += self.grid[(x, y)]
            print_string += '\n'
        print(print_string)
                  

if __name__ == '__main__':
    main()