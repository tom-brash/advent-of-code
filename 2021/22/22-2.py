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
    
    cubes = []
    dead_zones = []
    
    for x in input_data:
        current_cube = [int(x) for x in re.findall('\-?\d+', x)]
        new_cubes = []
        new_dead_zones = []
        if x[1] == 'n':
            new_cubes.append(current_cube)
        for c in cubes:
            if check_cubes(current_cube, c) == 'Overlapping':
                new_dead_zones.append(cube_overlap(current_cube, c))
        for c in dead_zones:
            if check_cubes(current_cube, c) == 'Overlapping':
                new_cubes.append(cube_overlap(current_cube, c))

        for c in new_cubes:
            if c in dead_zones:
                dead_zones.remove(c)
            else:
                cubes.append(c)
        
        for c in new_dead_zones:
            if c in cubes:
                cubes.remove(c)
            else:
                dead_zones.append(c)        

    total = 0
    for cube in cubes:
        total += cube_vol(cube)
    for dz in dead_zones:
        total -= cube_vol(dz)
    
    print(total)
    print(f'Part 2 time taken: {round((time.time() - start_time) * 1000, 3)} ms')

def check_cubes(a, b):
    if overlap(a[0], a[1], b[0], b[1]) != False:
        if overlap(a[2], a[3], b[2], b[3]) != False:
            if overlap(a[4], a[5], b[4], b[5]) != False:
                return 'Overlapping'
    return 'Not overlapping'

def cube_overlap(a, b):
    ax1, ax2, ay1, ay2, az1, az2 = a
    bx1, bx2, by1, by2, bz1, bz2 = b
    x1 = max(ax1, bx1)
    x2 = min(ax2, bx2)
    y1 = max(ay1, by1)
    y2 = min(ay2, by2)
    z1 = max(az1, bz1)
    z2 = min(az2, bz2)
    return (x1, x2, y1, y2, z1, z2)

def cube_vol(cube):
    x1, x2, y1, y2, z1, z2 = cube
    vol = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    return vol

def overlap(a1, a2, b1, b2):
    if a2 >= b1 and a1 <= b1:
        return 'overlapping'
    if a1 <= b2 and a2 >= b2:
        return 'overlapping'
    if a2 <= b2 and a1 >= b1:
        return 'contained'
    if b2 <= a2 and b1 >= a1:
        return 'containing'
    return False


if __name__ == '__main__':
    main()