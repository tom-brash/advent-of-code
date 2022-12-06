from collections import defaultdict
from collections import deque
import math
import re
import copy
import time


def main():
    start_time = time.time()
    with open('22/22.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    grid = {}
    for x in input_data[:20]:
        nums = [int(x) for x in re.findall('\-?\d+', x)]
        x1, x2, y1, y2, z1, z2 = nums
        val = 'on'
        if x[1] == 'f':
            val = 'off'
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    grid[(x, y, z)] = val

    
    total = 0
    for v in grid.values():
        if v == 'on':
            total += 1

    print(f'Total lit cubes for Part 1: {total}')
    print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')
    

if __name__ == '__main__':
    main()