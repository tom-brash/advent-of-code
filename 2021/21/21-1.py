from collections import defaultdict
from collections import deque
import math
import re
import copy


def main():
    # with open('21/21.txt', 'r') as open_file:
    #     input_data = open_file.read().split('\n')
    
    p1 = Player(6)
    p2 = Player(4)
    
    i = 0
    while p1.total < 1000 and p2.total < 1000:
        m = 0
        for _ in range(3):
            m += det_dice(i)
            i += 1
        p1.move(m)
        if p1.total >= 1000:
            break
        
        m = 0
        for _ in range(3):
            m += det_dice(i)
            i += 1
        p2.move(m)
    
    print(p1.total, p2.total, i)


def det_dice(i):
    return i % 100 + 1
    

def print_grid(grid):
    p_dict = {'1': '@', '0': ' '}
    y_min = 0
    y_max = 0
    x_min = 0
    x_max = 0
    for p in grid.keys():
        if p[0] < y_min:
            y_min = p[0]
        if p[0] > y_max:
            y_max = p[0]
        if p[1] < x_min:
            x_min = p[0]
        if p[1] > x_max:
            x_max = p[0]
        
    for y in range(y_min, y_max + 1):
        row = ''
        for x in range(x_min, x_max + 1):
            row += p_dict[grid[(y, x)]]
        print(row)

class Player:
    def __init__(self, n):
        self.n = n
        self.total = 0
    
    def move(self, n):
        self.n = ((self.n - 1) + n) % 10 + 1 
        self.total += self.n

if __name__ == '__main__':
    main()