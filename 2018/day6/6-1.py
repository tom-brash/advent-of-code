'''
Day 6-1: Finding largest region size

As we don't need to care about anything beyond the edges of the square defined by
the points (as any regione extending there will be infinitely sized), we just 
need to do all the points within this square.

We calclate the manhattan distance between the points, and disqualify any region
that is touching the edge (as being infinitely sized). One of my first submissions
within the top 100 time!
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

    outcome = dict()
    totals = defaultdict(int)
    for x in range(max_x):
        for y in range(max_y):
            o = closest_manhattan((x, y), locs)
            outcome[(x, y)] = o
            if o != '.':
                totals[o] += 1
    
    disqualified = set()
    for y in range(max_y):
        disqualified.add(outcome[(0, y)])
        disqualified.add(outcome[(max_x - 1, y)])
    
    for x in range(max_x):
        disqualified.add(outcome[(x, 0)])
        disqualified.add(outcome[(x, max_y - 1)])

    highest = 0
    for key, val in totals.items():
        if key not in disqualified:
            if val > highest:
                highest = val
                best = key

    print('Highest non infinite area:', highest)


def closest_manhattan(p, locs):
    d = 1000
    closest_list = []
    for i, l in enumerate(locs):
        m = abs(p[0] - l[0]) + abs(p[1] - l[1])
        if m < d:
            closest_list = [i]
            d = m
        elif m == d:
            closest_list.append(i)
    
    if len(closest_list) == 1:
        return closest_list[0]
    else:
        return '.'


if __name__ == '__main__':
    main()