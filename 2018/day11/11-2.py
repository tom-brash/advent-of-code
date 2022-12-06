'''
Day 11-2: Max power in any size window

Here we use the idea of summed_area_grids to do this at least somewhat efficiently 
(an earlier version relying on primitive caching took ~10min). The summed area grid
can be computed in a single pass and then used to produce the sum of any rectangular
area.

Heavy use of dictionary.get() is used in order to avoid negative index issues.
'''

from collections import defaultdict
from tqdm import tqdm

def main():
    with open('day11/11-1-input.txt', 'r') as open_file:
        serial = int(open_file.read())

    grid = dict()
    summed_area_grid = dict()


    for y in range(1,301):
        for x in range(1, 301):
            p = get_power(x, y, serial)
            grid[(x, y)] = p
            summed_area_grid[(x, y)] = p + summed_area_grid.get((x - 1, y), 0) + summed_area_grid.get((x, y - 1), 0) - summed_area_grid.get((x - 1, y - 1), 0)

    best_power = 0
    best_x = 0
    best_y = 0
    best_s = 0

    for s in tqdm(range(2, 301)):
        for x in range(1, 302 - s):
            for y in range(1, 302 - s):
                p = (summed_area_grid.get((x + (s - 1), y  + (s - 1)), 0) - 
                    summed_area_grid.get((x  + (s - 1), y - 1), 0) - 
                    summed_area_grid.get((x - 1, y  + (s - 1)), 0) + 
                    summed_area_grid.get((x - 1, y - 1), 0))
                if p > best_power:
                    best_power = p
                    best_x = x
                    best_y = y
                    best_s = s
    
    print('Best power:', best_power)
    print('Coordinates of best power:', (best_x, best_y, s))


def get_power(x, y, serial):
    p = ((x + 10) * y + serial) * (x + 10)
    p = ((p // 100) % 10) - 5
    return p
    

if __name__ == '__main__':
    main()