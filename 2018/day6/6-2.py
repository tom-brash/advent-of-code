'''
Day 6-2: Finding safe region size

Given implentation to day 6, this is relatively trivial. We have already mapped out 
the space, meaning we just to slightly modify the manhattan formula to add all of the 
distances, rather than just finding the smallest. Also within top 100 time
'''

import string
from collections import defaultdict

def main():
    with open('day6/6-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    locs = input_data.split('\n')
    locs = [tuple([int(x) for x in l.split(', ')]) for l in locs]
    max_x = 0
    max_y = 0
    for l in locs:
        if l[0] > max_x:
            max_x = l[0]
        if l[1] > max_y:
            max_y = l[1]

    total = 0
    for x in range(max_x):
        for y in range(max_y):
            s = check_manhattan((x, y), locs)
            if s == True:
                total += 1

    print('Size of safe region:', total)


def check_manhattan(p, locs, d=10000):
    safe = True
    t = 0
    for l in locs:
        m = abs(p[0] - l[0]) + abs(p[1] - l[1])
        t += m
    if t >= d:
        safe = False
    
    return safe


if __name__ == '__main__':
    main()