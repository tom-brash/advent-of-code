'''
Day 11-1: Max power in 3x3 window

Here we do a fairly naive method, creating a dictionary that has the total power
for every 3x3 area, and then just taking the maximum value
'''

from collections import defaultdict

def main():
    with open('day11/11-1-input.txt', 'r') as open_file:
        serial = int(open_file.read())

    grid_power = defaultdict(int)
    grid = {}

    for x in range(1,301):
        for y in range(1, 301):
            p = get_power(x, y, serial)
            for i in range(3):
                for j in range(3):
                    grid_power[(x - i, y -j)] += p
            grid[(x - 2, y - 2)] = p
    
    best_power = max(grid_power.values())
    print('Highest 3x3 grid has power:', best_power)
    print('Coordinates:',[k for k, v in grid_power.items() if v == best_power][0])


def get_power(x, y, serial):
    p = ((x + 10) * y + serial) * (x + 10)
    p = ((p // 100) % 10) - 5
    return p
    

if __name__ == '__main__':
    main()