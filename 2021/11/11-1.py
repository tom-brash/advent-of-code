import time
import copy
from collections import deque

def main():

    # start_time = time.time()
    # score = {')' : 3, ']': 57, '}': 1197, '>': 25137}
    # ed = {'(' : ')', '[': ']', '{': '}', '<': '>'}

    with open('11/11.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    grid = {}
    for i,r in enumerate(input_data):
        for j, c in enumerate(r):
            grid[(i, j)] = Octopus(int(c))
    
    
    
    height = len(input_data)
    width = len(input_data[0])
    #print_grid(grid, height, width)
    t = 0

    for _ in range(100):
        #print(f'step {_}')
        # step 1
        for i in range(width):
            for j in range(height):
                grid[(i, j)].increase()
        
        # step 2
        stable = False
        while not stable:
            flash_count = 0

            for i in range(width):
                for j in range(height):
                    current = grid[(i, j)]
                    if current.n == 10 and current.flashed == False:
                        t += 1
                        for x in [-1, 0, 1]:
                            for y in [-1, 0, 1]:
                                if not (x == 0 and y == 0) and i + x >= 0 and i + x < width and j + y >= 0 and j + y < height:
                                    grid[(i + x, j + y)].increase()
                        current.flashed = True
                        flash_count += 1
            #print_grid(new_grid, height, width)
            if flash_count == 0:
                stable = True
                
        
        # step 3
        for i in range(width):
            for j in range(height):
                current = grid[(i, j)]
                if current.flashed == True:
                    current.flashed = False
                    current.n = 0
        #print()
        #print_grid(grid, height, width)

    print(t)

    
def print_grid(grid, h, w):
    for i in range(w):
        row = ''
        for j in range(h):
            row += str(grid[(i, j)].n)
        print(row)

    #print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')

class Octopus():
    def __init__(self, n):
        self.n = n
        self.flashed = False
    
    def increase(self):
        self.n = min(10, self.n + 1)

        
    
if __name__ == '__main__':
    main()
    